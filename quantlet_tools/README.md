# Quantlet LaTeX Branding Tools

Automated tools for adding Quantlet branding (logo, QR codes, clickable URLs) to LaTeX Beamer presentations.

## Overview

These tools add branding to chart slides **at the LaTeX level** (not embedded in chart PDFs), making it easy to:
- Update branding across all slides by re-running one script
- Use the same clean chart PDFs in different presentations
- Automatically generate GitHub URLs pointing to Quantlet repository
- Support presentations with or without chart source code

## Folder Structure

```
quantlet_tools/
├── add_latex_branding.py      # Main script - adds branding to .tex files
├── sync_to_quantlet.py        # Sync repository to QuantLet with updated URLs
├── generate_metainfo.py        # Generate metainfo.txt for all charts
├── remove_chart_branding.py   # Remove embedded branding from chart scripts
├── regenerate_all_charts.py   # Regenerate chart PDFs without branding
├── utils/                      # Branding utilities (if using embedded approach)
│   ├── quantlet_branding.py
│   ├── branding_config.json
│   └── __init__.py
├── logo/
│   └── quantlet.png           # Quantlet logo
└── README.md                   # This file
```

## Quick Start

### For New Presentations

1. **Copy the quantlet_tools folder** to your presentation directory

2. **Run the branding script** on your .tex file:
   ```bash
   python quantlet_tools/add_latex_branding.py presentation.tex
   ```

3. **Compile the new .tex file**:
   ```bash
   pdflatex 20251126_XXXX_quantlet_branding.tex
   ```

Done! Your presentation now has Quantlet branding on all chart slides.

## Usage

### Basic Usage

Auto-detect latest .tex file and use current folder name as repo:
```bash
python quantlet_tools/add_latex_branding.py
```

### Specify .tex File

```bash
python quantlet_tools/add_latex_branding.py my_presentation.tex
```

### Custom Repository Name

If your Quantlet repo has a different name than the folder:
```bash
python quantlet_tools/add_latex_branding.py --repo-name DEDA_NeuralNetworks
```

### Custom Logo Path

```bash
python quantlet_tools/add_latex_branding.py --logo-path path/to/logo.png
```

## How It Works

### 1. URL Generation

The script auto-generates Quantlet GitHub URLs from chart folder names:

**Pattern:** `https://github.com/Quantlet/{repo_name}/tree/main/{chart_folder}`

**Examples:**
- Chart folder: `07_loss_landscape`
- Generated URL: `https://github.com/Quantlet/NeuralNetworks2/tree/main/07_loss_landscape`

### 2. Chart Detection

The script scans your .tex file for frames containing `\includegraphics` commands:

```latex
\begin{frame}{Title}
\includegraphics[options]{07_loss_landscape/chart.pdf}
\end{frame}
```

### 3. Branding Insertion

For each chart frame, the script adds a tikz overlay with:
- **Logo** (clickable, 50% transparent)
- **QR code** (clickable, 50% transparent)
- **URL text** (clickable, chart folder name)

All elements link to the chart's Quantlet GitHub URL.

### 4. Example Output

```latex
\begin{frame}{Loss Landscape}
\includegraphics[options]{07_loss_landscape/chart.pdf}

% Quantlet branding (auto-generated)
\begin{tikzpicture}[remember picture,overlay]
% Logo (clickable)
\node[anchor=south east,xshift=-0.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {
  \href{https://github.com/Quantlet/Repo/tree/main/07_loss_landscape}{\includegraphics[width=0.8cm]{quantlet_tools/logo/quantlet.png}}
};
% QR Code (clickable)
\node[anchor=south east,xshift=-1.3cm,yshift=0.6cm,opacity=0.5] at (current page.south east) {
  \href{https://github.com/Quantlet/Repo/tree/main/07_loss_landscape}{\includegraphics[width=0.6cm]{07_loss_landscape/qr_code.png}}
};
% URL text (clickable)
\node[anchor=south east,xshift=-0.3cm,yshift=0.2cm] at (current page.south east) {
  \href{https://github.com/Quantlet/Repo/tree/main/07_loss_landscape}{\tiny\texttt{\textcolor{gray}{07\_loss\_landscape}}}
};
\end{tikzpicture}

\end{frame}
```

## Workflow: GitHub → Quantlet

### Automated Sync to QuantLet Repository

The `sync_to_quantlet.py` script automates the process of creating a mirror repository with updated URLs:

```bash
python quantlet_tools/sync_to_quantlet.py
```

**What it does:**

1. **Clones/updates** `https://github.com/QuantLet/neural-networks-introduction.git`
2. **Copies** all files from current directory to QuantLet repo
3. **Updates all URLs** to point to QuantLet repository:
   - CHART_METADATA in Python files
   - URLs in metainfo.txt files
   - LaTeX branding overlays in .tex files
   - Regenerates all QR codes with new URLs
4. **Prepares** for commit (shows git commands to push)

**Result:** Two identical repositories with different URLs:
- **Main repo**: Original URLs (e.g., `Digital-AI-Finance/NeuralNetworks2`)
- **QuantLet repo**: QuantLet URLs (e.g., `QuantLet/neural-networks-introduction`)

**After running the script:**
```bash
cd ../neural-networks-introduction
git status    # Review changes
git diff      # Check URL updates
git add .
git commit -m "Sync from source repository with updated QuantLet URLs"
git push
```

### Manual Workflow (Alternative)

If you prefer manual control:

1. **Work in your main GitHub repo** (e.g., `Digital-AI-Finance/neural-networks`)
2. **Generate charts** with source code and metadata
3. **Run branding script** to add LaTeX-level branding
4. **Push/copy to Quantlet repo** (URLs automatically point to Quantlet)

### URL Handling

The script supports two modes:

**Mode 1: With CHART_METADATA (preferred)**
- If chart folder contains Python file with `CHART_METADATA['url']`, uses that URL
- Gives you full control over URLs

**Mode 2: Auto-generated (fallback)**
- If no Python file found, auto-generates URL from folder structure
- Pattern: `https://github.com/Quantlet/{repo_name}/tree/main/{chart_folder}`

## Chart Folder Structure

### Recommended Structure (with source code)

```
presentation/
├── 01_introduction/
│   ├── intro_chart.py          # Contains CHART_METADATA
│   ├── intro_chart.pdf
│   └── qr_code.png
├── 02_analysis/
│   ├── analysis.py
│   ├── analysis.pdf
│   └── qr_code.png
└── presentation.tex
```

### Standalone Structure (without source code)

```
presentation/
├── chart1/
│   ├── chart1.pdf
│   └── qr_code.png
├── chart2/
│   ├── chart2.pdf
│   └── qr_code.png
└── presentation.tex
```

Both work! The script auto-detects which mode to use.

## Requirements

- Python 3.6+
- LaTeX packages: `tikz`, `hyperref`

## Tips & Best Practices

### QR Codes

Generate QR codes for each chart folder using:
```bash
qrencode -o chart_folder/qr_code.png "https://github.com/Quantlet/Repo/tree/main/chart_folder"
```

Or use an online QR generator.

### Logo

The default logo path is `quantlet_tools/logo/quantlet.png`. You can:
- Replace this file with your own logo
- Use `--logo-path` to specify a different location

### Multiple Presentations

Reuse the same `quantlet_tools/` folder across presentations:
```
projects/
├── quantlet_tools/         # Shared branding tools
├── presentation1/
│   ├── charts/
│   └── slides.tex
└── presentation2/
    ├── charts/
    └── slides.tex
```

Run from each presentation folder:
```bash
python ../quantlet_tools/add_latex_branding.py
```

### Backup & Version Control

The script automatically:
- Creates backups in `previous/` folder
- Generates timestamped output files

Original files are never overwritten.

## Troubleshooting

### "No chart frames found"

**Cause:** Script couldn't find `\includegraphics` commands in your .tex file

**Solution:** Ensure your charts are included like:
```latex
\includegraphics[options]{path/to/chart.pdf}
```

### "Logo not found"

**Cause:** Logo path is incorrect

**Solution:**
- Check logo exists at `quantlet_tools/logo/quantlet.png`
- Or specify custom path: `--logo-path path/to/logo.png`

### Compilation errors

**Cause:** LaTeX can't find included files

**Solution:**
- Ensure chart PDFs and QR codes exist at specified paths
- Check logo path is correct
- Verify tikz and hyperref packages are installed

### URLs point to wrong repo

**Cause:** Script uses current folder name by default

**Solution:**
- Use `--repo-name` to specify correct Quantlet repo name:
  ```bash
  python add_latex_branding.py --repo-name DEDA_Project
  ```

## Advanced: Removing Embedded Branding

If you previously embedded branding in chart PDFs and want to switch to LaTeX-level branding:

1. **Remove branding from chart scripts:**
   ```bash
   python quantlet_tools/remove_chart_branding.py
   ```

2. **Regenerate clean charts:**
   ```bash
   python quantlet_tools/regenerate_all_charts.py
   ```

3. **Add LaTeX-level branding:**
   ```bash
   python quantlet_tools/add_latex_branding.py
   ```

## License

MIT License - Free to use and modify

## Contact

For issues or questions, please open an issue on the Quantlet GitHub repository.
