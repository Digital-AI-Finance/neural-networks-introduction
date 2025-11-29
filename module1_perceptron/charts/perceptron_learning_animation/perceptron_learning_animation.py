"""
Perceptron Learning Animation (Static Frames)
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Perceptron Learning Animation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/perceptron_learning_animation'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure with 4 subplots showing iterations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Generate linearly separable data
np.random.seed(42)
n_per_class = 15

# Class 1 (positive)
x1_pos = np.random.randn(n_per_class) * 0.5 + 2
x2_pos = np.random.randn(n_per_class) * 0.5 + 2

# Class 0 (negative)
x1_neg = np.random.randn(n_per_class) * 0.5 + 0.5
x2_neg = np.random.randn(n_per_class) * 0.5 + 0.5

# Perceptron learning simulation
# Starting weights (bad)
w_history = [
    {'w1': 0.5, 'w2': -0.5, 'b': 0.5, 'iter': 0, 'errors': 12},
    {'w1': 0.8, 'w2': 0.2, 'b': -0.5, 'iter': 3, 'errors': 6},
    {'w1': 1.0, 'w2': 0.8, 'b': -1.8, 'iter': 8, 'errors': 2},
    {'w1': 1.0, 'w2': 1.0, 'b': -2.5, 'iter': 15, 'errors': 0}  # Final (converged)
]

titles = [
    'Iteration 0: Random Initialization',
    'Iteration 3: Adjusting...',
    'Iteration 8: Getting Better',
    'Iteration 15: Converged!'
]

for idx, (ax, weights, title) in enumerate(zip(axes.flat, w_history, titles)):
    # Plot data points
    ax.scatter(x1_pos, x2_pos, c=mlgreen, s=80, marker='o', label='Class 1 (Buy)',
               edgecolors='white', linewidths=1, zorder=5)
    ax.scatter(x1_neg, x2_neg, c=mlorange, s=80, marker='s', label='Class 0 (Sell)',
               edgecolors='white', linewidths=1, zorder=5)

    # Draw decision boundary: w1*x1 + w2*x2 + b = 0
    # => x2 = -(w1*x1 + b) / w2
    w1, w2, b = weights['w1'], weights['w2'], weights['b']

    x_line = np.linspace(-0.5, 3.5, 100)
    if abs(w2) > 0.01:
        y_line = -(w1 * x_line + b) / w2
        ax.plot(x_line, y_line, color=mlpurple, linewidth=2.5, label='Decision Boundary')

        # Shade regions
        ax.fill_between(x_line, y_line, 4, alpha=0.1, color=mlgreen)
        ax.fill_between(x_line, -1, y_line, alpha=0.1, color=mlorange)

    # Mark misclassified points
    for x1, x2 in zip(x1_pos, x2_pos):
        if w1 * x1 + w2 * x2 + b < 0:  # Should be positive
            ax.scatter([x1], [x2], s=200, facecolors='none', edgecolors=mlred, linewidths=2)

    for x1, x2 in zip(x1_neg, x2_neg):
        if w1 * x1 + w2 * x2 + b >= 0:  # Should be negative
            ax.scatter([x1], [x2], s=200, facecolors='none', edgecolors=mlred, linewidths=2)

    # Title and labels
    ax.set_title(title, fontsize=12, fontweight='bold',
                 color=mlgreen if weights['errors'] == 0 else mlpurple)
    ax.set_xlabel('$x_1$', fontsize=10)
    ax.set_ylabel('$x_2$', fontsize=10)

    # Error count
    error_color = mlgreen if weights['errors'] == 0 else mlred
    ax.text(0.02, 0.98, f"Errors: {weights['errors']}", transform=ax.transAxes,
            fontsize=10, verticalalignment='top', fontweight='bold', color=error_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=error_color, alpha=0.9))

    # Weight values
    ax.text(0.98, 0.02, f"$w_1$={w1:.1f}, $w_2$={w2:.1f}, $b$={b:.1f}",
            transform=ax.transAxes, fontsize=9, ha='right', color=mlgray)

    # Formatting
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 3.5)
    ax.grid(True, alpha=0.3)

    if idx == 0:
        ax.legend(loc='upper right', fontsize=8)

fig.suptitle('Perceptron Learning: Decision Boundary Adjusts Until Convergence',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('perceptron_learning_animation.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('perceptron_learning_animation.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: perceptron_learning_animation.pdf")
