# ==============================================================================
# Chart: Network Architecture
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/05_network_architecture/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Network Architecture

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/05_network_architecture/
"""

CHART_METADATA = {
    'name': 'Network Architecture',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/05_network_architecture',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
fig.suptitle('Neural Network Architecture: Building Intelligence in Layers', fontsize=16, fontweight='bold')

# Layer positions
input_x = 2
hidden_x = 7
output_x = 12

# Number of neurons per layer
n_inputs = 5
n_hidden = 6
n_output = 1

# Input layer
input_y_positions = np.linspace(2, 8, n_inputs)
input_neurons = []
input_labels = ['Yesterday\nPrice', 'Trading\nVolume', 'Market\nSentiment', 'Volatility\nIndex', 'Interest\nRate']

ax.text(input_x, 9.5, 'INPUT LAYER', fontsize=12, ha='center', fontweight='bold', color='blue')
ax.text(input_x, 9, '(Market Features)', fontsize=9, ha='center', style='italic', color='blue')

for i, (y_pos, label) in enumerate(zip(input_y_positions, input_labels)):
    circle = Circle((input_x, y_pos), 0.35, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(circle)
    input_neurons.append((input_x, y_pos))
    ax.text(input_x - 1.3, y_pos, label, fontsize=8, ha='right', va='center')

# Hidden layer
hidden_y_positions = np.linspace(1.5, 8.5, n_hidden)
hidden_neurons = []

ax.text(hidden_x, 9.5, 'HIDDEN LAYER', fontsize=12, ha='center', fontweight='bold', color='green')
ax.text(hidden_x, 9, '(Pattern Detection)', fontsize=9, ha='center', style='italic', color='green')

for i, y_pos in enumerate(hidden_y_positions):
    circle = Circle((hidden_x, y_pos), 0.35, facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(circle)
    hidden_neurons.append((hidden_x, y_pos))

# Output layer
output_y = 5
ax.text(output_x, 9.5, 'OUTPUT LAYER', fontsize=12, ha='center', fontweight='bold', color='darkorange')
ax.text(output_x, 9, '(Prediction)', fontsize=9, ha='center', style='italic', color='darkorange')

output_circle = Circle((output_x, output_y), 0.4, facecolor='orange', edgecolor='darkorange', linewidth=3)
ax.add_patch(output_circle)
ax.text(output_x + 1.3, output_y, 'Price\nDirection', fontsize=9, ha='left', va='center', fontweight='bold')

# Draw connections (sample, not all to avoid clutter)
# Input to Hidden (show a subset)
for i, (in_x, in_y) in enumerate(input_neurons):
    for j, (h_x, h_y) in enumerate(hidden_neurons):
        # Draw all connections but with varying alpha
        alpha = 0.15 if (i + j) % 3 != 0 else 0.3
        linewidth = 0.5 if (i + j) % 3 != 0 else 1.5
        ax.plot([in_x + 0.35, h_x - 0.35], [in_y, h_y], 'gray', alpha=alpha, linewidth=linewidth, zorder=1)

# Highlight a few connections
ax.plot([input_neurons[0][0] + 0.35, hidden_neurons[2][0] - 0.35],
        [input_neurons[0][1], hidden_neurons[2][1]], 'blue', alpha=0.6, linewidth=2, zorder=2)
ax.plot([input_neurons[2][0] + 0.35, hidden_neurons[4][0] - 0.35],
        [input_neurons[2][1], hidden_neurons[4][1]], 'blue', alpha=0.6, linewidth=2, zorder=2)

# Hidden to Output (draw all)
for h_x, h_y in hidden_neurons:
    ax.plot([h_x + 0.35, output_x - 0.4], [h_y, output_y], 'gray', alpha=0.3, linewidth=1, zorder=1)

# Highlight a few
ax.plot([hidden_neurons[1][0] + 0.35, output_x - 0.4],
        [hidden_neurons[1][1], output_y], 'green', alpha=0.6, linewidth=2, zorder=2)
ax.plot([hidden_neurons[4][0] + 0.35, output_x - 0.4],
        [hidden_neurons[4][1], output_y], 'green', alpha=0.6, linewidth=2, zorder=2)

# Add weight notation
ax.text(4.5, 7, 'Weights $W^{(1)}$', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
ax.text(9.5, 7, 'Weights $W^{(2)}$', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

# Add information flow arrows
arrow1 = FancyArrowPatch((input_x, 0.8), (hidden_x, 0.8),
                        arrowstyle='->', mutation_scale=30, linewidth=3, color='darkblue', alpha=0.5)
ax.add_patch(arrow1)
ax.text((input_x + hidden_x) / 2, 0.3, 'Information Flow', fontsize=10, ha='center', color='darkblue', fontweight='bold')

arrow2 = FancyArrowPatch((hidden_x, 0.8), (output_x, 0.8),
                        arrowstyle='->', mutation_scale=30, linewidth=3, color='darkblue', alpha=0.5)
ax.add_patch(arrow2)

# Add annotations
annotation_text = 'Each connection has a WEIGHT\nEach neuron applies ACTIVATION FUNCTION'
ax.text(7, 0.5, annotation_text, fontsize=9, ha='center', style='italic',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

# Network summary box
summary_text = 'Network Summary:\n'
summary_text += f'{n_inputs} Inputs\n'
summary_text += f'{n_hidden} Hidden Neurons\n'
summary_text += f'{n_output} Output\n'
summary_text += f'Total Weights: {n_inputs * n_hidden + n_hidden * n_output}'
ax.text(13.5, 2.5, summary_text, fontsize=8, ha='right', va='center',
        bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

plt.tight_layout()
plt.savefig('network_architecture.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: network_architecture.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/05_network_architecture/
