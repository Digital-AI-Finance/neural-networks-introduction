# ==============================================================================
# Chart: Biological Neuron
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/01_biological_neuron/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Biological Neuron

Side-by-side comparison of biological and artificial neurons

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/01_biological_neuron/
"""

CHART_METADATA = {
    'name': 'Biological Neuron',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/01_biological_neuron',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Side-by-side comparison of biological and artificial neurons'
}

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
import numpy as np

# Set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('From Biology to Artificial Intelligence', fontsize=16, fontweight='bold')

# LEFT: Biological Neuron
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Biological Neuron', fontsize=14, fontweight='bold')

# Dendrites (inputs)
for i in range(3):
    y_pos = 7 - i * 1.5
    ax1.plot([0.5, 2.5], [y_pos, 6], 'k-', linewidth=2)
    ax1.plot([0, 0.5], [y_pos, y_pos], 'k-', linewidth=2)
    ax1.text(-0.3, y_pos, f'Input {i+1}', fontsize=9, ha='right', va='center')

# Soma (cell body)
soma = Circle((3.5, 5.5), 1.2, facecolor='lightblue', edgecolor='black', linewidth=2)
ax1.add_patch(soma)
ax1.text(3.5, 5.5, 'Soma', fontsize=10, ha='center', va='center', fontweight='bold')

# Axon
ax1.plot([4.7, 8], [5.5, 5.5], 'k-', linewidth=3)
ax1.text(6.5, 6, 'Axon', fontsize=9, ha='center')

# Synapses (output)
for i in range(2):
    y_pos = 6 - i * 1
    ax1.plot([8, 9], [5.5, y_pos], 'k-', linewidth=2)
    circle = Circle((9, y_pos), 0.15, facecolor='orange', edgecolor='black', linewidth=1)
    ax1.add_patch(circle)
    ax1.text(9.5, y_pos, f'Output {i+1}', fontsize=9, ha='left', va='center')

# Add annotation
ax1.text(3.5, 2, 'Processes signals from\nmultiple inputs', fontsize=9,
         ha='center', style='italic', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

# RIGHT: Artificial Neuron
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Artificial Neuron', fontsize=14, fontweight='bold')

# Inputs with weights
for i in range(3):
    y_pos = 7 - i * 1.5
    ax2.plot([0, 2], [y_pos, 5.5], 'b-', linewidth=2, alpha=0.7)
    ax2.plot([0, 0], [y_pos, y_pos], 'b-', linewidth=0)
    ax2.text(-0.3, y_pos, f'$x_{i+1}$', fontsize=11, ha='right', va='center')
    # Weight labels
    mid_x, mid_y = 1, (y_pos + 5.5) / 2
    ax2.text(mid_x - 0.3, mid_y, f'$w_{i+1}$', fontsize=9, ha='center',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

# Summation node
sum_circle = Circle((3.5, 5.5), 0.8, facecolor='lightgreen', edgecolor='blue', linewidth=2)
ax2.add_patch(sum_circle)
ax2.text(3.5, 5.5, r'$\Sigma$', fontsize=16, ha='center', va='center', fontweight='bold')

# Bias
ax2.plot([3.5, 3.5], [3, 4.5], 'r-', linewidth=2)
ax2.text(3.5, 2.5, 'bias (b)', fontsize=9, ha='center', color='red')

# Activation function
ax2.plot([4.5, 6], [5.5, 5.5], 'b-', linewidth=2)
activation_box = FancyBboxPatch((6, 4.8), 1.5, 1.4, boxstyle='round,pad=0.1',
                                facecolor='lavender', edgecolor='blue', linewidth=2)
ax2.add_patch(activation_box)
ax2.text(6.75, 5.5, r'$f$', fontsize=14, ha='center', va='center', fontweight='bold')
ax2.text(6.75, 4.3, 'Activation', fontsize=8, ha='center')

# Output
ax2.plot([7.5, 9], [5.5, 5.5], 'b-', linewidth=2, alpha=0.7)
output_circle = Circle((9.5, 5.5), 0.3, facecolor='orange', edgecolor='blue', linewidth=2)
ax2.add_patch(output_circle)
ax2.text(9.5, 5.5, '$y$', fontsize=11, ha='center', va='center', fontweight='bold')

# Formula annotation
formula_text = r'$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$'
ax2.text(5, 2, formula_text, fontsize=12, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

# Add process labels
ax2.text(3.5, 7, 'Weighted\nSum', fontsize=8, ha='center', style='italic')
ax2.text(6.75, 7, 'Non-linear\nTransform', fontsize=8, ha='center', style='italic')

plt.tight_layout()
plt.savefig('biological_vs_artificial.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: biological_vs_artificial.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/01_biological_neuron/
