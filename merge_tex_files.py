"""
Merge all module .tex files into one combined .tex file

Handles:
- Single preamble from first file
- Combined content from all modules
- Fixed relative paths for charts
"""

import re
from pathlib import Path
from datetime import datetime


def extract_preamble_and_content(tex_file):
    """Extract preamble and document content from a .tex file."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split at \begin{document}
    if '\\begin{document}' in content:
        parts = content.split('\\begin{document}', 1)
        preamble = parts[0]
        rest = parts[1]
    else:
        return content, ''

    # Split at \end{document}
    if '\\end{document}' in rest:
        body = rest.split('\\end{document}')[0]
    else:
        body = rest

    return preamble, body


def fix_chart_paths(content, module_folder):
    """Fix relative chart paths to include module folder."""
    # Replace charts/ with module_folder/charts/
    # Pattern: {charts/something/something.pdf} or {charts/something/something.png}
    pattern = r'\{charts/'
    replacement = f'{{{module_folder}/charts/'
    content = re.sub(pattern, replacement, content)

    # Also fix the quantlet_tools logo path
    content = content.replace('../quantlet_tools/', 'quantlet_tools/')

    return content


def merge_tex_files():
    project_root = Path(__file__).parent

    # Module files in order
    modules = [
        ('module1_perceptron', '20251128_0829_module1.tex'),
        ('module2_mlp', '20251128_0829_module2.tex'),
        ('module3_training', '20251128_0829_module3.tex'),
        ('module4_applications', '20251128_0829_module4.tex'),
    ]

    print("Merging .tex files...")
    print("=" * 60)

    combined_preamble = None
    combined_body = []

    for module_folder, tex_filename in modules:
        tex_file = project_root / module_folder / tex_filename

        if not tex_file.exists():
            print(f"[SKIP] Not found: {tex_file}")
            continue

        print(f"[OK] Processing: {module_folder}/{tex_filename}")

        preamble, body = extract_preamble_and_content(tex_file)

        # Use preamble from first file only
        if combined_preamble is None:
            combined_preamble = preamble

        # Fix chart paths in body
        fixed_body = fix_chart_paths(body, module_folder)

        # Add section separator
        separator = f"""
%% ============================================================================
%% {module_folder.upper().replace('_', ' ')}
%% ============================================================================
"""
        combined_body.append(separator)
        combined_body.append(fixed_body)

    # Build final document
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')

    final_content = combined_preamble
    final_content += '\\begin{document}\n'
    final_content += '\n'.join(combined_body)
    final_content += '\n\\end{document}\n'

    # Output file
    output_file = project_root / f'{timestamp}_NeuralNetworks_Complete.tex'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print("=" * 60)
    print(f"Merged .tex file: {output_file}")
    print(f"Modules merged: {len(combined_body) // 2}")

    return output_file


if __name__ == '__main__':
    merge_tex_files()
