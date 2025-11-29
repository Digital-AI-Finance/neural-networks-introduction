"""
Vanishing Gradient Problem Demonstration
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Vanishing Gradient Demo',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/vanishing_gradient_demo'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

# ==================== LEFT: Sigmoid Derivative ====================
ax = axes[0]

z = np.linspace(-6, 6, 200)
sigmoid = 1 / (1 + np.exp(-z))
sigmoid_deriv = sigmoid * (1 - sigmoid)

ax.plot(z, sigmoid, color=mlblue, linewidth=2, label='$\\sigma(z)$')
ax.plot(z, sigmoid_deriv, color=mlorange, linewidth=2, label="$\\sigma'(z)$")

ax.axhline(y=0.25, color=mlred, linestyle='--', alpha=0.5)
ax.text(4, 0.27, 'Max = 0.25', fontsize=9, color=mlred)

ax.set_xlabel('$z$', fontsize=11)
ax.set_ylabel('Value', fontsize=11)
ax.set_title('Sigmoid & Its Derivative', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-0.1, 1.1)

ax.text(0, -0.05, "Derivative always < 0.25!", fontsize=9, ha='center', color=mlred)

# ==================== MIDDLE: Gradient Decay Through Layers ====================
ax = axes[1]

layers = np.arange(1, 11)
# Gradient magnitude: 0.25^n (sigmoid derivative)
gradient_sigmoid = 0.25 ** layers
# ReLU: gradient doesn't decay (ideally)
gradient_relu = np.ones_like(layers, dtype=float) * 0.8

ax.semilogy(layers, gradient_sigmoid, 'o-', color=mlorange, linewidth=2, markersize=8,
            label='Sigmoid: $0.25^L$')
ax.semilogy(layers, gradient_relu, 's--', color=mlgreen, linewidth=2, markersize=8,
            label='ReLU: constant')

ax.set_xlabel('Layer Depth', fontsize=11)
ax.set_ylabel('Gradient Magnitude (log scale)', fontsize=11)
ax.set_title('Gradient Decay Through Layers', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3, which='both')
ax.set_xlim(0.5, 10.5)

# Annotations
ax.annotate('Layer 5: gradient = $10^{-3}$', xy=(5, gradient_sigmoid[4]),
            xytext=(6, 0.01), fontsize=8, color=mlorange,
            arrowprops=dict(arrowstyle='->', color=mlorange))
ax.annotate('Layer 10: gradient = $10^{-6}$!', xy=(10, gradient_sigmoid[9]),
            xytext=(7, 1e-5), fontsize=8, color=mlred,
            arrowprops=dict(arrowstyle='->', color=mlred))

# ==================== RIGHT: The Problem ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'The Vanishing Gradient Problem', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

problems = [
    ('Problem:', 'Gradients shrink exponentially with depth', mlred),
    ('Cause:', "Sigmoid/tanh derivatives are < 1", mlorange),
    ('Effect:', "Early layers don't learn (gradients ~ 0)", mlred),
    ('Solutions:', '', mlgreen),
]

y_pos = 7.5
for label, text, color in problems:
    ax.text(0.5, y_pos, label, fontsize=10, fontweight='bold', color=color)
    if text:
        ax.text(2.5, y_pos, text, fontsize=10, color=mlgray)
    y_pos -= 1.2

# Solutions list
solutions = [
    '1. Use ReLU activation (gradient = 1 for z > 0)',
    '2. Careful weight initialization (He, Xavier)',
    '3. Batch normalization',
    '4. Residual connections (skip connections)',
    '5. LSTM/GRU for recurrent networks',
]

y_pos = 4.5
for sol in solutions:
    ax.text(1, y_pos, sol, fontsize=9, color=mlgray)
    y_pos -= 0.8

ax.text(5, 0.5, 'Key insight: ReLU solved this for feedforward networks!',
        fontsize=10, ha='center', color=mlgreen, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgreen))

fig.suptitle('Vanishing Gradients: Why Deep Networks Were Hard to Train',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('vanishing_gradient_demo.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('vanishing_gradient_demo.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: vanishing_gradient_demo.pdf")
