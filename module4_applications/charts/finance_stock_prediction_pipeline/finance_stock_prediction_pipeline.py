"""
Finance Stock Prediction Pipeline
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

CHART_METADATA = {
    'title': 'Finance Stock Prediction Pipeline',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_stock_prediction_pipeline'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Stock Return Prediction Pipeline',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== PIPELINE STAGES ====================
stages = [
    (1.5, 6, 'DATA\nCOLLECTION', mlblue, [
        'Price history',
        'Volume data',
        'Fundamentals',
        'Market indices',
    ]),
    (4.5, 6, 'FEATURE\nENGINEERING', mlorange, [
        'Technical indicators',
        'Returns, volatility',
        'Momentum signals',
        'Lagged features',
    ]),
    (7.5, 6, 'MODEL\nTRAINING', mlpurple, [
        'Train/val/test split',
        'MLP architecture',
        'Cross-validation',
        'Hyperparameter tuning',
    ]),
    (10.5, 6, 'EVALUATION\n& BACKTEST', mlgreen, [
        'Out-of-sample test',
        'Walk-forward analysis',
        'Risk metrics',
        'Transaction costs',
    ]),
]

for x, y, title, color, items in stages:
    box = FancyBboxPatch((x - 1.3, y - 1.5), 2.6, 3, boxstyle="round,pad=0.1",
                          facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 1, title, ha='center', fontsize=9, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y + 0.2 - i * 0.5, '- ' + item, ha='center', fontsize=7, color=mlgray)

# Arrows between stages
arrow_positions = [(2.8, 6), (5.8, 6), (8.8, 6)]
for x, y in arrow_positions:
    ax.annotate('', xy=(x + 0.5, y), xytext=(x - 0.3, y),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# ==================== OUTPUT ====================
output_box = FancyBboxPatch((5.5, 1), 3, 1.5, boxstyle="round,pad=0.1",
                             facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=3)
ax.add_patch(output_box)
ax.text(7, 2, 'TRADING SIGNAL', ha='center', fontsize=10, fontweight='bold', color=mlgreen)
ax.text(7, 1.4, 'Buy / Hold / Sell', ha='center', fontsize=9, color=mlgray)

# Arrow from evaluation to output
ax.annotate('', xy=(7, 2.7), xytext=(7, 4.2),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=2))

# ==================== WARNINGS BOX ====================
warnings = """Key Considerations for Finance:
- Markets are non-stationary (patterns change over time)
- Overfitting is extremely common (many try, few succeed)
- Transaction costs erode profits
- Past performance does NOT guarantee future results
- Risk management is as important as prediction"""

ax.text(7, 0.3, warnings, ha='center', va='top', fontsize=8, color=mlgray,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF0F0', edgecolor=mlgray, alpha=0.9))

plt.tight_layout()
plt.savefig('finance_stock_prediction_pipeline.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_stock_prediction_pipeline.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_stock_prediction_pipeline.pdf")
