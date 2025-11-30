"""
Sync selective content to QuantLet repository.

Content rules:
- Chart folders: ALL files (Python, PDF, PNG, QR codes)
- Outside charts: ONLY latest compiled PDF
- Flatten module charts to root level

Usage:
    python sync_to_quantlet.py
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime


def get_project_root():
    return Path(__file__).parent


def get_latest_pdf(project_root):
    """Find the most recent NeuralNetworks_Complete.pdf"""
    pdfs = list(project_root.glob('*_NeuralNetworks_Complete.pdf'))
    if not pdfs:
        return None
    # Sort by modification time, get latest
    return max(pdfs, key=lambda p: p.stat().st_mtime)


def sync_to_quantlet():
    project_root = get_project_root()
    staging_dir = project_root / 'temp_quantlet'

    print("=" * 60)
    print("Syncing to QuantLet repository")
    print("=" * 60)

    # Clean staging directory
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir()

    copied_charts = 0

    # 1. Copy numbered chart folders (01_*, 02_*, etc.)
    print("\n--- Copying numbered chart folders ---")
    for folder in sorted(project_root.iterdir()):
        if folder.is_dir() and folder.name[:2].isdigit() and folder.name[2] == '_':
            dest = staging_dir / folder.name
            shutil.copytree(folder, dest)
            print(f"  [OK] {folder.name}")
            copied_charts += 1

    # 2. Flatten module*/charts/* folders to root
    print("\n--- Flattening module charts ---")
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
        'appendix'
    ]

    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            continue

        for chart_folder in sorted(charts_dir.iterdir()):
            if not chart_folder.is_dir():
                continue

            dest = staging_dir / chart_folder.name
            if dest.exists():
                print(f"  [SKIP] {chart_folder.name} (already exists)")
                continue

            shutil.copytree(chart_folder, dest)
            print(f"  [OK] {chart_folder.name} (from {module})")
            copied_charts += 1

    # 3. Copy latest compiled PDF
    print("\n--- Copying latest PDF ---")
    latest_pdf = get_latest_pdf(project_root)
    if latest_pdf:
        dest_pdf = staging_dir / 'NeuralNetworks_Complete.pdf'
        shutil.copy2(latest_pdf, dest_pdf)
        print(f"  [OK] {latest_pdf.name} -> NeuralNetworks_Complete.pdf")
    else:
        print("  [WARN] No compiled PDF found")

    # 4. Git operations
    print("\n--- Git operations ---")
    os.chdir(staging_dir)

    # Initialize git if needed
    git_dir = staging_dir / '.git'
    if not git_dir.exists():
        subprocess.run(['git', 'init'], check=True, capture_output=True)
        subprocess.run(['git', 'remote', 'add', 'origin',
                       'https://github.com/QuantLet/neural-networks-introduction.git'],
                       check=True, capture_output=True)
        print("  [OK] Git initialized")

    # Add all files
    subprocess.run(['git', 'add', '-A'], check=True, capture_output=True)

    # Check if there are changes
    result = subprocess.run(['git', 'status', '--porcelain'],
                           capture_output=True, text=True)

    if not result.stdout.strip():
        print("  [INFO] No changes to commit")
    else:
        # Commit
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        commit_msg = f"Sync charts and PDF - {timestamp}"
        subprocess.run(['git', 'commit', '-m', commit_msg],
                       check=True, capture_output=True)
        print(f"  [OK] Committed: {commit_msg}")

    # Force push to QuantLet
    print("\n--- Pushing to QuantLet ---")
    result = subprocess.run(['git', 'push', '--force', 'origin', 'main'],
                           capture_output=True, text=True)

    if result.returncode == 0:
        print("  [OK] Pushed to QuantLet")
    else:
        # Try with HEAD:main for first push
        result = subprocess.run(['git', 'push', '--force', 'origin', 'HEAD:main'],
                               capture_output=True, text=True)
        if result.returncode == 0:
            print("  [OK] Pushed to QuantLet (HEAD:main)")
        else:
            print(f"  [ERROR] Push failed: {result.stderr}")

    # Return to project root
    os.chdir(project_root)

    print("\n" + "=" * 60)
    print(f"Sync complete!")
    print(f"  Charts synced: {copied_charts}")
    print(f"  Staging dir: {staging_dir}")
    print("=" * 60)


if __name__ == '__main__':
    sync_to_quantlet()
