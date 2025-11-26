"""
Script to make Quantlet logos clickable with GitHub URLs.
Adds border/frame and clickable link to specific chart folder.
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# New clickable logo code
CLICKABLE_LOGO_CODE = """
# Add clickable Quantlet logo at bottom right
try:
    from PIL import Image
    from pathlib import Path
    from matplotlib.patches import Rectangle

    logo_path = Path(__file__).parent.parent / 'logo' / 'quantlet.tiff'
    if logo_path.exists():
        logo_img = Image.open(logo_path)

        # Get URL from metadata
        chart_url = CHART_METADATA['url']

        # Create inset axis for logo at bottom right
        ax_logo = fig.add_axes([0.87, 0.02, 0.11, 0.11], anchor='SE', zorder=1000)
        ax_logo.imshow(logo_img)

        # Add clickable border frame
        border = Rectangle((0, 0), 1, 1, transform=ax_logo.transAxes,
                          fill=False, edgecolor='gray', linewidth=1.5,
                          linestyle='--', alpha=0.6, url=chart_url)
        ax_logo.add_patch(border)
        ax_logo.axis('off')
except Exception as e:
    print(f"Warning: Could not add clickable logo - {e}")
"""

def replace_logo_code(py_file):
    """Replace existing logo code with clickable version."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has clickable logo
    if 'clickable Quantlet logo' in content or 'Rectangle' in content and 'url=chart_url' in content:
        print(f"    -> Already has clickable logo, skipping")
        return False

    # Check if logo code exists
    if '# Add Quantlet logo at bottom right' not in content:
        print(f"    -> No logo code found, skipping")
        return False

    # Find and replace logo code block
    # Pattern: from "# Add Quantlet logo" to "except Exception" line
    pattern = r'# Add Quantlet logo at bottom right.*?except Exception as e:\s+print\(f"Warning: Could not add logo.*?\)'

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"    -> Could not find logo code pattern, skipping")
        return False

    # Replace with new clickable version
    new_content = content[:match.start()] + CLICKABLE_LOGO_CODE.strip() + content[match.end():]

    # Backup original
    backup_path = Path('previous') / f"{py_file.name}.backup_clickable_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Write new content
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Added clickable logo with border")
    return True

def regenerate_chart(py_file):
    """Regenerate chart with clickable logo."""
    folder_name = py_file.parent.name
    print(f"  Regenerating: {folder_name}/{py_file.name}")

    try:
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            if 'Warning: Could not add' in result.stdout:
                print(f"    -> WARNING: {result.stdout.strip()}")
                return False
            else:
                print(f"    -> Success with clickable logo!")
                return True
        else:
            print(f"    -> ERROR: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"    -> ERROR: Timeout")
        return False
    except Exception as e:
        print(f"    -> ERROR: {e}")
        return False

def main():
    """Main execution function."""
    print("Making Quantlet logos clickable with GitHub URLs...\n")

    # Check logo exists
    logo_path = Path('logo') / 'quantlet.tiff'
    if not logo_path.exists():
        print(f"ERROR: Logo file not found at {logo_path}")
        return

    print(f"Logo found: {logo_path}\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found!")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Replace logo code
    print("="*78)
    print("PHASE 1: Adding clickable logo code with borders")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if replace_logo_code(py_files[0]):
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files were modified. All charts may already have clickable logos.")
        return

    # Phase 2: Regenerate charts
    print("\n" + "="*78)
    print("PHASE 2: Regenerating charts with clickable logos")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"Logos now link to specific chart folders on GitHub")
    print(f"Border style: Dashed gray frame around logo")
    print("="*78)

if __name__ == '__main__':
    main()
