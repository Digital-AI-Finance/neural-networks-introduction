# ==============================================================================
# Chart: Linear Limitation
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/04_linear_limitation/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Linear Limitation

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/04_linear_limitation/
"""

CHART_METADATA = {
    'name': 'Linear Limitation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/04_linear_limitation',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Set up the figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Why One Neuron Is Not Enough', fontsize=16, fontweight='bold')

# LEFT PLOT: Linearly Separable (Simple case - can be solved with one neuron)
ax1.set_xlim(-0.5, 3.5)
ax1.set_ylim(-0.5, 3.5)
ax1.set_aspect('equal')
ax1.set_xlabel('Market Indicator 1', fontsize=11)
ax1.set_ylabel('Market Indicator 2', fontsize=11)
ax1.set_title('Linearly Separable Problem\n(One Neuron CAN Solve)', fontsize=12, fontweight='bold', color='green')
ax1.grid(True, alpha=0.3)

# Simple separable data (e.g., buy vs don't buy based on two indicators)
# Class 0: Don't buy (bottom-left)
class0_x = [0.5, 0.8, 1.0, 0.7, 1.2]
class0_y = [0.5, 0.7, 0.9, 1.1, 0.6]
ax1.scatter(class0_x, class0_y, c='red', s=150, marker='o', edgecolors='black', linewidth=2, label='Don\'t Buy', zorder=3)

# Class 1: Buy (top-right)
class1_x = [2.0, 2.3, 2.5, 2.7, 2.2]
class1_y = [2.0, 2.3, 2.5, 2.2, 2.7]
ax1.scatter(class1_x, class1_y, c='blue', s=150, marker='s', edgecolors='black', linewidth=2, label='Buy', zorder=3)

# Decision boundary (linear line)
x_line = np.array([0, 3.5])
y_line = -x_line + 3
ax1.plot(x_line, y_line, 'g-', linewidth=3, label='Decision Boundary')
ax1.fill_between(x_line, -0.5, y_line, alpha=0.1, color='red')
ax1.fill_between(x_line, y_line, 3.5, alpha=0.1, color='blue')

ax1.legend(loc='upper left', fontsize=9)

# Add annotation
ax1.text(1.7, 0.3, 'One straight line\nseparates the classes', fontsize=9, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

# RIGHT PLOT: XOR Problem (Cannot be solved with one neuron)
ax2.set_xlim(-0.5, 1.5)
ax2.set_ylim(-0.5, 1.5)
ax2.set_aspect('equal')
ax2.set_xlabel('Indicator A', fontsize=11)
ax2.set_ylabel('Indicator B', fontsize=11)
ax2.set_title('Non-Linearly Separable Problem\n(One Neuron CANNOT Solve)', fontsize=12, fontweight='bold', color='red')
ax2.grid(True, alpha=0.3)

# XOR pattern data
# Class 0 (corners: both low or both high)
xor_class0_x = [0.2, 0.8]
xor_class0_y = [0.2, 0.8]
ax2.scatter(xor_class0_x, xor_class0_y, c='red', s=200, marker='o', edgecolors='black', linewidth=2, label='Stable (0)', zorder=3)

# Class 1 (opposite corners: one high, one low)
xor_class1_x = [0.2, 0.8]
xor_class1_y = [0.8, 0.2]
ax2.scatter(xor_class1_x, xor_class1_y, c='blue', s=200, marker='s', edgecolors='black', linewidth=2, label='Volatile (1)', zorder=3)

# Attempt at linear decision boundaries (showing they fail)
# Try horizontal line
ax2.plot([0, 1.5], [0.5, 0.5], 'orange', linewidth=2, linestyle='--', alpha=0.7, label='Failed attempt 1')

# Try vertical line
ax2.plot([0.5, 0.5], [0, 1.5], 'purple', linewidth=2, linestyle='--', alpha=0.7, label='Failed attempt 2')

# Try diagonal line
x_diag = np.array([0, 1.5])
y_diag = x_diag
ax2.plot(x_diag, y_diag, 'brown', linewidth=2, linestyle='--', alpha=0.7, label='Failed attempt 3')

ax2.legend(loc='upper left', fontsize=8)

# Add annotation
ax2.text(0.75, -0.35, 'NO straight line can\nseparate the classes!', fontsize=9, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

# Add big X across the plot to show impossibility
ax2.plot([0, 1], [0, 1], 'red', linewidth=4, alpha=0.2, zorder=1)
ax2.plot([0, 1], [1, 0], 'red', linewidth=4, alpha=0.2, zorder=1)

# Add conclusion text at the bottom
fig.text(0.5, 0.02, 'Solution: Use Multiple Layers (Hidden Layers) to Create Non-Linear Decision Boundaries',
         ha='center', fontsize=12, fontweight='bold', color='darkblue',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('linear_limitation.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: linear_limitation.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/04_linear_limitation/
