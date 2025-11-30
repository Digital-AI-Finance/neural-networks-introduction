# ==============================================================================
# Chart: Forward Propagation
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/06_forward_propagation/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Forward Propagation

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/06_forward_propagation/
"""

CHART_METADATA = {
    'name': 'Forward Propagation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/06_forward_propagation',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
fig.suptitle('Forward Propagation: Making a Prediction', fontsize=16, fontweight='bold')

# Example data (market features)
inputs = [105.2, 0.75, 0.62]  # Price, Volume index (normalized), Sentiment score
input_labels = ['Price:\n105.2', 'Volume:\n0.75', 'Sentiment:\n0.62']

# Simplified network: 3 inputs -> 3 hidden -> 1 output
layer_x = [2, 7, 12]
input_y = [7, 5, 3]
hidden_y = [7.5, 5, 2.5]
output_y = 5

# Step 1: Input Layer
ax.text(layer_x[0], 9, 'INPUT', fontsize=11, ha='center', fontweight='bold', color='blue')
for i, (y_pos, value, label) in enumerate(zip(input_y, inputs, input_labels)):
    circle = Circle((layer_x[0], y_pos), 0.4, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(circle)
    ax.text(layer_x[0], y_pos, f'{value}', fontsize=9, ha='center', va='center', fontweight='bold')
    ax.text(layer_x[0] - 1, y_pos, label, fontsize=8, ha='right', va='center')

# Simulated weights for input->hidden
W1 = np.array([[0.5, 0.3, -0.2],
               [0.2, 0.4, 0.6],
               [-0.3, 0.5, 0.4]])
b1 = np.array([0.1, -0.1, 0.2])

# Calculate hidden layer activations
z1 = np.dot(W1, inputs) + b1
a1 = 1 / (1 + np.exp(-z1))  # Sigmoid activation

# Step 2: Hidden Layer
ax.text(layer_x[1], 9, 'HIDDEN', fontsize=11, ha='center', fontweight='bold', color='green')
for i, (y_pos, value) in enumerate(zip(hidden_y, a1)):
    circle = Circle((layer_x[1], y_pos), 0.4, facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(circle)
    ax.text(layer_x[1], y_pos, f'{value:.2f}', fontsize=9, ha='center', va='center', fontweight='bold')

# Draw input->hidden connections with weight labels (select a few)
# Connection from input 0 to hidden 1
ax.plot([layer_x[0] + 0.4, layer_x[1] - 0.4], [input_y[0], hidden_y[1]],
        'blue', linewidth=2, alpha=0.6)
ax.text((layer_x[0] + layer_x[1]) / 2, (input_y[0] + hidden_y[1]) / 2 + 0.3,
        f'w={W1[1][0]}', fontsize=7, ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

# Connection from input 1 to hidden 0
ax.plot([layer_x[0] + 0.4, layer_x[1] - 0.4], [input_y[1], hidden_y[0]],
        'blue', linewidth=2, alpha=0.6)
ax.text((layer_x[0] + layer_x[1]) / 2, (input_y[1] + hidden_y[0]) / 2 + 0.3,
        f'w={W1[0][1]}', fontsize=7, ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

# Other connections (lighter)
for i, in_y in enumerate(input_y):
    for j, hid_y in enumerate(hidden_y):
        if not ((i == 0 and j == 1) or (i == 1 and j == 0)):
            ax.plot([layer_x[0] + 0.4, layer_x[1] - 0.4], [in_y, hid_y],
                    'gray', linewidth=0.5, alpha=0.3)

# Simulated weights for hidden->output
W2 = np.array([0.7, -0.3, 0.5])
b2 = 0.15

# Calculate output
z2 = np.dot(W2, a1) + b2
output = 1 / (1 + np.exp(-z2))  # Sigmoid activation

# Step 3: Output Layer
ax.text(layer_x[2], 9, 'OUTPUT', fontsize=11, ha='center', fontweight='bold', color='darkorange')
output_circle = Circle((layer_x[2], output_y), 0.5, facecolor='orange', edgecolor='darkorange', linewidth=3)
ax.add_patch(output_circle)
ax.text(layer_x[2], output_y, f'{output:.3f}', fontsize=11, ha='center', va='center', fontweight='bold')

# Draw hidden->output connections
for i, hid_y in enumerate(hidden_y):
    ax.plot([layer_x[1] + 0.4, layer_x[2] - 0.5], [hid_y, output_y],
            'green', linewidth=1.5, alpha=0.5)
    # Show weight on one connection
    if i == 1:
        ax.text((layer_x[1] + layer_x[2]) / 2, (hid_y + output_y) / 2 + 0.2,
                f'w={W2[i]}', fontsize=7, ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

# Output interpretation
interp_text = f'Prediction:\n{output:.1%} probability\nPrice will RISE'
ax.text(layer_x[2] + 1.5, output_y, interp_text, fontsize=9, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

# Add flow arrows at bottom
for i in range(2):
    arrow = FancyArrowPatch((layer_x[i] + 0.5, 1.2), (layer_x[i+1] - 0.5, 1.2),
                           arrowstyle='->', mutation_scale=25, linewidth=2.5, color='darkblue')
    ax.add_patch(arrow)

ax.text(7, 0.5, 'FORWARD PROPAGATION: Data flows left to right', fontsize=11, ha='center',
        fontweight='bold', color='darkblue')

# Add computation boxes showing the calculations
calc1_text = 'Step 1:\n$z = W \cdot x + b$\n$a = \sigma(z)$'
ax.text(4.5, 8.5, calc1_text, fontsize=8, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

calc2_text = 'Step 2:\n$z = W \cdot a + b$\n$y = \sigma(z)$'
ax.text(9.5, 8.5, calc2_text, fontsize=8, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

# Add note about activation function
note_text = r'$\sigma(z) = \frac{1}{1+e^{-z}}$ (Sigmoid)'
ax.text(7, 1.8, note_text, fontsize=8, ha='center', style='italic')

plt.tight_layout()
plt.savefig('forward_propagation.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: forward_propagation.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/06_forward_propagation/
