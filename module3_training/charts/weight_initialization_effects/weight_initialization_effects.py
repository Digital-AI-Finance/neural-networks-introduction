"""
Weight Initialization Effects
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Weight Initialization Effects',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/weight_initialization_effects'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

np.random.seed(42)

# ==================== LEFT: Too Small ====================
ax = axes[0]

# Simulate activations through layers with small init
n_layers = 10
n_neurons = 500

activations = np.random.randn(n_neurons)
variance_history = [np.var(activations)]

for _ in range(n_layers):
    W = np.random.randn(n_neurons, n_neurons) * 0.01  # Too small
    activations = np.tanh(W @ activations)
    variance_history.append(np.var(activations))

ax.semilogy(range(n_layers + 1), variance_history, 'o-', color=mlblue, linewidth=2, markersize=6)
ax.axhline(y=1, color=mlgray, linestyle='--', alpha=0.5)
ax.text(8, 1.2, 'Ideal', fontsize=9, color=mlgray)

ax.set_xlabel('Layer', fontsize=11)
ax.set_ylabel('Activation Variance (log)', fontsize=11)
ax.set_title('Init TOO SMALL (std=0.01)', fontsize=11, fontweight='bold', color=mlblue)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(1e-10, 10)

ax.text(5, 1e-7, 'Activations vanish!', fontsize=10, ha='center', color=mlblue)

# ==================== MIDDLE: Just Right (Xavier) ====================
ax = axes[1]

activations = np.random.randn(n_neurons)
variance_history = [np.var(activations)]

for _ in range(n_layers):
    W = np.random.randn(n_neurons, n_neurons) * np.sqrt(1.0 / n_neurons)  # Xavier
    activations = np.tanh(W @ activations)
    variance_history.append(np.var(activations))

ax.semilogy(range(n_layers + 1), variance_history, 'o-', color=mlgreen, linewidth=2, markersize=6)
ax.axhline(y=1, color=mlgray, linestyle='--', alpha=0.5)

ax.set_xlabel('Layer', fontsize=11)
ax.set_ylabel('Activation Variance (log)', fontsize=11)
ax.set_title('Xavier Init (std=$1/\\sqrt{n}$)', fontsize=11, fontweight='bold', color=mlgreen)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(1e-10, 10)

ax.text(5, 2, 'Variance stays stable!', fontsize=10, ha='center', color=mlgreen)

# ==================== RIGHT: Too Large ====================
ax = axes[2]

activations = np.random.randn(n_neurons)
variance_history = [np.var(activations)]

for _ in range(n_layers):
    W = np.random.randn(n_neurons, n_neurons) * 1.0  # Too large
    activations = np.tanh(W @ activations)
    variance_history.append(np.var(activations))

ax.semilogy(range(n_layers + 1), variance_history, 'o-', color=mlred, linewidth=2, markersize=6)
ax.axhline(y=1, color=mlgray, linestyle='--', alpha=0.5)

ax.set_xlabel('Layer', fontsize=11)
ax.set_ylabel('Activation Variance (log)', fontsize=11)
ax.set_title('Init TOO LARGE (std=1.0)', fontsize=11, fontweight='bold', color=mlred)
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(1e-10, 10)

ax.text(5, 0.3, 'Saturates at boundaries!', fontsize=10, ha='center', color=mlred)

# Summary
fig.text(0.5, 0.02,
         'Xavier (Glorot): $\\sigma = \\sqrt{1/n_{in}}$ for tanh  |  '
         'He: $\\sigma = \\sqrt{2/n_{in}}$ for ReLU',
         ha='center', fontsize=10, color=mlpurple)

fig.suptitle('Weight Initialization: Getting It Right Matters',
             fontsize=14, fontweight='bold', color=mlpurple, y=0.98)

plt.tight_layout(rect=[0, 0.06, 1, 0.95])
plt.savefig('weight_initialization_effects.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('weight_initialization_effects.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: weight_initialization_effects.pdf")
