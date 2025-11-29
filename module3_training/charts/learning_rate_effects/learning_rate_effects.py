"""
Learning Rate Effects on Training
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Learning Rate Effects',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/learning_rate_effects'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# ==================== TOP LEFT: Too Small ====================
ax = axes[0, 0]

epochs = np.arange(100)
loss_small = 1.0 * np.exp(-0.02 * epochs) + 0.3

ax.plot(epochs, loss_small, color=mlblue, linewidth=2)
ax.axhline(y=0.3, color=mlgray, linestyle='--', alpha=0.5)
ax.text(80, 0.32, 'Optimal', fontsize=9, color=mlgray)

ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Learning Rate TOO SMALL ($\\eta = 0.001$)', fontsize=11,
             fontweight='bold', color=mlblue)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.5)

ax.text(50, 1.2, 'Converges but\nVERY slowly!', fontsize=10, ha='center', color=mlblue,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlblue))

# ==================== TOP RIGHT: Just Right ====================
ax = axes[0, 1]

loss_good = 1.0 * np.exp(-0.15 * epochs) + 0.1 + np.random.randn(100) * 0.02

ax.plot(epochs, loss_good, color=mlgreen, linewidth=2)
ax.axhline(y=0.1, color=mlgray, linestyle='--', alpha=0.5)
ax.text(80, 0.12, 'Optimal', fontsize=9, color=mlgray)

ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Learning Rate GOOD ($\\eta = 0.01$)', fontsize=11,
             fontweight='bold', color=mlgreen)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.5)

ax.text(50, 1.2, 'Fast convergence\nto optimum!', fontsize=10, ha='center', color=mlgreen,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgreen))

# ==================== BOTTOM LEFT: Too Large ====================
ax = axes[1, 0]

loss_large = 0.5 + 0.3 * np.sin(epochs * 0.3) + 0.2 * np.sin(epochs * 0.7)

ax.plot(epochs, loss_large, color=mlorange, linewidth=2)
ax.axhline(y=0.1, color=mlgray, linestyle='--', alpha=0.5)

ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Learning Rate TOO LARGE ($\\eta = 0.5$)', fontsize=11,
             fontweight='bold', color=mlorange)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.5)

ax.text(50, 1.2, 'Oscillates around\nminimum!', fontsize=10, ha='center', color=mlorange,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlorange))

# ==================== BOTTOM RIGHT: Way Too Large (Diverges) ====================
ax = axes[1, 1]

loss_huge = np.exp(0.05 * epochs)
loss_huge = np.clip(loss_huge, 0, 10)

ax.plot(epochs[:80], loss_huge[:80], color=mlred, linewidth=2)
ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Learning Rate WAY TOO LARGE ($\\eta = 1.0$)', fontsize=11,
             fontweight='bold', color=mlred)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)

ax.text(50, 8, 'DIVERGES!\nLoss explodes', fontsize=10, ha='center', color=mlred,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlred))

fig.suptitle('Learning Rate: The Most Important Hyperparameter',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

# Summary at bottom
fig.text(0.5, 0.02, 'Rule of thumb: Start with 0.001-0.01 and adjust based on training dynamics',
         ha='center', fontsize=10, color=mlpurple)

plt.tight_layout(rect=[0, 0.04, 1, 0.98])
plt.savefig('learning_rate_effects.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('learning_rate_effects.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: learning_rate_effects.pdf")
