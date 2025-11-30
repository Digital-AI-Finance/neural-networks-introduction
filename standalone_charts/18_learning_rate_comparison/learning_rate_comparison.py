# ==============================================================================
# Chart: Learning Rate Comparison
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/18_learning_rate_comparison/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Learning Rate Comparison

Effect of learning rate on convergence speed

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/18_learning_rate_comparison/
"""

CHART_METADATA = {
    'name': 'Learning Rate Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/18_learning_rate_comparison',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Effect of learning rate on convergence speed'
}

"""
Chart 18: Learning Rate Comparison
Side-by-side: too small, just right, too large - actual loss curves.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Colors
mlpurple = '#3333b2'
mlblue = '#0066cc'
mlgreen = '#2ca02c'
mlorange = '#ff7f0e'
mlred = '#d62728'
mlgray = '#7f7f7f'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

epochs = np.arange(1, 101)

# Panel 1: Learning rate too small
ax1 = axes[0]
lr_small = 0.001
loss_small = 0.9 * np.exp(-epochs * lr_small * 0.3) + 0.3 + np.random.randn(100)*0.01

ax1.plot(epochs, loss_small, color=mlblue, linewidth=2)
ax1.axhline(y=0.35, color=mlgreen, linestyle='--', alpha=0.7, label='Optimal loss')

# Annotate slow progress
ax1.annotate('Still learning\nat epoch 100!', xy=(80, 0.5), fontsize=10, color=mlred,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax1.annotate('', xy=(100, 0.38), xytext=(100, 0.35),
            arrowprops=dict(arrowstyle='<->', color=mlred, lw=2))
ax1.text(102, 0.36, 'Gap', fontsize=9, color=mlred)

ax1.set_xlabel('Epoch', fontsize=10)
ax1.set_ylabel('Loss', fontsize=10)
ax1.set_title('TOO SMALL (lr=0.001)\nSlow convergence', fontsize=11, fontweight='bold', color=mlred)
ax1.legend(loc='upper right', fontsize=8)
ax1.set_xlim(0, 100)
ax1.set_ylim(0.2, 1.0)
ax1.grid(True, alpha=0.3)
ax1.text(50, 0.95, 'Learning Rate = 0.001', fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor=mlorange))

# Panel 2: Learning rate just right
ax2 = axes[1]
lr_good = 0.01
loss_good = 0.8 * np.exp(-epochs * lr_good * 0.5) + 0.15 + np.random.randn(100)*0.008

ax2.plot(epochs, loss_good, color=mlblue, linewidth=2)
ax2.axhline(y=0.17, color=mlgreen, linestyle='--', alpha=0.7, label='Optimal loss')

# Mark convergence
converge_epoch = 40
ax2.axvline(x=converge_epoch, color=mlgreen, linestyle=':', alpha=0.7)
ax2.annotate('Converged!', xy=(converge_epoch, 0.3), fontsize=10, color=mlgreen,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlgreen, alpha=0.8))

ax2.set_xlabel('Epoch', fontsize=10)
ax2.set_ylabel('Loss', fontsize=10)
ax2.set_title('JUST RIGHT (lr=0.01)\nFast & stable', fontsize=11, fontweight='bold', color=mlgreen)
ax2.legend(loc='upper right', fontsize=8)
ax2.set_xlim(0, 100)
ax2.set_ylim(0.0, 1.0)
ax2.grid(True, alpha=0.3)
ax2.text(50, 0.95, 'Learning Rate = 0.01', fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor=mlgreen))

# Panel 3: Learning rate too large
ax3 = axes[2]
lr_large = 0.5
# Oscillating loss
loss_large = 0.5 + 0.3 * np.sin(epochs * 0.3) * np.exp(-epochs * 0.01) + np.random.randn(100)*0.05
loss_large = np.clip(loss_large, 0.2, 1.2)

ax3.plot(epochs, loss_large, color=mlblue, linewidth=2)
ax3.axhline(y=0.35, color=mlgreen, linestyle='--', alpha=0.7, label='Optimal loss')

# Annotate instability
ax3.annotate('Oscillating!\nNever converges', xy=(50, 0.85), fontsize=10, color=mlred,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax3.set_xlabel('Epoch', fontsize=10)
ax3.set_ylabel('Loss', fontsize=10)
ax3.set_title('TOO LARGE (lr=0.5)\nUnstable', fontsize=11, fontweight='bold', color=mlred)
ax3.legend(loc='upper right', fontsize=8)
ax3.set_xlim(0, 100)
ax3.set_ylim(0.0, 1.2)
ax3.grid(True, alpha=0.3)
ax3.text(50, 1.1, 'Learning Rate = 0.5', fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor=mlred))

plt.tight_layout()
plt.savefig('learning_rate_comparison.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 18_learning_rate_comparison/learning_rate_comparison.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/18_learning_rate_comparison/
