# ==============================================================================
# Chart: Problem Visualization
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/11_problem_visualization/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Problem Visualization

XOR problem demonstrating why simple rules fail

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/11_problem_visualization/
"""

CHART_METADATA = {
    'name': 'Problem Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/11_problem_visualization',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'XOR problem demonstrating why simple rules fail'
}

"""
Chart 11: Problem Visualization
Shows why simple rules fail - non-linear, overlapping clusters in market data.
"""

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic market data
n_points = 100

# UP days - higher returns with certain patterns
up_returns = np.random.normal(0.02, 0.015, n_points//2)
up_volume = np.random.normal(1.2, 0.3, n_points//2)
up_sentiment = np.random.normal(0.6, 0.2, n_points//2)

# DOWN days - lower returns with different patterns
down_returns = np.random.normal(-0.01, 0.02, n_points//2)
down_volume = np.random.normal(0.9, 0.35, n_points//2)
down_sentiment = np.random.normal(0.4, 0.25, n_points//2)

# Add overlap to make it realistic (markets are noisy)
up_returns = np.concatenate([up_returns, np.random.normal(0.005, 0.02, 15)])
up_volume = np.concatenate([up_volume, np.random.normal(1.0, 0.3, 15)])
down_returns = np.concatenate([down_returns, np.random.normal(-0.005, 0.015, 15)])
down_volume = np.concatenate([down_volume, np.random.normal(1.1, 0.25, 15)])

# Colors
mlgreen = '#2ca02c'
mlred = '#d62728'
mlpurple = '#3333b2'
mlgray = '#7f7f7f'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Plot 1: Returns vs Volume
ax1 = axes[0]
ax1.scatter(up_volume[:50], up_returns[:50], c=mlgreen, alpha=0.6, s=50, label='Price Rose')
ax1.scatter(down_volume[:50], down_returns[:50], c=mlred, alpha=0.6, s=50, label='Price Fell')
ax1.set_xlabel('Trading Volume (normalized)', fontsize=10)
ax1.set_ylabel('Daily Return', fontsize=10)
ax1.set_title('Returns vs Volume', fontsize=11, fontweight='bold')
ax1.legend(loc='upper left', fontsize=8)
ax1.axhline(y=0, color=mlgray, linestyle='--', alpha=0.5)
ax1.grid(True, alpha=0.3)

# Add "no simple rule" annotation
ax1.annotate('No simple line\nseparates them!', xy=(1.1, 0.01), fontsize=9,
            ha='center', color=mlpurple, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, alpha=0.8))

# Plot 2: Returns vs Sentiment
ax2 = axes[1]
up_sent = np.random.normal(0.6, 0.2, 50)
down_sent = np.random.normal(0.4, 0.25, 50)
ax2.scatter(up_sent, up_returns[:50], c=mlgreen, alpha=0.6, s=50, label='Price Rose')
ax2.scatter(down_sent, down_returns[:50], c=mlred, alpha=0.6, s=50, label='Price Fell')
ax2.set_xlabel('Market Sentiment Score', fontsize=10)
ax2.set_ylabel('Daily Return', fontsize=10)
ax2.set_title('Returns vs Sentiment', fontsize=11, fontweight='bold')
ax2.axhline(y=0, color=mlgray, linestyle='--', alpha=0.5)
ax2.grid(True, alpha=0.3)

# Plot 3: The challenge summary
ax3 = axes[2]
ax3.scatter(up_volume[:50], up_sent, c=mlgreen, alpha=0.6, s=50, label='Price Rose')
ax3.scatter(down_volume[:50], down_sent, c=mlred, alpha=0.6, s=50, label='Price Fell')
ax3.set_xlabel('Trading Volume (normalized)', fontsize=10)
ax3.set_ylabel('Sentiment Score', fontsize=10)
ax3.set_title('Volume vs Sentiment', fontsize=11, fontweight='bold')
ax3.grid(True, alpha=0.3)

# Draw failed simple rules
ax3.axhline(y=0.5, color=mlpurple, linestyle='--', alpha=0.7, linewidth=2)
ax3.axvline(x=1.0, color=mlpurple, linestyle='--', alpha=0.7, linewidth=2)
ax3.annotate('Simple rules\nfail here', xy=(0.7, 0.7), fontsize=9,
            ha='center', color=mlpurple, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, alpha=0.8))

plt.tight_layout()
plt.savefig('problem_visualization.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 11_problem_visualization/problem_visualization.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/11_problem_visualization/
