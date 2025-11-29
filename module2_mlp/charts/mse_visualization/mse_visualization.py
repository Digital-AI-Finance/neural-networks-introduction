"""
Mean Squared Error Loss Visualization
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'MSE Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mse_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# ==================== LEFT: MSE Concept ====================
ax = axes[0]

np.random.seed(42)
x = np.linspace(0, 10, 20)
y_true = 2 + 0.5 * x + np.random.randn(20) * 0.8
y_pred = 2 + 0.5 * x  # Perfect line

ax.scatter(x, y_true, c=mlblue, s=80, label='True values $y_i$', zorder=5)
ax.plot(x, y_pred, color=mlpurple, linewidth=2, label='Predictions $\\hat{y}_i$')

# Draw error bars
for xi, yi, ypi in zip(x[::3], y_true[::3], y_pred[::3]):
    ax.plot([xi, xi], [yi, ypi], color=mlred, linewidth=2, alpha=0.7)
    ax.scatter([xi], [(yi + ypi)/2], marker='s', c=mlred, s=30, alpha=0.5)

ax.set_xlabel('$x$', fontsize=11)
ax.set_ylabel('$y$', fontsize=11)
ax.set_title('MSE: Measuring Prediction Error', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

# MSE formula
ax.text(5, 1.5, '$MSE = \\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2$',
        fontsize=11, ha='center', color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

# ==================== MIDDLE: MSE as Function of Parameter ====================
ax = axes[1]

# MSE as function of weight w
w_range = np.linspace(-2, 4, 100)
true_w = 1.0
mse_values = (w_range - true_w)**2 + 0.1  # Simplified MSE curve

ax.plot(w_range, mse_values, color=mlpurple, linewidth=3)
ax.scatter([true_w], [0.1], c=mlgreen, s=150, marker='*', zorder=5, label='Optimal $w^*$')
ax.axvline(x=true_w, color=mlgray, linewidth=1, linestyle='--', alpha=0.5)

ax.set_xlabel('Weight $w$', fontsize=11)
ax.set_ylabel('MSE Loss', fontsize=11)
ax.set_title('Loss Landscape (1D)', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)

# Gradient arrow
ax.annotate('', xy=(1.5, 0.35), xytext=(2.5, 2.4),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=2))
ax.text(2.7, 1.5, 'Gradient\ndescent', fontsize=9, color=mlorange)

# ==================== RIGHT: Properties ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'MSE Properties', fontsize=12, fontweight='bold', ha='center', color=mlpurple)

properties = [
    ('Convex', 'Single global minimum for linear models', mlgreen),
    ('Differentiable', 'Smooth gradients everywhere', mlgreen),
    ('Scale-sensitive', 'Large errors penalized more (squared)', mlorange),
    ('Outlier-sensitive', 'Squares amplify outlier impact', mlred),
]

y_pos = 7.5
for name, desc, color in properties:
    ax.text(0.5, y_pos, name + ':', fontsize=10, fontweight='bold', color=color)
    ax.text(3.5, y_pos, desc, fontsize=9, color=mlgray)
    y_pos -= 1.5

# Use cases
ax.text(5, 2.5, 'Best for:', fontsize=10, fontweight='bold', ha='center', color=mlpurple)
ax.text(5, 1.5, 'Regression problems with\nnormally distributed errors',
        fontsize=9, ha='center', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

fig.suptitle('Mean Squared Error: The Classic Regression Loss',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('mse_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('mse_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: mse_visualization.pdf")
