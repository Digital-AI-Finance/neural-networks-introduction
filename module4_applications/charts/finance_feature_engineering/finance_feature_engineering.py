"""
Feature Engineering for Financial Data
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Finance Feature Engineering',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_feature_engineering'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 8))

# ==================== LEFT: Feature Categories ====================
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(5, 11.5, 'Feature Engineering for Stocks', fontsize=14, fontweight='bold',
        ha='center', color=mlpurple)

categories = [
    ('Price-Based Features', mlblue, [
        'Returns: $r_t = \\frac{P_t - P_{t-1}}{P_{t-1}}$',
        'Log returns: $\\log(P_t/P_{t-1})$',
        'Moving averages: MA(5), MA(20)',
        'Bollinger Bands',
    ]),
    ('Momentum Features', mlorange, [
        'RSI (Relative Strength Index)',
        'MACD (Moving Avg Convergence)',
        '52-week high/low ratio',
        'Price momentum (various lags)',
    ]),
    ('Volatility Features', mlpurple, [
        'Historical volatility',
        'ATR (Average True Range)',
        'GARCH estimates',
        'Realized variance',
    ]),
    ('Volume Features', mlgreen, [
        'Volume moving average',
        'Volume/price correlation',
        'On-balance volume (OBV)',
        'Volume rate of change',
    ]),
]

y_pos = 10
for title, color, features in categories:
    box = FancyBboxPatch((0.3, y_pos - 2.2), 9.4, 2.4, boxstyle="round,pad=0.05",
                          facecolor=f'{color}11', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(0.5, y_pos, title, fontsize=10, fontweight='bold', color=color, va='top')
    for i, feat in enumerate(features):
        ax.text(0.7, y_pos - 0.6 - i * 0.4, '- ' + feat, fontsize=8, color=mlgray, va='top')
    y_pos -= 2.8

# ==================== RIGHT: Example Features ====================
ax = axes[1]

np.random.seed(42)
days = np.arange(100)

# Simulate stock price
price = 100 * np.exp(np.cumsum(np.random.randn(100) * 0.02))

ax.plot(days, price, color=mlblue, linewidth=2, label='Price')

# Moving averages
ma5 = np.convolve(price, np.ones(5)/5, mode='valid')
ma20 = np.convolve(price, np.ones(20)/20, mode='valid')

ax.plot(days[4:], ma5, color=mlorange, linewidth=1.5, linestyle='--', label='MA(5)')
ax.plot(days[19:], ma20, color=mlgreen, linewidth=1.5, linestyle=':', label='MA(20)')

# Bollinger Bands
bb_mid = ma20
bb_std = np.array([price[max(0, i-19):i+1].std() for i in range(19, 100)])
ax.fill_between(days[19:], bb_mid - 2*bb_std, bb_mid + 2*bb_std,
                alpha=0.2, color=mlgray, label='Bollinger Bands')

ax.set_xlabel('Days', fontsize=11)
ax.set_ylabel('Price', fontsize=11)
ax.set_title('Technical Indicators Example', fontsize=12, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

# Annotation
ax.text(50, price.min(), 'These features become\ninputs to the neural network',
        fontsize=9, ha='center', color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

fig.suptitle('Feature Engineering: Transforming Raw Data into Useful Inputs',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('finance_feature_engineering.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_feature_engineering.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_feature_engineering.pdf")
