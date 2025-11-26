# ==============================================================================
# Chart: Overfitting Underfitting
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/17_overfitting_underfitting/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Overfitting Underfitting

Training and validation loss curves for three scenarios

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/17_overfitting_underfitting/
"""

CHART_METADATA = {
    'name': 'Overfitting Underfitting',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/17_overfitting_underfitting',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Training and validation loss curves for three scenarios'
}

"""
Chart 17: Overfitting vs Underfitting
Training vs validation loss curves - the key practical concept.
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

# Panel 1: Underfitting
ax1 = axes[0]
train_loss_under = 0.8 - 0.3 * (1 - np.exp(-epochs/50)) + np.random.randn(100)*0.02
val_loss_under = 0.85 - 0.25 * (1 - np.exp(-epochs/50)) + np.random.randn(100)*0.02

ax1.plot(epochs, train_loss_under, color=mlblue, linewidth=2, label='Training Loss')
ax1.plot(epochs, val_loss_under, color=mlorange, linewidth=2, label='Validation Loss')
ax1.axhline(y=0.5, color=mlgray, linestyle='--', alpha=0.5, label='Target')

ax1.fill_between(epochs, 0.45, 0.55, alpha=0.1, color=mlgreen)
ax1.annotate('Both losses\nstay HIGH', xy=(70, 0.6), fontsize=10, color=mlred,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax1.set_xlabel('Epoch', fontsize=10)
ax1.set_ylabel('Loss', fontsize=10)
ax1.set_title('UNDERFITTING\n(Model too simple)', fontsize=11, fontweight='bold', color=mlred)
ax1.legend(loc='upper right', fontsize=8)
ax1.set_xlim(0, 100)
ax1.set_ylim(0.3, 1.0)
ax1.grid(True, alpha=0.3)

# Panel 2: Good Fit
ax2 = axes[1]
train_loss_good = 0.8 * np.exp(-epochs/25) + 0.15 + np.random.randn(100)*0.01
val_loss_good = 0.8 * np.exp(-epochs/25) + 0.18 + np.random.randn(100)*0.015

ax2.plot(epochs, train_loss_good, color=mlblue, linewidth=2, label='Training Loss')
ax2.plot(epochs, val_loss_good, color=mlorange, linewidth=2, label='Validation Loss')

ax2.fill_between(epochs[50:], train_loss_good[50:], val_loss_good[50:], alpha=0.2, color=mlgreen)
ax2.annotate('Small gap\n= Good generalization', xy=(75, 0.25), fontsize=10, color=mlgreen,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlgreen, alpha=0.8))

ax2.set_xlabel('Epoch', fontsize=10)
ax2.set_ylabel('Loss', fontsize=10)
ax2.set_title('GOOD FIT\n(Model just right)', fontsize=11, fontweight='bold', color=mlgreen)
ax2.legend(loc='upper right', fontsize=8)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1.0)
ax2.grid(True, alpha=0.3)

# Panel 3: Overfitting
ax3 = axes[2]
train_loss_over = 0.8 * np.exp(-epochs/15) + 0.05 + np.random.randn(100)*0.005
val_loss_over = 0.6 * np.exp(-epochs/30) + 0.2 + 0.003*epochs + np.random.randn(100)*0.02
val_loss_over = np.clip(val_loss_over, 0.2, 1.0)

ax3.plot(epochs, train_loss_over, color=mlblue, linewidth=2, label='Training Loss')
ax3.plot(epochs, val_loss_over, color=mlorange, linewidth=2, label='Validation Loss')

# Mark overfitting point
overfit_start = 30
ax3.axvline(x=overfit_start, color=mlred, linestyle='--', alpha=0.7)
ax3.annotate('STOP HERE!', xy=(overfit_start, 0.8), fontsize=10, color=mlred,
            fontweight='bold', ha='center', rotation=90)

ax3.fill_between(epochs[40:], train_loss_over[40:], val_loss_over[40:], alpha=0.2, color=mlred)
ax3.annotate('Gap grows\n= Memorizing noise!', xy=(75, 0.55), fontsize=10, color=mlred,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax3.set_xlabel('Epoch', fontsize=10)
ax3.set_ylabel('Loss', fontsize=10)
ax3.set_title('OVERFITTING\n(Model too complex)', fontsize=11, fontweight='bold', color=mlred)
ax3.legend(loc='upper right', fontsize=8)
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 1.0)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('overfitting_underfitting.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 17_overfitting_underfitting/overfitting_underfitting.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/17_overfitting_underfitting/
