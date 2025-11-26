"""
Add LaTeX-level branding to chart slides.

This script:
1. Parses the .tex file to find frames with charts
2. Auto-generates Quantlet GitHub URLs from chart folder names
3. Inserts tikz overlay code to add logo, QR, and URL at bottom-right
4. Creates timestamped backup and new .tex file

Usage:
    python add_latex_branding.py [tex_file] [--repo-name REPO]

Examples:
    python add_latex_branding.py  # Uses latest .tex and current folder name
    python add_latex_branding.py slides.tex --repo-name DEDA_NeuralNetworks
"""
import re
import ast
import shutil
import argparse
from pathlib import Path
from datetime import datetime


def get_repo_name():
    """Get repository name from current directory."""
    return Path.cwd().name


def generate_quantlet_url(chart_folder, repo_name):
    """
    Generate Quantlet GitHub URL from chart folder name.

    Pattern: https://github.com/Quantlet/{repo_name}/tree/main/{chart_folder}
    """
    return f"https://github.com/Quantlet/{repo_name}/tree/main/{chart_folder}"


def extract_metadata_from_chart(py_file):
    """Extract CHART_METADATA URL from a chart Python file (if exists)."""
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find CHART_METADATA dictionary
        pattern = r'CHART_METADATA\s*=\s*(\{[^}]+\})'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            dict_str = match.group(1)
            # Parse as Python literal
            metadata = ast.literal_eval(dict_str)
            return metadata.get('url', '')
        return ''

    except Exception:
        return ''


def find_chart_frames(tex_content):
    """Find all frames containing \\includegraphics commands."""
    frames = []

    # Split into frames
    frame_pattern = r'(\\begin\{frame\}.*?\\end\{frame\})'
    frame_matches = re.finditer(frame_pattern, tex_content, re.DOTALL)

    for match in frame_matches:
        frame_content = match.group(1)
        frame_start = match.start()
        frame_end = match.end()

        # Check if frame contains \\includegraphics with a chart path
        graphics_pattern = r'\\includegraphics\[.*?\]\{([^}]+\.pdf)\}'
        graphics_match = re.search(graphics_pattern, frame_content)

        if graphics_match:
            chart_path = graphics_match.group(1)
            # Process any chart (not just numbered folders)
            frames.append({
                'start': frame_start,
                'end': frame_end,
                'content': frame_content,
                'chart_path': chart_path
            })

    return frames


def create_branding_tikz(chart_folder, chart_url, logo_path='quantlet_tools/logo/quantlet.png'):
    """Create tikz overlay code for branding."""
    # Extract short path for display (e.g., "07_loss_landscape")
    short_path = chart_folder.replace('/', '').replace('_', '\\_')

    tikz_code = f"""
% Quantlet branding (auto-generated)
\\begin{{tikzpicture}}[remember picture,overlay]
% Logo (clickable)
\\node[anchor=south east,xshift=-0.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\includegraphics[width=0.8cm]{{{logo_path}}}}}
}};
% QR Code (clickable)
\\node[anchor=south east,xshift=-1.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\includegraphics[width=0.6cm]{{{chart_folder}/qr_code.png}}}}
}};
% URL text (clickable)
\\node[anchor=south east,xshift=-0.3cm,yshift=0.2cm] at (current page.south east) {{
  \\href{{{chart_url}}}{{\\tiny\\texttt{{\\textcolor{{gray}}{{{short_path}}}}}}}
}};
\\end{{tikzpicture}}
"""
    return tikz_code


def add_branding_to_frame(frame_content, chart_folder, chart_url, logo_path):
    """Insert branding tikz code into a frame before \\bottomnote or \\end{frame}."""
    tikz_code = create_branding_tikz(chart_folder, chart_url, logo_path)

    # Try to insert before \\bottomnote
    if '\\bottomnote' in frame_content:
        new_content = frame_content.replace('\\bottomnote', tikz_code + '\n\\bottomnote')
    else:
        # Insert before \\end{frame}
        new_content = frame_content.replace('\\end{frame}', tikz_code + '\n\\end{frame}')

    return new_content


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(description='Add Quantlet branding to LaTeX slides')
    parser.add_argument('tex_file', nargs='?', help='LaTeX file to process (optional, uses latest if not specified)')
    parser.add_argument('--repo-name', help='Quantlet repository name (default: current folder name)')
    parser.add_argument('--logo-path', default='quantlet_tools/logo/quantlet.png', help='Path to logo file')
    args = parser.parse_args()

    print("Adding LaTeX-level Quantlet branding to chart slides...\n")

    # Determine repo name
    repo_name = args.repo_name or get_repo_name()
    print(f"Repository: Quantlet/{repo_name}\n")

    # Find tex file
    if args.tex_file:
        tex_file = Path(args.tex_file)
        if not tex_file.exists():
            print(f"ERROR: File {args.tex_file} not found")
            return
    else:
        # Find latest .tex file
        tex_files = sorted(Path('.').glob('*.tex'))
        tex_files = [f for f in tex_files if 'template' not in f.name.lower()]

        if not tex_files:
            print("ERROR: No .tex file found")
            return

        tex_file = tex_files[-1]

    print(f"Processing: {tex_file.name}\n")

    # Read .tex file
    with open(tex_file, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    # Find all chart frames
    print("Scanning for chart frames...")
    chart_frames = find_chart_frames(tex_content)
    print(f"Found {len(chart_frames)} chart frames\n")

    if not chart_frames:
        print("No chart frames found. Exiting.")
        return

    # Build chart URL mapping
    print("Generating Quantlet URLs...")
    url_mapping = {}

    for frame in chart_frames:
        chart_path = frame['chart_path']
        # Extract folder name (e.g., "07_loss_landscape" from "07_loss_landscape/loss_landscape.pdf")
        if '/' in chart_path:
            chart_folder = chart_path.split('/')[0]
        else:
            # Handle charts in root (use filename without extension)
            chart_folder = Path(chart_path).stem

        # Try to extract from CHART_METADATA first (if Python file exists)
        py_files = list(Path(chart_folder).glob('*.py')) if Path(chart_folder).is_dir() else []

        if py_files:
            chart_url = extract_metadata_from_chart(py_files[0])
            if chart_url:
                print(f"  {chart_folder}: {chart_url} (from CHART_METADATA)")
            else:
                # Fallback to auto-generated URL
                chart_url = generate_quantlet_url(chart_folder, repo_name)
                print(f"  {chart_folder}: {chart_url} (auto-generated)")
        else:
            # Standalone mode: auto-generate URL
            chart_url = generate_quantlet_url(chart_folder, repo_name)
            print(f"  {chart_folder}: {chart_url} (auto-generated)")

        url_mapping[chart_folder] = chart_url

    print(f"\n{len(url_mapping)} URLs generated\n")

    # Process frames in reverse order (to preserve positions)
    print("Inserting branding code into frames...")
    modified_content = tex_content
    branding_count = 0

    # Sort frames by position (reverse) to maintain string positions
    for frame in reversed(chart_frames):
        chart_path = frame['chart_path']

        if '/' in chart_path:
            chart_folder = chart_path.split('/')[0]
        else:
            chart_folder = Path(chart_path).stem

        chart_url = url_mapping.get(chart_folder, '')

        if chart_url:
            # Create modified frame content
            new_frame = add_branding_to_frame(frame['content'], chart_folder, chart_url, args.logo_path)

            # Replace in full content
            modified_content = modified_content[:frame['start']] + new_frame + modified_content[frame['end']:]
            branding_count += 1
            print(f"  Added branding to: {chart_folder}")
        else:
            print(f"  Skipped (no URL): {chart_folder}")

    print(f"\nAdded branding to {branding_count} frames\n")

    # Create backup
    print("Creating backup...")
    backup_path = Path('previous') / tex_file.name
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(tex_file, backup_path)
    print(f"  Backup: {backup_path}")

    # Save new file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    base_name = tex_file.stem.replace(timestamp[:13], '')  # Remove old timestamp if present
    new_filename = f"{timestamp}_quantlet_branding.tex"
    new_path = Path(new_filename)

    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print(f"\nNew .tex file: {new_filename}")

    print("\n" + "="*78)
    print(f"COMPLETE: Quantlet branding added to {branding_count} chart slides")
    print(f"Repository: https://github.com/Quantlet/{repo_name}")
    print(f"\nNext step: Compile {new_filename} to verify branding")
    print("="*78)


if __name__ == '__main__':
    main()
