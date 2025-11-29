CHART_METADATA = {
    'title': 'Case Study Training',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/case_study_training'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

np.random.seed(42)

# Left: Training curves
ax1 = axes[0]
epochs = np.arange(0, 100)
train_loss = 0.02 * np.exp(-0.03 * epochs) + 0.005 + 0.001 * np.random.randn(len(epochs))
val_loss = 0.02 * np.exp(-0.025 * epochs) + 0.006 + 0.0015 * np.random.randn(len(epochs))

ax1.plot(epochs, train_loss, color=mlblue, lw=2, label='Training Loss (MSE)')
ax1.plot(epochs, val_loss, color=mlorange, lw=2, label='Validation Loss')
ax1.axvline(x=65, color=mlgreen, linestyle='--', lw=2, label='Early Stop (epoch 65)')
ax1.set_xlabel('Epoch', fontsize=11)
ax1.set_ylabel('Loss (MSE)', fontsize=11)
ax1.set_title('Training Progress', fontsize=12, fontweight='bold')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

# Right: Learning rate schedule
ax2 = axes[1]
epochs2 = np.arange(0, 100)
lr_constant = np.ones(100) * 0.001
lr_decay = 0.001 * (0.95 ** (epochs2 / 10))
lr_warmup = np.where(epochs2 < 10, 0.0001 + 0.00009 * epochs2, 0.001 * (0.95 ** ((epochs2-10) / 10)))

ax2.semilogy(epochs2, lr_constant, color=mlgray, lw=2, label='Constant', linestyle='--')
ax2.semilogy(epochs2, lr_decay, color=mlblue, lw=2, label='Exponential Decay')
ax2.semilogy(epochs2, lr_warmup, color=mlgreen, lw=2, label='Warmup + Decay')

ax2.set_xlabel('Epoch', fontsize=11)
ax2.set_ylabel('Learning Rate', fontsize=11)
ax2.set_title('Learning Rate Schedules', fontsize=12, fontweight='bold')
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)

plt.suptitle('Case Study: Training Configuration', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('case_study_training.pdf', bbox_inches='tight', dpi=300)
plt.savefig('case_study_training.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: case_study_training.pdf")
