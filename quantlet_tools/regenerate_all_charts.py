"""
Regenerate all chart PDFs without embedded branding.

This script runs each chart Python script to create clean PDFs
that will receive branding at the LaTeX level instead.
"""
import subprocess
from pathlib import Path


def regenerate_chart(py_file):
    """Regenerate a single chart PDF."""
    folder_name = py_file.parent.name
    print(f"  Regenerating: {folder_name}/{py_file.name}")

    try:
        result = subprocess.run(
            ['python', py_file.name],
            cwd=py_file.parent,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            # Check if PDF was created
            pdf_name = py_file.stem + '.pdf'
            pdf_path = py_file.parent / pdf_name
            if not pdf_path.exists():
                # Try alternative naming
                pdf_files = list(py_file.parent.glob('*.pdf'))
                if pdf_files:
                    print(f"    -> Success! ({pdf_files[0].name})")
                    return True
                else:
                    print(f"    -> WARNING: No PDF found")
                    return False
            print(f"    -> Success! ({pdf_name})")
            return True
        else:
            error_msg = result.stderr[:200] if result.stderr else result.stdout[:200]
            print(f"    -> ERROR: {error_msg}")
            return False

    except subprocess.TimeoutExpired:
        print(f"    -> ERROR: Timeout (>30s)")
        return False
    except Exception as e:
        print(f"    -> ERROR: {e}")
        return False


def main():
    """Main execution."""
    print("Regenerating all chart PDFs without embedded branding...\n")

    # Find all chart folders
    chart_folders = sorted([f for f in Path('.').iterdir()
                           if f.is_dir() and f.name[0:2].isdigit()])

    if not chart_folders:
        print("ERROR: No chart folders found")
        return

    print(f"Found {len(chart_folders)} chart folders\n")
    print("="*78)

    # Process each chart
    success_count = 0
    failed_charts = []

    for folder in chart_folders:
        py_files = list(folder.glob('*.py'))
        if py_files:
            if regenerate_chart(py_files[0]):
                success_count += 1
            else:
                failed_charts.append(folder.name)
        else:
            print(f"  WARNING: No Python file in {folder.name}")
        print()

    print("="*78)
    print(f"COMPLETE: Regenerated {success_count}/{len(chart_folders)} charts")

    if failed_charts:
        print(f"\nFailed charts:")
        for chart in failed_charts:
            print(f"  - {chart}")
        print(f"\nTip: Check errors above for details")
    else:
        print(f"\nAll charts regenerated successfully!")
        print(f"\nNext step: Run add_latex_branding.py to add branding at LaTeX level")

    print("="*78)


if __name__ == '__main__':
    main()
