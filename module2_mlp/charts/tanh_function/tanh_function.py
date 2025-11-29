"""
Tanh Activation Function
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Tanh Function',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/tanh_function'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ==================== LEFT: Tanh Function ====================
ax = axes[0]

z = np.linspace(-4, 4, 200)
tanh_val = np.tanh(z)

ax.plot(z, tanh_val, color=mlblue, linewidth=3, label='$\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$')

# Key points
ax.scatter([0], [0], c=mlblue, s=100, zorder=5)
ax.annotate('(0, 0)', xy=(0, 0), xytext=(0.8, 0.2), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=mlgray))

# Asymptotes
ax.axhline(y=1, color=mlgray, linewidth=1, linestyle='--', alpha=0.7)
ax.axhline(y=-1, color=mlgray, linewidth=1, linestyle='--', alpha=0.7)
ax.axhline(y=0, color=mlgray, linewidth=0.5, alpha=0.5)
ax.text(3.5, 1.08, 'y = 1', fontsize=9, color=mlgray)
ax.text(3.5, -1.15, 'y = -1', fontsize=9, color=mlgray)

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel('$\\tanh(z)$', fontsize=12)
ax.set_title('Tanh Function', fontsize=12, fontweight='bold', color=mlblue)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.3, 1.3)

# Properties annotation
props = """Properties:
- Output: (-1, 1)
- Zero-centered!
- Smooth, differentiable
- Steeper than sigmoid"""
ax.text(-3.8, 1.15, props, fontsize=8, va='top', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

# ==================== RIGHT: Comparison with Sigmoid ====================
ax = axes[1]

sigmoid = 1 / (1 + np.exp(-z))

ax.plot(z, tanh_val, color=mlblue, linewidth=3, label='tanh(z)')
ax.plot(z, sigmoid, color=mlorange, linewidth=3, linestyle='--', label='sigmoid(z)')

# Show zero-centered advantage
ax.axhline(y=0, color=mlgray, linewidth=1, linestyle='-', alpha=0.5)
ax.annotate('Zero-centered', xy=(-2, 0), xytext=(-3, 0.5), fontsize=9, color=mlblue,
            arrowprops=dict(arrowstyle='->', color=mlblue))
ax.annotate('Not zero-centered', xy=(-2, 0.5), xytext=(-3.5, 0.8), fontsize=9, color=mlorange,
            arrowprops=dict(arrowstyle='->', color=mlorange))

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel('Activation', fontsize=12)
ax.set_title('Tanh vs Sigmoid', fontsize=12, fontweight='bold', color=mlpurple)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.3, 1.3)

# Key difference
ax.text(0, -1.1, 'Key: tanh is zero-centered, better gradient flow',
        fontsize=9, ha='center', color=mlblue, fontweight='bold')

# Relation formula
ax.text(2.5, -0.5, '$\\tanh(z) = 2\\sigma(2z) - 1$', fontsize=9, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=mlpurple))

fig.suptitle('Tanh: Zero-Centered Alternative to Sigmoid',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('tanh_function.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('tanh_function.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: tanh_function.pdf")
