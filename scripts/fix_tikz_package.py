"""
Add tikz package to all module .tex files for QuantLet branding

The branding uses tikzpicture overlays which require the tikz package.
"""

from pathlib import Path
import re


def add_tikz_package(tex_file):
    """Add tikz package after amsmath if not present."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if tikz is already loaded
    if '\\usepackage{tikz}' in content or '\\usepackage[' in content and 'tikz' in content:
        print(f"  [SKIP] {tex_file.name}: tikz already present")
        return False

    # Find the last \usepackage line before \begin{document}
    # Add tikz after amsmath or amssymb
    if '\\usepackage{amsmath}' in content:
        content = content.replace(
            '\\usepackage{amsmath}',
            '\\usepackage{amsmath}\n\\usepackage{tikz}'
        )
    elif '\\usepackage{amssymb}' in content:
        content = content.replace(
            '\\usepackage{amssymb}',
            '\\usepackage{amssymb}\n\\usepackage{tikz}'
        )
    else:
        # Add before \begin{document}
        content = content.replace(
            '\\begin{document}',
            '\\usepackage{tikz}\n\\begin{document}'
        )

    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {tex_file.name}: Added tikz package")
    return True


def main():
    project_root = Path(__file__).parent

    # Find all module .tex files with branding (latest timestamp)
    tex_files = list(project_root.glob('module*/*0829*.tex')) + list(project_root.glob('appendix/*0829*.tex'))

    print("Adding tikz package to branded .tex files...")
    print(f"Found {len(tex_files)} files\n")

    for tex_file in tex_files:
        add_tikz_package(tex_file)


if __name__ == '__main__':
    main()
