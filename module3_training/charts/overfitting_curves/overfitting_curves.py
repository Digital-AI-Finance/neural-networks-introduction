"""
Overfitting Visualization: Training vs Validation Loss
Module 3: Learning from Mistakes
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Overfitting Curves',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/overfitting_curves'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 6))

# Generate realistic training curves
np.random.seed(42)
epochs = np.arange(1, 101)

# Training loss: decreases steadily
train_loss = 2.0 * np.exp(-0.05 * epochs) + 0.1 + np.random.randn(100) * 0.03

# Validation loss: decreases then increases (overfitting)
val_loss = 2.0 * np.exp(-0.03 * epochs) + 0.3 + 0.015 * (epochs - 30) * (epochs > 30)
val_loss += np.random.randn(100) * 0.05
val_loss = np.maximum(val_loss, 0.1)

# Smooth the curves
from scipy.ndimage import gaussian_filter1d
train_loss_smooth = gaussian_filter1d(train_loss, sigma=2)
val_loss_smooth = gaussian_filter1d(val_loss, sigma=2)

# Plot
ax.plot(epochs, train_loss_smooth, color=mlblue, linewidth=2.5, label='Training Loss')
ax.plot(epochs, val_loss_smooth, color=mlorange, linewidth=2.5, label='Validation Loss')

# Mark optimal stopping point
optimal_epoch = 35
ax.axvline(x=optimal_epoch, color=mlgreen, linestyle='--', linewidth=2, label='Optimal Stopping')
ax.scatter([optimal_epoch], [val_loss_smooth[optimal_epoch - 1]], s=150, c=mlgreen,
           zorder=5, edgecolors='white', linewidths=2)

# Shaded regions
ax.axvspan(1, optimal_epoch, alpha=0.1, color=mlgreen, label='Good generalization')
ax.axvspan(optimal_epoch, 100, alpha=0.1, color=mlred, label='Overfitting region')

# Annotations
ax.annotate('Overfitting:\nValidation loss increases\nwhile training loss decreases',
            xy=(75, val_loss_smooth[74]), xytext=(60, 1.3),
            fontsize=10, color=mlred,
            arrowprops=dict(arrowstyle='->', color=mlred, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlred, alpha=0.9))

ax.annotate('Gap = Overfitting',
            xy=(85, (val_loss_smooth[84] + train_loss_smooth[84]) / 2),
            xytext=(85, 0.7), fontsize=9, ha='center', color=mlgray,
            arrowprops=dict(arrowstyle='<->', color=mlgray, lw=1))

# Add "Early Stopping" label
ax.text(optimal_epoch + 2, 0.2, 'Early\nStopping', fontsize=10, color=mlgreen, fontweight='bold')

# Labels and title
ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Loss', fontsize=12)
ax.set_title('Overfitting: When to Stop Training', fontsize=14, fontweight='bold', color=mlpurple)

# Formatting
ax.set_xlim(0, 105)
ax.set_ylim(0, 2.2)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

# Finance analogy at bottom
ax.text(0.5, -0.12, 'Finance Analogy: Like backtesting a strategy that works perfectly on historical data but fails in live trading',
        transform=ax.transAxes, fontsize=9, ha='center', style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('overfitting_curves.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('overfitting_curves.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: overfitting_curves.pdf")
