CHART_METADATA = {
    'title': 'Early Stopping',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/early_stopping'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

np.random.seed(42)
epochs = np.arange(0, 150)

train_loss = 2.0 * np.exp(-0.03 * epochs) + 0.05 + 0.02 * np.random.randn(len(epochs))
val_loss = 2.0 * np.exp(-0.025 * epochs) + 0.1
val_loss[60:] = val_loss[60:] + 0.005 * (epochs[60:] - 60)
val_loss += 0.03 * np.random.randn(len(epochs))

ax.plot(epochs, train_loss, color=mlblue, lw=2, label='Training Loss')
ax.plot(epochs, val_loss, color=mlorange, lw=2, label='Validation Loss')

# Best point
best_epoch = 55
ax.axvline(x=best_epoch, color=mlgreen, linestyle='--', lw=2, label='Early Stopping Point')
ax.plot(best_epoch, val_loss[best_epoch], '*', color=mlgreen, markersize=20, zorder=5)

# Regions
ax.axvspan(0, best_epoch, alpha=0.1, color=mlgreen)
ax.axvspan(best_epoch, 150, alpha=0.1, color=mlred)
ax.text(25, 0.15, 'Learning', ha='center', fontsize=11, color=mlgreen)
ax.text(100, 0.15, 'Overfitting', ha='center', fontsize=11, color=mlred)

ax.set_xlabel('Epochs', fontsize=12)
ax.set_ylabel('Loss', fontsize=12)
ax.set_title('Early Stopping: Prevent Overfitting', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 150)
ax.set_ylim(0, 2.5)

plt.tight_layout()
plt.savefig('early_stopping.pdf', bbox_inches='tight', dpi=300)
plt.savefig('early_stopping.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: early_stopping.pdf")
