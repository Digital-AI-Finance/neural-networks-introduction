"""
Matrix Multiplication Visualization for Neural Networks
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

CHART_METADATA = {
    'title': 'Matrix Multiplication Visual',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/matrix_multiplication_visual'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# Title
ax.text(7, 8.5, 'Neural Network Layer as Matrix Multiplication',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== INPUT VECTOR ====================
# x vector (3x1)
x_data = [[0.5], [0.8], [0.2]]
for i, row in enumerate(x_data):
    rect = Rectangle((1, 5.5 - i * 0.8), 0.8, 0.7,
                      facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(rect)
    ax.text(1.4, 5.85 - i * 0.8, f'{row[0]}', ha='center', va='center', fontsize=10)

ax.text(1.4, 6.8, '$x$', ha='center', fontsize=14, fontweight='bold', color=mlblue)
ax.text(1.4, 3.5, '(3x1)', ha='center', fontsize=9, color=mlgray)

# ==================== WEIGHT MATRIX ====================
# W matrix (2x3)
w_data = [[0.3, 0.5, 0.2], [0.4, -0.3, 0.6]]

for i, row in enumerate(w_data):
    for j, val in enumerate(row):
        rect = Rectangle((3 + j * 0.9, 5.5 - i * 0.8), 0.8, 0.7,
                          facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
        ax.add_patch(rect)
        ax.text(3.4 + j * 0.9, 5.85 - i * 0.8, f'{val}', ha='center', va='center', fontsize=9)

ax.text(4.35, 6.8, '$W$', ha='center', fontsize=14, fontweight='bold', color=mlorange)
ax.text(4.35, 4.3, '(2x3)', ha='center', fontsize=9, color=mlgray)

# Multiplication symbol
ax.text(2.5, 5.2, '$\\times$', ha='center', fontsize=18, color=mlgray)

# Plus symbol
ax.text(6.5, 5.2, '$+$', ha='center', fontsize=18, color=mlgray)

# ==================== BIAS VECTOR ====================
# b vector (2x1)
b_data = [[0.1], [-0.2]]
for i, row in enumerate(b_data):
    rect = Rectangle((7, 5.5 - i * 0.8), 0.8, 0.7,
                      facecolor='#D8BFD8', edgecolor=mlpurple, linewidth=2)
    ax.add_patch(rect)
    ax.text(7.4, 5.85 - i * 0.8, f'{row[0]}', ha='center', va='center', fontsize=10)

ax.text(7.4, 6.8, '$b$', ha='center', fontsize=14, fontweight='bold', color=mlpurple)
ax.text(7.4, 4.3, '(2x1)', ha='center', fontsize=9, color=mlgray)

# Equals symbol
ax.text(8.5, 5.2, '$=$', ha='center', fontsize=18, color=mlgray)

# ==================== RESULT VECTOR ====================
# z vector (2x1)
z_data = [[0.69], [0.16]]
for i, row in enumerate(z_data):
    rect = Rectangle((9.2, 5.5 - i * 0.8), 0.8, 0.7,
                      facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
    ax.add_patch(rect)
    ax.text(9.6, 5.85 - i * 0.8, f'{row[0]}', ha='center', va='center', fontsize=10)

ax.text(9.6, 6.8, '$z$', ha='center', fontsize=14, fontweight='bold', color=mlgreen)
ax.text(9.6, 4.3, '(2x1)', ha='center', fontsize=9, color=mlgray)

# Then activation
ax.annotate('', xy=(12, 5.2), xytext=(10.5, 5.2),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.text(11.25, 5.7, '$\\sigma(z)$', ha='center', fontsize=11, color=mlpurple)

# h vector (2x1)
h_data = [[0.67], [0.54]]
for i in range(2):
    rect = Rectangle((12, 5.5 - i * 0.8), 0.8, 0.7,
                      facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
    ax.add_patch(rect)

ax.text(12.4, 5.85, '0.67', ha='center', va='center', fontsize=10)
ax.text(12.4, 5.05, '0.54', ha='center', va='center', fontsize=10)
ax.text(12.4, 6.8, '$h$', ha='center', fontsize=14, fontweight='bold', color=mlgreen)

# ==================== COMPUTATION DETAILS ====================
detail_box = FancyBboxPatch((0.5, 0.5), 13, 2.5, boxstyle="round,pad=0.1",
                             facecolor='white', edgecolor=mlpurple, linewidth=2, alpha=0.9)
ax.add_patch(detail_box)

ax.text(7, 2.7, 'Computation Details', ha='center', fontsize=11, fontweight='bold', color=mlpurple)

details = """$z_1 = w_{11}x_1 + w_{12}x_2 + w_{13}x_3 + b_1 = 0.3(0.5) + 0.5(0.8) + 0.2(0.2) + 0.1 = 0.69$
$z_2 = w_{21}x_1 + w_{22}x_2 + w_{23}x_3 + b_2 = 0.4(0.5) - 0.3(0.8) + 0.6(0.2) - 0.2 = 0.16$"""

ax.text(7, 1.5, details, ha='center', va='center', fontsize=9, family='monospace')

# Formula summary
ax.text(7, 3.5, 'Layer computation: $h = \\sigma(Wx + b)$',
        ha='center', fontsize=12, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

plt.tight_layout()
plt.savefig('matrix_multiplication_visual.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('matrix_multiplication_visual.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: matrix_multiplication_visual.pdf")
