# ==============================================================================
# Chart: Activation Functions
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/03_activation_functions/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Activation Functions

Comparison of step function, sigmoid, ReLU, and tanh activations

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/03_activation_functions/
"""

CHART_METADATA = {
    'name': 'Activation Functions',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/03_activation_functions',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Comparison of step function, sigmoid, ReLU, and tanh activations'
}

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
fig.suptitle('Activation Functions: Adding Non-Linearity', fontsize=16, fontweight='bold')

# Generate x values
x = np.linspace(-5, 5, 100)

# 1. Sigmoid Function
ax1 = axes[0]
sigmoid = 1 / (1 + np.exp(-x))
ax1.plot(x, sigmoid, 'b-', linewidth=3, label='Sigmoid')
ax1.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.axhline(y=1, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.axvline(x=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('Input (z)', fontsize=11)
ax1.set_ylabel('Output', fontsize=11)
ax1.set_title('Sigmoid (Logistic)', fontsize=13, fontweight='bold')
ax1.set_ylim([-0.1, 1.1])

# Add formula
ax1.text(0, -0.25, r'$f(z) = \frac{1}{1+e^{-z}}$', fontsize=11, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Add characteristics
char_text = 'Range: (0, 1)\nSmooth gradient\nGood for probabilities'
ax1.text(3, 0.3, char_text, fontsize=8, ha='left', va='center',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

# 2. ReLU Function
ax2 = axes[1]
relu = np.maximum(0, x)
ax2.plot(x, relu, 'r-', linewidth=3, label='ReLU')
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.axvline(x=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('Input (z)', fontsize=11)
ax2.set_ylabel('Output', fontsize=11)
ax2.set_title('ReLU (Rectified Linear Unit)', fontsize=13, fontweight='bold')
ax2.set_ylim([-1, 5])

# Add formula
ax2.text(0, -1.5, r'$f(z) = \max(0, z)$', fontsize=11, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Add characteristics
char_text = 'Range: [0, $\infty$)\nFast computation\nMost popular today'
ax2.text(3, 1.5, char_text, fontsize=8, ha='left', va='center',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

# Highlight the kink
ax2.plot(0, 0, 'ro', markersize=8)
ax2.annotate('Kink at zero', xy=(0, 0), xytext=(1.5, 0.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            fontsize=8)

# 3. Tanh Function
ax3 = axes[2]
tanh = np.tanh(x)
ax3.plot(x, tanh, 'g-', linewidth=3, label='Tanh')
ax3.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax3.axhline(y=1, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax3.axhline(y=-1, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax3.axvline(x=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax3.grid(True, alpha=0.3)
ax3.set_xlabel('Input (z)', fontsize=11)
ax3.set_ylabel('Output', fontsize=11)
ax3.set_title('Tanh (Hyperbolic Tangent)', fontsize=13, fontweight='bold')
ax3.set_ylim([-1.1, 1.1])

# Add formula
ax3.text(0, -1.45, r'$f(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$', fontsize=11, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Add characteristics
char_text = 'Range: (-1, 1)\nZero-centered\nSimilar to sigmoid'
ax3.text(3, 0.3, char_text, fontsize=8, ha='left', va='center',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.tight_layout()
plt.savefig('activation_functions.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: activation_functions.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/03_activation_functions/
