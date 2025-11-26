"""
Sync repository to QuantLet with updated URLs.

This script:
1. Clones/updates the QuantLet neural-networks-introduction repository
2. Copies all files from current directory to QuantLet repo
3. Updates all URLs to point to QuantLet repository:
   - CHART_METADATA in Python files
   - metainfo.txt files
   - LaTeX branding overlays
   - QR codes
4. Prepares for commit (but doesn't push automatically)

Usage:
    python quantlet_tools/sync_to_quantlet.py
"""

import os
import re
import subprocess
import shutil
from pathlib import Path
import qrcode

# Configuration
QUANTLET_REPO_URL = "https://github.com/QuantLet/neural-networks-introduction.git"
QUANTLET_REPO_NAME = "neural-networks-introduction"
NEW_GITHUB_BASE = "https://github.com/QuantLet/neural-networks-introduction"

def clone_or_update_repo(target_dir):
    """Clone the QuantLet repo or pull if it already exists."""
    if target_dir.exists():
        print(f">> Repository already exists at {target_dir}")
        print(">> Pulling latest changes...")
        try:
            subprocess.run(['git', 'pull'], cwd=target_dir, check=True, capture_output=True)
            print(">> Pull successful")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Git pull failed: {e}")
            print("Continuing with existing repository state...")
    else:
        print(f">> Cloning {QUANTLET_REPO_URL}...")
        subprocess.run(['git', 'clone', QUANTLET_REPO_URL, str(target_dir)], check=True)
        print(">> Clone successful")

def copy_files(source_dir, target_dir):
    """Copy all files from source to target, excluding git folders."""
    exclude = {'.git', '__pycache__', 'temp', 'previous', QUANTLET_REPO_NAME}

    print(f"\n>> Copying files from {source_dir.name} to {target_dir.name}...")
    copied_count = 0

    for item in source_dir.iterdir():
        if item.name in exclude:
            continue

        target_path = target_dir / item.name

        try:
            if item.is_dir():
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(item, target_path)
                copied_count += 1
            else:
                shutil.copy2(item, target_path)
                copied_count += 1
        except Exception as e:
            print(f"Warning: Could not copy {item.name}: {e}")

    print(f">> Copied {copied_count} items")

def update_chart_metadata_urls(chart_dir, folder_name):
    """Update CHART_METADATA URLs in Python files."""
    new_url = f"{NEW_GITHUB_BASE}/tree/main/{folder_name}"
    updated = False

    for py_file in chart_dir.glob("*.py"):
        try:
            content = py_file.read_text(encoding='utf-8')

            # Pattern to find CHART_METADATA dictionary with 'url' field
            pattern = r"(CHART_METADATA\s*=\s*\{[^}]*'url':\s*)'[^']*'([^}]*\})"
            replacement = rf"\1'{new_url}'\2"

            new_content = re.sub(pattern, replacement, content)

            if new_content != content:
                py_file.write_text(new_content, encoding='utf-8')
                print(f"    >> Updated CHART_METADATA in {py_file.name}")
                updated = True
        except Exception as e:
            print(f"    Warning: Could not update {py_file.name}: {e}")

    return updated

def update_metainfo_urls(metainfo_file, folder_name):
    """Update URLs in metainfo.txt files if they exist."""
    if not metainfo_file.exists():
        return False

    try:
        content = metainfo_file.read_text(encoding='utf-8')

        # Update any GitHub URLs to point to new repo
        # Pattern matches: https://github.com/{org}/{repo}/tree/main/{path}
        pattern = r'https://github\.com/[^/\s]+/[^/\s]+/tree/main/([^\s]*)'

        def replace_url(match):
            path = match.group(1)
            return f"{NEW_GITHUB_BASE}/tree/main/{path}"

        new_content = re.sub(pattern, replace_url, content)

        if new_content != content:
            metainfo_file.write_text(new_content, encoding='utf-8')
            print(f"    >> Updated URLs in metainfo.txt")
            return True
    except Exception as e:
        print(f"    Warning: Could not update metainfo.txt: {e}")

    return False

def regenerate_qr_code(chart_dir, folder_name):
    """Regenerate QR code with new URL."""
    new_url = f"{NEW_GITHUB_BASE}/tree/main/{folder_name}"
    qr_path = chart_dir / "qr_code.png"

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(new_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_path)
        print(f"    >> Regenerated QR code -> {new_url}")
        return True
    except Exception as e:
        print(f"    Warning: Could not regenerate QR code: {e}")
        return False

def update_latex_branding(tex_file):
    """Update tikz overlay URLs in LaTeX files."""
    if not tex_file.exists():
        return False

    try:
        content = tex_file.read_text(encoding='utf-8')

        # Pattern to find href URLs in tikz overlays
        # Matches: \href{https://github.com/{org}/{repo}/tree/main/{path}}
        pattern = r'(\\href\{)https://github\.com/[^/]+/[^/]+/tree/main/([^}]+)(\})'
        replacement = rf'\1{NEW_GITHUB_BASE}/tree/main/\2\3'

        new_content = re.sub(pattern, replacement, content)

        if new_content != content:
            tex_file.write_text(new_content, encoding='utf-8')
            print(f"  >> Updated LaTeX branding URLs in {tex_file.name}")
            return True
    except Exception as e:
        print(f"  Warning: Could not update {tex_file.name}: {e}")

    return False

def main():
    source_dir = Path.cwd()
    target_dir = source_dir.parent / QUANTLET_REPO_NAME

    print("=" * 70)
    print("QUANTLET REPOSITORY SYNC")
    print("=" * 70)
    print(f"Source directory: {source_dir}")
    print(f"Target directory: {target_dir}")
    print(f"Target GitHub:    {NEW_GITHUB_BASE}")
    print("=" * 70)

    # Step 1: Clone or update the QuantLet repo
    print("\n[STEP 1] Clone/Update Repository")
    clone_or_update_repo(target_dir)

    # Step 2: Copy all files
    print("\n[STEP 2] Copy Files")
    copy_files(source_dir, target_dir)

    # Step 3: Update all URLs
    print("\n[STEP 3] Update URLs")

    # Find all chart folders (numbered folders)
    chart_folders = sorted([d for d in target_dir.iterdir()
                           if d.is_dir() and d.name[:2].isdigit()])

    total_updates = 0

    for chart_dir in chart_folders:
        folder_name = chart_dir.name
        print(f"\n  Processing {folder_name}...")

        # Update Python CHART_METADATA
        if update_chart_metadata_urls(chart_dir, folder_name):
            total_updates += 1

        # Update metainfo.txt
        metainfo_file = chart_dir / "metainfo.txt"
        if update_metainfo_urls(metainfo_file, folder_name):
            total_updates += 1

        # Regenerate QR code
        if regenerate_qr_code(chart_dir, folder_name):
            total_updates += 1

    # Step 4: Update LaTeX files
    print("\n[STEP 4] Update LaTeX Files")
    for tex_file in target_dir.glob("*.tex"):
        if update_latex_branding(tex_file):
            total_updates += 1

    # Summary
    print("\n" + "=" * 70)
    print("SYNC COMPLETE")
    print("=" * 70)
    print(f">> Synchronized to: {target_dir}")
    print(f">> Updated {total_updates} components")
    print(f">> All URLs now point to: {NEW_GITHUB_BASE}")
    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print(f"1. Review changes:")
    print(f"   cd {target_dir}")
    print(f"   git status")
    print(f"   git diff")
    print(f"\n2. Commit and push:")
    print(f"   git add .")
    print(f"   git commit -m \"Sync from source repository with updated QuantLet URLs\"")
    print(f"   git push")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSync cancelled by user")
    except Exception as e:
        print(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()
