"""
Generate QR codes for all chart folders in NeuralNetworks3 project

Usage:
    python generate_qr_codes.py

Requirements:
    pip install qrcode[pil]
"""

import qrcode
from pathlib import Path
import importlib.util
import sys


def generate_qr_codes(project_root):
    """Generate QR codes for all chart folders across all modules"""
    project_root = Path(project_root)

    # Module directories to scan
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
        'appendix'
    ]

    total_generated = 0
    total_skipped = 0

    print(f"Generating QR codes for project in: {project_root}")
    print("=" * 60)

    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            print(f"[SKIP] Module {module}: No charts directory found")
            continue

        print(f"\n--- {module} ---")

        # Find all chart folders
        chart_folders = sorted([d for d in charts_dir.iterdir() if d.is_dir()])

        for chart_dir in chart_folders:
            # Find the Python script in the folder (same name as folder)
            py_file = chart_dir / f"{chart_dir.name}.py"
            if not py_file.exists():
                # Try finding any .py file
                py_files = list(chart_dir.glob("*.py"))
                if not py_files:
                    print(f"  [SKIP] {chart_dir.name}: No Python file found")
                    total_skipped += 1
                    continue
                py_file = py_files[0]

            try:
                # Load the script to get CHART_METADATA
                spec = importlib.util.spec_from_file_location("chart", py_file)
                module_obj = importlib.util.module_from_spec(spec)
                sys.modules["chart"] = module_obj
                spec.loader.exec_module(module_obj)

                if not hasattr(module_obj, 'CHART_METADATA'):
                    print(f"  [SKIP] {chart_dir.name}: No CHART_METADATA found")
                    total_skipped += 1
                    continue

                url = module_obj.CHART_METADATA.get('url', None)
                if not url:
                    print(f"  [SKIP] {chart_dir.name}: No 'url' in CHART_METADATA")
                    total_skipped += 1
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

                print(f"  [OK] {chart_dir.name}")
                total_generated += 1

            except Exception as e:
                print(f"  [ERROR] {chart_dir.name}: {e}")
                total_skipped += 1
                continue

    print("\n" + "=" * 60)
    print(f"QR code generation complete!")
    print(f"  Generated: {total_generated}")
    print(f"  Skipped: {total_skipped}")


if __name__ == "__main__":
    import os

    # Run from project root
    project_root = Path(__file__).parent
    generate_qr_codes(project_root)
