"""
Fix QR code opacity to match branding guidelines (0.8 instead of 1.0)
Logo stays at 1.0, QR code should be 0.8
"""

import re
from pathlib import Path

project_root = Path(__file__).parent

def fix_qr_opacity():
    """Fix QR code opacity in all module tex files."""
    modules = [
        'module1_perceptron',
        'module2_mlp',
        'module3_training',
        'module4_applications',
    ]

    print("Fixing QR code opacity (1.0 -> 0.8)...")
    print("=" * 50)

    total_fixed = 0

    for module in modules:
        module_dir = project_root / module
        tex_files = list(module_dir.glob('*0829*.tex'))

        for tex_file in tex_files:
            content = tex_file.read_text(encoding='utf-8')
            original = content

            # Pattern: QR Code node with opacity=1.0 (xshift=-1.3cm identifies QR code)
            # Logo is at xshift=-0.3cm, QR code is at xshift=-1.3cm
            content = content.replace(
                'xshift=-1.3cm,yshift=0.6cm,opacity=1.0',
                'xshift=-1.3cm,yshift=0.6cm,opacity=0.8'
            )

            if content != original:
                tex_file.write_text(content, encoding='utf-8')
                # Count fixes
                fixes = content.count('xshift=-1.3cm,yshift=0.6cm,opacity=0.8')
                print(f"  [OK] {tex_file.name}: {fixes} QR codes fixed")
                total_fixed += fixes

    print("\n" + "=" * 50)
    print(f"Total QR codes fixed: {total_fixed}")
    print("QR codes now at 80% opacity per guidelines.")

if __name__ == '__main__':
    fix_qr_opacity()
