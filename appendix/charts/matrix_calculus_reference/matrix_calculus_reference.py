"""
Matrix Calculus Reference for Neural Networks
Appendix: Mathematical Foundations
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Matrix Calculus Reference',
    'url': 'https://github.com/QuantLet/NeuralNetworks/tree/main/appendix/charts/matrix_calculus_reference'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.5, 'Matrix Calculus: Essential Rules for Neural Networks',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Sections
sections = [
    ('Vector Derivatives', mlblue, 10, [
        ('$\\frac{\\partial}{\\partial x}(Ax)$', '$= A$', 'Matrix-vector product'),
        ('$\\frac{\\partial}{\\partial x}(x^T A)$', '$= A^T$', 'Vector-matrix product'),
        ('$\\frac{\\partial}{\\partial x}(x^T x)$', '$= 2x$', 'Squared norm'),
        ('$\\frac{\\partial}{\\partial x}(x^T A x)$', '$= (A + A^T)x$', 'Quadratic form'),
    ]),
    ('Chain Rule', mlorange, 6.5, [
        ('$\\frac{\\partial L}{\\partial W}$', '$= \\frac{\\partial L}{\\partial y} \\cdot \\frac{\\partial y}{\\partial W}$', 'Scalar through matrix'),
        ('$\\frac{\\partial L}{\\partial x}$', '$= W^T \\frac{\\partial L}{\\partial y}$', 'Through linear layer'),
        ('$\\frac{\\partial L}{\\partial W}$', '$= \\frac{\\partial L}{\\partial y} x^T$', 'Weight gradient'),
    ]),
    ('Common Layer Gradients', mlgreen, 3, [
        ('Linear: $y = Wx + b$', '$\\frac{\\partial L}{\\partial W} = \\delta x^T$', '$\\frac{\\partial L}{\\partial b} = \\delta$'),
        ('Sigmoid: $y = \\sigma(z)$', '$\\frac{\\partial L}{\\partial z} = \\delta \\odot \\sigma(z)(1-\\sigma(z))$', ''),
        ('ReLU: $y = \\max(0,z)$', '$\\frac{\\partial L}{\\partial z} = \\delta \\odot \\mathbf{1}_{z>0}$', ''),
    ]),
]

for title, color, y, items in sections:
    # Section header
    header_box = FancyBboxPatch((0.5, y - 0.2), 13, 0.6, boxstyle="round,pad=0.02",
                                 facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(header_box)
    ax.text(7, y + 0.1, title, ha='center', fontsize=11, fontweight='bold', color=color)

    # Items
    for i, item in enumerate(items):
        row_y = y - 0.8 - i * 0.6
        if len(item) == 3:
            ax.text(0.8, row_y, item[0], fontsize=9, color=mlgray)
            ax.text(5, row_y, item[1], fontsize=9, color=color)
            ax.text(10, row_y, item[2], fontsize=8, color=mlgray, style='italic')

# Bottom notes
notes_box = FancyBboxPatch((0.5, 0.3), 13, 1.2, boxstyle="round,pad=0.1",
                            facecolor='white', edgecolor=mlpurple, linewidth=2)
ax.add_patch(notes_box)

ax.text(7, 1.1, 'Key Conventions', fontsize=10, fontweight='bold', ha='center', color=mlpurple)
ax.text(7, 0.6, '$\\delta = \\frac{\\partial L}{\\partial y}$ (upstream gradient)  |  '
              '$\\odot$ = element-wise multiplication  |  '
              'All vectors are column vectors by default',
        ha='center', fontsize=9, color=mlgray)

plt.tight_layout()
plt.savefig('matrix_calculus_reference.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('matrix_calculus_reference.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: matrix_calculus_reference.pdf")
