"""
Implement clickable logo and QR code using AnnotationBbox method.
This is the proper matplotlib approach for clickable images in PDFs.
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# AnnotationBbox-based clickable logo + QR code block
ANNOTATIONBBOX_BLOCK = """
# Add clickable Quantlet logo and QR code at bottom right
try:
    from PIL import Image
    from pathlib import Path
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import matplotlib.pyplot as plt

    logo_path = Path(__file__).parent.parent / 'logo' / 'quantlet.tiff'
    qr_path = Path(__file__).parent / 'qr_code.png'

    if logo_path.exists():
        chart_url = CHART_METADATA['url']

        # Load logo image
        logo_img = plt.imread(str(logo_path))

        # Create clickable logo with border (using AnnotationBbox)
        logo_offset = OffsetImage(logo_img, zoom=0.08)
        logo_box = AnnotationBbox(
            logo_offset,
            (0.95, 0.05),
            xycoords='figure fraction',
            frameon=True,
            box_alignment=(1, 0),
            bboxprops=dict(edgecolor='gray', linestyle='--', linewidth=1.5, alpha=0.6),
            url=chart_url
        )
        fig.add_artist(logo_box)

        # Create clickable QR code (right next to logo)
        if qr_path.exists():
            qr_img = plt.imread(str(qr_path))
            qr_offset = OffsetImage(qr_img, zoom=0.06)
            qr_box = AnnotationBbox(
                qr_offset,
                (0.87, 0.05),
                xycoords='figure fraction',
                frameon=False,
                box_alignment=(1, 0),
                url=chart_url
            )
            fig.add_artist(qr_box)
except Exception as e:
    print(f"Warning: Could not add logo/QR code - {e}")
"""

def update_chart_file(py_file):
    """Update chart Python file with AnnotationBbox method."""
    folder_name = py_file.parent.name
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Read file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has AnnotationBbox method
    if 'from matplotlib.offsetbox import OffsetImage, AnnotationBbox' in content:
        print(f"    -> Already using AnnotationBbox method")
        return False

    # Find and replace logo/QR code block
    pattern = r'# Add (?:clickable )?Quantlet logo and QR code at bottom right.*?except Exception as e:\s+print\(f"Warning: Could not add.*?(?:logo|logo/QR code).*?\)'

    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"    -> Could not find logo/QR code pattern")
        return False

    # Backup
    backup_path = Path('previous') / f"{py_file.name}.backup_annotationbbox_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup: {backup_path.name}")

    # Replace with AnnotationBbox code
    new_content = content[:match.start()] + ANNOTATIONBBOX_BLOCK.strip() + content[match.end():]

    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Updated: Using AnnotationBbox with url parameter")
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
    print("Implementing AnnotationBbox method for clickable logo/QR...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Update Python files
    print("="*78)
    print("PHASE 1: Updating Python files with AnnotationBbox method")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if update_chart_file(py_files[0]):
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files modified. All charts may already use AnnotationBbox.")
        return

    # Phase 2: Regenerate charts
    print("="*78)
    print("PHASE 2: Regenerating charts with AnnotationBbox method")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"")
    print(f"AnnotationBbox implementation:")
    print(f"  - Logo: zoom=0.08 at figure position (0.95, 0.05)")
    print(f"  - QR code: zoom=0.06 at figure position (0.87, 0.05)")
    print(f"  - Both use url parameter on AnnotationBbox for clickability")
    print(f"  - Cleaner code using matplotlib's recommended approach")
    print("="*78)

if __name__ == '__main__':
    main()
