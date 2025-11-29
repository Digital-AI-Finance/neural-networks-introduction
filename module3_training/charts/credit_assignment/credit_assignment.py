CHART_METADATA = {
    'title': 'Credit Assignment',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/credit_assignment'
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

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Network structure
layers = [[1.5, 2, 3, 4, 5], [2.5, 3.5, 4.5], [3, 4], [3.5]]
x_positions = [1, 3.5, 6, 8.5]

# Draw neurons
for layer_idx, (x, layer) in enumerate(zip(x_positions, layers)):
    for y in layer:
        color = mlpurple if layer_idx in [1, 2] else (mlblue if layer_idx == 0 else mlred)
        circle = plt.Circle((x, y), 0.25, color=color, alpha=0.8)
        ax.add_patch(circle)

# Draw connections with varying opacity to show credit
np.random.seed(42)
for i, (x1, layer1) in enumerate(zip(x_positions[:-1], layers[:-1])):
    x2 = x_positions[i+1]
    layer2 = layers[i+1]
    for y1 in layer1:
        for y2 in layer2:
            weight = np.random.uniform(0.1, 1.0)
            ax.plot([x1+0.25, x2-0.25], [y1, y2], color=mlgray, alpha=weight*0.5, lw=weight*2)

# Question marks showing credit assignment problem
ax.text(2.25, 5.5, '?', fontsize=20, color=mlorange, fontweight='bold')
ax.text(4.75, 5.5, '?', fontsize=20, color=mlorange, fontweight='bold')
ax.text(7.25, 5.5, '?', fontsize=20, color=mlorange, fontweight='bold')

# Error signal
ax.annotate('Error', xy=(8.5, 3.5), xytext=(9.5, 4.5),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=2),
            fontsize=11, color=mlred, fontweight='bold')

# Labels
ax.text(1, 0.5, 'Input', ha='center', fontsize=10, color=mlblue)
ax.text(3.5, 0.5, 'Hidden 1', ha='center', fontsize=10, color=mlpurple)
ax.text(6, 0.5, 'Hidden 2', ha='center', fontsize=10, color=mlpurple)
ax.text(8.5, 0.5, 'Output', ha='center', fontsize=10, color=mlred)

ax.text(5, 6.5, 'Credit Assignment Problem', fontsize=14, fontweight='bold', ha='center')
ax.text(5, 6, 'Which weights caused the error?', fontsize=11, ha='center', color=mlgray)

plt.tight_layout()
plt.savefig('credit_assignment.pdf', bbox_inches='tight', dpi=300)
plt.savefig('credit_assignment.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: credit_assignment.pdf")
