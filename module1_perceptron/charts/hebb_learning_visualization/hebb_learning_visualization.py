"""
Hebbian Learning Visualization
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

CHART_METADATA = {
    'title': 'Hebb Learning Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/hebb_learning_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

# ==================== BEFORE LEARNING ====================
ax = axes[0]
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Before Learning', fontsize=12, fontweight='bold', color=mlgray)

# Two neurons
n1 = Circle((1.5, 3), 0.6, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
n2 = Circle((4.5, 3), 0.6, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
ax.add_patch(n1)
ax.add_patch(n2)
ax.text(1.5, 3, 'A', ha='center', va='center', fontsize=14, fontweight='bold')
ax.text(4.5, 3, 'B', ha='center', va='center', fontsize=14, fontweight='bold')

# Weak connection
ax.annotate('', xy=(3.9, 3), xytext=(2.1, 3),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=1))
ax.text(3, 3.5, '$w$ = 0.1\n(weak)', ha='center', fontsize=9, color=mlgray)

ax.text(3, 0.8, 'Neurons not\nfiring together', ha='center', fontsize=10, color=mlgray)

# ==================== LEARNING ====================
ax = axes[1]
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('During Learning', fontsize=12, fontweight='bold', color=mlorange)

# Two neurons (active)
n1 = Circle((1.5, 3), 0.6, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=3)
n2 = Circle((4.5, 3), 0.6, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=3)
ax.add_patch(n1)
ax.add_patch(n2)
ax.text(1.5, 3, 'A', ha='center', va='center', fontsize=14, fontweight='bold', color=mlorange)
ax.text(4.5, 3, 'B', ha='center', va='center', fontsize=14, fontweight='bold', color=mlorange)

# Activity indication
ax.scatter([1.5], [4], s=100, c=mlorange, marker='*')
ax.scatter([4.5], [4], s=100, c=mlorange, marker='*')
ax.text(1.5, 4.5, 'FIRING', ha='center', fontsize=8, color=mlorange, fontweight='bold')
ax.text(4.5, 4.5, 'FIRING', ha='center', fontsize=8, color=mlorange, fontweight='bold')

# Connection strengthening
ax.annotate('', xy=(3.9, 3), xytext=(2.1, 3),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=3))
ax.text(3, 3.7, '$\\Delta w > 0$\nStrengthening!', ha='center', fontsize=9, color=mlorange, fontweight='bold')

ax.text(3, 0.8, '"Neurons that fire\ntogether, wire together"', ha='center', fontsize=10,
        color=mlorange, style='italic')

# ==================== AFTER LEARNING ====================
ax = axes[2]
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('After Learning', fontsize=12, fontweight='bold', color=mlgreen)

# Two neurons
n1 = Circle((1.5, 3), 0.6, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
n2 = Circle((4.5, 3), 0.6, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(n1)
ax.add_patch(n2)
ax.text(1.5, 3, 'A', ha='center', va='center', fontsize=14, fontweight='bold')
ax.text(4.5, 3, 'B', ha='center', va='center', fontsize=14, fontweight='bold')

# Strong connection
ax.annotate('', xy=(3.9, 3), xytext=(2.1, 3),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=4))
ax.text(3, 3.5, '$w$ = 0.9\n(strong)', ha='center', fontsize=9, color=mlgreen, fontweight='bold')

ax.text(3, 0.8, 'Connection\npermanently stronger', ha='center', fontsize=10, color=mlgreen)

# Main title
fig.suptitle('Hebbian Learning: "Neurons That Fire Together, Wire Together" (Donald Hebb, 1949)',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.05)

# Formula at bottom
fig.text(0.5, 0.02, 'Hebb Rule: $\\Delta w_{ij} = \\eta \\cdot x_i \\cdot x_j$ (weight increases when both neurons are active)',
         ha='center', fontsize=10, color=mlpurple)

plt.tight_layout()
plt.savefig('hebb_learning_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('hebb_learning_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: hebb_learning_visualization.pdf")
