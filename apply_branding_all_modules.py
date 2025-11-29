"""
Apply QuantLet branding to all module .tex files in NeuralNetworks3 project

This script handles the project structure:
- module*/charts/chart_name/chart_name.pdf

Usage:
    python apply_branding_all_modules.py
"""

import re
import ast
import shutil
from pathlib import Path
from datetime import datetime


GITHUB_BASE = "https://github.com/QuantLet/NeuralNetworks/tree/main"


def extract_metadata_from_chart(py_file):
    """Extract CHART_METADATA URL from a chart Python file."""
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'CHART_METADATA\s*=\s*(\{[^}]+\})'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            dict_str = match.group(1)
            metadata = ast.literal_eval(dict_str)
            return metadata.get('url', '')
        return ''
    except Exception:
        return ''


def find_chart_frames(tex_content):
    """Find all frames containing includegraphics commands with charts."""
    frames = []

    frame_pattern = r'(\\begin\{frame\}.*?\\end\{frame\})'
    frame_matches = re.finditer(frame_pattern, tex_content, re.DOTALL)

    for match in frame_matches:
        frame_content = match.group(1)
        frame_start = match.start()
        frame_end = match.end()

        # Look for charts/chart_name/chart_name.pdf pattern
        graphics_pattern = r'\\includegraphics\[.*?\]\{(charts/[^/]+/[^}]+\.pdf)\}'
        graphics_match = re.search(graphics_pattern, frame_content)

        if graphics_match:
            chart_path = graphics_match.group(1)
            frames.append({
                'start': frame_start,
                'end': frame_end,
                'content': frame_content,
                'chart_path': chart_path
            })

    return frames


def create_branding_tikz(chart_folder, chart_url, qr_path, logo_path):
    """Create tikz overlay code for branding."""
    # Escape underscores for LaTeX display
    short_display = chart_folder.replace('_', '\\_')

    tikz_code = f"""
% Quantlet branding (auto-generated)
\\begin{{tikzpicture}}[remember picture,overlay]
% Logo (clickable)
\\node[anchor=south east,xshift=-0.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\includegraphics[width=0.8cm]{{{logo_path}}}}}
}};
% QR Code (clickable)
\\node[anchor=south east,xshift=-1.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\includegraphics[width=0.6cm]{{{qr_path}}}}}
}};
% URL text (clickable)
\\node[anchor=south east,xshift=-0.3cm,yshift=0.2cm] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\tiny\\texttt{{\\textcolor{{gray}}{{{short_display}}}}}}}
}};
\\end{{tikzpicture}}
"""
    return tikz_code


def add_branding_to_frame(frame_content, chart_folder, chart_url, qr_path, logo_path):
    """Insert branding tikz code into a frame."""
    tikz_code = create_branding_tikz(chart_folder, chart_url, qr_path, logo_path)

    if '\\bottomnote' in frame_content:
        new_content = frame_content.replace('\\bottomnote', tikz_code + '\n\\bottomnote')
    else:
        new_content = frame_content.replace('\\end{frame}', tikz_code + '\n\\end{frame}')

    return new_content


def has_branding(frame_content):
    """Check if frame already has branding."""
    return 'Quantlet branding' in frame_content


def process_tex_file(tex_file, module_name):
    """Process a single .tex file and add branding."""
    print(f"\n{'='*60}")
    print(f"Processing: {tex_file.name}")
    print(f"Module: {module_name}")
    print(f"{'='*60}")

    with open(tex_file, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    # Find chart frames
    chart_frames = find_chart_frames(tex_content)
    print(f"Found {len(chart_frames)} chart frames")

    if not chart_frames:
        print("No chart frames found. Skipping.")
        return 0

    # Logo path relative to module folder
    logo_path = '../quantlet_tools/logo/quantlet.png'

    # Process frames
    modified_content = tex_content
    branding_count = 0

    for frame in reversed(chart_frames):
        if has_branding(frame['content']):
            print(f"  [SKIP] Already branded: {frame['chart_path']}")
            continue

        chart_path = frame['chart_path']  # e.g., "charts/perceptron_architecture/perceptron_architecture.pdf"

        # Extract chart folder name (e.g., "perceptron_architecture")
        parts = chart_path.split('/')
        if len(parts) >= 2:
            chart_folder = parts[1]  # "perceptron_architecture"
        else:
            continue

        # Build paths
        chart_dir = tex_file.parent / 'charts' / chart_folder
        py_file = chart_dir / f"{chart_folder}.py"
        qr_path = f"charts/{chart_folder}/qr_code.png"

        # Get URL from CHART_METADATA
        if py_file.exists():
            chart_url = extract_metadata_from_chart(py_file)
            if not chart_url:
                chart_url = f"{GITHUB_BASE}/{module_name}/charts/{chart_folder}"
        else:
            chart_url = f"{GITHUB_BASE}/{module_name}/charts/{chart_folder}"

        # Check if QR code exists
        qr_file = chart_dir / "qr_code.png"
        if not qr_file.exists():
            print(f"  [SKIP] No QR code: {chart_folder}")
            continue

        # Add branding
        new_frame = add_branding_to_frame(frame['content'], chart_folder, chart_url, qr_path, logo_path)
        modified_content = modified_content[:frame['start']] + new_frame + modified_content[frame['end']:]
        branding_count += 1
        print(f"  [OK] {chart_folder}")

    if branding_count > 0:
        # Create backup in previous folder
        previous_dir = tex_file.parent.parent / 'previous'
        previous_dir.mkdir(exist_ok=True)
        backup_path = previous_dir / tex_file.name
        shutil.copy2(tex_file, backup_path)
        print(f"\nBackup: {backup_path}")

        # Write modified content with new timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        # Extract base name without old timestamp
        old_name = tex_file.stem
        if old_name[:8].isdigit() and old_name[8] == '_':
            base_name = old_name[14:]  # Remove YYYYMMDD_HHMM_
        else:
            base_name = old_name

        new_filename = f"{timestamp}_{base_name}.tex"
        new_path = tex_file.parent / new_filename

        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print(f"New file: {new_path}")

    print(f"\nBranded {branding_count} frames in {tex_file.name}")
    return branding_count


def main():
    """Process all module .tex files."""
    project_root = Path(__file__).parent

    modules = [
        ('module1_perceptron', '20251126_0900_module1.tex'),
        ('module2_mlp', '20251126_0930_module2.tex'),
        ('module3_training', '20251126_1000_module3.tex'),
        ('module4_applications', '20251126_1030_module4.tex'),
        ('appendix', '20251126_1100_appendix.tex'),
    ]

    print("Adding QuantLet branding to all modules...")
    print(f"Project: {project_root}")

    total_branded = 0

    for module_name, tex_filename in modules:
        tex_file = project_root / module_name / tex_filename
        if tex_file.exists():
            total_branded += process_tex_file(tex_file, module_name)
        else:
            # Try to find latest .tex file in the module
            module_dir = project_root / module_name
            tex_files = sorted(module_dir.glob('*.tex'))
            tex_files = [f for f in tex_files if 'template' not in f.name.lower()]
            if tex_files:
                total_branded += process_tex_file(tex_files[-1], module_name)
            else:
                print(f"\n[SKIP] No .tex file found in {module_name}")

    print(f"\n{'='*60}")
    print(f"COMPLETE: Added branding to {total_branded} frames total")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
