"""
Generate QR codes for all chart folders in a project

Usage:
    Copy this file to your project root and run:
    python generate_qr_codes.py

Requirements:
    pip install qrcode[pil]
"""

import qrcode
from pathlib import Path
import importlib.util
import sys


def generate_qr_codes(project_root):
    """Generate QR codes for all chart folders"""
    project_root = Path(project_root)

    # Find all numbered chart folders (01, 02, 03, etc.)
    chart_folders = sorted([d for d in project_root.iterdir()
                           if d.is_dir() and len(d.name) >= 2 and d.name[:2].isdigit()])

    print(f"Found {len(chart_folders)} chart folders")
    print("="*60)

    for chart_dir in chart_folders:
        # Find the Python script in the folder
        py_files = list(chart_dir.glob("*.py"))
        if not py_files:
            print(f"[SKIP] {chart_dir.name}: No Python file found")
            continue

        py_file = py_files[0]

        try:
            # Load the script to get CHART_METADATA
            spec = importlib.util.spec_from_file_location("chart", py_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules["chart"] = module
            spec.loader.exec_module(module)

            if not hasattr(module, 'CHART_METADATA'):
                print(f"[SKIP] {chart_dir.name}: No CHART_METADATA found")
                continue

            url = module.CHART_METADATA.get('url', None)
            if not url:
                print(f"[SKIP] {chart_dir.name}: No 'url' in CHART_METADATA")
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

            # Save QR code
            qr_path = chart_dir / "qr_code.png"
            img.save(qr_path)

            print(f"[OK] {chart_dir.name}: Generated QR code")
            print(f"     URL: {url}")

        except Exception as e:
            print(f"[ERROR] {chart_dir.name}: {e}")
            continue

    print("="*60)
    print("QR code generation complete!")


if __name__ == "__main__":
    import os

    # Run from current directory
    current_dir = os.getcwd()
    print(f"Generating QR codes for project in: {current_dir}")
    print("="*60)

    generate_qr_codes(current_dir)
