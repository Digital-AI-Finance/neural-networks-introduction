"""
Activation Functions Comparison
Module 2: Stacking Layers
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Activation Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/activation_comparison'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# X range
x = np.linspace(-5, 5, 200)

# Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Tanh
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# ReLU
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

# Step function
def step(x):
    return (x >= 0).astype(float)

# ==================== SIGMOID ====================
ax = axes[0, 0]
ax.plot(x, sigmoid(x), color=mlpurple, linewidth=2.5, label='$\\sigma(z)$')
ax.plot(x, sigmoid_derivative(x), color=mlorange, linewidth=2, linestyle='--', label="$\\sigma'(z)$")
ax.axhline(y=0, color='lightgray', linewidth=0.5)
ax.axhline(y=1, color='lightgray', linewidth=0.5)
ax.axhline(y=0.5, color='lightgray', linewidth=0.5, linestyle=':')
ax.axvline(x=0, color='lightgray', linewidth=0.5)
ax.set_title('Sigmoid', fontsize=14, fontweight='bold', color=mlpurple)
ax.set_xlabel('z', fontsize=11)
ax.set_ylabel('Output', fontsize=11)
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(-5, 5)
ax.set_ylim(-0.3, 1.3)
ax.grid(True, alpha=0.3)
ax.text(2, 0.1, '$\\sigma(z) = \\frac{1}{1+e^{-z}}$', fontsize=10, color=mlpurple)
ax.text(2, -0.15, 'Range: (0, 1)', fontsize=9, color=mlgray)

# ==================== TANH ====================
ax = axes[0, 1]
ax.plot(x, tanh(x), color=mlblue, linewidth=2.5, label='$\\tanh(z)$')
ax.plot(x, tanh_derivative(x), color=mlorange, linewidth=2, linestyle='--', label="$\\tanh'(z)$")
ax.axhline(y=0, color='lightgray', linewidth=0.5)
ax.axhline(y=1, color='lightgray', linewidth=0.5, linestyle=':')
ax.axhline(y=-1, color='lightgray', linewidth=0.5, linestyle=':')
ax.axvline(x=0, color='lightgray', linewidth=0.5)
ax.set_title('Tanh', fontsize=14, fontweight='bold', color=mlblue)
ax.set_xlabel('z', fontsize=11)
ax.set_ylabel('Output', fontsize=11)
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(-5, 5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3)
ax.text(2, -0.9, '$\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$', fontsize=10, color=mlblue)
ax.text(2, -1.3, 'Range: (-1, 1)', fontsize=9, color=mlgray)

# ==================== ReLU ====================
ax = axes[1, 0]
ax.plot(x, relu(x), color=mlgreen, linewidth=2.5, label='ReLU(z)')
ax.plot(x, relu_derivative(x), color=mlorange, linewidth=2, linestyle='--', label="ReLU'(z)")
ax.axhline(y=0, color='lightgray', linewidth=0.5)
ax.axvline(x=0, color='lightgray', linewidth=0.5)
ax.set_title('ReLU (Rectified Linear Unit)', fontsize=14, fontweight='bold', color=mlgreen)
ax.set_xlabel('z', fontsize=11)
ax.set_ylabel('Output', fontsize=11)
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.grid(True, alpha=0.3)
ax.text(1.5, 3.5, 'ReLU$(z) = \\max(0, z)$', fontsize=10, color=mlgreen)
ax.text(1.5, 2.8, 'Range: [0, +inf)', fontsize=9, color=mlgray)

# ==================== COMPARISON ====================
ax = axes[1, 1]
ax.plot(x, sigmoid(x), color=mlpurple, linewidth=2, label='Sigmoid')
ax.plot(x, tanh(x), color=mlblue, linewidth=2, label='Tanh')
ax.plot(x, relu(x) / 5, color=mlgreen, linewidth=2, label='ReLU (scaled)')
ax.plot(x, step(x), color=mlgray, linewidth=2, linestyle=':', label='Step')
ax.axhline(y=0, color='lightgray', linewidth=0.5)
ax.axvline(x=0, color='lightgray', linewidth=0.5)
ax.set_title('Comparison (All Functions)', fontsize=14, fontweight='bold', color='black')
ax.set_xlabel('z', fontsize=11)
ax.set_ylabel('Output', fontsize=11)
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(-5, 5)
ax.set_ylim(-1.3, 1.3)
ax.grid(True, alpha=0.3)

# Add comparison table
comparison_text = """Key Differences:
- Step: Not differentiable (can't use gradient descent)
- Sigmoid: Smooth but saturates (vanishing gradients)
- Tanh: Zero-centered (better than sigmoid)
- ReLU: Simple, fast, no saturation for z > 0"""
ax.text(0, -1.1, comparison_text, fontsize=8, va='top', color=mlgray,
        transform=ax.transData)

fig.suptitle('Activation Functions: Function and Derivative', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('activation_comparison.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('activation_comparison.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: activation_comparison.pdf")
