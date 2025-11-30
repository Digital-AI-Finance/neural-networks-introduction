"""
Fix remaining overfull vbox warnings - Round 2
"""

import re
from pathlib import Path

project_root = Path(__file__).parent

# Additional fixes and further reductions
fixes = {
    # Module 1
    'timeline_1943_1969': ('0.85', '0.78'),  # 21pt -> target <10pt
    'perceptron_architecture': ('0.73', '0.66'),  # 31pt -> target <10pt
    'decision_boundary_2d': ('0.98', '0.85'),  # 38pt -> target <10pt

    # Module 2
    'activation_comparison': ('0.68', '0.55'),  # 69pt -> target <10pt
    'mlp_architecture_2_3_1': ('0.85', '0.78'),  # 23pt -> target <10pt

    # Module 3
    'gradient_descent_contour': ('0.60', '0.52'),  # 39pt -> target <10pt
    'module3_summary_diagram': ('0.70', '0.62'),  # 27pt -> target <10pt
}

def fix_chart_widths_in_file(tex_file):
    """Fix chart widths in a tex file."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    for chart_name, (old_width, new_width) in fixes.items():
        pattern = rf'(\\includegraphics\[width=){old_width}(\\textwidth\]{{[^}}]*{chart_name}[^}}]*}})'

        def replace_width(m):
            return f"{m.group(1)}{new_width}{m.group(2)}"

        new_content, count = re.subn(pattern, replace_width, content)

        if count > 0:
            content = new_content
            modified = True
            print(f"  [OK] {chart_name}: {old_width} -> {new_width}")

    if modified:
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    print("Fixing overfull widths - Round 2...")
    print("=" * 50)

    for module in modules:
        module_dir = project_root / module
        tex_files = sorted(module_dir.glob('*0829*.tex'))

        for tex_file in tex_files:
            print(f"\n{tex_file.name}:")
            fix_chart_widths_in_file(tex_file)

    print("\n" + "=" * 50)
    print("Done! Now regenerate merged file.")

if __name__ == '__main__':
    main()
