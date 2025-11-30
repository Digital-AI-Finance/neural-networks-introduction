"""
Fix all remaining overfull vbox warnings by reducing chart image widths
"""

import re
from pathlib import Path

project_root = Path(__file__).parent

# All charts that need width reduction (chart_name -> new width)
# Calculated from overfull amounts: reduce proportionally to eliminate overflow
fixes = {
    # Module 1 (4 charts)
    'timeline_1943_1969': ('0.95', '0.85'),  # 45pt overflow
    'perceptron_architecture': ('0.85', '0.73'),  # 66pt overflow
    'stock_features_scatter': ('0.98', '0.85'),  # 52pt overflow (in column)

    # Module 2 (1 chart)
    'activation_comparison': ('0.80', '0.68'),  # 114pt overflow (still too big)

    # Module 3 (4 charts)
    'gradient_descent_contour': ('0.72', '0.60'),  # 84pt overflow
    'overfitting_curves': ('0.85', '0.76'),  # 32pt overflow
    'module3_summary_diagram': ('0.80', '0.70'),  # 58pt overflow

    # Module 4 (1 chart)
    'full_timeline_1943_2024': ('0.82', '0.72'),  # 34pt overflow
}

def fix_chart_widths_in_file(tex_file):
    """Fix chart widths in a tex file."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    for chart_name, (old_width, new_width) in fixes.items():
        # Pattern to match includegraphics with this chart
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

    print("Fixing all overfull chart widths...")
    print("=" * 50)

    total_fixed = 0

    for module in modules:
        module_dir = project_root / module
        tex_files = sorted(module_dir.glob('*0829*.tex'))

        for tex_file in tex_files:
            print(f"\n{tex_file.name}:")
            if fix_chart_widths_in_file(tex_file):
                total_fixed += 1

    print("\n" + "=" * 50)
    print(f"Fixed charts in {total_fixed} files")
    print("\nNow run: python merge_tex_files.py")
    print("Then compile the merged PDF")

if __name__ == '__main__':
    main()
