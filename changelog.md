# NeuralNetworks3 Changelog

## 2025-11-26 - QuantLet Branding Implementation

### Added
- `quantlet_tools/` directory - Complete branding infrastructure
  - `add_latex_branding.py` - Original LaTeX branding script
  - `remove_chart_branding.py` - Branding removal tool
  - `sync_to_quantlet.py` - Repository sync tool
  - `generate_qr_codes_template.py` - QR code template
  - `generate_metainfo.py` - Metainfo generation
  - `logo/quantlet.png` - QuantLet logo
  - `utils/` - Branding utilities

- `generate_qr_codes.py` - Custom QR code generator for project structure
- `add_metadata_to_charts.py` - Automation script to add CHART_METADATA to all chart Python files
- `apply_branding_all_modules.py` - Custom branding script for module-based structure
- `fix_tikz_package.py` - Script to add tikz package to branded .tex files
- `status.md` - Project status tracking
- `changelog.md` - This file

### Modified
- 73 chart Python files - Added CHART_METADATA with title and GitHub URL
- `module1_perceptron/20251126_2217_module1.tex` - 19 frames branded
- `module2_mlp/20251126_2217_module2.tex` - 19 frames branded
- `module3_training/20251126_2217_module3.tex` - 10 frames branded
- `module4_applications/20251126_2217_module4.tex` - 1 frame branded

### Generated
- 73 QR code PNG files (one per chart with Python script)
- 4 compiled PDF files with QuantLet branding

### Backups Created
- `previous/20251126_0900_module1.tex`
- `previous/20251126_0930_module2.tex`
- `previous/20251126_1000_module3.tex`
- `previous/20251126_1030_module4.tex`

## Notes
- GitHub URLs: QuantLet/NeuralNetworks and Digital-AI-Finance/NeuralNetworks
- Branding includes: logo, QR code, clickable URL text
- 33 chart folders skipped (no Python files - placeholder folders)
