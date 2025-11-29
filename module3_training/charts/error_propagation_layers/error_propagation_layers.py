CHART_METADATA = {
    'title': 'Error Propagation Layers',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/error_propagation_layers'
}

import matplotlib.pyplot as plt
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Error magnitude through layers
ax1 = axes[0]
layers = ['Output', 'Hidden 3', 'Hidden 2', 'Hidden 1', 'Input']
errors_healthy = [1.0, 0.8, 0.6, 0.4, 0.25]
errors_vanishing = [1.0, 0.5, 0.2, 0.05, 0.01]

x = np.arange(len(layers))
width = 0.35

bars1 = ax1.barh(x + width/2, errors_healthy, width, label='Healthy Gradient', color=mlgreen, alpha=0.8)
bars2 = ax1.barh(x - width/2, errors_vanishing, width, label='Vanishing Gradient', color=mlred, alpha=0.8)

ax1.set_yticks(x)
ax1.set_yticklabels(layers)
ax1.set_xlabel('Gradient Magnitude', fontsize=11)
ax1.set_title('Error Signal Magnitude by Layer', fontsize=12, fontweight='bold')
ax1.legend(loc='lower right')
ax1.set_xlim(0, 1.2)

# Right: Gradient flow visualization
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 6)
ax2.axis('off')

# Draw layers as boxes
layer_x = [1, 3, 5, 7, 9]
for i, x in enumerate(layer_x):
    rect = plt.Rectangle((x-0.4, 2), 0.8, 2, fill=True,
                          color=mlpurple if i > 0 and i < 4 else (mlblue if i == 0 else mlred),
                          alpha=0.7)
    ax2.add_patch(rect)

# Gradient arrows (decreasing size)
arrow_sizes = [1.0, 0.7, 0.4, 0.2]
for i in range(len(layer_x)-1):
    ax2.annotate('', xy=(layer_x[i]+0.5, 3), xytext=(layer_x[i+1]-0.5, 3),
                arrowprops=dict(arrowstyle='->', color=mlred, lw=3*arrow_sizes[i],
                               mutation_scale=15*arrow_sizes[i]))

ax2.text(5, 5.2, 'Gradient Flow (Backward)', fontsize=12, fontweight='bold', ha='center')
ax2.text(5, 0.8, 'Gradients shrink as they propagate backward', fontsize=10, ha='center', color=mlgray)

# Layer labels
labels = ['Input', 'H1', 'H2', 'H3', 'Output']
for i, (x, label) in enumerate(zip(layer_x, labels)):
    ax2.text(x, 1.5, label, ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('error_propagation_layers.pdf', bbox_inches='tight', dpi=300)
plt.savefig('error_propagation_layers.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: error_propagation_layers.pdf")
