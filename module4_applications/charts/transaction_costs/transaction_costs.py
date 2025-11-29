CHART_METADATA = {
    'title': 'Transaction Costs',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/transaction_costs'
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

# Left: Strategy returns with/without costs
ax1 = axes[0]
days = np.arange(252)
gross_returns = np.random.randn(252) * 0.008 + 0.0003
# High turnover strategy
turnover = 0.5  # 50% daily turnover
cost_per_trade = 0.001  # 10 bps
daily_cost = turnover * cost_per_trade * 2  # buy and sell

net_returns = gross_returns - daily_cost

gross_equity = 100 * np.exp(np.cumsum(gross_returns))
net_equity = 100 * np.exp(np.cumsum(net_returns))

ax1.plot(days, gross_equity, color=mlgreen, lw=2, label='Gross Returns')
ax1.plot(days, net_equity, color=mlred, lw=2, label='Net Returns (after costs)')
ax1.fill_between(days, net_equity, gross_equity, alpha=0.3, color=mlorange, label='Cost Drag')

ax1.set_xlabel('Trading Days', fontsize=11)
ax1.set_ylabel('Portfolio Value', fontsize=11)
ax1.set_title('Impact of Transaction Costs', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# Right: Cost breakdown
ax2 = axes[1]
costs = ['Commissions', 'Bid-Ask\nSpread', 'Market\nImpact', 'Slippage']
values = [0.05, 0.10, 0.15, 0.05]
colors = [mlblue, mlgreen, mlorange, mlpurple]

bars = ax2.bar(costs, values, color=colors, alpha=0.8)
ax2.set_ylabel('Cost (% per trade)', fontsize=11)
ax2.set_title('Components of Transaction Costs', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

for bar, val in zip(bars, values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{val:.2%}', ha='center', fontsize=10)

ax2.set_ylim(0, 0.22)

plt.tight_layout()
plt.savefig('transaction_costs.pdf', bbox_inches='tight', dpi=300)
plt.savefig('transaction_costs.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: transaction_costs.pdf")
