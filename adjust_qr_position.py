"""
Move QR code closer to logo - right next to it with no space.
Changes QR position from (0.87, 0.05) to (0.89, 0.05).
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def update_chart_file(py_file):
    """Move QR code position closer to logo."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already at new position
    if '(0.89, 0.05)' in content and 'qr_box = AnnotationBbox' in content:
        print(f"    -> QR already at new position")
        return False

    # Replace QR position
    old_pattern = r'qr_box = AnnotationBbox\(\s+qr_offset,\s+\(0\.87, 0\.05\),'
    new_text = 'qr_box = AnnotationBbox(\n                qr_offset,\n                (0.89, 0.05),'

    if re.search(old_pattern, content):
        # Backup
        backup_path = Path('previous') / f"{py_file.name}.backup_qrpos_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_path.parent.mkdir(exist_ok=True)
        shutil.copy2(py_file, backup_path)
        print(f"    -> Backup: {backup_path.name}")

        # Replace
        new_content = re.sub(old_pattern, new_text, content)

        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"    -> QR moved from (0.87, 0.05) to (0.89, 0.05)")
        return True
    else:
        print(f"    -> Could not find QR position pattern")
        return False

def regenerate_chart(py_file):
    """Regenerate chart PDF."""
    folder_name = py_file.parent.name
    print(f"  Regenerating: {folder_name}")

    try:
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"    -> Success!")
            return True
        else:
            print(f"    -> Error: {result.stderr[:150]}")
            return False
    except Exception as e:
        print(f"    -> Error: {e}")
        return False

def main():
    """Main execution."""
    print("Moving QR code closer to logo (no space)...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Update Python files
    print("="*78)
    print("PHASE 1: Adjusting QR code position")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if update_chart_file(py_files[0]):
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files modified. All QR codes may already be at new position.")
        return

    # Phase 2: Regenerate charts
    print("="*78)
    print("PHASE 2: Regenerating charts with adjusted QR position")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"")
    print(f"QR code position adjusted:")
    print(f"  - Old position: (0.87, 0.05)")
    print(f"  - New position: (0.89, 0.05) - right next to logo")
    print("="*78)

if __name__ == '__main__':
    main()
