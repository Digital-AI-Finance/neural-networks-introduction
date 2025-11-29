"""
Linear Collapse Proof - Why We Need Non-Linear Activations
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Linear Collapse Proof',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/linear_collapse_proof'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Without Activation ====================
ax = axes[0]
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6, 9.5, 'Without Non-Linear Activation', fontsize=14, fontweight='bold',
        ha='center', color=mlred)

# Network diagram
input_y = [7, 5, 3]
hidden_y = [6, 4]
output_y = [5]

# Input
for i, y in enumerate(input_y):
    circle = Circle((1.5, y), 0.4, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(1.5, y, f'$x_{i+1}$', ha='center', va='center', fontsize=9)

# Hidden
for i, y in enumerate(hidden_y):
    circle = Circle((4.5, y), 0.4, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
    ax.add_patch(circle)
    ax.text(4.5, y, f'$h_{i+1}$', ha='center', va='center', fontsize=9)

# Output
circle = Circle((7.5, 5), 0.4, fill=True, facecolor='#FFE4E4', edgecolor=mlred, linewidth=2)
ax.add_patch(circle)
ax.text(7.5, 5, '$y$', ha='center', va='center', fontsize=9)

# Connections
for iy in input_y:
    for hy in hidden_y:
        ax.plot([1.9, 4.1], [iy, hy], color=mlgray, linewidth=0.8, alpha=0.5)

for hy in hidden_y:
    ax.plot([4.9, 7.1], [hy, 5], color=mlgray, linewidth=0.8, alpha=0.5)

# Math box
math_box = FancyBboxPatch((8.5, 1.5), 3.3, 7, boxstyle="round,pad=0.1",
                           facecolor='#FFF0F0', edgecolor=mlred, linewidth=2)
ax.add_patch(math_box)

ax.text(10.15, 8, 'Math:', fontsize=10, fontweight='bold', ha='center', color=mlred)
ax.text(10.15, 7, '$h = W_1 x$', fontsize=10, ha='center')
ax.text(10.15, 6.2, '$y = W_2 h$', fontsize=10, ha='center')
ax.text(10.15, 5.2, '$y = W_2 (W_1 x)$', fontsize=10, ha='center')
ax.text(10.15, 4.2, '$y = (W_2 W_1) x$', fontsize=10, ha='center', color=mlred)
ax.text(10.15, 3.2, '$y = W_{eff} x$', fontsize=10, ha='center', fontweight='bold', color=mlred)
ax.text(10.15, 2.2, 'Still just a\nlinear transform!', fontsize=9, ha='center', color=mlred)

ax.text(4.5, 1, 'Multiple linear layers = One linear layer', fontsize=10, ha='center',
        color=mlred, style='italic')

# ==================== RIGHT: With Activation ====================
ax = axes[1]
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6, 9.5, 'With Non-Linear Activation', fontsize=14, fontweight='bold',
        ha='center', color=mlgreen)

# Input
for i, y in enumerate(input_y):
    circle = Circle((1.5, y), 0.4, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(1.5, y, f'$x_{i+1}$', ha='center', va='center', fontsize=9)

# Hidden with activation symbol
for i, y in enumerate(hidden_y):
    circle = Circle((4.5, y), 0.4, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
    ax.add_patch(circle)
    ax.text(4.5, y, '$\\sigma$', ha='center', va='center', fontsize=9)

# Output
circle = Circle((7.5, 5), 0.4, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(circle)
ax.text(7.5, 5, '$y$', ha='center', va='center', fontsize=9)

# Connections
for iy in input_y:
    for hy in hidden_y:
        ax.plot([1.9, 4.1], [iy, hy], color=mlgray, linewidth=0.8, alpha=0.5)

for hy in hidden_y:
    ax.plot([4.9, 7.1], [hy, 5], color=mlgray, linewidth=0.8, alpha=0.5)

# Math box
math_box = FancyBboxPatch((8.5, 1.5), 3.3, 7, boxstyle="round,pad=0.1",
                           facecolor='#F0FFF0', edgecolor=mlgreen, linewidth=2)
ax.add_patch(math_box)

ax.text(10.15, 8, 'Math:', fontsize=10, fontweight='bold', ha='center', color=mlgreen)
ax.text(10.15, 7, '$h = \\sigma(W_1 x)$', fontsize=10, ha='center')
ax.text(10.15, 6.2, '$y = W_2 h$', fontsize=10, ha='center')
ax.text(10.15, 5.2, '$y = W_2 \\sigma(W_1 x)$', fontsize=10, ha='center')
ax.text(10.15, 4.0, 'Cannot simplify!', fontsize=10, ha='center', fontweight='bold', color=mlgreen)
ax.text(10.15, 3.0, 'Non-linearity\nbreaks collapse', fontsize=9, ha='center', color=mlgreen)
ax.text(10.15, 2.0, 'Each layer adds\nexpressiveness', fontsize=9, ha='center', color=mlgreen)

ax.text(4.5, 1, 'Activation functions enable deep learning', fontsize=10, ha='center',
        color=mlgreen, style='italic')

fig.suptitle('Why Non-Linear Activations Are Essential',
             fontsize=16, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('linear_collapse_proof.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('linear_collapse_proof.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: linear_collapse_proof.pdf")
