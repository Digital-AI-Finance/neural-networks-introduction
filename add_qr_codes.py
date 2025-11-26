"""
Script to add QR codes linking to GitHub for each chart.
Generates QR code images and modifies chart Python files to display them.
"""
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def check_qrcode_library():
    """Check if qrcode library is available, install if needed."""
    try:
        import qrcode
        print("qrcode library found\n")
        return True
    except ImportError:
        print("Installing qrcode library...")
        result = subprocess.run(
            ['pip', 'install', 'qrcode[pil]'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("qrcode library installed\n")
            return True
        else:
            print(f"ERROR: Could not install qrcode library: {result.stderr}")
            return False

def generate_qr_code(url, output_path):
    """Generate QR code image for given URL."""
    import qrcode

    qr = qrcode.QRCode(
        version=3,  # 29x29 modules (small but scannable)
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # ~15% error recovery
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    return True

# New logo + QR code block
QR_CODE_BLOCK = """
# Add Quantlet logo and QR code at bottom right
try:
    from PIL import Image
    from pathlib import Path
    from matplotlib.patches import Rectangle

    logo_path = Path(__file__).parent.parent / 'logo' / 'quantlet.tiff'
    qr_path = Path(__file__).parent / 'qr_code.png'

    if logo_path.exists():
        logo_img = Image.open(logo_path)
        chart_url = CHART_METADATA['url']

        # Logo at bottom right
        ax_logo = fig.add_axes([0.87, 0.02, 0.11, 0.11], anchor='SE', zorder=1000)
        ax_logo.imshow(logo_img)
        border = Rectangle((0, 0), 1, 1, transform=ax_logo.transAxes,
                          fill=False, edgecolor='gray', linewidth=1.5,
                          linestyle='--', alpha=0.6)
        ax_logo.add_patch(border)
        ax_logo.axis('off')

        # QR code to the left of logo
        if qr_path.exists():
            qr_img = Image.open(qr_path)
            ax_qr = fig.add_axes([0.75, 0.02, 0.10, 0.10], anchor='SE', zorder=1000)
            ax_qr.imshow(qr_img)
            ax_qr.axis('off')
except Exception as e:
    print(f"Warning: Could not add logo/QR code - {e}")
"""

def process_chart_folder(folder):
    """Generate QR code and update chart Python file."""
    folder_name = folder.name
    print(f"Processing: {folder_name}")

    # Find Python file
    py_files = list(folder.glob('*.py'))
    if not py_files:
        print(f"  -> No Python file found")
        return False

    py_file = py_files[0]

    # Read file to get URL from metadata
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract URL from CHART_METADATA
    url_match = re.search(r"'url':\s*'([^']+)'", content)
    if not url_match:
        print(f"  -> Could not find URL in metadata")
        return False

    chart_url = url_match.group(1)

    # Generate QR code
    qr_output = folder / 'qr_code.png'
    try:
        generate_qr_code(chart_url, qr_output)
        print(f"  -> QR code generated: qr_code.png")
    except Exception as e:
        print(f"  -> ERROR generating QR code: {e}")
        return False

    # Check if already has QR code in the code
    if 'qr_code.png' in content:
        print(f"  -> Already has QR code, skipping modification")
        return False

    # Replace logo code with logo + QR code
    pattern = r'# Add clickable Quantlet logo at bottom right.*?except Exception as e:\s+print\(f"Warning: Could not add clickable logo.*?\)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        # Try old pattern without "clickable"
        pattern = r'# Add Quantlet logo at bottom right.*?except Exception as e:\s+print\(f"Warning: Could not add.*?logo.*?\)'
        match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"  -> Could not find logo code pattern")
        return False

    # Backup
    backup_path = Path('previous') / f"{py_file.name}.backup_qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"  -> Backup: {backup_path.name}")

    # Replace with new code
    new_content = content[:match.start()] + QR_CODE_BLOCK.strip() + content[match.end():]

    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  -> Logo + QR code added to Python file")
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
            if 'Warning:' in result.stdout:
                print(f"    -> Warning: {result.stdout.strip()}")
                return False
            else:
                print(f"    -> Success!")
                return True
        else:
            print(f"    -> Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"    -> Error: {e}")
        return False

def main():
    """Main execution."""
    print("Adding QR codes to all chart folders...\n")

    # Check qrcode library
    if not check_qrcode_library():
        return

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Phase 1: Generate QR codes and modify files
    print("="*78)
    print("PHASE 1: Generating QR codes and updating Python files")
    print("="*78)
    modified_files = []
    for folder in chart_folders:
        if process_chart_folder(folder):
            py_files = list(folder.glob('*.py'))
            if py_files:
                modified_files.append(py_files[0])
        print()

    if not modified_files:
        print("No files modified. All charts may already have QR codes.")
        return

    # Phase 2: Regenerate charts
    print("="*78)
    print("PHASE 2: Regenerating charts with QR codes")
    print("="*78)
    success_count = 0
    for py_file in modified_files:
        if regenerate_chart(py_file):
            success_count += 1
        print()

    print("="*78)
    print(f"COMPLETE: Modified {len(modified_files)} files, regenerated {success_count} charts")
    print(f"Each chart now has a scannable QR code linking to its GitHub folder")
    print("="*78)

if __name__ == '__main__':
    main()
