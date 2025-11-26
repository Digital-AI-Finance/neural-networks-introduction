"""
Remove embedded branding from all chart Python scripts.

This script removes the add_quantlet_branding() calls and related imports
from all chart Python files, preparing them for LaTeX-level branding.

Keeps CHART_METADATA intact as it's needed for URL extraction.
"""
import re
import shutil
from pathlib import Path
from datetime import datetime


def remove_branding_from_chart(py_file):
    """Remove branding code block from a chart Python file."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if branding code exists
    if 'add_quantlet_branding' not in content:
        print(f"    -> No branding found, skipping")
        return False

    # Backup original
    backup_path = Path('previous') / f"{folder_name}_{py_file.name}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Pattern to match the entire branding block
    # Matches from the comment line through add_quantlet_branding call
    pattern = r'\n*# Add Quantlet branding.*?\nimport sys\nfrom pathlib import Path\nsys\.path\.insert\(0, str\(Path\(__file__\)\.parent\.parent\)\)\nfrom utils\.quantlet_branding import add_quantlet_branding\nadd_quantlet_branding\(fig, CHART_METADATA\[\'url\'\]\)\n*'

    # Remove the branding block
    new_content = re.sub(pattern, '\n', content, flags=re.DOTALL)

    # If pattern didn't match, try alternative pattern (without sys.path)
    if new_content == content:
        alt_pattern = r'\n*# Add Quantlet branding.*?\nfrom utils\.quantlet_branding import add_quantlet_branding\nadd_quantlet_branding\(fig, CHART_METADATA\[\'url\'\]\)\n*'
        new_content = re.sub(alt_pattern, '\n', content, flags=re.DOTALL)

    if new_content == content:
        print(f"    -> WARNING: Could not find branding pattern")
        return False

    # Write cleaned file
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Removed branding code")
    return True


def main():
    """Main execution."""
    print("Removing embedded branding from all chart files...\n")

    # Find all chart folders (numbered folders)
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Process each chart
    modified_count = 0
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if remove_branding_from_chart(py_files[0]):
                modified_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Removed branding from {modified_count} chart files")
    print(f"\nNext step: Run regenerate_all_charts.py to create clean chart PDFs")
    print("="*78)


if __name__ == '__main__':
    main()
