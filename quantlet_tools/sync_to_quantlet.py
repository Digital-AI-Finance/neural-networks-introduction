"""
Sync repository to QuantLet with updated URLs and fresh PDF compilation.

This script:
1. Clones/updates the QuantLet neural-networks-introduction repository
2. Cleans target directory and copies ONLY essential files:
   - Chart folders (01-20)
   - quantlet_tools folder
3. Updates all URLs to point to QuantLet repository:
   - CHART_METADATA in Python files
   - metainfo.txt files
   - QR codes
4. Copies latest .tex file and updates LaTeX branding
5. Compiles fresh PDF with QuantLet URLs
6. Removes .tex file (keeps only compiled PDF)
7. Prepares for commit (but doesn't push automatically)

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

def clean_target_directory(target_dir):
    """Remove all files except .git folder."""
    print(f">> Cleaning target directory (keeping .git)...")
    cleaned_count = 0

    for item in target_dir.iterdir():
        if item.name == '.git':
            continue

        try:
            if item.is_dir():
                shutil.rmtree(item)
                cleaned_count += 1
            else:
                item.unlink()
                cleaned_count += 1
        except Exception as e:
            print(f"Warning: Could not remove {item.name}: {e}")

    print(f">> Removed {cleaned_count} old items")

def copy_files(source_dir, target_dir):
    """Copy only chart folders and quantlet_tools (PDF will be compiled fresh)."""
    print(f"\n>> Copying selective files to {target_dir.name}...")
    copied_items = []

    # 1. Copy chart folders (numbered folders)
    chart_folders = sorted([d for d in source_dir.iterdir()
                           if d.is_dir() and d.name[:2].isdigit()])

    print(f">> Copying {len(chart_folders)} chart folders...")
    for chart_dir in chart_folders:
        target_path = target_dir / chart_dir.name
        try:
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(chart_dir, target_path)
            copied_items.append(chart_dir.name)
        except Exception as e:
            print(f"Warning: Could not copy {chart_dir.name}: {e}")

    # 2. Copy quantlet_tools folder
    quantlet_tools = source_dir / "quantlet_tools"
    if quantlet_tools.exists():
        print(f">> Copying quantlet_tools folder...")
        target_path = target_dir / "quantlet_tools"
        try:
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(quantlet_tools, target_path)
            copied_items.append("quantlet_tools")
        except Exception as e:
            print(f"Warning: Could not copy quantlet_tools: {e}")

    # 3. Copy .gitignore if exists
    gitignore = source_dir / ".gitignore"
    if gitignore.exists():
        print(f">> Copying .gitignore...")
        target_path = target_dir / ".gitignore"
        try:
            shutil.copy2(gitignore, target_path)
            copied_items.append(".gitignore")
        except Exception as e:
            print(f"Warning: Could not copy .gitignore: {e}")

    print(f">> Copied {len(copied_items)} items: {len(chart_folders)} charts + tools")

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

def find_latest_tex(source_dir):
    """Find the most recently modified .tex file in the source directory."""
    tex_files = list(source_dir.glob("*.tex"))
    if not tex_files:
        return None

    # Sort by modification time, newest first
    latest_tex = max(tex_files, key=lambda p: p.stat().st_mtime)
    return latest_tex

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

def compile_pdf(tex_file):
    """Compile LaTeX file to PDF using pdflatex."""
    if not tex_file.exists():
        return False

    print(f"\n>> Compiling PDF from {tex_file.name}...")

    try:
        # Run pdflatex twice for proper references
        for run in [1, 2]:
            print(f"  >> pdflatex run {run}/2...")
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_file.name],
                cwd=tex_file.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                print(f"  Warning: pdflatex run {run} had errors (but may have still produced PDF)")

        # Clean up auxiliary files
        aux_files = ['aux', 'log', 'nav', 'out', 'snm', 'toc']
        for ext in aux_files:
            aux_file = tex_file.with_suffix(f'.{ext}')
            if aux_file.exists():
                aux_file.unlink()

        # Check if PDF was created
        pdf_file = tex_file.with_suffix('.pdf')
        if pdf_file.exists():
            print(f"  >> PDF compiled successfully: {pdf_file.name}")
            return True
        else:
            print(f"  Warning: PDF was not created")
            return False

    except subprocess.TimeoutExpired:
        print(f"  Error: PDF compilation timed out")
        return False
    except Exception as e:
        print(f"  Error: Could not compile PDF: {e}")
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

    # Step 2: Clean target directory
    print("\n[STEP 2] Clean Target Directory")
    clean_target_directory(target_dir)

    # Step 3: Copy essential files
    print("\n[STEP 3] Copy Files")
    copy_files(source_dir, target_dir)

    # Step 4: Copy latest .tex file
    print("\n[STEP 4] Copy Latest .tex File")
    latest_tex = find_latest_tex(source_dir)
    if latest_tex:
        print(f">> Copying latest .tex file: {latest_tex.name}")
        target_tex = target_dir / latest_tex.name
        shutil.copy2(latest_tex, target_tex)
    else:
        print("Error: No .tex file found in source directory")
        return

    # Step 5: Update all URLs to QuantLet
    print("\n[STEP 5] Update URLs to QuantLet")

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

    # Step 6: Update LaTeX branding
    print("\n[STEP 6] Update LaTeX Branding")
    if update_latex_branding(target_tex):
        total_updates += 1

    # Step 7: Compile PDF with QuantLet links
    print("\n[STEP 7] Compile PDF")
    pdf_compiled = compile_pdf(target_tex)

    # Step 8: Clean up - remove .tex file (keep only PDF)
    if pdf_compiled:
        print("\n[STEP 8] Cleanup")
        print(f">> Removing .tex file (keeping compiled PDF)...")
        target_tex.unlink()

    # Summary
    print("\n" + "=" * 70)
    print("SYNC COMPLETE")
    print("=" * 70)
    print(f">> Synchronized to: {target_dir}")
    print(f">> Updated {total_updates} components")
    print(f">> All URLs now point to: {NEW_GITHUB_BASE}")
    if pdf_compiled:
        pdf_name = target_tex.with_suffix('.pdf').name
        print(f">> Compiled PDF: {pdf_name}")
    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print(f"1. Review changes:")
    print(f"   cd {target_dir}")
    print(f"   git status")
    print(f"   git diff")
    print(f"\n2. Commit and push:")
    print(f"   git add .")
    print(f"   git commit -m \"Update: Sync with QuantLet URLs and recompiled PDF\"")
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
