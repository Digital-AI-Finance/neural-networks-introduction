"""
Regularization Comparison - Effect on Decision Boundaries
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Regularization Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/regularization_comparison'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

np.random.seed(42)

# Generate data
n = 50
X1_class1 = np.random.randn(n, 2) * 0.5 + np.array([1, 1])
X1_class2 = np.random.randn(n, 2) * 0.5 + np.array([-1, -1])

# Grid for decision boundary
xx, yy = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))

# ==================== LEFT: No Regularization ====================
ax = axes[0]

ax.scatter(X1_class1[:, 0], X1_class1[:, 1], c=mlgreen, s=50, alpha=0.7, label='Class 1')
ax.scatter(X1_class2[:, 0], X1_class2[:, 1], c=mlorange, s=50, alpha=0.7, label='Class 2')

# Complex (overfitting) decision boundary
# Simulate wiggling boundary
theta = np.linspace(-3, 3, 100)
boundary = 0.3 * np.sin(3 * theta) + np.random.randn(100) * 0.1
ax.plot(theta, boundary, color=mlred, linewidth=2)
ax.fill_between(theta, boundary, 3, alpha=0.1, color=mlgreen)
ax.fill_between(theta, -3, boundary, alpha=0.1, color=mlorange)

ax.set_xlabel('$x_1$', fontsize=11)
ax.set_ylabel('$x_2$', fontsize=11)
ax.set_title('No Regularization', fontsize=11, fontweight='bold', color=mlred)
ax.legend(loc='upper right', fontsize=8)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)

ax.text(0, -2.5, 'Overfits: complex boundary\nfits noise', fontsize=9, ha='center', color=mlred)

# ==================== MIDDLE: With Regularization ====================
ax = axes[1]

ax.scatter(X1_class1[:, 0], X1_class1[:, 1], c=mlgreen, s=50, alpha=0.7)
ax.scatter(X1_class2[:, 0], X1_class2[:, 1], c=mlorange, s=50, alpha=0.7)

# Simple (regularized) decision boundary
ax.plot([-3, 3], [-3, 3], color=mlblue, linewidth=2)
ax.fill_between([-3, 3], [-3, 3], [3, 3], alpha=0.1, color=mlgreen)
ax.fill_between([-3, 3], [-3, -3], [-3, 3], alpha=0.1, color=mlorange)

ax.set_xlabel('$x_1$', fontsize=11)
ax.set_ylabel('$x_2$', fontsize=11)
ax.set_title('With Regularization', fontsize=11, fontweight='bold', color=mlblue)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)

ax.text(0, -2.5, 'Generalizes: simple boundary\nignores noise', fontsize=9, ha='center', color=mlblue)

# ==================== RIGHT: Learning Curves ====================
ax = axes[2]

epochs = np.arange(100)

# No regularization
train_no_reg = 0.8 * np.exp(-0.1 * epochs) + 0.05
val_no_reg = 0.6 * np.exp(-0.05 * epochs) + 0.3 + 0.01 * epochs

# With regularization
train_reg = 0.8 * np.exp(-0.08 * epochs) + 0.15
val_reg = 0.6 * np.exp(-0.06 * epochs) + 0.18

ax.plot(epochs, train_no_reg, color=mlred, linewidth=2, label='Train (no reg)')
ax.plot(epochs, val_no_reg, color=mlred, linewidth=2, linestyle='--', label='Val (no reg)')
ax.plot(epochs, train_reg, color=mlblue, linewidth=2, label='Train (with reg)')
ax.plot(epochs, val_reg, color=mlblue, linewidth=2, linestyle='--', label='Val (with reg)')

ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Learning Curves', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)

# Annotation
ax.annotate('Gap = Overfitting', xy=(80, 0.6), xytext=(50, 0.8),
            fontsize=9, color=mlred,
            arrowprops=dict(arrowstyle='->', color=mlred))

fig.suptitle('Regularization: Preventing Overfitting',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('regularization_comparison.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('regularization_comparison.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: regularization_comparison.pdf")
