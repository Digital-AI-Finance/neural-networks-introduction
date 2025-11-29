# QuantLet Branding Guide

## How to Add QuantLet Logo/QR/URL to Any LaTeX Project with Charts

This guide explains how to automatically add QuantLet branding (logo + QR code + URL) to any LaTeX presentation with chart folders.

---

## Prerequisites

Your project should have:
- LaTeX file(s) with `\includegraphics` commands for charts
- Chart folders (numbered: 01, 02, 03, etc.)
- Each chart folder contains a Python script that generates a PDF

---

## Step 1: Copy the `quantlet_tools` Folder

Copy the entire `quantlet_tools/` folder to your project root:

```
your_project/
├── quantlet_tools/
│   ├── add_latex_branding.py
│   ├── logo/
│   │   └── quantlet.png
│   └── BRANDING_GUIDE.md
├── 01_your_chart/
├── 02_another_chart/
└── your_slides.tex
```

---

## Step 2: Update Chart Metadata

Each chart Python script must have a `CHART_METADATA` dictionary with the GitHub URL:

```python
# At the top of your chart script (e.g., 01_your_chart/your_chart.py)
CHART_METADATA = {
    'title': 'Your Chart Title',
    'url': 'https://github.com/YourOrg/your-repo/tree/main/01_your_chart'
}
```

The `url` must point to the specific chart folder on GitHub.

---

## Step 3: Generate QR Codes

Run this script to generate QR codes for all chart folders:

```python
# generate_qr_codes.py (create in project root)
import qrcode
from pathlib import Path
import importlib.util
import sys

def generate_qr_codes(project_root):
    """Generate QR codes for all chart folders"""
    project_root = Path(project_root)

    # Find all numbered chart folders
    chart_folders = sorted([d for d in project_root.iterdir()
                           if d.is_dir() and d.name[:2].isdigit()])

    print(f"Found {len(chart_folders)} chart folders")

    for chart_dir in chart_folders:
        # Find the Python script
        py_files = list(chart_dir.glob("*.py"))
        if not py_files:
            print(f"No Python file in {chart_dir.name}, skipping")
            continue

        py_file = py_files[0]

        # Load the script to get CHART_METADATA
        spec = importlib.util.spec_from_file_location("chart", py_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules["chart"] = module
        spec.loader.exec_module(module)

        if not hasattr(module, 'CHART_METADATA'):
            print(f"No CHART_METADATA in {py_file.name}, skipping")
            continue

        url = module.CHART_METADATA['url']

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        qr_path = chart_dir / "qr_code.png"
        img.save(qr_path)
        print(f"Generated QR code: {qr_path}")

if __name__ == "__main__":
    generate_qr_codes(".")
    print("QR code generation complete!")
```

Run it:
```bash
python generate_qr_codes.py
```

---

## Step 4: Add Branding to LaTeX

Run the branding script:

```bash
cd quantlet_tools
python add_latex_branding.py
```

This will:
1. Find all `.tex` files in the parent directory
2. Find all `\includegraphics` commands that reference chart folders
3. Add tikz overlay with logo + QR + URL after each chart frame

### What Gets Added

After each frame with a chart, this tikz code is inserted:

```latex
% Quantlet branding (auto-generated)
\begin{tikzpicture}[remember picture, overlay]
  % Logo (bottom left)
  \node[anchor=south west, inner sep=0pt] at ([xshift=0.3cm, yshift=0.3cm]current page.south west) {
    \includegraphics[width=2cm]{quantlet_tools/logo/quantlet.png}
  };

  % QR code (bottom right)
  \node[anchor=south east, inner sep=0pt] at ([xshift=-0.3cm, yshift=0.3cm]current page.south east) {
    \includegraphics[width=1.5cm]{01_chart_folder/qr_code.png}
  };

  % URL text (below QR code)
  \node[anchor=north east, font=\tiny] at ([xshift=-0.3cm, yshift=0.25cm]current page.south east) {
    \texttt{github.com/.../01\_chart\_folder}
  };
\end{tikzpicture}
```

---

## Step 5: Compile LaTeX

Compile your LaTeX file as usual:

```bash
pdflatex your_slides.tex
```

The branding will appear on every chart slide!

---

## Customization

### Logo Position

Edit `add_latex_branding.py`, line with logo node:

```python
# Current: bottom left
\node[anchor=south west, inner sep=0pt] at ([xshift=0.3cm, yshift=0.3cm]current page.south west)

# To change position, modify: xshift, yshift, or anchor point
# Examples:
# Top left: anchor=north west, current page.north west
# Top right: anchor=north east, current page.north east
```

### Logo Size

Change `width=2cm` to your desired size:

```python
\includegraphics[width=2cm]{quantlet_tools/logo/quantlet.png}
#                    ^^^^ change this
```

### QR Code Size

Change `width=1.5cm`:

```python
\includegraphics[width=1.5cm]{...qr_code.png}
#                    ^^^^^ change this
```

### Font Size

Change `\tiny` to `\scriptsize`, `\footnotesize`, etc.:

```python
\node[anchor=north east, font=\tiny]
#                            ^^^^^ change this
```

---

## Removing Branding

To remove all branding from `.tex` files:

```bash
cd quantlet_tools
python remove_duplicate_branding.py
```

This removes all auto-generated branding blocks (identified by `% Quantlet branding (auto-generated)` comment).

---

## For Different Repositories

### Local Repository (e.g., your main research repo)

Use your local GitHub URL pattern:

```python
CHART_METADATA = {
    'title': 'Chart Title',
    'url': 'https://github.com/YourName/your-repo/tree/main/01_chart'
}
```

### QuantLet Repository

For syncing to QuantLet:

1. Use the sync script (see `sync_to_quantlet.py`)
2. It will automatically update all URLs to QuantLet pattern:
   ```
   https://github.com/QuantLet/your-project/tree/main/01_chart
   ```

---

## Quick Reference Commands

```bash
# 1. Generate QR codes
python generate_qr_codes.py

# 2. Add branding to LaTeX
cd quantlet_tools
python add_latex_branding.py

# 3. Compile PDF
pdflatex your_slides.tex

# 4. Move aux files to temp
mkdir -p temp
mv *.aux *.log *.nav *.out *.snm *.toc temp/ 2>/dev/null

# 5. Remove branding (if needed)
cd quantlet_tools
python remove_duplicate_branding.py
```

---

## Template Project Structure

```
my_project/
├── quantlet_tools/
│   ├── add_latex_branding.py
│   ├── remove_duplicate_branding.py
│   ├── logo/
│   │   └── quantlet.png
│   └── BRANDING_GUIDE.md
├── 01_first_chart/
│   ├── first_chart.py           # Contains CHART_METADATA with URL
│   ├── first_chart.pdf          # Generated by script
│   └── qr_code.png              # Generated by generate_qr_codes.py
├── 02_second_chart/
│   ├── second_chart.py          # Contains CHART_METADATA with URL
│   ├── second_chart.pdf
│   └── qr_code.png
├── generate_qr_codes.py         # QR code generator script
├── my_slides.tex                # Your LaTeX file
├── my_slides.pdf                # Compiled output
└── temp/                        # Auxiliary files
    ├── my_slides.aux
    ├── my_slides.log
    └── ...
```

---

## Troubleshooting

### Logo not showing
- Check path: `quantlet_tools/logo/quantlet.png` exists
- Verify LaTeX can find the file (use absolute path if needed)

### QR code not showing
- Verify `qr_code.png` exists in each chart folder
- Run `generate_qr_codes.py` again

### Duplicate branding
- Run `remove_duplicate_branding.py` first
- Then run `add_latex_branding.py` again

### URL text too long
- Edit the script to use shorter URL format
- Or reduce font size in the tikz node

---

## Summary

**3 Files Needed:**
1. `quantlet_tools/add_latex_branding.py` - Adds branding
2. `quantlet_tools/logo/quantlet.png` - Logo image
3. `generate_qr_codes.py` - Generates QR codes

**3 Steps to Apply:**
1. Add `CHART_METADATA` to all chart scripts
2. Run `python generate_qr_codes.py`
3. Run `python quantlet_tools/add_latex_branding.py`

Done! Your LaTeX file now has QuantLet branding on all chart slides.
