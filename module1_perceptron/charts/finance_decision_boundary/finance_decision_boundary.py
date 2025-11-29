"""
Finance Decision Boundary - Stock Buy/Sell Classification
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Finance Decision Boundary',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_decision_boundary'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(10, 8))

# Generate realistic stock data
np.random.seed(123)
n = 35

# Buy stocks: high P/E ratio growth potential, positive momentum
pe_buy = np.random.uniform(15, 35, n)
momentum_buy = np.random.uniform(0.02, 0.15, n)

# Sell stocks: low P/E (value traps), negative momentum
pe_sell = np.random.uniform(5, 20, n)
momentum_sell = np.random.uniform(-0.10, 0.03, n)

# Plot stocks
ax.scatter(pe_buy, momentum_buy * 100, c=mlgreen, s=100, marker='^',
           label='Buy Recommendations', edgecolors='white', linewidths=1.5, zorder=5)
ax.scatter(pe_sell, momentum_sell * 100, c=mlorange, s=100, marker='v',
           label='Sell Recommendations', edgecolors='white', linewidths=1.5, zorder=5)

# Decision boundary: linear combination
# w1 * PE + w2 * Momentum + b = 0
# Using: 0.1 * PE + 2 * Momentum - 2 = 0
# => Momentum = (2 - 0.1 * PE) / 2 = 1 - 0.05 * PE
pe_line = np.linspace(0, 40, 100)
momentum_line = (2.5 - 0.08 * pe_line)

ax.plot(pe_line, momentum_line, color=mlpurple, linewidth=3, label='Decision Boundary')

# Shade regions
ax.fill_between(pe_line, momentum_line, 20, alpha=0.15, color=mlgreen)
ax.fill_between(pe_line, -15, momentum_line, alpha=0.15, color=mlorange)

# Region labels
ax.text(30, 12, 'BUY REGION', fontsize=14, fontweight='bold', color=mlgreen, ha='center')
ax.text(10, -8, 'SELL REGION', fontsize=14, fontweight='bold', color=mlorange, ha='center')

# Boundary equation
ax.text(35, 1, '$0.08 \\times PE + 0.4 \\times Momentum - 2 = 0$',
        fontsize=10, color=mlpurple, rotation=-20)

# Axis labels
ax.set_xlabel('P/E Ratio', fontsize=12)
ax.set_ylabel('3-Month Momentum (%)', fontsize=12)
ax.set_title('Perceptron for Stock Classification', fontsize=14, fontweight='bold', color=mlpurple)

# Formatting
ax.set_xlim(0, 40)
ax.set_ylim(-12, 18)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='-')

# Add interpretation
interpretation = """Interpretation:
- Stocks above the line: positive signal
- Stocks below the line: negative signal
- The line represents a weighted combination
  of P/E ratio and momentum"""
ax.text(0.02, 0.98, interpretation, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

plt.tight_layout()
plt.savefig('finance_decision_boundary.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_decision_boundary.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_decision_boundary.pdf")
