"""
Training Diagnostics - Reading Learning Curves
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Training Diagnostics',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/training_diagnostics'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(2, 3, figsize=(14, 9))

np.random.seed(42)
epochs = np.arange(100)

# ==================== TOP LEFT: Good Training ====================
ax = axes[0, 0]

train_good = 0.8 * np.exp(-0.05 * epochs) + 0.1 + np.random.randn(100) * 0.01
val_good = 0.85 * np.exp(-0.045 * epochs) + 0.12 + np.random.randn(100) * 0.015

ax.plot(epochs, train_good, color=mlblue, linewidth=2, label='Train')
ax.plot(epochs, val_good, color=mlorange, linewidth=2, label='Val')
ax.set_title('GOOD: Both converging together', fontsize=10, fontweight='bold', color=mlgreen)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.8, 'Diagnosis: Training is healthy!\nSmall gap between train/val', fontsize=8, ha='center')

# ==================== TOP MIDDLE: Overfitting ====================
ax = axes[0, 1]

train_over = 0.8 * np.exp(-0.1 * epochs) + 0.02 + np.random.randn(100) * 0.005
val_over = 0.7 * np.exp(-0.03 * epochs) + 0.25 + 0.003 * epochs + np.random.randn(100) * 0.02

ax.plot(epochs, train_over, color=mlblue, linewidth=2, label='Train')
ax.plot(epochs, val_over, color=mlorange, linewidth=2, label='Val')
ax.set_title('OVERFITTING: Val loss increases', fontsize=10, fontweight='bold', color=mlred)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.8, 'Fix: More data, regularization,\ndropout, early stopping', fontsize=8, ha='center', color=mlred)

# ==================== TOP RIGHT: Underfitting ====================
ax = axes[0, 2]

train_under = 0.8 * np.exp(-0.01 * epochs) + 0.4 + np.random.randn(100) * 0.02
val_under = 0.85 * np.exp(-0.01 * epochs) + 0.42 + np.random.randn(100) * 0.02

ax.plot(epochs, train_under, color=mlblue, linewidth=2, label='Train')
ax.plot(epochs, val_under, color=mlorange, linewidth=2, label='Val')
ax.set_title('UNDERFITTING: Both losses high', fontsize=10, fontweight='bold', color=mlblue)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.2, 'Fix: Larger model, more features,\nlonger training', fontsize=8, ha='center', color=mlblue)

# ==================== BOTTOM LEFT: Learning Rate Too High ====================
ax = axes[1, 0]

train_lr_high = 0.5 + 0.2 * np.sin(epochs * 0.3) + 0.1 * np.random.randn(100)

ax.plot(epochs, train_lr_high, color=mlblue, linewidth=2, label='Train')
ax.set_title('LR TOO HIGH: Oscillating loss', fontsize=10, fontweight='bold', color=mlorange)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.1, 'Fix: Reduce learning rate', fontsize=8, ha='center', color=mlorange)

# ==================== BOTTOM MIDDLE: Learning Rate Too Low ====================
ax = axes[1, 1]

train_lr_low = 0.9 - 0.001 * epochs + np.random.randn(100) * 0.01

ax.plot(epochs, train_lr_low, color=mlblue, linewidth=2, label='Train')
ax.set_title('LR TOO LOW: Very slow progress', fontsize=10, fontweight='bold', color=mlgray)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.1, 'Fix: Increase learning rate', fontsize=8, ha='center', color=mlgray)

# ==================== BOTTOM RIGHT: Stuck at Plateau ====================
ax = axes[1, 2]

train_plateau = np.concatenate([
    0.8 * np.exp(-0.1 * np.arange(30)) + 0.4,
    0.4 + np.random.randn(40) * 0.02,
    0.4 * np.exp(-0.05 * (np.arange(30))) + 0.1
])

ax.plot(np.arange(100), train_plateau, color=mlblue, linewidth=2, label='Train')
ax.axvspan(30, 70, alpha=0.2, color=mlgray)
ax.set_title('PLATEAU: Learning stalled', fontsize=10, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
ax.set_xlabel('Epoch', fontsize=9)
ax.set_ylabel('Loss', fontsize=9)
ax.text(50, 0.6, 'Plateau region', fontsize=8, ha='center', color=mlgray)
ax.text(50, 0.1, 'Fix: LR schedule, momentum,\nor wait patiently', fontsize=8, ha='center', color=mlpurple)

fig.suptitle('Training Diagnostics: Learning to Read Learning Curves',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('training_diagnostics.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('training_diagnostics.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: training_diagnostics.pdf")
