CHART_METADATA = {
    'title': 'Backprop Flow Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/backprop_flow_diagram'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

# Draw layers
layer_positions = [1.5, 4, 6.5, 9, 10.5]
layer_names = ['Input\n$x$', 'Hidden 1\n$h_1$', 'Hidden 2\n$h_2$', 'Output\n$\\hat{y}$', 'Loss\n$L$']
layer_colors = [mlblue, mlpurple, mlpurple, mlgreen, mlred]

for i, (pos, name, color) in enumerate(zip(layer_positions, layer_names, layer_colors)):
    circle = plt.Circle((pos, 3), 0.6, color=color, alpha=0.7)
    ax.add_patch(circle)
    ax.text(pos, 3, name, ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# Forward pass arrows (top)
for i in range(len(layer_positions)-1):
    ax.annotate('', xy=(layer_positions[i+1]-0.7, 3.8), xytext=(layer_positions[i]+0.7, 3.8),
                arrowprops=dict(arrowstyle='->', color=mlblue, lw=2))
ax.text(6, 4.5, 'Forward Pass', ha='center', fontsize=11, color=mlblue, fontweight='bold')

# Backward pass arrows (bottom)
for i in range(len(layer_positions)-1, 0, -1):
    ax.annotate('', xy=(layer_positions[i-1]+0.7, 2.2), xytext=(layer_positions[i]-0.7, 2.2),
                arrowprops=dict(arrowstyle='->', color=mlred, lw=2))
ax.text(6, 1.3, 'Backward Pass (Gradients)', ha='center', fontsize=11, color=mlred, fontweight='bold')

# Gradient labels
grad_labels = ['$\\frac{\\partial L}{\\partial x}$', '$\\frac{\\partial L}{\\partial h_1}$',
               '$\\frac{\\partial L}{\\partial h_2}$', '$\\frac{\\partial L}{\\partial \\hat{y}}$']
for i, label in enumerate(grad_labels):
    ax.text(layer_positions[i]+1.25, 1.8, label, ha='center', fontsize=9, color=mlred)

ax.set_title('Backpropagation: Forward and Backward Pass', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('backprop_flow_diagram.pdf', bbox_inches='tight', dpi=300)
plt.savefig('backprop_flow_diagram.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: backprop_flow_diagram.pdf")
