"""
Merge all module PDFs into one combined PDF
"""

from pathlib import Path
from PyPDF2 import PdfMerger
from datetime import datetime


def merge_pdfs():
    project_root = Path(__file__).parent

    # PDF files to merge in order
    pdf_files = [
        project_root / 'module1_perceptron' / '20251126_2217_module1.pdf',
        project_root / 'module2_mlp' / '20251126_2217_module2.pdf',
        project_root / 'module3_training' / '20251126_2217_module3.pdf',
        project_root / 'module4_applications' / '20251126_2217_module4.pdf',
    ]

    # Check which files exist
    existing_files = []
    for pdf in pdf_files:
        if pdf.exists():
            existing_files.append(pdf)
            print(f"[OK] Found: {pdf.name}")
        else:
            print(f"[SKIP] Not found: {pdf}")

    if not existing_files:
        print("No PDF files found!")
        return

    # Create merger
    merger = PdfMerger()

    for pdf in existing_files:
        print(f"Adding: {pdf.name}")
        merger.append(str(pdf))

    # Output filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    output_file = project_root / f'{timestamp}_NeuralNetworks_Complete.pdf'

    merger.write(str(output_file))
    merger.close()

    print(f"\nMerged PDF created: {output_file}")
    print(f"Total files merged: {len(existing_files)}")


if __name__ == '__main__':
    merge_pdfs()
