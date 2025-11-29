"""
Fix overfull vbox warnings by reducing chart image widths
"""

import re
from pathlib import Path

project_root = Path(__file__).parent

# Charts that need width reduction (frame title -> new width)
fixes = {
    # Module 2
    'Activation Functions: Comparison': '0.80',

    # Module 3
    'Gradient Descent: Move Downhill': '0.75',
    'Training Pipeline Overview': '0.80',

    # Module 4
    'Case Study: Results Summary': '0.85',
}

def fix_chart_widths(tex_file):
    """Fix chart widths in a tex file."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    for frame_title, new_width in fixes.items():
        # Find frame with this title
        frame_pattern = rf'(\\begin{{frame}}\[t\]{{{re.escape(frame_title)}}}.*?)(\\includegraphics\[width=)(\d+\.?\d*)(\\textwidth\])'

        def replace_width(m):
            return f"{m.group(1)}{m.group(2)}{new_width}{m.group(4)}"

        new_content, count = re.subn(frame_pattern, replace_width, content, flags=re.DOTALL)

        if count > 0:
            content = new_content
            modified = True
            print(f"  [OK] {frame_title}: width -> {new_width}\\textwidth")

    if modified:
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(content)

    return modified

def main():
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    print("Fixing overfull chart widths...")

    for module in modules:
        module_dir = project_root / module
        tex_files = sorted(module_dir.glob('*0829*.tex'))

        for tex_file in tex_files:
            print(f"\n{tex_file.name}:")
            fix_chart_widths(tex_file)

if __name__ == '__main__':
    main()
