# Check which chart PDFs are missing and generate a report.
# Run from: D:/Joerg/Research/slides/NeuralNetworks3

import os
from pathlib import Path

base_dir = Path("D:/Joerg/Research/slides/NeuralNetworks3")
modules = ["module1_perceptron", "module2_mlp", "module3_training",
           "module4_applications", "appendix"]

missing = []
existing = []

for module in modules:
    charts_dir = base_dir / module / "charts"
    if not charts_dir.exists():
        continue
    for chart_folder in sorted(charts_dir.iterdir()):
        if chart_folder.is_dir():
            py_file = chart_folder / f"{chart_folder.name}.py"
            pdf_file = chart_folder / f"{chart_folder.name}.pdf"
            if py_file.exists():
                if pdf_file.exists():
                    existing.append(str(pdf_file))
                else:
                    missing.append(str(py_file))

print(f"=== Chart Status Report ===")
print(f"Existing PDFs: {len(existing)}")
print(f"Missing PDFs: {len(missing)}")
print(f"\n=== Missing Charts by Module ===")

# Group by module
for module in modules:
    module_missing = [m for m in missing if module in m]
    if module_missing:
        print(f"\n{module}: {len(module_missing)} missing")
        for m in module_missing:
            name = Path(m).parent.name
            print(f"  - {name}")
