"""
Backtesting Results Visualization
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Finance Backtest Results',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_backtest_results'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

np.random.seed(42)
days = np.arange(252 * 3)  # 3 years

# ==================== TOP LEFT: Cumulative Returns ====================
ax = axes[0, 0]

# Simulate strategies
market_returns = np.random.randn(len(days)) * 0.01 + 0.0003
mlp_returns = np.random.randn(len(days)) * 0.012 + 0.0004

market_cumulative = np.cumprod(1 + market_returns)
mlp_cumulative = np.cumprod(1 + mlp_returns)

ax.plot(days, market_cumulative, color=mlgray, linewidth=2, label='Buy & Hold (Market)')
ax.plot(days, mlp_cumulative, color=mlpurple, linewidth=2, label='MLP Strategy')

ax.set_xlabel('Trading Days', fontsize=11)
ax.set_ylabel('Cumulative Return', fontsize=11)
ax.set_title('Cumulative Returns Comparison', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

# ==================== TOP RIGHT: Drawdown ====================
ax = axes[0, 1]

# Calculate drawdown
mlp_peak = np.maximum.accumulate(mlp_cumulative)
mlp_drawdown = (mlp_cumulative - mlp_peak) / mlp_peak * 100

ax.fill_between(days, mlp_drawdown, 0, color=mlred, alpha=0.5)
ax.plot(days, mlp_drawdown, color=mlred, linewidth=1)

ax.set_xlabel('Trading Days', fontsize=11)
ax.set_ylabel('Drawdown (%)', fontsize=11)
ax.set_title('Maximum Drawdown Analysis', fontsize=11, fontweight='bold', color=mlred)
ax.grid(True, alpha=0.3)

max_dd = np.min(mlp_drawdown)
ax.axhline(y=max_dd, color=mlred, linestyle='--', alpha=0.5)
ax.text(len(days) * 0.8, max_dd - 1, f'Max DD: {max_dd:.1f}%', fontsize=9, color=mlred)

# ==================== BOTTOM LEFT: Monthly Returns Heatmap ====================
ax = axes[1, 0]

# Monthly returns (3 years x 12 months)
monthly_returns = np.random.randn(3, 12) * 3 + 0.5

im = ax.imshow(monthly_returns, cmap='RdYlGn', aspect='auto', vmin=-10, vmax=10)
plt.colorbar(im, ax=ax, label='Return (%)')

ax.set_xticks(range(12))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=8)
ax.set_yticks(range(3))
ax.set_yticklabels(['Year 1', 'Year 2', 'Year 3'], fontsize=9)
ax.set_title('Monthly Returns Heatmap', fontsize=11, fontweight='bold', color=mlpurple)

# ==================== BOTTOM RIGHT: Performance Metrics ====================
ax = axes[1, 1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'Performance Metrics', fontsize=12, fontweight='bold', ha='center', color=mlpurple)

metrics = [
    ('Annualized Return', '12.4%', '8.2%', mlgreen),
    ('Annualized Volatility', '18.2%', '15.1%', mlorange),
    ('Sharpe Ratio', '0.68', '0.54', mlgreen),
    ('Max Drawdown', '-22.3%', '-18.7%', mlred),
    ('Win Rate', '53.2%', '-', mlblue),
    ('Profit Factor', '1.12', '-', mlblue),
]

# Table header
ax.text(0.5, 7.8, 'Metric', fontsize=10, fontweight='bold', color=mlgray)
ax.text(4, 7.8, 'MLP Strategy', fontsize=10, fontweight='bold', color=mlpurple)
ax.text(7, 7.8, 'Buy & Hold', fontsize=10, fontweight='bold', color=mlgray)

for i, (metric, mlp_val, market_val, color) in enumerate(metrics):
    y = 7 - i * 0.9
    ax.text(0.5, y, metric, fontsize=9, color=mlgray)
    ax.text(4.5, y, mlp_val, fontsize=9, color=color, fontweight='bold')
    ax.text(7.5, y, market_val, fontsize=9, color=mlgray)

# Warning note
ax.text(5, 1, 'Note: These are simulated results for illustration.\nReal performance will vary significantly.',
        ha='center', fontsize=8, color=mlred, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor=mlred))

fig.suptitle('Backtesting Results: MLP Trading Strategy',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('finance_backtest_results.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_backtest_results.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_backtest_results.pdf")
