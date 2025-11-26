"""
Script to make logo and QR code clickable, smaller, and positioned at very bottom right.
Updates all 20 chart Python files.
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# New clickable logo + QR code block
CLICKABLE_BLOCK = """
# Add clickable Quantlet logo and QR code at bottom right
try:
    from PIL import Image
    from pathlib import Path
    from matplotlib.patches import Rectangle

    logo_path = Path(__file__).parent.parent / 'logo' / 'quantlet.tiff'
    qr_path = Path(__file__).parent / 'qr_code.png'

    if logo_path.exists():
        logo_img = Image.open(logo_path)
        chart_url = CHART_METADATA['url']

        # Logo at very bottom right (clickable)
        ax_logo = fig.add_axes([0.90, 0.01, 0.11, 0.11], anchor='SE', zorder=1000)
        ax_logo.imshow(logo_img)

        # Visible border
        border = Rectangle((0, 0), 1, 1, transform=ax_logo.transAxes,
                          fill=False, edgecolor='gray', linewidth=1.5,
                          linestyle='--', alpha=0.6)
        ax_logo.add_patch(border)

        # Invisible clickable area
        logo_click = Rectangle((0, 0), 1, 1, transform=ax_logo.transAxes,
                              fill=False, edgecolor='none', linewidth=0,
                              url=chart_url)
        ax_logo.add_patch(logo_click)
        ax_logo.axis('off')

        # QR code to the left of logo (smaller, clickable)
        if qr_path.exists():
            qr_img = Image.open(qr_path)
            ax_qr = fig.add_axes([0.79, 0.01, 0.08, 0.08], anchor='SE', zorder=1000)
            ax_qr.imshow(qr_img)

            # Invisible clickable area
            qr_click = Rectangle((0, 0), 1, 1, transform=ax_qr.transAxes,
                                fill=False, edgecolor='none', linewidth=0,
                                url=chart_url)
            ax_qr.add_patch(qr_click)
            ax_qr.axis('off')
except Exception as e:
    print(f"Warning: Could not add logo/QR code - {e}")
"""

def update_chart_file(py_file):
    """Update chart Python file with new clickable logo/QR code."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has the new code (check for the new position)
    if 'ax_logo = fig.add_axes([0.90, 0.01' in content:
        print(f"    -> Already updated with new positioning")
        return False

    # Find and replace logo/QR code block
    pattern = r'# Add (?:clickable )?Quantlet logo and QR code at bottom right.*?except Exception as e:\s+print\(f"Warning: Could not add.*?(?:logo|logo/QR code).*?\)'

    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"    -> Could not find logo/QR code pattern")
        return False

    # Backup
    backup_path = Path('previous') / f"{py_file.name}.backup_clickable_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Replace with new code
    new_content = content[:match.start()] + CLICKABLE_BLOCK.strip() + content[match.end():]

    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Updated: smaller QR, repositioned, clickable")
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
            if 'Warning:' not in result.stdout:
                print(f"    -> Success!")
                return True
            else:
                print(f"    -> Completed with warnings")
                return True
        else:
            print(f"    -> Error: {result.stderr[:150]}")
            return False
    except Exception as e:
        print(f"    -> Error: {e}")
        return False

def main():
    """Main execution."""
    print("Making logo and QR code clickable, smaller, and repositioning...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Update Python files
    print("="*78)
    print("PHASE 1: Updating Python files with clickable, repositioned elements")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if update_chart_file(py_files[0]):
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files modified. All charts may already be updated.")
        return

    # Phase 2: Regenerate charts
    print("="*78)
    print("PHASE 2: Regenerating charts")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"Changes:")
    print(f"  - QR code: 20% smaller (0.08 width)")
    print(f"  - Logo position: [0.90, 0.01] (very bottom right)")
    print(f"  - QR position: [0.79, 0.01] (left of logo)")
    print(f"  - Both logo and QR are now clickable")
    print("="*78)

if __name__ == '__main__':
    main()
