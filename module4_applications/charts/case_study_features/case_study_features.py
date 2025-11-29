CHART_METADATA = {
    'title': 'Case Study Features',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/case_study_features'
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

# Left: Feature categories
ax1 = axes[0]
categories = ['Technical\nIndicators', 'Price-Based', 'Volume', 'Fundamental', 'Sentiment']
counts = [20, 12, 8, 7, 3]
colors = [mlblue, mlpurple, mlgreen, mlorange, mlred]

bars = ax1.barh(categories, counts, color=colors, alpha=0.7)
ax1.set_xlabel('Number of Features', fontsize=11)
ax1.set_title('Feature Categories (50 total)', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='x')

for bar, count in zip(bars, counts):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, str(count),
             va='center', fontsize=10)

# Right: Feature importance (example)
ax2 = axes[1]
features = ['RSI(14)', 'MACD', 'Volume MA', 'P/E Ratio', 'Returns(5d)', 'Volatility', 'SMA(20)', 'Momentum']
importance = [0.15, 0.12, 0.11, 0.09, 0.08, 0.08, 0.07, 0.06]
colors2 = [mlblue if i < 2 else (mlgreen if i < 4 else mlgray) for i in range(len(features))]

bars2 = ax2.barh(features, importance, color=colors2, alpha=0.7)
ax2.set_xlabel('Feature Importance', fontsize=11)
ax2.set_title('Top Features by Importance', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='x')
ax2.invert_yaxis()

plt.suptitle('Case Study: Feature Engineering', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('case_study_features.pdf', bbox_inches='tight', dpi=300)
plt.savefig('case_study_features.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: case_study_features.pdf")
