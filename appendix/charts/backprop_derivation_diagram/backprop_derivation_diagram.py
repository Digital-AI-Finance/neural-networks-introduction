"""
Backpropagation Derivation Diagram
Appendix: Mathematical Foundations
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Backprop Derivation Diagram',
    'url': 'https://github.com/QuantLet/NeuralNetworks/tree/main/appendix/charts/backprop_derivation_diagram'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.5, 'Backpropagation: Complete Derivation',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Step-by-step derivation
steps = [
    ('Step 1: Forward Pass', mlblue, 10, [
        '$z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$',
        '$a^{(l)} = \\sigma(z^{(l)})$',
    ]),
    ('Step 2: Output Error', mlorange, 8, [
        '$\\delta^{(L)} = \\nabla_a L \\odot \\sigma\'(z^{(L)})$',
        'For MSE: $\\delta^{(L)} = (a^{(L)} - y) \\odot \\sigma\'(z^{(L)})$',
    ]),
    ('Step 3: Backpropagate Error', mlpurple, 6, [
        '$\\delta^{(l)} = ((W^{(l+1)})^T \\delta^{(l+1)}) \\odot \\sigma\'(z^{(l)})$',
        'Error flows backward through weights',
    ]),
    ('Step 4: Compute Gradients', mlgreen, 4, [
        '$\\frac{\\partial L}{\\partial W^{(l)}} = \\delta^{(l)} (a^{(l-1)})^T$',
        '$\\frac{\\partial L}{\\partial b^{(l)}} = \\delta^{(l)}$',
    ]),
    ('Step 5: Update Weights', mlred, 2, [
        '$W^{(l)} \\leftarrow W^{(l)} - \\eta \\frac{\\partial L}{\\partial W^{(l)}}$',
        '$b^{(l)} \\leftarrow b^{(l)} - \\eta \\frac{\\partial L}{\\partial b^{(l)}}$',
    ]),
]

for title, color, y, formulas in steps:
    box = FancyBboxPatch((0.5, y - 0.8), 13, 1.5, boxstyle="round,pad=0.05",
                          facecolor=f'{color}11', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(0.8, y + 0.4, title, fontsize=10, fontweight='bold', color=color)
    for i, formula in enumerate(formulas):
        ax.text(7, y + 0.2 - i * 0.5, formula, fontsize=10, ha='center', color=mlgray)

# Arrows between steps
for y in [9, 7, 5, 3]:
    ax.annotate('', xy=(7, y + 0.2), xytext=(7, y + 0.7),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Key insight
ax.text(7, 0.5, 'Key insight: The chain rule allows efficient computation of all gradients in one backward pass',
        ha='center', fontsize=10, color=mlpurple, style='italic')

plt.tight_layout()
plt.savefig('backprop_derivation_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('backprop_derivation_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: backprop_derivation_diagram.pdf")
