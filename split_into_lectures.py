"""
Split neural networks content into 8 topic-based lectures.

Reads 4 module .tex files and creates 8 lecture files with ~28 slides each.
"""

import re
import os
import subprocess
from pathlib import Path
from datetime import datetime


# Lecture definitions: (filename, title, [(module, section_name), ...])
LECTURES = [
    (
        'history_biological_inspiration',
        'History and Biological Inspiration',
        [
            ('module1_perceptron', 'Opening'),
            ('module1_perceptron', 'Historical Context: 1943-1969'),
            ('module1_perceptron', 'Biological Inspiration'),
        ]
    ),
    (
        'perceptron_fundamentals',
        'Perceptron Fundamentals',
        [
            ('module1_perceptron', 'The Perceptron: Intuition First'),
            ('module1_perceptron', 'The Perceptron: Mathematical Formulation'),
            ('module1_perceptron', 'The Perceptron Learning Algorithm'),
            ('module1_perceptron', 'Limitations and the First AI Winter'),
            ('module1_perceptron', 'Summary and Preview'),
        ]
    ),
    (
        'mlp_architecture',
        'Multi-Layer Perceptron Architecture',
        [
            ('module2_mlp', 'Opening'),
            ('module2_mlp', 'Historical Context: 1969-1986'),
            ('module2_mlp', 'MLP Architecture: Intuition'),
            ('module2_mlp', 'MLP Architecture: Mathematical Formulation'),
        ]
    ),
    (
        'activation_loss_functions',
        'Activation and Loss Functions',
        [
            ('module2_mlp', 'Activation Functions'),
            ('module2_mlp', 'Universal Approximation'),
            ('module2_mlp', 'Loss Functions'),
            ('module2_mlp', 'Summary and Preview'),
        ]
    ),
    (
        'gradient_descent_backprop',
        'Gradient Descent and Backpropagation',
        [
            ('module3_training', 'Opening'),
            ('module3_training', 'Historical Context: 1986-2012'),
            ('module3_training', 'Loss Functions: Measuring Mistakes'),
            ('module3_training', 'Gradient Descent: Finding the Minimum'),
            ('module3_training', 'Backpropagation: Credit Assignment'),
        ]
    ),
    (
        'training_regularization',
        'Training Dynamics and Regularization',
        [
            ('module3_training', 'Training Dynamics'),
            ('module3_training', 'Overfitting: The Enemy of Generalization'),
            ('module3_training', 'Summary and Preview'),
            ('module4_applications', 'Opening'),
            ('module4_applications', 'Regularization: Fighting Overfitting'),
        ]
    ),
    (
        'financial_applications',
        'Financial Applications',
        [
            ('module4_applications', 'Historical Context: 2012-Present'),
            ('module4_applications', 'Financial Data Challenges'),
            ('module4_applications', 'Case Study: Stock Prediction'),
        ]
    ),
    (
        'modern_networks_future',
        'Modern Networks and Future Directions',
        [
            ('module4_applications', 'Modern Architectures'),
            ('module4_applications', 'Limitations and Ethical Considerations'),
            ('module4_applications', 'Synthesis and Future'),
        ]
    ),
]


def get_project_root():
    return Path(__file__).parent


def get_tex_file(module):
    """Find the tex file for a module."""
    project_root = get_project_root()
    module_dir = project_root / module
    tex_files = list(module_dir.glob('*0829*.tex'))
    if tex_files:
        return tex_files[0]
    return None


def extract_preamble(content):
    """Extract preamble (before \\begin{document})."""
    match = re.search(r'^(.*?)\\begin\{document\}', content, re.DOTALL)
    if match:
        return match.group(1)
    return ''


def parse_sections(content):
    """Parse content into sections with their frames."""
    # Find document body
    match = re.search(r'\\begin\{document\}(.*)\\end\{document\}', content, re.DOTALL)
    if not match:
        return {}

    body = match.group(1)

    sections = {}
    current_section = None
    current_content = []

    # Split by section markers
    parts = re.split(r'(\\section\{[^}]+\})', body)

    for part in parts:
        section_match = re.match(r'\\section\{([^}]+)\}', part)
        if section_match:
            # Save previous section
            if current_section:
                sections[current_section] = ''.join(current_content)
            current_section = section_match.group(1)
            current_content = []
        else:
            if current_section:
                current_content.append(part)

    # Save last section
    if current_section:
        sections[current_section] = ''.join(current_content)

    return sections


def fix_chart_paths(content, module):
    """Fix chart paths to include module prefix."""
    # Fix paths like charts/chart_name/ to ../module/charts/chart_name/
    content = re.sub(
        r'\{charts/',
        f'{{../{module}/charts/',
        content
    )
    # Fix quantlet_tools path
    content = content.replace('../quantlet_tools/', '../../quantlet_tools/')
    content = content.replace('{quantlet_tools/', '{../quantlet_tools/')

    return content


def create_lecture_content(lecture_name, lecture_title, sections_list, all_sections, preamble):
    """Create a complete lecture .tex file."""

    # Modify preamble for this lecture
    modified_preamble = preamble

    # Update title
    modified_preamble = re.sub(
        r'\\title\{[^}]+\}',
        f'\\\\title{{{lecture_title}}}',
        modified_preamble
    )

    # Update subtitle
    modified_preamble = re.sub(
        r'\\subtitle\{[^}]+\}',
        f'\\\\subtitle{{Neural Networks for Finance}}',
        modified_preamble
    )

    # Build content
    content_parts = []

    for module, section_name in sections_list:
        key = (module, section_name)
        if key in all_sections:
            section_content = all_sections[key]
            # Fix chart paths for this module
            section_content = fix_chart_paths(section_content, module)
            # Add section header
            content_parts.append(f'\n\\section{{{section_name}}}\n')
            content_parts.append(section_content)
        else:
            print(f"  [WARN] Section not found: {module}/{section_name}")

    # Assemble document
    document = modified_preamble
    document += '\\begin{document}\n'
    document += ''.join(content_parts)
    document += '\n\\end{document}\n'

    return document


def count_frames(content):
    """Count number of frames in content."""
    return len(re.findall(r'\\begin\{frame\}', content))


def split_into_lectures():
    project_root = get_project_root()
    lectures_dir = project_root / 'lectures'
    lectures_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("Splitting into 8 topic-based lectures")
    print("=" * 60)

    # Load all module content
    modules = ['module1_perceptron', 'module2_mlp', 'module3_training', 'module4_applications']
    all_sections = {}
    preamble = None

    print("\n--- Loading modules ---")
    for module in modules:
        tex_file = get_tex_file(module)
        if not tex_file:
            print(f"  [SKIP] {module}: No tex file found")
            continue

        content = tex_file.read_text(encoding='utf-8')

        # Get preamble from first module
        if preamble is None:
            preamble = extract_preamble(content)

        # Parse sections
        sections = parse_sections(content)
        for section_name, section_content in sections.items():
            all_sections[(module, section_name)] = section_content
            frame_count = count_frames(section_content)
            print(f"  [OK] {module}/{section_name}: {frame_count} frames")

    print(f"\nTotal sections loaded: {len(all_sections)}")

    # Create lectures
    print("\n--- Creating lectures ---")

    for lecture_name, lecture_title, sections_list in LECTURES:
        lecture_content = create_lecture_content(
            lecture_name, lecture_title, sections_list, all_sections, preamble
        )

        frame_count = count_frames(lecture_content)

        # Write tex file
        tex_path = lectures_dir / f'{lecture_name}.tex'
        tex_path.write_text(lecture_content, encoding='utf-8')

        print(f"  [OK] {lecture_name}.tex: {frame_count} slides")

    print("\n" + "=" * 60)
    print(f"Created 8 lecture files in: {lectures_dir}")
    print("\nTo compile all lectures:")
    print("  cd lectures && for f in *.tex; do pdflatex $f; done")
    print("=" * 60)

    return lectures_dir


def compile_lectures(lectures_dir):
    """Compile all lecture tex files to PDF."""
    print("\n--- Compiling PDFs ---")

    os.chdir(lectures_dir)

    for tex_file in sorted(lectures_dir.glob('*.tex')):
        print(f"  Compiling {tex_file.name}...", end=' ', flush=True)
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_file.name],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                print("[OK]")
            else:
                print("[ERROR]")
        except Exception as e:
            print(f"[ERROR: {e}]")

    # Clean up auxiliary files
    for ext in ['aux', 'log', 'nav', 'out', 'snm', 'toc']:
        for f in lectures_dir.glob(f'*.{ext}'):
            f.unlink()

    print("\nCompilation complete!")


if __name__ == '__main__':
    import sys

    lectures_dir = split_into_lectures()

    if '--compile' in sys.argv:
        compile_lectures(lectures_dir)
