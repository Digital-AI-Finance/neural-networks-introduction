"""
Generate all chart PDFs by running each chart's Python script
"""

import subprocess
import os
from pathlib import Path

project_root = Path(__file__).parent

# All chart directories
modules = ['module1_perceptron', 'module2_mlp', 'module3_training', 'module4_applications', 'appendix']

success = 0
failed = 0

for module in modules:
    charts_dir = project_root / module / 'charts'
    if not charts_dir.exists():
        continue

    print(f"\n=== {module} ===")

    for chart_dir in sorted(charts_dir.iterdir()):
        if not chart_dir.is_dir():
            continue

        py_file = chart_dir / f"{chart_dir.name}.py"
        if not py_file.exists():
            continue

        # Check if PDF already exists
        pdf_file = chart_dir / f"{chart_dir.name}.pdf"

        try:
            os.chdir(chart_dir)
            result = subprocess.run(['python', py_file.name], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"  [OK] {chart_dir.name}")
                success += 1
            else:
                print(f"  [FAIL] {chart_dir.name}: {result.stderr[:100]}")
                failed += 1
        except Exception as e:
            print(f"  [ERROR] {chart_dir.name}: {e}")
            failed += 1

os.chdir(project_root)
print(f"\n{'='*60}")
print(f"Chart generation complete!")
print(f"  Success: {success}")
print(f"  Failed: {failed}")
