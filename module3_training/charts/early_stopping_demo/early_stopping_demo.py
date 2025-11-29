"""
Early Stopping Demonstration
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Early Stopping Demo',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/early_stopping_demo'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

np.random.seed(42)
epochs = np.arange(200)

# ==================== LEFT: Training and Validation Loss ====================
ax = axes[0]

# Training loss (keeps decreasing)
train_loss = 1.0 * np.exp(-0.02 * epochs) + 0.05 + np.random.randn(200) * 0.01

# Validation loss (decreases then increases - overfitting)
val_loss = 0.8 * np.exp(-0.015 * epochs) + 0.2 + 0.002 * np.maximum(epochs - 80, 0) + np.random.randn(200) * 0.02

ax.plot(epochs, train_loss, color=mlblue, linewidth=2, label='Training loss')
ax.plot(epochs, val_loss, color=mlorange, linewidth=2, label='Validation loss')

# Mark optimal point
optimal_epoch = 80
ax.axvline(x=optimal_epoch, color=mlgreen, linewidth=2, linestyle='--', label='Early stopping point')
ax.scatter([optimal_epoch], [val_loss[optimal_epoch]], c=mlgreen, s=150, marker='*', zorder=5)

# Regions
ax.axvspan(0, optimal_epoch, alpha=0.1, color=mlgreen)
ax.axvspan(optimal_epoch, 200, alpha=0.1, color=mlred)

ax.text(40, 0.9, 'Underfitting\nregion', ha='center', fontsize=9, color=mlgreen)
ax.text(140, 0.9, 'Overfitting\nregion', ha='center', fontsize=9, color=mlred)

ax.set_xlabel('Epoch', fontsize=11)
ax.set_ylabel('Loss', fontsize=11)
ax.set_title('Early Stopping: Stop Before Overfitting', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 200)
ax.set_ylim(0, 1.1)

# ==================== RIGHT: How It Works ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'Early Stopping Algorithm', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

algorithm = """1. Split data into train and validation sets

2. Train model, computing validation loss each epoch

3. Keep track of best validation loss seen so far

4. If validation loss hasn't improved for
   'patience' epochs, STOP training

5. Restore weights from best epoch"""

ax.text(0.5, 7.5, algorithm, fontsize=10, va='top', family='monospace')

# Hyperparameters box
params_box = """Hyperparameters:
- patience: epochs to wait (typically 5-20)
- min_delta: minimum improvement threshold"""

ax.text(5, 2.5, params_box, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlorange, linewidth=2))

# Key insight
ax.text(5, 0.7, 'Early stopping is a form of regularization:\nit limits model complexity by limiting training time',
        ha='center', fontsize=9, color=mlpurple, style='italic')

fig.suptitle('Early Stopping: Simple and Effective Regularization',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('early_stopping_demo.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('early_stopping_demo.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: early_stopping_demo.pdf")
