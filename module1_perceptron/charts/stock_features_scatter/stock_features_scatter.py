"""
Stock Features Scatter Plot for Perceptron Classification
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Stock Features Scatter',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/stock_features_scatter'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 8))

# Generate sample stock data
np.random.seed(42)
n_samples = 40

# Good stocks (Buy) - high normalized P/E, high momentum
pe_buy = np.random.randn(n_samples) * 0.5 + 2.5
momentum_buy = np.random.randn(n_samples) * 0.5 + 2.5

# Bad stocks (Sell) - low normalized P/E, low momentum
pe_sell = np.random.randn(n_samples) * 0.5 + 0.8
momentum_sell = np.random.randn(n_samples) * 0.5 + 0.8

# Add some company labels for a few points
company_labels = {
    'buy': ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'AMZN'],
    'sell': ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL']
}

# Plot data points
ax.scatter(pe_buy, momentum_buy, c=mlgreen, s=100, marker='o',
           label='Buy Stocks', edgecolors='white', linewidths=1.5, alpha=0.8, zorder=5)
ax.scatter(pe_sell, momentum_sell, c=mlorange, s=100, marker='s',
           label='Sell Stocks', edgecolors='white', linewidths=1.5, alpha=0.8, zorder=5)

# Add company labels to some points
for i, label in enumerate(company_labels['buy'][:3]):
    ax.annotate(label, (pe_buy[i], momentum_buy[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=8, color=mlgreen)

for i, label in enumerate(company_labels['sell'][:3]):
    ax.annotate(label, (pe_sell[i], momentum_sell[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=8, color=mlorange)

# Fill regions lightly
ax.fill_between([-0.5, 4.5], [-0.5, 4.5], [5, 5], alpha=0.1, color=mlgreen)
ax.fill_between([-0.5, 4.5], [-0.5, -0.5], [-0.5, 4.5], alpha=0.1, color=mlorange)

# Note: No decision boundary yet - this is the raw data
ax.text(3.5, 3.8, 'Buy Region', fontsize=12, color=mlgreen, fontweight='bold', alpha=0.7)
ax.text(0.3, 0.2, 'Sell Region', fontsize=12, color=mlorange, fontweight='bold', alpha=0.7)

# Axis labels
ax.set_xlabel('Normalized P/E Ratio ($x_1$)', fontsize=12)
ax.set_ylabel('Momentum Score ($x_2$)', fontsize=12)
ax.set_title('Stock Classification: Feature Space', fontsize=14, fontweight='bold', color=mlpurple)

# Formatting
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# Add question
ax.text(0.5, -0.12, 'Challenge: Can we draw a single line to separate Buy from Sell?',
        transform=ax.transAxes, fontsize=10, ha='center', style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('stock_features_scatter.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('stock_features_scatter.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: stock_features_scatter.pdf")
