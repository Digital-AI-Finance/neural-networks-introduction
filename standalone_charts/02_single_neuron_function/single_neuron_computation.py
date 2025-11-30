# ==============================================================================
# Chart: Single Neuron Function
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/02_single_neuron_function/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Single Neuron Function

Mathematical computation inside a single artificial neuron

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/02_single_neuron_function/
"""

CHART_METADATA = {
    'name': 'Single Neuron Function',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/02_single_neuron_function',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Mathematical computation inside a single artificial neuron'
}

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')
fig.suptitle('How a Neuron Computes: Step-by-Step', fontsize=16, fontweight='bold')

# Example values for demonstration
inputs = [100, 85, 120]  # Market features: yesterday's price, volume index, sentiment score
weights = [0.5, 0.3, 0.2]
bias = 10
input_labels = ['Yesterday\nPrice', 'Volume\nIndex', 'Sentiment\nScore']

# Step 1: Inputs
x_start = 0.5
for i in range(3):
    y_pos = 6 - i * 2
    # Input box
    input_box = FancyBboxPatch((x_start, y_pos-0.3), 1.2, 0.6, boxstyle='round,pad=0.05',
                               facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(input_box)
    ax.text(x_start + 0.6, y_pos, f'{inputs[i]}', fontsize=12, ha='center', va='center', fontweight='bold')
    ax.text(x_start + 0.6, y_pos - 0.8, input_labels[i], fontsize=8, ha='center', va='top')

    # Arrow to multiplication
    ax.annotate('', xy=(2.8, 4), xytext=(x_start + 1.2, y_pos),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # Weight label on arrow
    mid_x = (x_start + 1.2 + 2.8) / 2
    mid_y = (y_pos + 4) / 2
    ax.text(mid_x, mid_y + 0.2, f'$w_{i+1}$ = {weights[i]}', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

# Step 2: Multiplication and Summation
sum_box = FancyBboxPatch((2.8, 3.2), 2, 1.6, boxstyle='round,pad=0.1',
                         facecolor='lightgreen', edgecolor='green', linewidth=3)
ax.add_patch(sum_box)
ax.text(3.8, 4.5, r'$\Sigma$', fontsize=24, ha='center', va='center', fontweight='bold')
ax.text(3.8, 3.5, 'Weighted Sum', fontsize=9, ha='center', va='center', style='italic')

# Calculate weighted sum
weighted_sum = sum([inputs[i] * weights[i] for i in range(3)])

# Show calculation details
calc_text = f'{inputs[0]}*{weights[0]} + {inputs[1]}*{weights[1]} + {inputs[2]}*{weights[2]}\n'
calc_text += f'= {inputs[0]*weights[0]:.1f} + {inputs[1]*weights[1]:.1f} + {inputs[2]*weights[2]:.1f}\n'
calc_text += f'= {weighted_sum:.1f}'
ax.text(3.8, 1.8, calc_text, fontsize=8, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Bias addition
ax.annotate('', xy=(4.8, 4), xytext=(5.5, 6),
            arrowprops=dict(arrowstyle='->', lw=2, color='red'))
bias_box = FancyBboxPatch((5.5, 5.8), 0.8, 0.5, boxstyle='round,pad=0.05',
                          facecolor='pink', edgecolor='red', linewidth=2)
ax.add_patch(bias_box)
ax.text(5.9, 6.05, f'b = {bias}', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(5.9, 5.4, 'Bias', fontsize=8, ha='center', va='top')

# Arrow to activation function
ax.annotate('', xy=(6.5, 4), xytext=(4.8, 4),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(5.65, 4.3, f'z = {weighted_sum + bias:.1f}', fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))

# Step 3: Activation Function
activation_box = FancyBboxPatch((6.5, 3), 2.5, 2, boxstyle='round,pad=0.1',
                                facecolor='lavender', edgecolor='purple', linewidth=3)
ax.add_patch(activation_box)
ax.text(7.75, 4.5, 'Activation', fontsize=11, ha='center', va='center', fontweight='bold')
ax.text(7.75, 4, r'$f(z) = \frac{1}{1+e^{-z}}$', fontsize=10, ha='center', va='center')

# Sigmoid curve illustration (small)
x_curve = np.linspace(-3, 3, 100)
y_curve = 1 / (1 + np.exp(-x_curve))
# Normalize to fit in the box
x_plot = 7.75 + x_curve * 0.4
y_plot = 3.2 + y_curve * 1
ax.plot(x_plot, y_plot, 'purple', linewidth=2)
ax.plot([7.35, 8.15], [3.7, 3.7], 'gray', linewidth=0.5, linestyle='--')  # center line

# Calculate output
z = weighted_sum + bias
output = 1 / (1 + np.exp(-z))

# Arrow to output
ax.annotate('', xy=(10, 4), xytext=(9, 4),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Step 4: Output
output_circle = Circle((11, 4), 0.7, facecolor='orange', edgecolor='darkorange', linewidth=3)
ax.add_patch(output_circle)
ax.text(11, 4, f'{output:.3f}', fontsize=12, ha='center', va='center', fontweight='bold')
ax.text(11, 2.8, 'Output\n(Prediction)', fontsize=9, ha='center', va='top', style='italic')

# Interpretation box
interp_text = f'Prediction: {output:.1%} confidence\nPrice will increase tomorrow'
ax.text(11, 6.5, interp_text, fontsize=9, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

# Add step labels
ax.text(1.1, 7.3, 'STEP 1:\nInputs', fontsize=10, ha='center', fontweight='bold', color='blue')
ax.text(3.8, 6.2, 'STEP 2:\nWeighted Sum + Bias', fontsize=10, ha='center', fontweight='bold', color='green')
ax.text(7.75, 6, 'STEP 3:\nActivation', fontsize=10, ha='center', fontweight='bold', color='purple')
ax.text(11, 7.3, 'STEP 4:\nOutput', fontsize=10, ha='center', fontweight='bold', color='darkorange')

plt.tight_layout()
plt.savefig('single_neuron_computation.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: single_neuron_computation.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/02_single_neuron_function/
