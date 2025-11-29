CHART_METADATA = {
    'title': 'Training Curve',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/training_curve'
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

fig, ax = plt.subplots(1, 1, figsize=(10, 5))

np.random.seed(42)
epochs = np.arange(0, 100)

# Training loss (decreasing with noise)
train_loss = 2.0 * np.exp(-0.04 * epochs) + 0.1 + 0.05 * np.random.randn(len(epochs))
train_loss = np.maximum(train_loss, 0.05)

# Validation loss (decreasing then increasing - overfitting)
val_loss = 2.0 * np.exp(-0.035 * epochs) + 0.15
val_loss[50:] = val_loss[50:] + 0.008 * (epochs[50:] - 50)
val_loss += 0.03 * np.random.randn(len(epochs))
val_loss = np.maximum(val_loss, 0.1)

ax.plot(epochs, train_loss, color=mlblue, lw=2.5, label='Training Loss')
ax.plot(epochs, val_loss, color=mlorange, lw=2.5, label='Validation Loss')

# Mark regions
ax.axvspan(0, 30, alpha=0.1, color=mlgreen, label='Underfitting')
ax.axvspan(30, 60, alpha=0.1, color=mlblue, label='Good Fit')
ax.axvspan(60, 100, alpha=0.1, color=mlred, label='Overfitting')

# Best model point
best_epoch = 55
ax.axvline(x=best_epoch, color=mlgreen, linestyle='--', lw=2)
ax.plot(best_epoch, val_loss[best_epoch], '*', color=mlgreen, markersize=20, zorder=5)
ax.annotate('Best Model', xy=(best_epoch, val_loss[best_epoch]), xytext=(best_epoch + 10, 0.8),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5),
            fontsize=11, color=mlgreen, fontweight='bold')

ax.set_xlabel('Epochs', fontsize=12)
ax.set_ylabel('Loss', fontsize=12)
ax.set_title('Training and Validation Loss Curves', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
ax.set_ylim(0, 2.5)

# Add annotations
ax.text(15, 2.2, 'High Bias', ha='center', fontsize=10, color=mlgreen)
ax.text(45, 2.2, 'Optimal', ha='center', fontsize=10, color=mlblue)
ax.text(80, 2.2, 'High Variance', ha='center', fontsize=10, color=mlred)

plt.tight_layout()
plt.savefig('training_curve.pdf', bbox_inches='tight', dpi=300)
plt.savefig('training_curve.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: training_curve.pdf")
