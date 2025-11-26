"""
Script to add GitHub repository URLs and metadata to all chart Python files.
Adds metadata in multiple locations: header comment, module docstring, variable, and footer.
"""
import os
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
REPO_BASE_URL = "https://github.com/Digital-AI-Finance/neural-networks/tree/main/"
AUTHOR = "Digital-AI-Finance"
LICENSE = "MIT License"

# Chart descriptions mapping (extracted from folder names)
CHART_DESCRIPTIONS = {
    '01_biological_neuron': 'Side-by-side comparison of biological and artificial neurons',
    '02_single_neuron_function': 'Mathematical computation inside a single artificial neuron',
    '03_activation_functions': 'Comparison of step function, sigmoid, ReLU, and tanh activations',
    '04_perceptron_geometry': 'Geometric interpretation of perceptron decision boundary',
    '05_training_visualization': 'Weight updates during perceptron training iterations',
    '06_mlp_architecture': 'Multi-layer perceptron structure with input, hidden, and output layers',
    '07_forward_propagation': 'Step-by-step signal flow through network layers',
    '08_backpropagation_flow': 'Error gradient flow backward through the network',
    '09_gradient_descent': 'Weight space optimization trajectory toward minimum loss',
    '10_real_application': 'Stock prediction neural network with real market data',
    '11_problem_visualization': 'XOR problem demonstrating why simple rules fail',
    '12_decision_boundary_concept': 'Linear vs curved decision boundaries comparison',
    '13_neuron_decision_maker': 'Buy/sell threshold decision visualization',
    '14_sigmoid_saturation': 'Vanishing gradient problem in sigmoid activation',
    '15_boundary_evolution': 'Real trained neural networks showing curved decision boundaries',
    '16_feature_hierarchy': 'Layer-by-layer data transformation visualization',
    '17_overfitting_underfitting': 'Training and validation loss curves for three scenarios',
    '18_learning_rate_comparison': 'Effect of learning rate on convergence speed',
    '19_confusion_matrix': 'Classification performance metrics visualization',
    '20_trading_backtest': 'Cumulative returns comparison: neural network vs buy-and-hold'
}

def get_file_creation_date(file_path):
    """Extract creation date from file system."""
    timestamp = os.path.getctime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def get_chart_name(folder_name):
    """Convert folder name to human-readable chart name."""
    # Remove number prefix and replace underscores
    name = folder_name.split('_', 1)[1] if '_' in folder_name else folder_name
    return ' '.join(word.capitalize() for word in name.split('_'))

def create_header_comment(folder_name, chart_name, description, creation_date, url):
    """Create header comment block."""
    return f'''# {'=' * 78}
# Chart: {chart_name}
# Source: {url}
# Author: {AUTHOR}
# License: {LICENSE}
# Created: {creation_date}
# {'=' * 78}

'''

def create_module_docstring(chart_name, description, url):
    """Create module docstring."""
    return f'''"""
{chart_name}

{description}

Source: {url}
"""

'''

def create_metadata_variable(folder_name, chart_name, description, creation_date, url):
    """Create CHART_METADATA module-level variable."""
    return f'''CHART_METADATA = {{
    'name': '{chart_name}',
    'url': '{url}',
    'author': '{AUTHOR}',
    'license': '{LICENSE}',
    'created': '{creation_date}',
    'description': '{description}'
}}

'''

def create_footer_comment(url):
    """Create footer comment."""
    return f'\n# Source: {url}\n'

def process_chart_file(folder_path):
    """Process a single chart Python file and add metadata."""
    folder_name = folder_path.name

    # Find the Python file in the folder
    py_files = list(folder_path.glob('*.py'))
    if not py_files:
        print(f"  WARNING: No Python file found in {folder_name}")
        return False

    py_file = py_files[0]
    print(f"  Processing: {folder_name}/{py_file.name}")

    # Extract metadata
    chart_name = get_chart_name(folder_name)
    description = CHART_DESCRIPTIONS.get(folder_name, 'Neural network visualization chart')
    creation_date = get_file_creation_date(py_file)
    url = f"{REPO_BASE_URL}{folder_name}/"

    # Read existing content
    with open(py_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Check if metadata already exists
    if 'CHART_METADATA' in original_content or '# Source: https://github.com' in original_content:
        print(f"    -> Already has metadata, skipping")
        return False

    # Build new content with metadata in all locations
    header = create_header_comment(folder_name, chart_name, description, creation_date, url)
    docstring = create_module_docstring(chart_name, description, url)
    metadata_var = create_metadata_variable(folder_name, chart_name, description, creation_date, url)
    footer = create_footer_comment(url)

    # Construct new file content
    new_content = header + docstring + metadata_var + original_content + footer

    # Backup original file
    backup_path = Path('previous') / f"{py_file.name}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path.parent.mkdir(exist_ok=True)
    shutil.copy2(py_file, backup_path)
    print(f"    -> Backup created: {backup_path}")

    # Write new content
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"    -> Metadata added successfully")
    return True

def main():
    """Main execution function."""
    print("Adding GitHub URLs and metadata to all chart Python files...\n")

    # Find all chart folders (numbered 01-20)
    base_path = Path('.')
    chart_folders = sorted([f for f in base_path.iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found!")
        return

    print(f"Found {len(chart_folders)} chart folders\n")

    # Process each folder
    processed_count = 0
    for folder in chart_folders:
        if process_chart_file(folder):
            processed_count += 1
        print()

    print(f"\n{'=' * 78}")
    print(f"COMPLETE: Processed {processed_count} of {len(chart_folders)} chart files")
    print(f"Repository: {REPO_BASE_URL}")
    print(f"{'=' * 78}")

if __name__ == '__main__':
    main()
