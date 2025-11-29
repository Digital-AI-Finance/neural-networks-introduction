"""
Fast QR code regeneration - reads URLs from CHART_METADATA without executing scripts
"""

import qrcode
import re
from pathlib import Path

def extract_url_from_script(py_file):
    """Extract URL from CHART_METADATA without executing the script."""
    content = py_file.read_text(encoding='utf-8')

    # Look for: 'url': 'https://...'
    match = re.search(r"'url'\s*:\s*'([^']+)'", content)
    if match:
        return match.group(1)
    return None

def main():
    project_root = Path(__file__).parent

    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    generated = 0
    skipped = 0

    print("Regenerating QR codes (fast mode)")
    print("=" * 60)

    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            continue

        print(f"\n--- {module} ---")

        for chart_dir in sorted(charts_dir.iterdir()):
            if not chart_dir.is_dir():
                continue

            # Find Python script
            py_files = list(chart_dir.glob('*.py'))
            if not py_files:
                skipped += 1
                continue

            url = extract_url_from_script(py_files[0])
            if not url:
                print(f"  [SKIP] {chart_dir.name}: No URL found")
                skipped += 1
                continue

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=2,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            qr_path = chart_dir / "qr_code.png"
            img.save(qr_path)

            print(f"  [OK] {chart_dir.name}")
            generated += 1

    print("\n" + "=" * 60)
    print(f"Generated: {generated}, Skipped: {skipped}")

if __name__ == '__main__':
    main()
