"""
ReLU Activation Function
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Relu Function',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/relu_function'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ==================== LEFT: ReLU Function ====================
ax = axes[0]

z = np.linspace(-4, 4, 200)
relu = np.maximum(0, z)

ax.plot(z, relu, color=mlgreen, linewidth=3, label='ReLU$(z) = \\max(0, z)$')

# Key point
ax.scatter([0], [0], c=mlgreen, s=100, zorder=5)
ax.annotate('Kink at 0', xy=(0, 0), xytext=(1, 1), fontsize=9,
            arrowprops=dict(arrowstyle='->', color=mlgray))

# Dead region
ax.fill_between(z[z < 0], 0, -0.5, alpha=0.3, color=mlred)
ax.text(-2, -0.3, 'Dead region\n(output = 0)', fontsize=8, ha='center', color=mlred)

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel('ReLU$(z)$', fontsize=12)
ax.set_title('ReLU: Rectified Linear Unit', fontsize=12, fontweight='bold', color=mlgreen)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-4, 4)
ax.set_ylim(-0.5, 4)

# Properties annotation
props = """Properties:
- Output: [0, inf)
- Non-saturating for z > 0
- Computationally efficient
- Sparse activation"""
ax.text(0.5, 3.5, props, fontsize=8, va='top', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

# ==================== RIGHT: ReLU vs Others ====================
ax = axes[1]

sigmoid = 1 / (1 + np.exp(-z))
tanh_val = np.tanh(z)

ax.plot(z, relu, color=mlgreen, linewidth=3, label='ReLU')
ax.plot(z, sigmoid, color=mlorange, linewidth=2, linestyle='--', label='Sigmoid')
ax.plot(z, tanh_val, color=mlblue, linewidth=2, linestyle=':', label='Tanh')

ax.set_xlabel('$z$', fontsize=12)
ax.set_ylabel('Activation', fontsize=12)
ax.set_title('Activation Functions Compared', fontsize=12, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 4)

# Advantages/disadvantages table
table_text = """ReLU Advantages:
+ No vanishing gradient (z > 0)
+ Fast computation
+ Sparse representations
+ Works well in practice

ReLU Disadvantages:
- Dead neurons (z < 0)
- Not zero-centered
- Unbounded output"""

ax.text(2.5, 3.5, table_text, fontsize=7, va='top', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgreen, alpha=0.9))

fig.suptitle('ReLU: The Modern Default Activation',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('relu_function.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('relu_function.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: relu_function.pdf")
