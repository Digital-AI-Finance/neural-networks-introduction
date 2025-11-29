CHART_METADATA = {
    'title': 'Learning Rate Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/learning_rate_comparison'
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

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

epochs = np.arange(0, 100)

# Too small learning rate
ax1 = axes[0]
loss_small = 2.0 * np.exp(-0.01 * epochs) + 0.5
ax1.plot(epochs, loss_small, color=mlblue, lw=2)
ax1.set_title('LR = 0.0001 (Too Small)', fontsize=11, fontweight='bold')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Loss')
ax1.set_ylim(0, 2.5)
ax1.axhline(y=0.5, color=mlgray, linestyle='--', alpha=0.5, label='Optimal')
ax1.text(50, 1.5, 'Very slow\nconvergence', ha='center', fontsize=9, color=mlblue)

# Good learning rate
ax2 = axes[1]
loss_good = 2.0 * np.exp(-0.05 * epochs) + 0.1
ax2.plot(epochs, loss_good, color=mlgreen, lw=2)
ax2.set_title('LR = 0.01 (Good)', fontsize=11, fontweight='bold')
ax2.set_xlabel('Epochs')
ax2.set_ylim(0, 2.5)
ax2.axhline(y=0.1, color=mlgray, linestyle='--', alpha=0.5)
ax2.text(50, 1.2, 'Fast\nconvergence', ha='center', fontsize=9, color=mlgreen)

# Too large learning rate
ax3 = axes[2]
np.random.seed(42)
loss_large = 0.5 + 0.3 * np.sin(0.3 * epochs) + 0.2 * np.random.randn(len(epochs))
loss_large = np.maximum(loss_large, 0.2)
loss_large[:10] = np.linspace(2.0, 0.8, 10)
ax3.plot(epochs, loss_large, color=mlred, lw=2)
ax3.set_title('LR = 1.0 (Too Large)', fontsize=11, fontweight='bold')
ax3.set_xlabel('Epochs')
ax3.set_ylim(0, 2.5)
ax3.text(50, 1.8, 'Oscillating /\nDiverging', ha='center', fontsize=9, color=mlred)

for ax in axes:
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 100)

plt.suptitle('Effect of Learning Rate on Training', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('learning_rate_comparison.pdf', bbox_inches='tight', dpi=300)
plt.savefig('learning_rate_comparison.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: learning_rate_comparison.pdf")
