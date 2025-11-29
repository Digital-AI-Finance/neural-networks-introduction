"""
XOR Problem Visualization - Why Perceptrons Fail
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'XOR Problem',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/xor_problem'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: XOR Truth Table ====================
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

# Title
ax1.text(5, 9.5, 'XOR Truth Table', fontsize=16, fontweight='bold',
         ha='center', color=mlpurple)

# Table data
headers = ['$x_1$', '$x_2$', 'XOR', 'Output']
data = [
    ['0', '0', '0 XOR 0', '0'],
    ['0', '1', '0 XOR 1', '1'],
    ['1', '0', '1 XOR 0', '1'],
    ['1', '1', '1 XOR 1', '0']
]

# Draw table
cell_height = 1.2
cell_width = 2
start_x = 1
start_y = 7

# Header row
for i, header in enumerate(headers):
    rect = plt.Rectangle((start_x + i * cell_width, start_y), cell_width, cell_height,
                          fill=True, facecolor=mlpurple, edgecolor='white', linewidth=2)
    ax1.add_patch(rect)
    ax1.text(start_x + i * cell_width + cell_width/2, start_y + cell_height/2,
             header, ha='center', va='center', fontsize=12, color='white', fontweight='bold')

# Data rows
for row_idx, row in enumerate(data):
    y = start_y - (row_idx + 1) * cell_height
    for col_idx, cell in enumerate(row):
        color = '#E6E6FA' if row_idx % 2 == 0 else 'white'
        if col_idx == 3:  # Output column
            color = mlgreen if cell == '1' else mlorange
        rect = plt.Rectangle((start_x + col_idx * cell_width, y), cell_width, cell_height,
                              fill=True, facecolor=color, edgecolor=mlgray, linewidth=1)
        ax1.add_patch(rect)
        text_color = 'white' if col_idx == 3 else 'black'
        ax1.text(start_x + col_idx * cell_width + cell_width/2, y + cell_height/2,
                 cell, ha='center', va='center', fontsize=11, color=text_color)

# Explanation
ax1.text(5, 1.5, '"Same inputs = 0, Different inputs = 1"', fontsize=11,
         ha='center', style='italic', color=mlgray)

# ==================== RIGHT: XOR Scatter Plot ====================
# XOR data points
xor_x = [0, 0, 1, 1]
xor_y = [0, 1, 0, 1]
xor_labels = [0, 1, 1, 0]  # XOR outputs

# Plot points
for i in range(4):
    color = mlgreen if xor_labels[i] == 1 else mlorange
    marker = 'o' if xor_labels[i] == 1 else 's'
    ax2.scatter(xor_x[i], xor_y[i], c=color, s=400, marker=marker,
                edgecolors='white', linewidths=2, zorder=5)
    ax2.text(xor_x[i] + 0.12, xor_y[i] + 0.12, f'({xor_x[i]},{xor_y[i]})', fontsize=10)

# Try to draw various failed decision boundaries
lines = [
    (0.5, -0.2, 0.5, 1.2, 'Vertical line: fails'),
    (-0.2, 0.5, 1.2, 0.5, 'Horizontal line: fails'),
    (-0.2, -0.2, 1.2, 1.2, 'Diagonal line: fails'),
    (-0.2, 1.2, 1.2, -0.2, 'Other diagonal: fails')
]

for x1, y1, x2, y2, label in lines:
    ax2.plot([x1, x2], [y1, y2], color=mlred, linewidth=1.5, linestyle='--', alpha=0.5)

# Big X to show failure
ax2.text(0.5, -0.4, 'No single line can separate the classes!', fontsize=12,
         ha='center', color=mlred, fontweight='bold')

# Labels
ax2.set_xlabel('$x_1$', fontsize=14)
ax2.set_ylabel('$x_2$', fontsize=14)
ax2.set_title('XOR is NOT Linearly Separable', fontsize=14, fontweight='bold', color=mlpurple)

# Legend
ax2.scatter([], [], c=mlgreen, s=100, marker='o', label='Output = 1')
ax2.scatter([], [], c=mlorange, s=100, marker='s', label='Output = 0')
ax2.legend(loc='upper right', fontsize=10)

# Formatting
ax2.set_xlim(-0.3, 1.3)
ax2.set_ylim(-0.5, 1.3)
ax2.set_xticks([0, 1])
ax2.set_yticks([0, 1])
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)

# Main message
fig.suptitle('The XOR Problem: Why Single-Layer Perceptrons Fail',
             fontsize=16, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('xor_problem.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('xor_problem.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: xor_problem.pdf")
