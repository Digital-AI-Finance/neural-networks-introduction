CHART_METADATA = {
    'title': 'Vanishing Gradient',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/vanishing_gradient'
}

import matplotlib.pyplot as plt
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Sigmoid saturation
ax1 = axes[0]
x = np.linspace(-6, 6, 200)
sigmoid = 1 / (1 + np.exp(-x))
sigmoid_derivative = sigmoid * (1 - sigmoid)

ax1.plot(x, sigmoid, color=mlpurple, lw=2.5, label='Sigmoid $\\sigma(x)$')
ax1.plot(x, sigmoid_derivative, color=mlred, lw=2.5, label="Derivative $\\sigma'(x)$")

# Shade saturation regions
ax1.axvspan(-6, -3, alpha=0.2, color=mlred)
ax1.axvspan(3, 6, alpha=0.2, color=mlred)
ax1.text(-4.5, 0.6, 'Saturated\n(gradient~0)', ha='center', fontsize=9, color=mlred)
ax1.text(4.5, 0.6, 'Saturated\n(gradient~0)', ha='center', fontsize=9, color=mlred)

ax1.axhline(y=0.25, color=mlgray, linestyle='--', alpha=0.5)
ax1.text(0, 0.28, 'Max gradient = 0.25', ha='center', fontsize=9, color=mlgray)

ax1.set_xlabel('Input $x$', fontsize=11)
ax1.set_ylabel('Output', fontsize=11)
ax1.set_title('Sigmoid Saturation Problem', fontsize=12, fontweight='bold')
ax1.legend(loc='right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-6, 6)
ax1.set_ylim(-0.1, 1.1)

# Right: Gradient magnitude through layers
ax2 = axes[1]
layers = np.arange(1, 11)

# Vanishing (sigmoid)
grad_sigmoid = 0.25 ** layers
ax2.semilogy(layers, grad_sigmoid, 'o-', color=mlred, lw=2, markersize=8, label='Sigmoid (vanishing)')

# Healthy (ReLU-like)
grad_relu = 0.9 ** layers
ax2.semilogy(layers, grad_relu, 's-', color=mlgreen, lw=2, markersize=8, label='ReLU (healthy)')

# Exploding
grad_explode = 1.5 ** layers
ax2.semilogy(layers, grad_explode, '^-', color=mlorange, lw=2, markersize=8, label='Large weights (exploding)')

ax2.axhline(y=1, color=mlgray, linestyle='--', alpha=0.5)
ax2.axhspan(1e-10, 1e-4, alpha=0.1, color=mlred)
ax2.axhspan(1e4, 1e10, alpha=0.1, color=mlorange)

ax2.set_xlabel('Layer Depth', fontsize=11)
ax2.set_ylabel('Gradient Magnitude', fontsize=11)
ax2.set_title('Gradient Flow Through Deep Networks', fontsize=12, fontweight='bold')
ax2.legend(loc='center right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 11)
ax2.set_ylim(1e-10, 1e10)

plt.tight_layout()
plt.savefig('vanishing_gradient.pdf', bbox_inches='tight', dpi=300)
plt.savefig('vanishing_gradient.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: vanishing_gradient.pdf")
