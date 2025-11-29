"""
Add CHART_METADATA to all chart Python files in NeuralNetworks3 project

Usage:
    python add_metadata_to_charts.py

This script will:
1. Scan all module*/charts/ and appendix/charts/ directories
2. For each chart folder, find the main .py file
3. Generate CHART_METADATA with title and GitHub URL
4. Insert CHART_METADATA at the beginning of each .py file (after docstring/imports)
"""

import re
from pathlib import Path


# GitHub base URL
GITHUB_BASE = "https://github.com/QuantLet/NeuralNetworks/tree/main"


def folder_name_to_title(folder_name):
    """Convert folder_name to Title Case

    Examples:
        'perceptron_architecture' -> 'Perceptron Architecture'
        'mlp_architecture_2_3_1' -> 'MLP Architecture 2 3 1'
        'xor_problem' -> 'XOR Problem'
    """
    # Special abbreviations to keep uppercase
    abbreviations = {'mlp', 'xor', 'mse', 'l1', 'l2', '2d', '3d', 'ai'}

    words = folder_name.split('_')
    title_words = []

    for word in words:
        if word.lower() in abbreviations:
            title_words.append(word.upper())
        else:
            title_words.append(word.capitalize())

    return ' '.join(title_words)


def has_chart_metadata(content):
    """Check if file already has CHART_METADATA"""
    return 'CHART_METADATA' in content


def add_metadata_to_file(py_file, module_name, chart_name):
    """Add CHART_METADATA to a Python file"""

    # Read the file
    with open(py_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has metadata
    if has_chart_metadata(content):
        return False, "Already has CHART_METADATA"

    # Generate metadata
    title = folder_name_to_title(chart_name)
    url = f"{GITHUB_BASE}/{module_name}/charts/{chart_name}"

    metadata_block = f'''CHART_METADATA = {{
    'title': '{title}',
    'url': '{url}'
}}

'''

    # Find the best insertion point (after initial docstring and imports)
    lines = content.split('\n')
    insert_line = 0
    in_docstring = False
    docstring_char = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track multi-line docstrings
        if not in_docstring:
            if stripped.startswith('"""') or stripped.startswith("'''"):
                docstring_char = stripped[:3]
                if stripped.count(docstring_char) >= 2 and len(stripped) > 6:
                    # Single-line docstring
                    insert_line = i + 1
                else:
                    in_docstring = True
                continue
        else:
            if docstring_char in stripped:
                in_docstring = False
                insert_line = i + 1
            continue

        # Skip imports and blank lines at the start
        if stripped.startswith('import ') or stripped.startswith('from '):
            insert_line = i + 1
            continue
        elif stripped == '':
            continue
        else:
            # Found actual code, stop here
            break

    # Insert metadata
    lines.insert(insert_line, '')
    lines.insert(insert_line + 1, metadata_block.rstrip())

    # Write back
    new_content = '\n'.join(lines)

    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"Added metadata: {title}"


def process_all_charts(project_root):
    """Process all chart files in the project"""
    project_root = Path(project_root)

    # Module directories to scan
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
        'appendix'
    ]

    total_added = 0
    total_skipped = 0
    total_errors = 0

    print(f"Adding CHART_METADATA to charts in: {project_root}")
    print("=" * 60)

    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            print(f"[SKIP] Module {module}: No charts directory found")
            continue

        print(f"\n--- {module} ---")

        # Find all chart folders
        chart_folders = sorted([d for d in charts_dir.iterdir() if d.is_dir()])

        for chart_dir in chart_folders:
            chart_name = chart_dir.name

            # Find the Python script (same name as folder)
            py_file = chart_dir / f"{chart_name}.py"
            if not py_file.exists():
                # Try finding any .py file
                py_files = list(chart_dir.glob("*.py"))
                if not py_files:
                    print(f"  [SKIP] {chart_name}: No Python file found")
                    total_skipped += 1
                    continue
                py_file = py_files[0]

            try:
                success, message = add_metadata_to_file(py_file, module, chart_name)
                if success:
                    print(f"  [OK] {chart_name}")
                    total_added += 1
                else:
                    print(f"  [SKIP] {chart_name}: {message}")
                    total_skipped += 1

            except Exception as e:
                print(f"  [ERROR] {chart_name}: {e}")
                total_errors += 1

    print("\n" + "=" * 60)
    print(f"CHART_METADATA addition complete!")
    print(f"  Added: {total_added}")
    print(f"  Skipped: {total_skipped}")
    print(f"  Errors: {total_errors}")


if __name__ == "__main__":
    project_root = Path(__file__).parent
    process_all_charts(project_root)
