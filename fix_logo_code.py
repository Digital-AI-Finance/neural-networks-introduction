"""
Script to fix logo code in all chart files (add missing pathlib import).
"""
import re
import subprocess
from pathlib import Path

def fix_logo_code(py_file):
    """Fix logo code by adding pathlib import."""
    print(f"  Fixing: {py_file.parent.name}/{py_file.name}")

    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old logo code with fixed version
    old_pattern = r'# Add Quantlet logo at bottom right\ntry:\n    from PIL import Image\n    logo_path = Path'
    new_code = '# Add Quantlet logo at bottom right\ntry:\n    from PIL import Image\n    from pathlib import Path\n    logo_path = Path'

    if 'from pathlib import Path' in content and 'Add Quantlet logo' in content:
        print("    -> Already fixed")
        return False

    new_content = content.replace(old_pattern, new_code)

    if new_content != content:
        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("    -> Fixed import")
        return True
    else:
        print("    -> No changes needed")
        return False

def regenerate_chart(py_file):
    """Regenerate chart."""
    print(f"  Regenerating: {py_file.parent.name}/{py_file.name}")
    try:
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            # Check if there's a warning
            if 'Warning: Could not add logo' not in result.stdout:
                print("    -> Success with logo!")
                return True
            else:
                print(f"    -> Warning: {result.stdout.strip()}")
                return False
        else:
            print(f"    -> Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"    -> Error: {e}")
        return False

def main():
    print("Fixing logo code in all chart files...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    print(f"Found {len(chart_folders)} chart folders\n")

    # Fix all files
    print("="*78)
    print("PHASE 1: Fixing logo code")
    print("="*78)
    fixed_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if fix_logo_code(py_files[0]):
                fixed_files.append(py_files[0])

    # Regenerate charts
    print("\n" + "="*78)
    print("PHASE 2: Regenerating charts with corrected logo code")
    print("="*78)
    success_count = 0
    for py_file in (fixed_files if fixed_files else [f.glob('*.py').__next__() for f in chart_folders]):
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Regenerated {success_count} charts with logos")
    print("="*78)

if __name__ == '__main__':
    main()
