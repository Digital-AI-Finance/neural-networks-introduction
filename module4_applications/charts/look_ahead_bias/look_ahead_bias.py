CHART_METADATA = {
    'title': 'Look Ahead Bias',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/look_ahead_bias'
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

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Timeline showing the problem
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8)
ax1.axis('off')

# Timeline
ax1.axhline(y=4, xmin=0.1, xmax=0.9, color=mlgray, lw=3)
ax1.plot([1, 5, 9], [4, 4, 4], 'ko', markersize=12)

# Labels
ax1.text(1, 3.3, 'Decision\nTime', ha='center', fontsize=10)
ax1.text(5, 3.3, 'Data\nAvailable', ha='center', fontsize=10)
ax1.text(9, 3.3, 'Earnings\nAnnounced', ha='center', fontsize=10)

# Wrong arrow (look-ahead)
ax1.annotate('', xy=(1, 5), xytext=(9, 5),
            arrowprops=dict(arrowstyle='<-', color=mlred, lw=3, ls='--'))
ax1.text(5, 5.5, 'WRONG: Using future data', ha='center', fontsize=11, color=mlred, fontweight='bold')

# Correct arrow
ax1.annotate('', xy=(1, 2.5), xytext=(5, 2.5),
            arrowprops=dict(arrowstyle='<-', color=mlgreen, lw=3))
ax1.text(3, 1.8, 'CORRECT: Only past data', ha='center', fontsize=11, color=mlgreen, fontweight='bold')

ax1.set_title('Look-Ahead Bias in Backtesting', fontsize=12, fontweight='bold')

# Right: Example with results
ax2 = axes[1]
np.random.seed(42)
days = np.arange(250)

# With look-ahead (unrealistic performance)
returns_biased = np.random.randn(250) * 0.015
returns_biased[returns_biased < 0] *= 0.3  # Avoid losses using "future knowledge"
portfolio_biased = 100 * np.exp(np.cumsum(returns_biased))

# Without look-ahead (realistic)
returns_real = np.random.randn(250) * 0.01
portfolio_real = 100 * np.exp(np.cumsum(returns_real))

ax2.plot(days, portfolio_biased, color=mlred, lw=2, label='With Look-Ahead Bias')
ax2.plot(days, portfolio_real, color=mlgreen, lw=2, label='Realistic (No Bias)')
ax2.axhline(y=100, color=mlgray, linestyle='--', alpha=0.5)

ax2.set_xlabel('Trading Days', fontsize=11)
ax2.set_ylabel('Portfolio Value', fontsize=11)
ax2.set_title('Impact of Look-Ahead Bias', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')
ax2.grid(True, alpha=0.3)

# Annotation
ax2.annotate('Unrealistic\nperformance', xy=(200, portfolio_biased[200]), xytext=(150, 180),
            arrowprops=dict(arrowstyle='->', color=mlred), fontsize=10, color=mlred)

plt.tight_layout()
plt.savefig('look_ahead_bias.pdf', bbox_inches='tight', dpi=300)
plt.savefig('look_ahead_bias.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: look_ahead_bias.pdf")
