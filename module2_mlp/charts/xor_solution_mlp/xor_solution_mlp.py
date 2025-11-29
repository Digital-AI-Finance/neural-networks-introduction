"""
XOR Solution with MLP - How Hidden Layers Solve Non-Linear Problems
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

CHART_METADATA = {
    'title': 'XOR Solution MLP',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/xor_solution_mlp'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# ==================== LEFT: XOR Problem ====================
ax = axes[0]
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)

# Data points
xor_data = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
for x1, x2, label in xor_data:
    color = mlgreen if label == 1 else mlred
    marker = '^' if label == 1 else 'o'
    ax.scatter(x1, x2, c=color, s=200, marker=marker, edgecolors='white', linewidths=2, zorder=5)
    ax.annotate(f'({x1},{x2})={label}', (x1, x2), xytext=(10, 10),
                textcoords='offset points', fontsize=9)

ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12)
ax.set_title('XOR: Not Linearly Separable', fontsize=12, fontweight='bold', color=mlred)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# Show no single line works
ax.text(0.5, -0.3, 'No single line can separate!', ha='center', fontsize=10, color=mlred)

# ==================== MIDDLE: Hidden Layer Transforms ====================
ax = axes[1]
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)

# Transform coordinates (what hidden layer produces)
# h1 = sigmoid(x1 + x2 - 0.5) roughly: OR gate
# h2 = sigmoid(x1 + x2 - 1.5) roughly: AND gate
# The hidden layer maps to a new space where XOR is separable

# Original -> Transformed
transforms = [
    ((0, 0), (0.0, 0.0), 0),  # (0,0) -> OR=0, AND=0
    ((0, 1), (1.0, 0.0), 1),  # (0,1) -> OR=1, AND=0
    ((1, 0), (1.0, 0.0), 1),  # (1,0) -> OR=1, AND=0
    ((1, 1), (1.0, 1.0), 0),  # (1,1) -> OR=1, AND=1
]

for orig, trans, label in transforms:
    color = mlgreen if label == 1 else mlred
    marker = '^' if label == 1 else 'o'
    ax.scatter(trans[0], trans[1], c=color, s=200, marker=marker, edgecolors='white', linewidths=2, zorder=5)

# Now we can draw a separating line!
x_line = np.linspace(-0.5, 1.5, 100)
y_line = 1.5 - x_line  # h1 - h2 = 0.5 approximately
ax.plot(x_line, y_line, color=mlpurple, linewidth=2, linestyle='--', label='Decision boundary')
ax.fill_between(x_line, y_line, 1.5, alpha=0.2, color=mlgreen)
ax.fill_between(x_line, -0.5, y_line, alpha=0.2, color=mlred)

ax.set_xlabel('$h_1$ (OR output)', fontsize=12)
ax.set_ylabel('$h_2$ (AND output)', fontsize=12)
ax.set_title('Hidden Layer Space: Separable!', fontsize=12, fontweight='bold', color=mlgreen)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
ax.legend(loc='upper right', fontsize=9)

# ==================== RIGHT: MLP Architecture ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Input layer
input_y = [6, 2]
for i, y in enumerate(input_y):
    circle = Circle((1.5, y), 0.5, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(1.5, y, f'$x_{i+1}$', ha='center', va='center', fontsize=11)

# Hidden layer
hidden_y = [6, 2]
hidden_labels = ['OR', 'AND']
for i, (y, label) in enumerate(zip(hidden_y, hidden_labels)):
    circle = Circle((5, y), 0.5, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
    ax.add_patch(circle)
    ax.text(5, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# Output layer
circle = Circle((8.5, 4), 0.5, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(circle)
ax.text(8.5, 4, 'XOR', ha='center', va='center', fontsize=9, fontweight='bold')

# Connections input to hidden
for iy in input_y:
    for hy in hidden_y:
        ax.annotate('', xy=(4.5, hy), xytext=(2, iy),
                    arrowprops=dict(arrowstyle='->', color=mlgray, lw=1))

# Connections hidden to output
for hy in hidden_y:
    ax.annotate('', xy=(8, 4), xytext=(5.5, hy),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=1))

# Labels
ax.text(1.5, 7.5, 'Input', ha='center', fontsize=10, fontweight='bold', color=mlblue)
ax.text(5, 7.5, 'Hidden', ha='center', fontsize=10, fontweight='bold', color=mlorange)
ax.text(8.5, 5.5, 'Output', ha='center', fontsize=10, fontweight='bold', color=mlgreen)

# Formula
ax.text(5, 0.5, 'XOR = OR AND (NOT AND)\n$= h_1 \\cdot (1 - h_2)$',
        ha='center', fontsize=10, color=mlpurple)

ax.set_title('2-2-1 MLP Solves XOR', fontsize=12, fontweight='bold', color=mlpurple)

fig.suptitle('XOR Solution: Hidden Layer Creates Linearly Separable Representation',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('xor_solution_mlp.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('xor_solution_mlp.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: xor_solution_mlp.pdf")
