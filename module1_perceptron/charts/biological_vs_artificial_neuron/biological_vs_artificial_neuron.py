"""
Biological vs Artificial Neuron Comparison
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

CHART_METADATA = {
    'title': 'Biological Vs Artificial Neuron',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/biological_vs_artificial_neuron'
}

# Set up figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# ==================== LEFT: BIOLOGICAL NEURON ====================
ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 9)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Biological Neuron', fontsize=16, fontweight='bold', color=mlpurple, pad=20)

# Cell body (soma)
soma = Circle((5, 4.5), 1.2, fill=True, facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=2)
ax1.add_patch(soma)
ax1.text(5, 4.5, 'Soma', ha='center', va='center', fontsize=10, fontweight='bold')

# Dendrites (inputs)
dendrite_starts = [(0.5, 7), (0.5, 5.5), (0.5, 4), (0.5, 2.5)]
for i, (dx, dy) in enumerate(dendrite_starts):
    # Wavy dendrite line
    x = np.linspace(dx, 3.8, 30)
    y = dy + 0.3 * np.sin(np.linspace(0, 3*np.pi, 30)) * (1 - (x - dx) / 3.3)
    target_y = 4.5 + (i - 1.5) * 0.8
    y = y + (target_y - dy) * (x - dx) / 3.3
    ax1.plot(x, y, color=mlblue, linewidth=2)
    ax1.scatter([dx], [dy], s=50, c=mlblue, marker='o')

ax1.text(-0.5, 7.5, 'Dendrites\n(Inputs)', fontsize=9, ha='center', color=mlblue)

# Axon (output)
ax1.annotate('', xy=(10, 4.5), xytext=(6.2, 4.5),
             arrowprops=dict(arrowstyle='->', color=mlorange, lw=3))
ax1.text(8, 5.2, 'Axon\n(Output)', fontsize=9, ha='center', color=mlorange)

# Axon terminals
for y_offset in [-0.5, 0, 0.5]:
    ax1.plot([9.5, 10.3], [4.5, 4.5 + y_offset], color=mlorange, linewidth=2)
    ax1.scatter([10.3], [4.5 + y_offset], s=60, c=mlorange, marker='o')

# Labels
ax1.text(5, 1, 'Processes information\nand generates output signal',
         fontsize=9, ha='center', style='italic', color=mlgray)

# ==================== RIGHT: ARTIFICIAL NEURON ====================
ax2.set_xlim(-1, 11)
ax2.set_ylim(-1, 9)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Artificial Neuron', fontsize=16, fontweight='bold', color=mlpurple, pad=20)

# Input nodes
input_y = [7, 5.5, 4, 2.5]
input_labels = ['$x_1$', '$x_2$', '$x_3$', '$x_n$']
weight_labels = ['$w_1$', '$w_2$', '$w_3$', '$w_n$']

for i, (y, label, wlabel) in enumerate(zip(input_y, input_labels, weight_labels)):
    # Input circle
    circle = Circle((1, y), 0.4, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax2.add_patch(circle)
    ax2.text(1, y, label, ha='center', va='center', fontsize=11)

    # Arrow with weight label
    ax2.annotate('', xy=(4.2, 4.5), xytext=(1.5, y),
                 arrowprops=dict(arrowstyle='->', color=mlblue, lw=1.5))

    # Weight label
    mid_x = (1.5 + 4.2) / 2
    mid_y = (y + 4.5) / 2
    ax2.text(mid_x - 0.3, mid_y + 0.3, wlabel, fontsize=9, color=mlblue)

# Dots for continuation
ax2.text(1, 3.2, '...', fontsize=14, ha='center', va='center')

ax2.text(0, 7.5, 'Inputs', fontsize=9, ha='center', color=mlblue)

# Sum node
sum_circle = Circle((5, 4.5), 0.8, fill=True, facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=2)
ax2.add_patch(sum_circle)
ax2.text(5, 4.5, '$\\Sigma$', ha='center', va='center', fontsize=16, fontweight='bold')

# Activation function box
activation_box = FancyBboxPatch((6.5, 3.7), 1.5, 1.6, boxstyle="round,pad=0.05",
                                  facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax2.add_patch(activation_box)
ax2.text(7.25, 4.5, '$f$', ha='center', va='center', fontsize=14, fontweight='bold')

# Arrow from sum to activation
ax2.annotate('', xy=(6.5, 4.5), xytext=(5.8, 4.5),
             arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Output arrow
ax2.annotate('', xy=(10, 4.5), xytext=(8, 4.5),
             arrowprops=dict(arrowstyle='->', color=mlorange, lw=3))

# Output circle
output_circle = Circle((10.3, 4.5), 0.4, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax2.add_patch(output_circle)
ax2.text(10.3, 4.5, '$y$', ha='center', va='center', fontsize=11)

ax2.text(10.3, 5.3, 'Output', fontsize=9, ha='center', color=mlorange)

# Bias
ax2.annotate('', xy=(5, 3.7), xytext=(5, 2.5),
             arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5))
ax2.text(5, 2, '$b$ (bias)', fontsize=9, ha='center', color=mlgreen)

# Labels
ax2.text(5, 0.8, '$y = f(\\sum_{i} w_i x_i + b)$',
         fontsize=11, ha='center', color=mlpurple, fontweight='bold')

plt.tight_layout()
plt.savefig('biological_vs_artificial_neuron.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('biological_vs_artificial_neuron.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: biological_vs_artificial_neuron.pdf")
