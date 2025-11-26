"""
Fix imports in all chart files to add parent directory to sys.path.
This allows charts to import from utils/ folder.
"""
import re
from pathlib import Path

# New import block with sys.path fix
NEW_IMPORT_BLOCK = """
# Add Quantlet branding (logo, QR code, clickable URL)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.quantlet_branding import add_quantlet_branding
add_quantlet_branding(fig, CHART_METADATA['url'])
"""

def fix_chart_file(py_file):
    """Fix import statement in chart file."""
    folder_name = py_file.parent.name
    print(f"  Fixing: {folder_name}/{py_file.name}")

    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already fixed
    if 'sys.path.insert(0, str(Path(__file__).parent.parent))' in content:
        print(f"    -> Already fixed")
        return False

    # Replace old import with new one
    old_pattern = r'# Add Quantlet branding \(logo, QR code, clickable URL\)\nfrom utils\.quantlet_branding import add_quantlet_branding\nadd_quantlet_branding\(fig, CHART_METADATA\[\'url\'\]\)'

    if re.search(old_pattern, content):
        new_content = re.sub(old_pattern, NEW_IMPORT_BLOCK.strip(), content)

        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"    -> Fixed import with sys.path adjustment")
        return True
    else:
        print(f"    -> Could not find import pattern")
        return False

def main():
    print("Fixing imports in all chart files...\n")

    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    fixed_count = 0
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if fix_chart_file(py_files[0]):
                fixed_count += 1

    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()
