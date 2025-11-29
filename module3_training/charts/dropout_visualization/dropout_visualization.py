"""
Dropout Visualization
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

CHART_METADATA = {
    'title': 'Dropout Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/dropout_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 6))

np.random.seed(42)

# Network structure
layer_sizes = [4, 6, 6, 2]
layer_x = [1.5, 4, 6.5, 9]

def draw_network(ax, title, dropout_mask=None, color=mlpurple):
    """Draw neural network with optional dropout"""
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=11, fontweight='bold', color=color)

    neurons = {}
    for l, (x, n) in enumerate(zip(layer_x, layer_sizes)):
        start_y = 5 + (n - 1) * 0.7 / 2
        for i in range(n):
            y = start_y - i * 0.7
            neurons[(l, i)] = (x, y)

            # Check if dropped
            dropped = False
            if dropout_mask is not None and l > 0 and l < len(layer_sizes) - 1:
                dropped = dropout_mask[l - 1][i] if i < len(dropout_mask[l - 1]) else False

            if dropped:
                # Dropped neuron
                circle = Circle((x, y), 0.25, fill=True,
                               facecolor='white', edgecolor=mlgray, linewidth=1, linestyle='--', alpha=0.3)
                ax.add_patch(circle)
                ax.text(x, y, 'X', ha='center', va='center', fontsize=8, color=mlgray)
            else:
                # Active neuron
                facecolor = [mlblue, mlorange, mlorange, mlgreen][l]
                circle = Circle((x, y), 0.25, fill=True,
                               facecolor=f'{facecolor}44', edgecolor=facecolor, linewidth=2)
                ax.add_patch(circle)

    # Draw connections
    for l in range(len(layer_sizes) - 1):
        for i in range(layer_sizes[l]):
            for j in range(layer_sizes[l + 1]):
                x1, y1 = neurons[(l, i)]
                x2, y2 = neurons[(l + 1, j)]

                # Check if either neuron is dropped
                dropped1 = False
                dropped2 = False
                if dropout_mask is not None:
                    if l > 0 and l < len(layer_sizes) - 1:
                        dropped1 = dropout_mask[l - 1][i] if i < len(dropout_mask[l - 1]) else False
                    if l + 1 > 0 and l + 1 < len(layer_sizes) - 1:
                        dropped2 = dropout_mask[l][j] if j < len(dropout_mask[l]) else False

                if dropped1 or dropped2:
                    ax.plot([x1 + 0.25, x2 - 0.25], [y1, y2], color=mlgray,
                           linewidth=0.3, alpha=0.2, linestyle='--')
                else:
                    ax.plot([x1 + 0.25, x2 - 0.25], [y1, y2], color=mlgray,
                           linewidth=0.5, alpha=0.5)

    return neurons

# ==================== LEFT: Full Network (No Dropout) ====================
draw_network(axes[0], 'Full Network (Inference)', None, mlblue)
axes[0].text(5.25, 1.5, 'All neurons active\nduring inference', ha='center', fontsize=9, color=mlblue)

# ==================== MIDDLE: Training with Dropout ====================
# Random dropout mask (50% dropout)
dropout_mask = [
    [True, False, True, False, True, False],  # Hidden 1
    [False, True, False, True, False, True],  # Hidden 2
]
draw_network(axes[1], 'Training with Dropout (p=0.5)', dropout_mask, mlorange)
axes[1].text(5.25, 1.5, '50% neurons randomly\ndropped each batch', ha='center', fontsize=9, color=mlorange)

# ==================== RIGHT: Explanation ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'Dropout Explained', fontsize=12, fontweight='bold', ha='center', color=mlpurple)

content = [
    ('Training:', 'Randomly drop neurons with probability p', mlorange),
    ('', 'Forces redundant representations', mlgray),
    ('', 'Prevents co-adaptation', mlgray),
    ('Inference:', 'Use ALL neurons', mlblue),
    ('', 'Scale outputs by (1-p)', mlblue),
    ('Effect:', 'Ensemble of thin networks', mlgreen),
    ('Typical p:', '0.2-0.5 for hidden layers', mlgray),
]

y_pos = 7.5
for label, text, color in content:
    if label:
        ax.text(0.5, y_pos, label, fontsize=10, fontweight='bold', color=color)
    ax.text(2.5, y_pos, text, fontsize=9, color=color if not label else mlgray)
    y_pos -= 0.8

# Formula
ax.text(5, 2, 'During training: $\\tilde{h} = h \\cdot m$, where $m \\sim \\text{Bernoulli}(1-p)$',
        ha='center', fontsize=10, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

ax.text(5, 0.8, 'Introduced by Hinton et al. (2012) - Simple yet highly effective!',
        ha='center', fontsize=9, style='italic', color=mlgray)

fig.suptitle('Dropout: A Simple Regularization Technique',
             fontsize=14, fontweight='bold', color=mlpurple, y=0.98)

plt.tight_layout()
plt.savefig('dropout_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('dropout_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: dropout_visualization.pdf")
