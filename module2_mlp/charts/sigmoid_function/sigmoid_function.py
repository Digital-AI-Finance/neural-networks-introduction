"""
Sigmoid Activation Function
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Sigmoid Function',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/sigmoid_function'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ==================== LEFT: Sigmoid Function ====================
ax = axes[0]

z = np.linspace(-6, 6, 200)
sigmoid = 1 / (1 + np.exp(-z))

ax.plot(z, sigmoid, color=mlpurple, linewidth=3, label='$\\sigma(z) = \\frac{1}{1 + e^{-z}}$')

# Key points
ax.scatter([0], [0.5], c=mlpurple, s=100, zorder=5)
ax.annotate('(0, 0.5)', xy=(0, 0.5), xytext=(1, 0.6), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=mlgray))

# Asymptotes
ax.axhline(y=1, color=mlgray, linewidth=1, linestyle='--', alpha=0.7)
ax.axhline(y=0, color=mlgray, linewidth=1, linestyle='--', alpha=0.7)
ax.text(5, 1.05, 'y = 1', fontsize=9, color=mlgray)
ax.text(5, -0.08, 'y = 0', fontsize=9, color=mlgray)

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel('$\\sigma(z)$', fontsize=12)
ax.set_title('Sigmoid Function', fontsize=12, fontweight='bold', color=mlpurple)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-0.1, 1.1)

# Properties annotation
props = """Properties:
- Output: (0, 1)
- Smooth, differentiable
- S-shaped curve
- Maps any input to probability"""
ax.text(-5.5, 0.95, props, fontsize=8, va='top', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

# ==================== RIGHT: Sigmoid Derivative ====================
ax = axes[1]

sigmoid_derivative = sigmoid * (1 - sigmoid)

ax.plot(z, sigmoid_derivative, color=mlorange, linewidth=3,
        label="$\\sigma'(z) = \\sigma(z)(1 - \\sigma(z))$")

# Maximum point
ax.scatter([0], [0.25], c=mlorange, s=100, zorder=5)
ax.annotate('Max = 0.25', xy=(0, 0.25), xytext=(1, 0.3), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=mlgray))

# Vanishing gradient regions
ax.fill_between(z[z < -3], sigmoid_derivative[z < -3], alpha=0.3, color='red')
ax.fill_between(z[z > 3], sigmoid_derivative[z > 3], alpha=0.3, color='red')
ax.text(-5, 0.08, 'Vanishing\ngradient', fontsize=8, color='red', ha='center')
ax.text(5, 0.08, 'Vanishing\ngradient', fontsize=8, color='red', ha='center')

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel("$\\sigma'(z)$", fontsize=12)
ax.set_title('Sigmoid Derivative (Gradient)', fontsize=12, fontweight='bold', color=mlorange)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-0.02, 0.35)

# Warning annotation
ax.text(0, -0.015, 'Problem: Gradient vanishes for large |z|', fontsize=9,
        ha='center', color='red', fontweight='bold')

fig.suptitle('Sigmoid: The Classic Activation Function',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('sigmoid_function.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('sigmoid_function.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: sigmoid_function.pdf")
