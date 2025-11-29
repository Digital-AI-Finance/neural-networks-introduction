"""
Chain Rule Visualization for Backpropagation
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Chain Rule Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/chain_rule_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Chain Rule Intuition ====================
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'Chain Rule: The Key to Backprop', fontsize=14, fontweight='bold',
        ha='center', color=mlpurple)

# Chain of functions
positions = [(2, 6), (5, 6), (8, 6)]
labels = ['$x$', '$g(x)$', '$f(g(x))$']
colors = [mlblue, mlorange, mlgreen]

for (x, y), label, color in zip(positions, labels, colors):
    circle = Circle((x, y), 0.6, fill=True, facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=11, fontweight='bold')

# Forward arrows
ax.annotate('', xy=(4.3, 6), xytext=(2.7, 6),
            arrowprops=dict(arrowstyle='->', color=mlblue, lw=2))
ax.text(3.5, 6.5, '$g$', fontsize=11, ha='center', color=mlorange)

ax.annotate('', xy=(7.3, 6), xytext=(5.7, 6),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=2))
ax.text(6.5, 6.5, '$f$', fontsize=11, ha='center', color=mlgreen)

# Chain rule formula
ax.text(5, 4.2, 'Chain Rule:', fontsize=12, fontweight='bold', ha='center', color=mlpurple)
ax.text(5, 3.3, '$\\frac{d}{dx}f(g(x)) = \\frac{df}{dg} \\cdot \\frac{dg}{dx}$',
        fontsize=14, ha='center', color=mlpurple)

# Intuition
ax.text(5, 2, 'Intuition: Rate of change multiplies through the chain',
        fontsize=10, ha='center', color=mlgray)

# Example
example_text = """Example:
$f(u) = u^2$,  $g(x) = 3x + 1$
$\\frac{df}{du} = 2u$,  $\\frac{dg}{dx} = 3$
$\\frac{d}{dx}f(g(x)) = 2(3x+1) \\cdot 3 = 6(3x+1)$"""

ax.text(5, 0.8, example_text, fontsize=9, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray))

# ==================== RIGHT: Multi-Variable Chain Rule ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'Multi-Variable Chain Rule', fontsize=14, fontweight='bold',
        ha='center', color=mlpurple)

# Diagram: multiple paths
# x -> z1, z2 -> y
ax.text(1.5, 6, '$x$', fontsize=14, ha='center', color=mlblue,
        bbox=dict(boxstyle='circle,pad=0.3', facecolor='#E6E6FA', edgecolor=mlblue))
ax.text(5, 7.5, '$z_1$', fontsize=12, ha='center', color=mlorange,
        bbox=dict(boxstyle='circle,pad=0.3', facecolor='#FFE4B5', edgecolor=mlorange))
ax.text(5, 4.5, '$z_2$', fontsize=12, ha='center', color=mlorange,
        bbox=dict(boxstyle='circle,pad=0.3', facecolor='#FFE4B5', edgecolor=mlorange))
ax.text(8.5, 6, '$y$', fontsize=14, ha='center', color=mlgreen,
        bbox=dict(boxstyle='circle,pad=0.3', facecolor='#E6FFE6', edgecolor=mlgreen))

# Arrows
ax.annotate('', xy=(4.3, 7.2), xytext=(2.2, 6.3),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.annotate('', xy=(4.3, 4.8), xytext=(2.2, 5.7),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.annotate('', xy=(7.8, 6.3), xytext=(5.7, 7.2),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.annotate('', xy=(7.8, 5.7), xytext=(5.7, 4.8),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Path labels
ax.text(3, 7.2, '$\\frac{\\partial z_1}{\\partial x}$', fontsize=9, color=mlorange)
ax.text(3, 4.8, '$\\frac{\\partial z_2}{\\partial x}$', fontsize=9, color=mlorange)
ax.text(7, 7.2, '$\\frac{\\partial y}{\\partial z_1}$', fontsize=9, color=mlgreen)
ax.text(7, 4.8, '$\\frac{\\partial y}{\\partial z_2}$', fontsize=9, color=mlgreen)

# Formula
ax.text(5, 2.8, 'Total Derivative (sum over all paths):', fontsize=11,
        fontweight='bold', ha='center', color=mlpurple)
ax.text(5, 1.8, '$\\frac{\\partial y}{\\partial x} = \\frac{\\partial y}{\\partial z_1}\\frac{\\partial z_1}{\\partial x} + \\frac{\\partial y}{\\partial z_2}\\frac{\\partial z_2}{\\partial x}$',
        fontsize=12, ha='center', color=mlpurple)

ax.text(5, 0.8, 'In neural networks: gradients flow back through ALL paths',
        fontsize=9, ha='center', color=mlgray)

fig.suptitle('Chain Rule: Foundation of Backpropagation',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('chain_rule_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('chain_rule_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: chain_rule_visualization.pdf")
