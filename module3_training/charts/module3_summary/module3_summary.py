CHART_METADATA = {
    'title': 'Module 3 Summary',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/module3_summary'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.5, 'Module 3: Training Neural Networks', fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Main topics as boxes
topics = [
    (1.5, 7, 'Backpropagation', ['Chain rule', 'Gradient flow', 'Computational graphs'], mlpurple),
    (6, 7, 'Optimization', ['Gradient descent', 'Learning rate', 'Momentum', 'Adam'], mlblue),
    (10.5, 7, 'Challenges', ['Vanishing gradients', 'Exploding gradients', 'Local minima'], mlred),
    (1.5, 3.5, 'Regularization', ['L1/L2 penalties', 'Dropout', 'Early stopping'], mlgreen),
    (6, 3.5, 'Diagnostics', ['Train/Val curves', 'Overfitting detection', 'Hyperparameter tuning'], mlorange),
    (10.5, 3.5, 'Best Practices', ['Data splitting', 'Batch normalization', 'Weight init'], mlgray),
]

for x, y, title, items, color in topics:
    # Box
    rect = mpatches.FancyBboxPatch((x-1.3, y-1.5), 2.6, 2.8, boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.15, edgecolor=color, lw=2)
    ax.add_patch(rect)
    # Title
    ax.text(x, y+1, title, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
    # Items
    for i, item in enumerate(items):
        ax.text(x, y - 0.2 - i*0.5, f'- {item}', ha='center', va='center', fontsize=9, color='black')

# Key equation
ax.text(6, 1, 'Key Update Rule:', ha='center', fontsize=11, fontweight='bold')
ax.text(6, 0.4, r'$w \leftarrow w - \eta \cdot \nabla_w L$', ha='center', fontsize=14, color=mlpurple)

plt.tight_layout()
plt.savefig('module3_summary.pdf', bbox_inches='tight', dpi=300)
plt.savefig('module3_summary.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: module3_summary.pdf")
