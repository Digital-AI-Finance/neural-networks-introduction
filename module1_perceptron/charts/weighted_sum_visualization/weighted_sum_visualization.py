"""
Weighted Sum Visualization
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

CHART_METADATA = {
    'title': 'Weighted Sum Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/weighted_sum_visualization'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Weighted Sum: How Inputs Combine', fontsize=16, fontweight='bold',
        ha='center', color=mlpurple)

# Input values and weights
inputs = [
    {'name': 'P/E Ratio', 'symbol': '$x_1$', 'value': 0.8, 'weight': 0.5, 'w_symbol': '$w_1$'},
    {'name': 'Momentum', 'symbol': '$x_2$', 'value': 0.6, 'weight': 0.3, 'w_symbol': '$w_2$'},
    {'name': 'Volume', 'symbol': '$x_3$', 'value': 0.4, 'weight': 0.2, 'w_symbol': '$w_3$'}
]

y_positions = [7, 5, 3]

# Draw inputs
for i, (inp, y) in enumerate(zip(inputs, y_positions)):
    # Input box
    input_box = FancyBboxPatch((0.5, y - 0.5), 2.5, 1, boxstyle="round,pad=0.05",
                                facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.75, y, f"{inp['name']}\n{inp['symbol']} = {inp['value']}", ha='center', va='center',
            fontsize=10, color=mlblue)

    # Weight arrow
    ax.annotate('', xy=(5.5, y), xytext=(3.1, y),
                arrowprops=dict(arrowstyle='->', color=mlpurple, lw=2))

    # Weight label
    ax.text(4.3, y + 0.4, f"{inp['w_symbol']} = {inp['weight']}", ha='center', fontsize=10,
            color=mlpurple, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=mlpurple, alpha=0.9))

    # Multiplication box
    mult_box = FancyBboxPatch((5.5, y - 0.4), 2, 0.8, boxstyle="round,pad=0.05",
                               facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
    ax.add_patch(mult_box)
    product = inp['value'] * inp['weight']
    ax.text(6.5, y, f"{inp['value']} x {inp['weight']} = {product:.2f}", ha='center', va='center',
            fontsize=9, color=mlorange)

    # Arrow to sum
    ax.annotate('', xy=(9.5, 5), xytext=(7.6, y),
                arrowprops=dict(arrowstyle='->', color=mlorange, lw=1.5,
                               connectionstyle="arc3,rad=0.2" if i != 1 else "arc3,rad=0"))

# Sum node
sum_circle = Circle((10, 5), 0.8, fill=True, facecolor='#D8BFD8', edgecolor=mlpurple, linewidth=3)
ax.add_patch(sum_circle)
ax.text(10, 5, '$\\Sigma$', ha='center', va='center', fontsize=20, fontweight='bold', color=mlpurple)

# Calculate total
total = sum(inp['value'] * inp['weight'] for inp in inputs)
bias = 0.1

# Bias arrow
ax.annotate('', xy=(10, 4.2), xytext=(10, 2.8),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=2))
ax.text(10, 2.3, f'$b$ = {bias}', ha='center', fontsize=10, color=mlgreen,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E6FFE6', edgecolor=mlgreen, alpha=0.9))

# Output arrow
ax.annotate('', xy=(12.5, 5), xytext=(10.8, 5),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=3))

# Result box
result_box = FancyBboxPatch((12.5, 4.2), 1.3, 1.6, boxstyle="round,pad=0.05",
                             facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(result_box)
ax.text(13.15, 5, f'$z$ = {total + bias:.2f}', ha='center', va='center',
        fontsize=11, color=mlgreen, fontweight='bold')

# Equation at bottom
eq_text = f"$z = w_1 x_1 + w_2 x_2 + w_3 x_3 + b = {inputs[0]['weight']} \\times {inputs[0]['value']} + {inputs[1]['weight']} \\times {inputs[1]['value']} + {inputs[2]['weight']} \\times {inputs[2]['value']} + {bias} = {total + bias:.2f}$"
ax.text(7, 0.8, eq_text, ha='center', fontsize=10, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, alpha=0.9))

# Legend
ax.text(7, 1.6, 'Finance Example: Combining multiple factors to score a stock', ha='center',
        fontsize=10, style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('weighted_sum_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('weighted_sum_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: weighted_sum_visualization.pdf")
