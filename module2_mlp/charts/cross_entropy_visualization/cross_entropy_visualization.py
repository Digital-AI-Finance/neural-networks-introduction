"""
Cross-Entropy Loss Visualization
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Cross Entropy Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/cross_entropy_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# ==================== LEFT: Binary Cross-Entropy ====================
ax = axes[0]

p = np.linspace(0.001, 0.999, 200)

# When y = 1: loss = -log(p)
loss_y1 = -np.log(p)
# When y = 0: loss = -log(1-p)
loss_y0 = -np.log(1 - p)

ax.plot(p, loss_y1, color=mlgreen, linewidth=3, label='$y=1$: $-\\log(\\hat{y})$')
ax.plot(p, loss_y0, color=mlred, linewidth=3, label='$y=0$: $-\\log(1-\\hat{y})$')

ax.set_xlabel('Predicted probability $\\hat{y}$', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Binary Cross-Entropy', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper center', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 1)
ax.set_ylim(0, 5)

# Annotations
ax.annotate('High penalty\nfor wrong prediction', xy=(0.1, 2.3), xytext=(0.3, 3.5),
            fontsize=8, color=mlgreen,
            arrowprops=dict(arrowstyle='->', color=mlgreen))

# Formula
ax.text(0.5, 4.5, '$L = -[y\\log(\\hat{y}) + (1-y)\\log(1-\\hat{y})]$',
        fontsize=9, ha='center', color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=mlpurple))

# ==================== MIDDLE: Gradient Behavior ====================
ax = axes[1]

# Gradient of cross-entropy
grad_ce = p - 1  # When y=1, gradient is (p-1) = -(1-p)

ax.plot(p, np.abs(grad_ce), color=mlorange, linewidth=3, label='$|\\nabla L|$ (Cross-Entropy)')

# Compare to MSE gradient
grad_mse = 2 * (p - 1) * p * (1 - p)  # MSE through sigmoid
ax.plot(p, np.abs(grad_mse), color=mlblue, linewidth=3, linestyle='--', label='$|\\nabla L|$ (MSE)')

ax.set_xlabel('Predicted probability $\\hat{y}$', fontsize=11)
ax.set_ylabel('Gradient magnitude', fontsize=11)
ax.set_title('Gradient Behavior', fontsize=11, fontweight='bold', color=mlorange)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)

# Key insight
ax.text(0.5, 1.3, 'Cross-entropy: Strong gradient when wrong',
        fontsize=9, ha='center', color=mlorange)
ax.text(0.5, 1.15, 'MSE: Weak gradient (saturates)',
        fontsize=9, ha='center', color=mlblue)

# ==================== RIGHT: Properties ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'Cross-Entropy Properties', fontsize=12, fontweight='bold', ha='center', color=mlpurple)

properties = [
    ('Probability-based', 'Measures information difference', mlgreen),
    ('Strong gradients', 'Fast learning from mistakes', mlgreen),
    ('No saturation', 'Always learns from errors', mlgreen),
    ('Natural for classification', 'Matches softmax output', mlblue),
]

y_pos = 7.5
for name, desc, color in properties:
    ax.text(0.5, y_pos, name + ':', fontsize=10, fontweight='bold', color=color)
    ax.text(4, y_pos, desc, fontsize=9, color=mlgray)
    y_pos -= 1.5

# Comparison box
ax.text(5, 2.2, 'Why use Cross-Entropy over MSE?', fontsize=10, fontweight='bold',
        ha='center', color=mlpurple)
comparison = """- Stronger gradients for confident wrong predictions
- Information-theoretic foundation
- Standard for classification tasks"""
ax.text(5, 0.8, comparison, fontsize=9, ha='center', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

fig.suptitle('Cross-Entropy: The Standard Classification Loss',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('cross_entropy_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('cross_entropy_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: cross_entropy_visualization.pdf")
