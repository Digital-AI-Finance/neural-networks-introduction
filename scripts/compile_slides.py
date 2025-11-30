# Compile all slide modules
# Run from: D:/Joerg/Research/slides/NeuralNetworks3

import subprocess
import os
from pathlib import Path

base_dir = Path("D:/Joerg/Research/slides/NeuralNetworks3")

modules = [
    ("module1_perceptron", "20251126_0900_module1.tex"),
    ("module2_mlp", "20251126_0930_module2.tex"),
    ("module3_training", "20251126_1000_module3.tex"),
    ("module4_applications", "20251126_1030_module4.tex"),
    ("appendix", "20251126_1100_appendix.tex"),
]

# First, try to remove existing PDFs
print("=== Removing existing PDFs ===")
for module_dir, tex_file in modules:
    pdf_name = tex_file.replace(".tex", ".pdf")
    pdf_path = base_dir / module_dir / pdf_name
    try:
        if pdf_path.exists():
            os.remove(pdf_path)
            print(f"Removed: {pdf_path}")
    except Exception as e:
        print(f"Could not remove {pdf_path}: {e}")

# Compile each module
print("\n=== Compiling Slides ===")
for module_dir, tex_file in modules:
    work_dir = base_dir / module_dir
    print(f"\nCompiling: {tex_file}")

    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=120
        )

        pdf_name = tex_file.replace(".tex", ".pdf")
        pdf_path = work_dir / pdf_name

        if pdf_path.exists():
            print(f"  SUCCESS: {pdf_path}")
        else:
            print(f"  FAILED: PDF not created")
            # Show last few lines of log
            log_file = work_dir / tex_file.replace(".tex", ".log")
            if log_file.exists():
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines[-20:]:
                        if "!" in line or "Error" in line:
                            print(f"    {line.strip()}")

        # Move auxiliary files to temp
        temp_dir = work_dir / "temp"
        temp_dir.mkdir(exist_ok=True)
        for ext in [".aux", ".log", ".nav", ".out", ".snm", ".toc"]:
            aux_file = work_dir / tex_file.replace(".tex", ext)
            if aux_file.exists():
                try:
                    aux_file.rename(temp_dir / aux_file.name)
                except:
                    pass

    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT: Compilation took too long")
    except Exception as e:
        print(f"  ERROR: {e}")

print("\n=== Summary ===")
for module_dir, tex_file in modules:
    pdf_name = tex_file.replace(".tex", ".pdf")
    pdf_path = base_dir / module_dir / pdf_name
    status = "EXISTS" if pdf_path.exists() else "MISSING"
    print(f"{module_dir}: {status}")
    if pdf_path.exists():
        print(f"  Path: {pdf_path}")
