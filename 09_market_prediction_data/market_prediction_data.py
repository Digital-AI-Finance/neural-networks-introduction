# ==============================================================================
# Chart: Market Prediction Data
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/09_market_prediction_data/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Market Prediction Data

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/09_market_prediction_data/
"""

CHART_METADATA = {
    'name': 'Market Prediction Data',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/09_market_prediction_data',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set up the figure
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle('Market Data: Input Features for Neural Network', fontsize=16, fontweight='bold')

# Generate synthetic but realistic market data
np.random.seed(42)
days = 60
dates = np.arange(days)

# Feature 1: Stock Price (with trend and noise)
base_price = 100
trend = np.linspace(0, 15, days)
noise = np.random.randn(days) * 2
price = base_price + trend + noise
price = np.maximum(price, 90)  # Floor at 90

# Feature 2: Trading Volume (normalized)
volume_base = 1.0
volume = volume_base + 0.3 * np.sin(dates / 5) + 0.2 * np.random.randn(days)
volume = np.abs(volume)

# Feature 3: Market Sentiment Score (oscillating)
sentiment = 0.5 + 0.3 * np.sin(dates / 7) + 0.1 * np.random.randn(days)
sentiment = np.clip(sentiment, 0, 1)

# Feature 4: Volatility Index
volatility = 0.4 + 0.2 * np.abs(np.sin(dates / 10)) + 0.15 * np.random.randn(days)
volatility = np.clip(volatility, 0.1, 1.0)

# Target: Price direction (up or down next day)
price_change = np.diff(price, prepend=price[0])
target = (price_change > 0).astype(int)

# PLOT 1: Stock Price
ax1 = axes[0, 0]
ax1.plot(dates, price, 'b-', linewidth=2, label='Stock Price')
ax1.fill_between(dates, price, alpha=0.3)
ax1.scatter(dates[target == 1], price[target == 1], color='green', s=30, alpha=0.6, label='Price Increased')
ax1.scatter(dates[target == 0], price[target == 0], color='red', s=30, alpha=0.6, label='Price Decreased')
ax1.set_xlabel('Day', fontsize=10)
ax1.set_ylabel('Price ($)', fontsize=10)
ax1.set_title('Feature 1: Historical Stock Price', fontsize=11, fontweight='bold')
ax1.legend(loc='upper left', fontsize=8)
ax1.grid(True, alpha=0.3)

# Add annotation
ax1.text(30, 92, 'Input: Yesterday\'s price\nTarget: Will it rise tomorrow?',
        fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# PLOT 2: Trading Volume
ax2 = axes[0, 1]
colors = ['green' if t == 1 else 'red' for t in target]
ax2.bar(dates, volume, color=colors, alpha=0.6, edgecolor='black', linewidth=0.5)
ax2.set_xlabel('Day', fontsize=10)
ax2.set_ylabel('Volume (normalized)', fontsize=10)
ax2.set_title('Feature 2: Trading Volume', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
ax2.axhline(y=1.0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Add annotation
ax2.text(30, 1.8, 'High volume often\nprecedes price changes',
        fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# PLOT 3: Market Sentiment
ax3 = axes[1, 0]
ax3.plot(dates, sentiment, 'purple', linewidth=2, label='Sentiment Score')
ax3.fill_between(dates, sentiment, alpha=0.4, color='purple')
ax3.axhline(y=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='Neutral')
ax3.set_xlabel('Day', fontsize=10)
ax3.set_ylabel('Sentiment Score', fontsize=10)
ax3.set_title('Feature 3: Market Sentiment', fontsize=11, fontweight='bold')
ax3.set_ylim([0, 1])
ax3.legend(loc='upper left', fontsize=8)
ax3.grid(True, alpha=0.3)

# Add color bands
ax3.axhspan(0, 0.3, alpha=0.1, color='red', label='Negative')
ax3.axhspan(0.3, 0.7, alpha=0.1, color='yellow')
ax3.axhspan(0.7, 1.0, alpha=0.1, color='green')
ax3.text(5, 0.15, 'Bearish', fontsize=7)
ax3.text(5, 0.85, 'Bullish', fontsize=7)

# PLOT 4: Volatility Index
ax4 = axes[1, 1]
ax4.plot(dates, volatility, 'orange', linewidth=2, label='Volatility Index')
ax4.fill_between(dates, volatility, alpha=0.4, color='orange')
ax4.set_xlabel('Day', fontsize=10)
ax4.set_ylabel('Volatility Index', fontsize=10)
ax4.set_title('Feature 4: Market Volatility', fontsize=11, fontweight='bold')
ax4.legend(loc='upper left', fontsize=8)
ax4.grid(True, alpha=0.3)

# Add annotation
ax4.text(30, 0.85, 'Higher volatility =\nGreater uncertainty',
        fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

# Add overall explanation
explanation = 'Neural Network Input: All 4 features for each day | Output: Probability of price increase tomorrow'
fig.text(0.5, 0.02, explanation, ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout(rect=[0, 0.04, 1, 0.97])
plt.savefig('market_prediction_data.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: market_prediction_data.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/09_market_prediction_data/
