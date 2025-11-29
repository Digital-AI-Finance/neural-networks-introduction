CHART_METADATA = {
    'title': 'Dropout Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/dropout_visualization'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Without dropout
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8)
ax1.axis('off')

layers = [[2, 4, 6], [2, 4, 6], [2, 4, 6], [4]]
x_pos = [1.5, 4, 6.5, 9]

for i, (x, layer) in enumerate(zip(x_pos, layers)):
    for y in layer:
        circle = plt.Circle((x, y), 0.3, color=mlblue, alpha=0.8)
        ax1.add_patch(circle)

# Draw all connections
for i in range(len(x_pos)-1):
    for y1 in layers[i]:
        for y2 in layers[i+1]:
            ax1.plot([x_pos[i]+0.3, x_pos[i+1]-0.3], [y1, y2], 'k-', alpha=0.3, lw=1)

ax1.set_title('Standard Network\n(All connections active)', fontsize=11, fontweight='bold')

# Right: With dropout
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 8)
ax2.axis('off')

np.random.seed(42)
dropout_mask = [[True, True, False], [False, True, True], [True, False, True], [True]]

for i, (x, layer, mask) in enumerate(zip(x_pos, layers, dropout_mask)):
    for y, active in zip(layer, mask):
        if active:
            circle = plt.Circle((x, y), 0.3, color=mlgreen, alpha=0.8)
        else:
            circle = plt.Circle((x, y), 0.3, color=mlred, alpha=0.3)
            ax2.plot([x-0.2, x+0.2], [y-0.2, y+0.2], 'r-', lw=2)
            ax2.plot([x-0.2, x+0.2], [y+0.2, y-0.2], 'r-', lw=2)
        ax2.add_patch(circle)

# Draw only active connections
for i in range(len(x_pos)-1):
    for j, y1 in enumerate(layers[i]):
        for k, y2 in enumerate(layers[i+1]):
            if dropout_mask[i][j] and dropout_mask[i+1][k]:
                ax2.plot([x_pos[i]+0.3, x_pos[i+1]-0.3], [y1, y2], 'g-', alpha=0.5, lw=1)

ax2.set_title('With Dropout (p=0.3)\n(Random neurons disabled)', fontsize=11, fontweight='bold')

# Legend
fig.text(0.5, 0.02, 'Dropout prevents co-adaptation and reduces overfitting',
         ha='center', fontsize=11, color=mlgray)

plt.tight_layout()
plt.savefig('dropout_visualization.pdf', bbox_inches='tight', dpi=300)
plt.savefig('dropout_visualization.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: dropout_visualization.pdf")
