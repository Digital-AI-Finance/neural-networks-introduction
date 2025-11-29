CHART_METADATA = {
    'title': 'Financial Data Challenges',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/financial_data_challenges'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(6, 8.5, 'Challenges with Financial Data for ML', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

challenges = [
    (2, 6.5, 'Low Signal-to-Noise', ['High randomness', 'Weak patterns', 'Efficient markets'], mlred),
    (6, 6.5, 'Non-Stationarity', ['Regime changes', 'Structural breaks', 'Evolving relationships'], mlorange),
    (10, 6.5, 'Limited Data', ['Short history', 'Rare events', 'Survivorship bias'], mlblue),
    (2, 3, 'Look-Ahead Bias', ['Data timestamps', 'Restatements', 'Delayed reporting'], mlpurple),
    (6, 3, 'Multicollinearity', ['Correlated features', 'Factor exposure', 'Redundant signals'], mlgreen),
    (10, 3, 'Class Imbalance', ['Rare events (crashes)', 'Skewed returns', 'Asymmetric outcomes'], mlgray),
]

for x, y, title, items, color in challenges:
    rect = mpatches.FancyBboxPatch((x-1.5, y-1.3), 3, 2.4, boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.15, edgecolor=color, lw=2)
    ax.add_patch(rect)
    ax.text(x, y+0.8, title, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y - 0.1 - i*0.45, f'- {item}', ha='center', va='center', fontsize=9)

ax.text(6, 0.5, 'These challenges make financial ML harder than typical ML applications',
        ha='center', fontsize=11, color=mlgray, style='italic')

plt.tight_layout()
plt.savefig('financial_data_challenges.pdf', bbox_inches='tight', dpi=300)
plt.savefig('financial_data_challenges.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: financial_data_challenges.pdf")
