"""
Update GitHub URLs and logo opacity for NeuralNetworks3 project.
- New URL: https://github.com/QuantLet/neural-networks-introduction/tree/main/{chart_name}
- Logo opacity: 0.5 -> 1.0
"""

import re
from pathlib import Path

project_root = Path(__file__).parent
NEW_BASE_URL = "https://github.com/QuantLet/neural-networks-introduction/tree/main"

def update_chart_metadata():
    """Update CHART_METADATA URLs in all chart Python scripts."""
    print("=" * 60)
    print("Step 1: Updating CHART_METADATA in chart scripts")
    print("=" * 60)

    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    updated_count = 0

    for module in modules:
        charts_dir = project_root / module / 'charts'
        if not charts_dir.exists():
            continue

        for chart_dir in sorted(charts_dir.iterdir()):
            if not chart_dir.is_dir():
                continue

            chart_name = chart_dir.name
            py_files = list(chart_dir.glob('*.py'))

            for py_file in py_files:
                content = py_file.read_text(encoding='utf-8')

                # Check if it has CHART_METADATA
                if 'CHART_METADATA' not in content:
                    continue

                # New flat URL structure
                new_url = f"{NEW_BASE_URL}/{chart_name}"

                # Replace the URL in CHART_METADATA
                # Pattern matches: 'url': '...'
                old_content = content
                content = re.sub(
                    r"('url'\s*:\s*')[^']+(')",
                    rf"\g<1>{new_url}\g<2>",
                    content
                )

                if content != old_content:
                    py_file.write_text(content, encoding='utf-8')
                    print(f"  [OK] {module}/charts/{chart_name}")
                    updated_count += 1

    print(f"\nUpdated {updated_count} chart scripts")
    return updated_count


def update_tex_files():
    """Update .tex files: URLs and logo opacity."""
    print("\n" + "=" * 60)
    print("Step 2: Updating .tex files (URLs + opacity)")
    print("=" * 60)

    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    for module in modules:
        module_dir = project_root / module
        tex_files = list(module_dir.glob('*0829*.tex'))

        for tex_file in tex_files:
            content = tex_file.read_text(encoding='utf-8')
            original = content

            # 1. Update GitHub URLs to flat structure
            # Match: https://github.com/QuantLet/NeuralNetworks/tree/main/module.../charts/chart_name
            def replace_url(m):
                # Extract chart name from the old URL
                old_url = m.group(0)
                # Get the chart name (last part of path)
                chart_name = old_url.rstrip('/').split('/')[-1]
                return f"{NEW_BASE_URL}/{chart_name}"

            content = re.sub(
                r'https://github\.com/QuantLet/NeuralNetworks/tree/main/[^}]+/charts/([^}]+)',
                lambda m: f"{NEW_BASE_URL}/{m.group(1)}",
                content
            )

            # 2. Update logo opacity from 0.5 to 1.0
            content = re.sub(
                r'opacity=0\.5',
                'opacity=1.0',
                content
            )

            if content != original:
                tex_file.write_text(content, encoding='utf-8')
                print(f"  [OK] {tex_file.name}")

    print("\nTeX files updated")


def main():
    print("Updating URLs and opacity for NeuralNetworks3")
    print("New base URL:", NEW_BASE_URL)
    print()

    # Step 1: Update chart metadata
    update_chart_metadata()

    # Step 2: Update tex files
    update_tex_files()

    print("\n" + "=" * 60)
    print("DONE! Next steps:")
    print("  1. python generate_qr_codes.py")
    print("  2. python merge_tex_files.py")
    print("  3. pdflatex the merged file")
    print("=" * 60)


if __name__ == '__main__':
    main()
