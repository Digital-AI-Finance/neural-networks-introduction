# ==============================================================================
# Chart: Sigmoid Saturation
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/14_sigmoid_saturation/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Sigmoid Saturation

Vanishing gradient problem in sigmoid activation

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/14_sigmoid_saturation/
"""

CHART_METADATA = {
    'name': 'Sigmoid Saturation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/14_sigmoid_saturation',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Vanishing gradient problem in sigmoid activation'
}

"""
Chart 14: Sigmoid Saturation Problem
Shows vanishing gradient regions - why ReLU became popular.
"""

import numpy as np
import matplotlib.pyplot as plt

# Colors
mlpurple = '#3333b2'
mlblue = '#0066cc'
mlred = '#d62728'
mlgreen = '#2ca02c'
mlorange = '#ff7f0e'
mlgray = '#7f7f7f'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

x = np.linspace(-6, 6, 500)

# Sigmoid and its derivative
sigmoid = 1 / (1 + np.exp(-x))
sigmoid_deriv = sigmoid * (1 - sigmoid)

# ReLU and its derivative
relu = np.maximum(0, x)
relu_deriv = (x > 0).astype(float)

# Plot 1: Sigmoid with saturation zones
ax1 = axes[0]
ax1.plot(x, sigmoid, color=mlpurple, linewidth=3, label='Sigmoid')
ax1.axhline(y=0, color=mlgray, linestyle='-', alpha=0.3)
ax1.axhline(y=1, color=mlgray, linestyle='--', alpha=0.5)
ax1.axhline(y=0.5, color=mlgray, linestyle='--', alpha=0.5)

# Highlight saturation zones
ax1.axvspan(-6, -3, alpha=0.2, color=mlred, label='Saturation (gradient~0)')
ax1.axvspan(3, 6, alpha=0.2, color=mlred)
ax1.axvspan(-3, 3, alpha=0.15, color=mlgreen, label='Active zone')

ax1.annotate('Gradient\nvanishes!', xy=(-4.5, 0.1), fontsize=9, color=mlred,
            fontweight='bold', ha='center')
ax1.annotate('Gradient\nvanishes!', xy=(4.5, 0.9), fontsize=9, color=mlred,
            fontweight='bold', ha='center')

ax1.set_xlabel('Weighted Sum (z)', fontsize=10)
ax1.set_ylabel('Activation', fontsize=10)
ax1.set_title('Sigmoid: Saturation Problem', fontsize=11, fontweight='bold')
ax1.legend(loc='right', fontsize=8)
ax1.set_xlim(-6, 6)
ax1.set_ylim(-0.1, 1.1)
ax1.grid(True, alpha=0.3)

# Plot 2: Gradient comparison
ax2 = axes[1]
ax2.plot(x, sigmoid_deriv, color=mlpurple, linewidth=3, label='Sigmoid gradient')
ax2.fill_between(x, sigmoid_deriv, alpha=0.3, color=mlpurple)

ax2.axhline(y=0.25, color=mlorange, linestyle='--', alpha=0.7, linewidth=2)
ax2.annotate('Max = 0.25 only!', xy=(2, 0.27), fontsize=10, color=mlorange, fontweight='bold')

# Highlight the problem
ax2.annotate('Near-zero gradients\nmean no learning', xy=(-4, 0.05), fontsize=9,
            color=mlred, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax2.set_xlabel('Weighted Sum (z)', fontsize=10)
ax2.set_ylabel('Gradient Magnitude', fontsize=10)
ax2.set_title('Sigmoid Gradient is Tiny!', fontsize=11, fontweight='bold')
ax2.set_xlim(-6, 6)
ax2.set_ylim(-0.05, 0.35)
ax2.grid(True, alpha=0.3)

# Plot 3: ReLU solution
ax3 = axes[2]
ax3.plot(x, relu, color=mlblue, linewidth=3, label='ReLU')
ax3.plot(x[x>0], np.ones(sum(x>0)), color=mlgreen, linewidth=3, linestyle='--',
        label='ReLU gradient = 1')

ax3.axvline(x=0, color=mlgray, linestyle='-', alpha=0.3)
ax3.axhline(y=0, color=mlgray, linestyle='-', alpha=0.3)

# Highlight advantage
ax3.annotate('Constant gradient = 1\n(no vanishing!)', xy=(3, 1.5), fontsize=10,
            color=mlgreen, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlgreen, alpha=0.9))

ax3.annotate('Dead zone\n(but sparse)', xy=(-3, 0.5), fontsize=9,
            color=mlgray, ha='center')

ax3.set_xlabel('Weighted Sum (z)', fontsize=10)
ax3.set_ylabel('Activation / Gradient', fontsize=10)
ax3.set_title('ReLU: The Solution', fontsize=11, fontweight='bold')
ax3.legend(loc='upper left', fontsize=8)
ax3.set_xlim(-6, 6)
ax3.set_ylim(-1, 6)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sigmoid_saturation.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 14_sigmoid_saturation/sigmoid_saturation.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/14_sigmoid_saturation/
