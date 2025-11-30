"""
Generate metainfo.txt files for all chart folders from CHART_METADATA.

Standard QuantLet format:
- Name
- Description
- Keywords
- Author
- Datafile
- Output
"""

import re
from pathlib import Path


def extract_metadata_from_script(py_file):
    """Extract CHART_METADATA from Python script without executing it."""
    content = py_file.read_text(encoding='utf-8')

    # Extract title
    title_match = re.search(r"'title'\s*:\s*'([^']+)'", content)
    title = title_match.group(1) if title_match else py_file.stem

    # Extract url
    url_match = re.search(r"'url'\s*:\s*'([^']+)'", content)
    url = url_match.group(1) if url_match else ''

    return {'title': title, 'url': url}


def generate_keywords(chart_name, title):
    """Generate keywords based on chart name and title."""
    keywords = set()

    # Common neural network keywords
    nn_keywords = {
        'perceptron', 'mlp', 'neural', 'network', 'activation',
        'gradient', 'backprop', 'training', 'loss', 'optimization',
        'sigmoid', 'relu', 'tanh', 'softmax', 'dropout', 'regularization',
        'overfitting', 'learning', 'rate', 'batch', 'epoch',
        'weight', 'bias', 'layer', 'hidden', 'output', 'input',
        'classification', 'regression', 'prediction', 'finance',
        'stock', 'timeline', 'architecture', 'visualization'
    }

    # Extract keywords from chart name
    words = chart_name.lower().replace('_', ' ').split()
    for word in words:
        if word in nn_keywords or len(word) > 4:
            keywords.add(word)

    # Extract keywords from title
    title_words = title.lower().replace('-', ' ').replace(':', ' ').split()
    for word in title_words:
        if word in nn_keywords:
            keywords.add(word)

    # Add some defaults
    keywords.add('neural network')
    keywords.add('visualization')

    return sorted(keywords)[:8]  # Limit to 8 keywords


def create_metainfo(chart_folder, metadata):
    """Create metainfo.txt content."""
    chart_name = chart_folder.name
    title = metadata.get('title', chart_name.replace('_', ' ').title())

    # Find output files
    outputs = []
    for ext in ['pdf', 'png']:
        files = list(chart_folder.glob(f'*.{ext}'))
        outputs.extend([f.name for f in files if f.name != 'qr_code.png'])

    # Find datafiles (if any)
    datafiles = list(chart_folder.glob('*.csv')) + list(chart_folder.glob('*.json'))

    keywords = generate_keywords(chart_name, title)

    metainfo = f"""Name of Quantlet: {chart_name}

Published in: Neural Networks Introduction - BSc Lecture Series

Description: {title}. Educational visualization for neural networks course covering fundamental concepts of deep learning and machine learning.

Keywords: {', '.join(keywords)}

Author: Joerg Osterrieder

Datafile: {', '.join([d.name for d in datafiles]) if datafiles else 'None'}

Output: {', '.join(outputs) if outputs else 'chart.pdf'}

Example: See {chart_name}.py for implementation details
"""
    return metainfo


def generate_all_metainfo():
    project_root = Path(__file__).parent

    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
        'appendix'
    ]

    generated = 0
    skipped = 0

    print("Generating metainfo.txt files...")
    print("=" * 60)

    # Process numbered chart folders at root
    print("\n--- Numbered chart folders ---")
    for folder in sorted(project_root.iterdir()):
        if folder.is_dir() and folder.name[:2].isdigit() and folder.name[2] == '_':
            py_files = list(folder.glob('*.py'))
            if py_files:
                metadata = extract_metadata_from_script(py_files[0])
                metainfo_path = folder / 'metainfo.txt'
                metainfo_path.write_text(create_metainfo(folder, metadata), encoding='utf-8')
                print(f"  [OK] {folder.name}")
                generated += 1
            else:
                print(f"  [SKIP] {folder.name} - no Python file")
                skipped += 1

    # Process module chart folders
    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            continue

        print(f"\n--- {module} ---")
        for chart_folder in sorted(charts_dir.iterdir()):
            if not chart_folder.is_dir():
                continue

            py_files = list(chart_folder.glob('*.py'))
            if py_files:
                metadata = extract_metadata_from_script(py_files[0])
                metainfo_path = chart_folder / 'metainfo.txt'
                metainfo_path.write_text(create_metainfo(chart_folder, metadata), encoding='utf-8')
                print(f"  [OK] {chart_folder.name}")
                generated += 1
            else:
                print(f"  [SKIP] {chart_folder.name} - no Python file")
                skipped += 1

    print("\n" + "=" * 60)
    print(f"Generated: {generated}, Skipped: {skipped}")


if __name__ == '__main__':
    generate_all_metainfo()
