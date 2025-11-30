# ==============================================================================
# Chart: Feature Hierarchy
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/16_feature_hierarchy/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Feature Hierarchy

Layer-by-layer data transformation visualization

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/16_feature_hierarchy/
"""

CHART_METADATA = {
    'name': 'Feature Hierarchy',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/16_feature_hierarchy',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Layer-by-layer data transformation visualization'
}

"""
Chart 16: Feature Hierarchy
Shows what each layer "sees": raw price -> patterns -> strategy.
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

fig, axes = plt.subplots(1, 4, figsize=(14, 4))

# Generate price data
days = 30
t = np.arange(days)
price = 100 + 5*np.sin(t/5) + np.cumsum(np.random.randn(days)*0.5)
volume = np.abs(np.random.randn(days)) * 1000000

# Panel 1: Raw Input (what network receives)
ax1 = axes[0]
ax1.plot(t, price, color=mlblue, linewidth=2)
ax1.fill_between(t, price.min()-2, price, alpha=0.2, color=mlblue)
ax1.set_xlabel('Day', fontsize=9)
ax1.set_ylabel('Price ($)', fontsize=9)
ax1.set_title('INPUT LAYER\nRaw Data', fontsize=11, fontweight='bold', color=mlgray)
ax1.tick_params(labelsize=8)
ax1.grid(True, alpha=0.3)

# Add data points annotation
ax1.annotate('Just numbers:\n[102.3, 103.1, ...]', xy=(15, price.min()), fontsize=9,
            ha='center', color=mlgray,
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlgray, alpha=0.8))

# Panel 2: Hidden Layer 1 (simple patterns)
ax2 = axes[1]
# Show trend detection
trend = np.convolve(price, np.ones(5)/5, mode='same')
ax2.plot(t, price, color=mlgray, linewidth=1, alpha=0.5, label='Price')
ax2.plot(t, trend, color=mlorange, linewidth=3, label='Trend')

# Mark trend changes
peaks = [8, 18, 25]
for p in peaks:
    ax2.axvline(x=p, color=mlred, linestyle='--', alpha=0.5)

ax2.set_xlabel('Day', fontsize=9)
ax2.set_title('HIDDEN LAYER 1\nSimple Patterns', fontsize=11, fontweight='bold', color=mlorange)
ax2.tick_params(labelsize=8)
ax2.legend(fontsize=8, loc='upper left')
ax2.grid(True, alpha=0.3)

ax2.annotate('Detects:\n- Trends\n- Momentum', xy=(22, price.max()), fontsize=9,
            ha='center', color=mlorange,
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlorange, alpha=0.8))

# Panel 3: Hidden Layer 2 (complex patterns)
ax3 = axes[2]
# Show pattern recognition
ax3.plot(t, price, color=mlgray, linewidth=1, alpha=0.3)

# Highlight bullish and bearish zones
bullish_zones = [(5, 12), (20, 26)]
bearish_zones = [(0, 5), (12, 20)]

for start, end in bullish_zones:
    ax3.axvspan(start, end, alpha=0.3, color=mlgreen)
for start, end in bearish_zones:
    ax3.axvspan(start, end, alpha=0.3, color=mlred)

ax3.set_xlabel('Day', fontsize=9)
ax3.set_title('HIDDEN LAYER 2\nComplex Patterns', fontsize=11, fontweight='bold', color=mlblue)
ax3.tick_params(labelsize=8)
ax3.grid(True, alpha=0.3)

ax3.annotate('Combines:\n- Trend + Volume\n- Support/Resistance', xy=(15, price.min()),
            fontsize=9, ha='center', color=mlblue,
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlblue, alpha=0.8))

# Panel 4: Output Layer (decision)
ax4 = axes[3]
ax4.axis('off')

# Draw decision boxes
ax4.add_patch(plt.Rectangle((0.1, 0.6), 0.35, 0.3, fill=True,
              facecolor=mlgreen, alpha=0.3, edgecolor=mlgreen, linewidth=2))
ax4.add_patch(plt.Rectangle((0.55, 0.6), 0.35, 0.3, fill=True,
              facecolor=mlred, alpha=0.3, edgecolor=mlred, linewidth=2))

ax4.text(0.275, 0.75, 'BUY', fontsize=16, ha='center', va='center',
        fontweight='bold', color=mlgreen)
ax4.text(0.275, 0.67, '68%', fontsize=14, ha='center', va='center', color=mlgreen)

ax4.text(0.725, 0.75, 'SELL', fontsize=16, ha='center', va='center',
        fontweight='bold', color=mlred)
ax4.text(0.725, 0.67, '32%', fontsize=14, ha='center', va='center', color=mlred)

ax4.set_title('OUTPUT LAYER\nDecision', fontsize=11, fontweight='bold', color=mlpurple)

# Arrow showing decision
ax4.annotate('', xy=(0.275, 0.55), xytext=(0.5, 0.35),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=3))

ax4.text(0.5, 0.25, 'Final:\nBUY\nConfidence: 68%', fontsize=11, ha='center',
        fontweight='bold', color=mlpurple,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, linewidth=2))

ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)

# Add connecting arrows between panels
fig.text(0.26, 0.5, '-->', fontsize=20, ha='center', va='center', color=mlgray)
fig.text(0.51, 0.5, '-->', fontsize=20, ha='center', va='center', color=mlgray)
fig.text(0.76, 0.5, '-->', fontsize=20, ha='center', va='center', color=mlgray)

plt.tight_layout()
plt.savefig('feature_hierarchy.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 16_feature_hierarchy/feature_hierarchy.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/16_feature_hierarchy/
