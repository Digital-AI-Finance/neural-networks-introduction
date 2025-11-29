"""
Activation Functions and Their Derivatives
Appendix: Mathematical Foundations
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Activation Derivatives',
    'url': 'https://github.com/QuantLet/NeuralNetworks/tree/main/appendix/charts/activation_derivatives'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(2, 3, figsize=(14, 9))

z = np.linspace(-5, 5, 200)

# ==================== Sigmoid ====================
ax = axes[0, 0]
sigmoid = 1 / (1 + np.exp(-z))
sigmoid_deriv = sigmoid * (1 - sigmoid)

ax.plot(z, sigmoid, color=mlblue, linewidth=2, label='$\\sigma(z)$')
ax.plot(z, sigmoid_deriv, color=mlorange, linewidth=2, linestyle='--', label="$\\sigma'(z)$")
ax.set_title('Sigmoid', fontsize=11, fontweight='bold', color=mlblue)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('$z$', fontsize=10)

# Formula
ax.text(0, -0.05, "$\\sigma(z) = \\frac{1}{1+e^{-z}}$\n$\\sigma'(z) = \\sigma(z)(1-\\sigma(z))$",
        fontsize=7, ha='center', va='top', color=mlgray)

# ==================== Tanh ====================
ax = axes[0, 1]
tanh = np.tanh(z)
tanh_deriv = 1 - tanh**2

ax.plot(z, tanh, color=mlblue, linewidth=2, label='$\\tanh(z)$')
ax.plot(z, tanh_deriv, color=mlorange, linewidth=2, linestyle='--', label="$\\tanh'(z)$")
ax.set_title('Tanh', fontsize=11, fontweight='bold', color=mlblue)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel('$z$', fontsize=10)

ax.text(0, -1.05, "$\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$\n$\\tanh'(z) = 1 - \\tanh^2(z)$",
        fontsize=7, ha='center', va='top', color=mlgray)

# ==================== ReLU ====================
ax = axes[0, 2]
relu = np.maximum(0, z)
relu_deriv = (z > 0).astype(float)

ax.plot(z, relu, color=mlblue, linewidth=2, label='ReLU$(z)$')
ax.step(z, relu_deriv, color=mlorange, linewidth=2, linestyle='--', label="ReLU$'(z)$", where='mid')
ax.set_title('ReLU', fontsize=11, fontweight='bold', color=mlgreen)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-0.5, 5)
ax.set_xlabel('$z$', fontsize=10)

ax.text(0, -0.4, "ReLU$(z) = \\max(0, z)$\nReLU$'(z) = 1$ if $z > 0$, else $0$",
        fontsize=7, ha='center', va='top', color=mlgray)

# ==================== Leaky ReLU ====================
ax = axes[1, 0]
alpha = 0.1
leaky_relu = np.where(z > 0, z, alpha * z)
leaky_relu_deriv = np.where(z > 0, 1, alpha)

ax.plot(z, leaky_relu, color=mlblue, linewidth=2, label='LeakyReLU$(z)$')
ax.step(z, leaky_relu_deriv, color=mlorange, linewidth=2, linestyle='--', label="LeakyReLU$'(z)$", where='mid')
ax.set_title('Leaky ReLU ($\\alpha=0.1$)', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.set_xlabel('$z$', fontsize=10)

ax.text(0, -0.9, "LeakyReLU$(z) = z$ if $z > 0$, else $\\alpha z$\nLeakyReLU$'(z) = 1$ if $z > 0$, else $\\alpha$",
        fontsize=7, ha='center', va='top', color=mlgray)

# ==================== Softplus ====================
ax = axes[1, 1]
softplus = np.log(1 + np.exp(z))
softplus_deriv = sigmoid  # derivative of softplus is sigmoid

ax.plot(z, softplus, color=mlblue, linewidth=2, label='Softplus$(z)$')
ax.plot(z, softplus_deriv, color=mlorange, linewidth=2, linestyle='--', label="Softplus$'(z)$")
ax.set_title('Softplus', fontsize=11, fontweight='bold', color=mlorange)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-0.5, 5)
ax.set_xlabel('$z$', fontsize=10)

ax.text(0, -0.4, "Softplus$(z) = \\log(1 + e^z)$\nSoftplus$'(z) = \\sigma(z)$",
        fontsize=7, ha='center', va='top', color=mlgray)

# ==================== Swish ====================
ax = axes[1, 2]
swish = z * sigmoid
swish_deriv = sigmoid + z * sigmoid_deriv

ax.plot(z, swish, color=mlblue, linewidth=2, label='Swish$(z)$')
ax.plot(z, swish_deriv, color=mlorange, linewidth=2, linestyle='--', label="Swish$'(z)$")
ax.set_title('Swish', fontsize=11, fontweight='bold', color=mlred)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.set_xlabel('$z$', fontsize=10)

ax.text(0, -0.9, "Swish$(z) = z \\cdot \\sigma(z)$\nSwish$'(z) = \\sigma(z) + z \\cdot \\sigma(z)(1-\\sigma(z))$",
        fontsize=7, ha='center', va='top', color=mlgray)

fig.suptitle('Activation Functions and Their Derivatives (for Backpropagation)',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('activation_derivatives.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('activation_derivatives.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: activation_derivatives.pdf")
