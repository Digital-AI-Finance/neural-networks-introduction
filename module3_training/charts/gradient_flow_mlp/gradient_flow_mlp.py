"""
Gradient Flow Through MLP
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

CHART_METADATA = {
    'title': 'Gradient Flow MLP',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/gradient_flow_mlp'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Gradient Flow Through a 3-Layer MLP',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Network architecture
layer_x = [2, 5, 8, 11]
layer_sizes = [3, 4, 4, 1]
layer_names = ['Input', 'Hidden 1', 'Hidden 2', 'Output']
layer_colors = [mlblue, mlorange, mlpurple, mlgreen]

neurons = {}
for l, (x, n, name, color) in enumerate(zip(layer_x, layer_sizes, layer_names, layer_colors)):
    start_y = 5 + (n - 1) * 0.8 / 2
    for i in range(n):
        y = start_y - i * 0.8
        neurons[(l, i)] = (x, y)
        circle = Circle((x, y), 0.25, fill=True, facecolor=f'{color}44', edgecolor=color, linewidth=2)
        ax.add_patch(circle)
    ax.text(x, 8, name, ha='center', fontsize=10, fontweight='bold', color=color)

# Connections (forward)
for l in range(3):
    for i in range(layer_sizes[l]):
        for j in range(layer_sizes[l + 1]):
            x1, y1 = neurons[(l, i)]
            x2, y2 = neurons[(l + 1, j)]
            ax.plot([x1 + 0.25, x2 - 0.25], [y1, y2], color=mlgray, linewidth=0.5, alpha=0.3)

# Forward pass label
ax.text(6.5, 7.2, 'FORWARD: $x \\rightarrow z^{(1)} \\rightarrow a^{(1)} \\rightarrow z^{(2)} \\rightarrow a^{(2)} \\rightarrow \\hat{y}$',
        fontsize=10, ha='center', color=mlblue,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlblue))

# Backward pass arrows (red, below network)
ax.annotate('', xy=(2.5, 3.5), xytext=(10.5, 3.5),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=3))
ax.text(6.5, 3, 'BACKWARD: Gradient flows from loss to weights',
        fontsize=10, ha='center', color=mlred)

# Gradient magnitude visualization
gradient_sizes = [0.4, 0.3, 0.2, 0.1]  # Gradients get smaller (vanishing gradient)
for l, (x, size) in enumerate(zip([11, 8, 5, 2], gradient_sizes)):
    rect_height = size * 3
    rect = FancyBboxPatch((x - 0.3, 2 - rect_height/2), 0.6, rect_height,
                           boxstyle="round,pad=0.02", facecolor=mlred, alpha=0.6, edgecolor=mlred)
    ax.add_patch(rect)
    ax.text(x, 2 - rect_height/2 - 0.3, f'${size}$', fontsize=8, ha='center', color=mlred)

ax.text(6.5, 0.8, 'Gradient magnitude decreases as it flows backward (vanishing gradient problem)',
        fontsize=9, ha='center', color=mlred, style='italic')

# Formulas on right side
formulas = """Backward Pass Equations:

$\\delta^{(L)} = \\nabla_a L \\odot \\sigma'(z^{(L)})$

$\\delta^{(l)} = (W^{(l+1)})^T \\delta^{(l+1)} \\odot \\sigma'(z^{(l)})$

$\\frac{\\partial L}{\\partial W^{(l)}} = \\delta^{(l)} (a^{(l-1)})^T$

$\\frac{\\partial L}{\\partial b^{(l)}} = \\delta^{(l)}$"""

ax.text(13.5, 5.5, formulas, fontsize=8, va='center', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, linewidth=2))

plt.tight_layout()
plt.savefig('gradient_flow_mlp.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('gradient_flow_mlp.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: gradient_flow_mlp.pdf")
