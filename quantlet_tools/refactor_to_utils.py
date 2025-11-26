"""
Refactor all chart scripts to use the new utils/quantlet_branding module.

Replaces ~40 lines of branding code with 2 simple lines:
    from utils.quantlet_branding import add_quantlet_branding
    add_quantlet_branding(fig, CHART_METADATA['url'])
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# New branding code to insert
NEW_BRANDING_CODE = """
# Add Quantlet branding (logo, QR code, clickable URL)
from utils.quantlet_branding import add_quantlet_branding
add_quantlet_branding(fig, CHART_METADATA['url'])
"""

def refactor_chart_file(py_file):
    """Replace old branding code with new utils module call."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already refactored
    if 'from utils.quantlet_branding import add_quantlet_branding' in content:
        print(f"    -> Already using utils module")
        return False

    # Find and remove old branding code block
    pattern = r'# Add (?:clickable )?Quantlet (?:logo and QR code|branding).*?except Exception as e:\s+print\(f"Warning: Could not add.*?(?:logo|logo/QR code|Quantlet branding).*?\)'

    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"    -> Could not find branding code pattern")
        return False

    # Backup
    backup_path = Path('previous') / f"{py_file.name}.backup_refactor_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Replace old code with new simple call
    new_content = content[:match.start()] + NEW_BRANDING_CODE.strip() + '\n' + content[match.end():]

    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Refactored to use utils module (~40 lines -> 3 lines)")
    return True

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
    print("Refactoring all charts to use utils/quantlet_branding module...\n")

    # Check if utils module exists
    utils_module = Path('utils/quantlet_branding.py')
    if not utils_module.exists():
        print(f"ERROR: {utils_module} not found!")
        print("Make sure utils folder and quantlet_branding.py exist.")
        return

    config_file = Path('utils/branding_config.json')
    if not config_file.exists():
        print(f"ERROR: {config_file} not found!")
        return

    print(f"Using utils module: {utils_module}")
    print(f"Using config file:  {config_file}\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Refactor Python files
    print("="*78)
    print("PHASE 1: Refactoring chart files to use utils module")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if refactor_chart_file(py_files[0]):
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files modified. All charts may already use utils module.")
        return

    # Phase 2: Regenerate charts
    print("="*78)
    print("PHASE 2: Regenerating charts with utils module")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Refactored {len(modified_files)} files, regenerated {success_count} charts")
    print(f"")
    print(f"Benefits of new structure:")
    print(f"  - Clean code: ~3 lines instead of ~40 lines")
    print(f"  - Reusable: Can be imported into any chart script")
    print(f"  - Centralized config: Change once in branding_config.json")
    print(f"  - Easy to maintain and update")
    print(f"")
    print(f"Module location: utils/quantlet_branding.py")
    print(f"Config location: utils/branding_config.json")
    print("="*78)

if __name__ == '__main__':
    main()
