"""
Hyperparameter Search Landscape
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Hyperparameter Landscape',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/hyperparameter_landscape'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

np.random.seed(42)

# ==================== LEFT: 2D Hyperparameter Landscape ====================
ax = axes[0]

# Create hyperparameter grid
lr = np.linspace(-4, 0, 100)  # log10(learning rate)
hidden = np.linspace(1, 3, 100)  # log10(hidden units)
LR, HIDDEN = np.meshgrid(lr, hidden)

# Simulated validation accuracy surface
acc = (0.9 - 0.3 * (LR + 2)**2 - 0.1 * (HIDDEN - 2)**2
       - 0.05 * np.sin(LR * 5) * np.sin(HIDDEN * 5))
acc = np.clip(acc, 0.4, 0.95)

contour = ax.contourf(LR, HIDDEN, acc, levels=20, cmap='RdYlGn')
plt.colorbar(contour, ax=ax, label='Validation Accuracy')

# Mark optimal region
ax.scatter([-2], [2], c='white', s=200, marker='*', edgecolors='black', linewidths=2)
ax.annotate('Optimal region', xy=(-2, 2), xytext=(-3, 2.5), fontsize=9,
            arrowprops=dict(arrowstyle='->', color='white'))

ax.set_xlabel('log$_{10}$(Learning Rate)', fontsize=11)
ax.set_ylabel('log$_{10}$(Hidden Units)', fontsize=11)
ax.set_title('Hyperparameter Landscape', fontsize=11, fontweight='bold', color=mlpurple)

# Grid search points
grid_lr = np.linspace(-3.5, -0.5, 5)
grid_hidden = np.linspace(1.3, 2.7, 5)
for l in grid_lr:
    for h in grid_hidden:
        ax.scatter([l], [h], c='blue', s=30, marker='s', alpha=0.5)

ax.text(-3.8, 1.1, 'Grid Search\npoints', fontsize=8, color=mlblue)

# Random search points
rand_lr = np.random.uniform(-4, 0, 25)
rand_hidden = np.random.uniform(1, 3, 25)
ax.scatter(rand_lr, rand_hidden, c='orange', s=30, marker='o', alpha=0.5)
ax.text(-0.8, 2.8, 'Random Search\npoints', fontsize=8, color=mlorange)

# ==================== RIGHT: Search Methods Comparison ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.3, 'Hyperparameter Search Methods', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

methods = [
    ('Grid Search', mlblue, [
        'Exhaustive search over grid',
        'Exponentially expensive',
        'May miss optimal region',
    ]),
    ('Random Search', mlorange, [
        'Sample randomly from ranges',
        'Often better than grid',
        'More efficient exploration',
    ]),
    ('Bayesian Optimization', mlgreen, [
        'Uses prior results',
        'Smart exploration',
        'Best for expensive evaluations',
    ]),
]

y_start = 7.5
for name, color, points in methods:
    ax.text(0.5, y_start, name, fontsize=10, fontweight='bold', color=color)
    for i, point in enumerate(points):
        ax.text(1, y_start - 0.6 - i * 0.5, '- ' + point, fontsize=9, color=mlgray)
    y_start -= 2.2

# Common hyperparameters box
hyperparams = """Key Hyperparameters to Tune:
- Learning rate: 1e-4 to 1e-1
- Hidden layer size: 32 to 1024
- Number of layers: 1 to 5
- Batch size: 16 to 256
- Regularization strength: 1e-5 to 1e-1
- Dropout rate: 0.1 to 0.5"""

ax.text(5, 0.8, hyperparams, ha='center', va='top', fontsize=8,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, linewidth=2))

fig.suptitle('Hyperparameter Optimization: Finding the Best Configuration',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('hyperparameter_landscape.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('hyperparameter_landscape.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: hyperparameter_landscape.pdf")
