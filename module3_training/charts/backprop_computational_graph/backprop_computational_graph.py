"""
Backpropagation Computational Graph
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

CHART_METADATA = {
    'title': 'Backprop Computational Graph',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/backprop_computational_graph'
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
ax.text(7, 9.5, 'Computational Graph: Forward and Backward Pass',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== NODES ====================
# Node positions
nodes = {
    'x': (1, 5),
    'w': (1, 7.5),
    'b': (4, 7.5),
    'z': (4, 5),
    'a': (7, 5),
    'y': (10, 7.5),
    'L': (10, 5),
}

# Draw nodes
node_styles = {
    'x': (mlblue, 'Input'),
    'w': (mlorange, 'Weight'),
    'b': (mlorange, 'Bias'),
    'z': (mlpurple, 'Linear'),
    'a': (mlgreen, 'Activation'),
    'y': (mlgray, 'Target'),
    'L': (mlred, 'Loss'),
}

for name, (x, y) in nodes.items():
    color, label = node_styles[name]
    circle = Circle((x, y), 0.5, fill=True, facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, f'${name}$', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(x, y - 0.8, label, ha='center', fontsize=8, color=mlgray)

# ==================== FORWARD PASS (Blue arrows) ====================
forward_edges = [
    ('x', 'z', '$w \\cdot x$'),
    ('w', 'z', ''),
    ('b', 'z', '$+ b$'),
    ('z', 'a', '$\\sigma(z)$'),
    ('a', 'L', ''),
    ('y', 'L', 'MSE'),
]

for start, end, label in forward_edges:
    x1, y1 = nodes[start]
    x2, y2 = nodes[end]

    # Adjust for circle radius
    dx, dy = x2 - x1, y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    x1_adj = x1 + 0.5 * dx / dist
    y1_adj = y1 + 0.5 * dy / dist
    x2_adj = x2 - 0.5 * dx / dist
    y2_adj = y2 - 0.5 * dy / dist

    ax.annotate('', xy=(x2_adj, y2_adj), xytext=(x1_adj, y1_adj),
                arrowprops=dict(arrowstyle='->', color=mlblue, lw=2))

    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 0.3
        ax.text(mx, my, label, fontsize=8, ha='center', color=mlblue)

# Forward label
ax.text(5.5, 3.5, 'FORWARD PASS', fontsize=12, fontweight='bold', color=mlblue,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlblue))
ax.annotate('', xy=(9, 3.5), xytext=(2, 3.5),
            arrowprops=dict(arrowstyle='->', color=mlblue, lw=3, alpha=0.5))

# ==================== BACKWARD PASS (Red arrows below) ====================
ax.text(5.5, 1.5, 'BACKWARD PASS', fontsize=12, fontweight='bold', color=mlred,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlred))
ax.annotate('', xy=(2, 1.5), xytext=(9, 1.5),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=3, alpha=0.5))

# Gradient flow
gradient_labels = [
    (10, 2.3, '$\\frac{\\partial L}{\\partial L} = 1$'),
    (8.5, 2.3, '$\\frac{\\partial L}{\\partial a}$'),
    (5.5, 2.3, '$\\frac{\\partial L}{\\partial z}$'),
    (2.5, 2.3, '$\\frac{\\partial L}{\\partial w}$'),
]

for x, y, label in gradient_labels:
    ax.text(x, y, label, fontsize=9, ha='center', color=mlred)

# Key equations box
equations = """Chain Rule:
$\\frac{\\partial L}{\\partial w} = \\frac{\\partial L}{\\partial a} \\cdot \\frac{\\partial a}{\\partial z} \\cdot \\frac{\\partial z}{\\partial w}$

Gradient computation:
- Start from loss: $\\frac{\\partial L}{\\partial L} = 1$
- Propagate backwards through each operation
- Accumulate gradients using chain rule"""

ax.text(12.5, 6.5, equations, ha='center', va='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlpurple, linewidth=2))

plt.tight_layout()
plt.savefig('backprop_computational_graph.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('backprop_computational_graph.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: backprop_computational_graph.pdf")
