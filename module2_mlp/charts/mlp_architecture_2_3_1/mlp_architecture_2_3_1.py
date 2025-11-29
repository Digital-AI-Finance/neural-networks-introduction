"""
Multi-Layer Perceptron Architecture (2-3-1)
Module 2: Stacking Layers
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

CHART_METADATA = {
    'title': 'MLP Architecture 2 3 1',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mlp_architecture_2_3_1'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'
mllavender = '#ADADE0'

# Set up figure
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 9)
ax.axis('off')

# Title
ax.text(7, 8.5, 'Multi-Layer Perceptron: 2-3-1 Architecture', fontsize=16, fontweight='bold',
        ha='center', color=mlpurple)

# Layer positions
input_x = 2
hidden_x = 7
output_x = 12

# Node positions
input_y = [5.5, 3.5]
hidden_y = [6.5, 4.5, 2.5]
output_y = [4.5]

# Draw connections first (so they're behind nodes)
# Input to Hidden
for iy in input_y:
    for hy in hidden_y:
        ax.plot([input_x + 0.5, hidden_x - 0.5], [iy, hy], color=mlblue, linewidth=1, alpha=0.6)

# Hidden to Output
for hy in hidden_y:
    for oy in output_y:
        ax.plot([hidden_x + 0.5, output_x - 0.5], [hy, oy], color=mlorange, linewidth=1, alpha=0.6)

# Draw input layer
for i, y in enumerate(input_y):
    circle = Circle((input_x, y), 0.5, fill=True, facecolor='#E6E6FA',
                    edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(input_x, y, f'$x_{i+1}$', ha='center', va='center', fontsize=14, fontweight='bold')

ax.text(input_x, 1.5, 'Input Layer', ha='center', fontsize=12, fontweight='bold', color=mlblue)
ax.text(input_x, 0.8, '(2 neurons)', ha='center', fontsize=10, color=mlgray)

# Draw hidden layer
for i, y in enumerate(hidden_y):
    circle = Circle((hidden_x, y), 0.5, fill=True, facecolor=mllavender,
                    edgecolor=mlpurple, linewidth=2)
    ax.add_patch(circle)
    ax.text(hidden_x, y, f'$h_{i+1}$', ha='center', va='center', fontsize=14, fontweight='bold')

ax.text(hidden_x, 1.5, 'Hidden Layer', ha='center', fontsize=12, fontweight='bold', color=mlpurple)
ax.text(hidden_x, 0.8, '(3 neurons)', ha='center', fontsize=10, color=mlgray)

# Draw output layer
for i, y in enumerate(output_y):
    circle = Circle((output_x, y), 0.5, fill=True, facecolor='#FFE4B5',
                    edgecolor=mlorange, linewidth=2)
    ax.add_patch(circle)
    ax.text(output_x, y, '$y$', ha='center', va='center', fontsize=14, fontweight='bold')

ax.text(output_x, 1.5, 'Output Layer', ha='center', fontsize=12, fontweight='bold', color=mlorange)
ax.text(output_x, 0.8, '(1 neuron)', ha='center', fontsize=10, color=mlgray)

# Weight labels
ax.text(4.5, 6.8, '$W^{(1)}$', fontsize=12, color=mlblue, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=mlblue, alpha=0.9))
ax.text(9.5, 5.8, '$W^{(2)}$', fontsize=12, color=mlorange, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=mlorange, alpha=0.9))

# Add bias indicators
for y in hidden_y:
    ax.annotate('', xy=(hidden_x, y - 0.5), xytext=(hidden_x, y - 1.2),
                arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1))
ax.text(hidden_x, 1.8, '$b^{(1)}$', ha='center', fontsize=10, color=mlgreen)

ax.annotate('', xy=(output_x, output_y[0] - 0.5), xytext=(output_x, output_y[0] - 1.2),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1))
ax.text(output_x, 2.8, '$b^{(2)}$', ha='center', fontsize=10, color=mlgreen)

# Information flow arrows
ax.annotate('', xy=(5, 7.5), xytext=(3.5, 7.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.text(4.25, 7.9, 'Forward', fontsize=9, ha='center', color=mlgray)

ax.annotate('', xy=(10, 7.5), xytext=(8.5, 7.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.text(9.25, 7.9, 'Pass', fontsize=9, ha='center', color=mlgray)

# Parameter count
param_text = "Parameters:\n$W^{(1)}$: 2x3 = 6\n$b^{(1)}$: 3\n$W^{(2)}$: 3x1 = 3\n$b^{(2)}$: 1\nTotal: 13"
ax.text(14, 7, param_text, fontsize=9, ha='left', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

# Equations at bottom
eq_text = "$h = \\phi(W^{(1)}x + b^{(1)})$    $y = \\phi(W^{(2)}h + b^{(2)})$"
ax.text(7, 0, eq_text, fontsize=11, ha='center', color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, alpha=0.9))

plt.tight_layout()
plt.savefig('mlp_architecture_2_3_1.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('mlp_architecture_2_3_1.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: mlp_architecture_2_3_1.pdf")
