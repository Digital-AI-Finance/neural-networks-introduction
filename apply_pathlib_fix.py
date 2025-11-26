"""
Quick script to add missing pathlib import to all chart files.
"""
import subprocess
from pathlib import Path

def fix_and_regenerate(py_file):
    """Fix pathlib import and regenerate chart."""
    print(f"Processing: {py_file.parent.name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already fixed
    if 'from pathlib import Path' in content and 'Add Quantlet logo' in content:
        print("  -> Already has pathlib import, skipping")
        return

    # Apply fix
    old_text = '# Add Quantlet logo at bottom right\ntry:\n    from PIL import Image\n    logo_path = Path'
    new_text = '# Add Quantlet logo at bottom right\ntry:\n    from PIL import Image\n    from pathlib import Path\n    logo_path = Path'

    new_content = content.replace(old_text, new_text)

    if new_content == content:
        print("  -> No logo code found or already fixed")
        return

    # Write fixed content
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  -> Added pathlib import")

    # Regenerate chart
    try:
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0 and 'Warning: Could not add logo' not in result.stdout:
            print("  -> Regenerated successfully with logo!")
        else:
            print(f"  -> Regeneration output: {result.stdout.strip()}")
    except Exception as e:
        print(f"  -> Error regenerating: {e}")

def main():
    print("Applying pathlib fix to all chart files...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            fix_and_regenerate(py_files[0])
        print()

    print(f"\nCOMPLETE: Processed {len(chart_folders)} charts")

if __name__ == '__main__':
    main()
