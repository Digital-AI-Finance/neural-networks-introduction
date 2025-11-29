"""
Perceptron Architecture Diagram
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

CHART_METADATA = {
    'title': 'Perceptron Architecture',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/perceptron_architecture'
}

# Set up figure
fig, ax = plt.subplots(figsize=(12, 7))

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'
mllavender = '#ADADE0'

ax.set_xlim(-1, 13)
ax.set_ylim(-1, 9)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 8.5, 'The Perceptron: Architecture', fontsize=18, fontweight='bold',
        ha='center', color=mlpurple)

# ==================== INPUT LAYER ====================
input_y = [7, 5.5, 4, 2]
input_labels = ['$x_1$', '$x_2$', '$x_3$', '$x_n$']
input_descriptions = ['P/E Ratio', 'Momentum', 'Volume', '...']

for i, (y, label, desc) in enumerate(zip(input_y, input_labels, input_descriptions)):
    # Input circle
    circle = Circle((1, y), 0.5, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(1, y, label, ha='center', va='center', fontsize=12, fontweight='bold')

    # Description
    ax.text(-0.5, y, desc, ha='right', va='center', fontsize=9, color=mlgray, style='italic')

# Dots for continuation
ax.text(1, 3, '...', fontsize=16, ha='center', va='center', color=mlgray)

# Input layer label
ax.text(1, 0.5, 'Input Layer', fontsize=11, ha='center', fontweight='bold', color=mlblue)

# ==================== WEIGHTS ====================
weight_labels = ['$w_1$', '$w_2$', '$w_3$', '$w_n$']

for i, (y, wlabel) in enumerate(zip(input_y, weight_labels)):
    # Arrow with weight
    ax.annotate('', xy=(5.3, 4.5), xytext=(1.6, y),
                arrowprops=dict(arrowstyle='->', color=mlblue, lw=2,
                               connectionstyle="arc3,rad=-0.1" if y > 4.5 else "arc3,rad=0.1"))

    # Weight label with box
    mid_x = (1.6 + 5.3) / 2
    mid_y = (y + 4.5) / 2 + (0.3 if i < 2 else -0.3)

    bbox = dict(boxstyle='round,pad=0.2', facecolor='#E6F3FF', edgecolor=mlblue, alpha=0.9)
    ax.text(mid_x, mid_y, wlabel, fontsize=10, ha='center', va='center',
            color=mlblue, fontweight='bold', bbox=bbox)

# ==================== SUMMATION NODE ====================
sum_circle = Circle((6, 4.5), 0.7, fill=True, facecolor=mllavender, edgecolor=mlpurple, linewidth=3)
ax.add_patch(sum_circle)
ax.text(6, 4.5, '$\\Sigma$', ha='center', va='center', fontsize=20, fontweight='bold', color=mlpurple)

# Bias arrow
ax.annotate('', xy=(6, 3.8), xytext=(6, 2.5),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=2))
bias_box = dict(boxstyle='round,pad=0.2', facecolor='#E6FFE6', edgecolor=mlgreen, alpha=0.9)
ax.text(6, 2, '$b$', fontsize=11, ha='center', va='center', color=mlgreen,
        fontweight='bold', bbox=bias_box)
ax.text(6, 1.3, 'Bias', fontsize=9, ha='center', color=mlgreen)

# Arrow from sum to activation
ax.annotate('', xy=(8.3, 4.5), xytext=(6.7, 4.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Net input label
ax.text(7.5, 5.2, '$z = \\sum w_i x_i + b$', fontsize=10, ha='center', color=mlgray)

# ==================== ACTIVATION FUNCTION ====================
# Draw step function box
activation_box = FancyBboxPatch((8.3, 3.5), 2, 2, boxstyle="round,pad=0.1",
                                 facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax.add_patch(activation_box)

# Draw mini step function inside
step_x = np.array([8.6, 9.3, 9.3, 10])
step_y = np.array([4, 4, 5, 5])
ax.plot(step_x, step_y, color=mlorange, linewidth=2)
ax.text(9.3, 3.8, '$f(z)$', fontsize=10, ha='center', color=mlorange)

# Arrow from activation to output
ax.annotate('', xy=(11.5, 4.5), xytext=(10.3, 4.5),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=3))

# ==================== OUTPUT ====================
output_circle = Circle((12, 4.5), 0.5, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax.add_patch(output_circle)
ax.text(12, 4.5, '$y$', ha='center', va='center', fontsize=12, fontweight='bold')

# Output label
ax.text(12, 0.5, 'Output', fontsize=11, ha='center', fontweight='bold', color=mlorange)
ax.text(12, 3.5, 'Buy (1)\nor\nSell (0)', fontsize=9, ha='center', color=mlorange, style='italic')

# ==================== LEGEND BOX ====================
legend_box = FancyBboxPatch((0, -0.5), 12, 1, boxstyle="round,pad=0.1",
                             facecolor='white', edgecolor=mlgray, linewidth=1, alpha=0.9)
ax.add_patch(legend_box)
ax.text(6, 0, 'Perceptron: $y = f(w_1 x_1 + w_2 x_2 + ... + w_n x_n + b)$',
        fontsize=12, ha='center', va='center', color=mlpurple, fontweight='bold')

plt.tight_layout()
plt.savefig('perceptron_architecture.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('perceptron_architecture.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: perceptron_architecture.pdf")
