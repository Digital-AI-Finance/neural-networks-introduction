"""
Risk-Adjusted Returns in Finance
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Finance Risk Adjusted Returns',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_risk_adjusted_returns'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Risk vs Return Scatter ====================
ax = axes[0]

np.random.seed(42)

# Different strategies
strategies = [
    ('Buy & Hold', 8, 15, mlgray, 'o'),
    ('MLP Conservative', 10, 12, mlblue, 's'),
    ('MLP Moderate', 14, 18, mlorange, '^'),
    ('MLP Aggressive', 18, 28, mlred, 'D'),
    ('Risk-Free', 3, 0.5, mlgreen, '*'),
]

for name, ret, vol, color, marker in strategies:
    ax.scatter([vol], [ret], c=color, s=200, marker=marker, label=name, edgecolors='white', linewidths=2)

# Efficient frontier (approximate)
ef_vol = np.linspace(5, 30, 100)
ef_ret = 3 + 0.5 * ef_vol - 0.005 * ef_vol**2 + 3 * np.sqrt(ef_vol)
ax.plot(ef_vol, ef_ret, '--', color=mlpurple, linewidth=2, alpha=0.5, label='Efficient Frontier')

# Capital Market Line
cml_vol = np.linspace(0, 25, 100)
cml_ret = 3 + 0.5 * cml_vol  # Sharpe ratio of 0.5
ax.plot(cml_vol, cml_ret, ':', color=mlgreen, linewidth=2, alpha=0.7, label='Capital Market Line')

ax.set_xlabel('Risk (Volatility %)', fontsize=11)
ax.set_ylabel('Expected Return (%)', fontsize=11)
ax.set_title('Risk vs Return: Strategy Comparison', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 32)
ax.set_ylim(0, 25)

# ==================== RIGHT: Risk Metrics ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'Key Risk Metrics', fontsize=12, fontweight='bold', ha='center', color=mlpurple)

metrics = [
    ('Sharpe Ratio', '$(R_p - R_f) / \\sigma_p$', 'Risk-adjusted return', mlblue),
    ('Sortino Ratio', '$(R_p - R_f) / \\sigma_d$', 'Only downside risk', mlorange),
    ('Max Drawdown', '$\\max(Peak - Trough)$', 'Worst loss from peak', mlred),
    ('Calmar Ratio', '$R_p / MaxDD$', 'Return vs worst loss', mlgreen),
    ('Information Ratio', '$(R_p - R_b) / TE$', 'Active return per risk', mlpurple),
]

y_pos = 8
for name, formula, desc, color in metrics:
    ax.text(0.3, y_pos, name, fontsize=10, fontweight='bold', color=color)
    ax.text(3.5, y_pos, formula, fontsize=9, color=mlgray)
    ax.text(6.5, y_pos, desc, fontsize=8, color=mlgray)
    y_pos -= 1.3

# Key insight
ax.text(5, 1.2, 'High returns mean nothing without considering risk!\n'
              'Always evaluate strategies using risk-adjusted metrics.',
        ha='center', fontsize=9, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

fig.suptitle('Risk-Adjusted Performance: The Complete Picture',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('finance_risk_adjusted_returns.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_risk_adjusted_returns.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_risk_adjusted_returns.pdf")
