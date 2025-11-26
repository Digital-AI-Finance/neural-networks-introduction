# ==============================================================================
# Chart: Trading Backtest
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/20_trading_backtest/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Trading Backtest

Cumulative returns comparison: neural network vs buy-and-hold

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/20_trading_backtest/
"""

CHART_METADATA = {
    'name': 'Trading Backtest',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/20_trading_backtest',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Cumulative returns comparison: neural network vs buy-and-hold'
}

"""
Chart 20: Trading Strategy Backtest
Cumulative returns: Neural network strategy vs buy-and-hold.
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

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Generate 250 trading days (~1 year)
days = 250
t = np.arange(days)

# Market returns (realistic daily returns)
market_returns = np.random.normal(0.0004, 0.012, days)  # ~10% annual, 19% vol

# Neural network signals (70% accuracy)
actual_direction = (market_returns > 0).astype(int)
nn_correct = np.random.rand(days) < 0.70  # 70% accuracy
nn_signal = np.where(nn_correct, actual_direction, 1 - actual_direction)

# Strategy returns: go long when signal=1, short when signal=0
# (simplified: just stay out when signal=0)
nn_returns = np.where(nn_signal == 1, market_returns, 0)  # Long only
nn_returns_full = np.where(nn_signal == 1, market_returns, -market_returns)  # Long/short

# Cumulative returns
cum_market = np.cumprod(1 + market_returns) - 1
cum_nn = np.cumprod(1 + nn_returns) - 1
cum_nn_full = np.cumprod(1 + nn_returns_full) - 1

# Panel 1: Cumulative returns comparison
ax1 = axes[0]

ax1.plot(t, cum_market * 100, color=mlgray, linewidth=2, label='Buy & Hold', linestyle='--')
ax1.plot(t, cum_nn * 100, color=mlblue, linewidth=2, label='NN Long-Only')
ax1.plot(t, cum_nn_full * 100, color=mlgreen, linewidth=2.5, label='NN Long/Short')

ax1.axhline(y=0, color=mlgray, linestyle='-', alpha=0.3)

# Highlight outperformance
final_market = cum_market[-1] * 100
final_nn = cum_nn_full[-1] * 100
ax1.annotate(f'Buy & Hold: {final_market:.1f}%', xy=(days-5, final_market),
            fontsize=9, color=mlgray, ha='right', va='bottom')
ax1.annotate(f'NN Strategy: {final_nn:.1f}%', xy=(days-5, final_nn),
            fontsize=9, color=mlgreen, ha='right', va='top', fontweight='bold')

# Mark significant events
ax1.axvspan(80, 100, alpha=0.1, color=mlred)
ax1.annotate('Volatile\nPeriod', xy=(90, cum_market[90]*100 + 5), fontsize=8,
            ha='center', color=mlred)

ax1.set_xlabel('Trading Days', fontsize=10)
ax1.set_ylabel('Cumulative Return (%)', fontsize=10)
ax1.set_title('Strategy Performance: 1 Year Backtest', fontsize=11, fontweight='bold')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, days)

# Panel 2: Performance metrics
ax2 = axes[1]
ax2.axis('off')

# Calculate metrics
def sharpe_ratio(returns, rf=0.02/252):
    excess = returns - rf
    return np.sqrt(252) * np.mean(excess) / np.std(returns) if np.std(returns) > 0 else 0

def max_drawdown(cum_returns):
    peak = np.maximum.accumulate(cum_returns + 1)
    drawdown = (cum_returns + 1) / peak - 1
    return np.min(drawdown) * 100

metrics = {
    'Buy & Hold': {
        'Total Return': f'{final_market:.1f}%',
        'Sharpe Ratio': f'{sharpe_ratio(market_returns):.2f}',
        'Max Drawdown': f'{max_drawdown(cum_market):.1f}%',
        'Win Rate': f'{np.mean(market_returns > 0)*100:.0f}%',
    },
    'NN Strategy': {
        'Total Return': f'{final_nn:.1f}%',
        'Sharpe Ratio': f'{sharpe_ratio(nn_returns_full):.2f}',
        'Max Drawdown': f'{max_drawdown(cum_nn_full):.1f}%',
        'Win Rate': f'{np.mean(nn_returns_full > 0)*100:.0f}%',
    }
}

# Draw comparison table
ax2.text(0.5, 0.95, 'PERFORMANCE COMPARISON', fontsize=14, ha='center',
        fontweight='bold', color=mlpurple)

# Headers
ax2.text(0.15, 0.82, 'Metric', fontsize=11, fontweight='bold', ha='left')
ax2.text(0.50, 0.82, 'Buy & Hold', fontsize=11, fontweight='bold', ha='center', color=mlgray)
ax2.text(0.80, 0.82, 'NN Strategy', fontsize=11, fontweight='bold', ha='center', color=mlgreen)

# Horizontal line
ax2.axhline(y=0.78, xmin=0.1, xmax=0.9, color=mlgray, linewidth=1)

# Metric rows
y_positions = [0.68, 0.54, 0.40, 0.26]
metric_names = ['Total Return', 'Sharpe Ratio', 'Max Drawdown', 'Win Rate']
better_colors = [mlgreen, mlgreen, mlgreen, mlgreen]  # NN is better on all

for i, metric in enumerate(metric_names):
    y = y_positions[i]
    ax2.text(0.15, y, metric, fontsize=10, ha='left', color=mlgray)
    ax2.text(0.50, y, metrics['Buy & Hold'][metric], fontsize=11, ha='center', color=mlgray)
    ax2.text(0.80, y, metrics['NN Strategy'][metric], fontsize=11, ha='center',
            color=mlgreen, fontweight='bold')

# Add winner annotation
ax2.add_patch(plt.Rectangle((0.65, 0.2), 0.3, 0.7, fill=True,
              facecolor=mlgreen, alpha=0.05, edgecolor=mlgreen, linewidth=2))

# Bottom insight
ax2.text(0.5, 0.08, 'Key Insight: 70% accuracy translates to significant alpha!',
        fontsize=11, ha='center', fontweight='bold', color=mlpurple,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, alpha=0.8))

ax2.text(0.5, 0.02, '(Backtest only - past performance does not guarantee future results)',
        fontsize=8, ha='center', color=mlgray, style='italic')

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

plt.tight_layout()
plt.savefig('trading_backtest.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 20_trading_backtest/trading_backtest.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/20_trading_backtest/
