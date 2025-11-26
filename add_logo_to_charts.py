"""
Script to add Quantlet logo to all chart Python files and regenerate PDFs.
Adds logo display code before plt.savefig() in each chart script.
"""
import os
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

LOGO_CODE = """
# Add Quantlet logo at bottom right
try:
    from PIL import Image
    from pathlib import Path
    logo_path = Path(__file__).parent.parent / 'logo' / 'quantlet.tiff'
    if logo_path.exists():
        logo_img = Image.open(logo_path)
        # Create inset axis for logo at bottom right
        ax_logo = fig.add_axes([0.87, 0.02, 0.11, 0.11], anchor='SE', zorder=1000)
        ax_logo.imshow(logo_img)
        ax_logo.axis('off')
except Exception as e:
    print(f"Warning: Could not add logo - {e}")
"""

def add_logo_to_chart_file(py_file):
    """Add logo code to a chart Python file before plt.savefig()."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if logo code already exists
    if 'Add Quantlet logo' in content or 'quantlet.tiff' in content.lower():
        print(f"    -> Already has logo code, skipping")
        return False

    # Find plt.savefig() line
    savefig_pattern = r'(plt\.tight_layout\(\)\s*\n)(plt\.savefig\()'
    match = re.search(savefig_pattern, content)

    if not match:
        # Try without tight_layout
        savefig_pattern = r'(\n)(plt\.savefig\()'
        match = re.search(savefig_pattern, content)

    if not match:
        print(f"    -> WARNING: Could not find plt.savefig() line")
        return False

    # Insert logo code before savefig
    new_content = content[:match.end(1)] + LOGO_CODE + content[match.end(1):]

    # Backup original
    backup_path = Path('previous') / f"{py_file.name}.backup_logo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Write modified content
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Logo code added")
    return True

def regenerate_chart(py_file):
    """Run the Python script to regenerate the chart with logo."""
    folder_name = py_file.parent.name
    print(f"  Regenerating: {folder_name}/{py_file.name}")

    try:
        # Run the script from its folder
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"    -> Chart regenerated successfully")
            if result.stdout:
                print(f"    -> {result.stdout.strip()}")
            return True
        else:
            print(f"    -> ERROR: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"    -> ERROR: Script timed out")
        return False
    except Exception as e:
        print(f"    -> ERROR: {e}")
        return False

def main():
    """Main execution function."""
    print("Adding Quantlet logo to all chart Python files...\n")

    # Check if logo exists
    logo_path = Path('logo') / 'quantlet.tiff'
    if not logo_path.exists():
        print(f"ERROR: Logo file not found at {logo_path}")
        return

    print(f"Logo found: {logo_path}\n")

    # Find all chart folders
    base_path = Path('.')
    chart_folders = sorted([f for f in base_path.iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found!")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Add logo code to all files
    print("="*78)
    print("PHASE 1: Adding logo code to Python files")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if add_logo_to_chart_file(py_files[0]):
                modified_files.append(py_files[0])
        print()

    # Phase 2: Regenerate all charts
    print("\n" + "="*78)
    print("PHASE 2: Regenerating charts with logos")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"Logo: {logo_path}")
    print("="*78)

if __name__ == '__main__':
    main()
