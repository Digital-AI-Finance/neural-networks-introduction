CHART_METADATA = {
    'title': 'Regime Changes',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/regime_changes'
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

fig, ax = plt.subplots(1, 1, figsize=(12, 5))

np.random.seed(42)

# Create regime-switching data
n = 500
price = [100]

# Regime indicators
regimes = []
current_regime = 'bull'

for i in range(n-1):
    if i == 100:
        current_regime = 'bear'
    elif i == 200:
        current_regime = 'high_vol'
    elif i == 300:
        current_regime = 'bull'
    elif i == 400:
        current_regime = 'sideways'

    regimes.append(current_regime)

    if current_regime == 'bull':
        ret = np.random.randn() * 0.01 + 0.001
    elif current_regime == 'bear':
        ret = np.random.randn() * 0.015 - 0.002
    elif current_regime == 'high_vol':
        ret = np.random.randn() * 0.03
    else:  # sideways
        ret = np.random.randn() * 0.005

    price.append(price[-1] * (1 + ret))

price = np.array(price)
t = np.arange(n)

# Plot price
ax.plot(t, price, color=mlpurple, lw=1.5)

# Shade regimes
ax.axvspan(0, 100, alpha=0.2, color=mlgreen, label='Bull Market')
ax.axvspan(100, 200, alpha=0.2, color=mlred, label='Bear Market')
ax.axvspan(200, 300, alpha=0.2, color=mlorange, label='High Volatility')
ax.axvspan(300, 400, alpha=0.2, color=mlgreen)
ax.axvspan(400, 500, alpha=0.2, color=mlgray, label='Sideways')

# Regime labels
ax.text(50, price.max()*1.05, 'Bull', ha='center', fontsize=10, color=mlgreen)
ax.text(150, price.max()*1.05, 'Bear', ha='center', fontsize=10, color=mlred)
ax.text(250, price.max()*1.05, 'Crisis', ha='center', fontsize=10, color=mlorange)
ax.text(350, price.max()*1.05, 'Bull', ha='center', fontsize=10, color=mlgreen)
ax.text(450, price.max()*1.05, 'Range', ha='center', fontsize=10, color=mlgray)

ax.set_xlabel('Time', fontsize=11)
ax.set_ylabel('Price', fontsize=11)
ax.set_title('Market Regime Changes: A Challenge for ML Models', fontsize=13, fontweight='bold')
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

# Add annotation
ax.text(250, price.min()*0.95, 'Model trained on one regime may fail in another',
        ha='center', fontsize=10, color=mlred, style='italic')

plt.tight_layout()
plt.savefig('regime_changes.pdf', bbox_inches='tight', dpi=300)
plt.savefig('regime_changes.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: regime_changes.pdf")
