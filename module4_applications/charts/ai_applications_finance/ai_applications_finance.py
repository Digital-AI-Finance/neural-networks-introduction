CHART_METADATA = {
    'title': 'AI Applications Finance',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/ai_applications_finance'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Color palette
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

ax.text(6, 8.5, 'AI/ML Applications in Finance', fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Application boxes
apps = [
    (2, 6, 'Trading', ['Algorithmic trading', 'Price prediction', 'Portfolio optimization'], mlblue),
    (6, 6, 'Risk Management', ['Credit scoring', 'Fraud detection', 'Market risk'], mlred),
    (10, 6, 'Operations', ['Document processing', 'Customer service', 'Compliance'], mlgreen),
    (2, 2.5, 'Asset Management', ['Factor models', 'Alternative data', 'Sentiment analysis'], mlorange),
    (6, 2.5, 'Banking', ['Loan approval', 'Customer churn', 'Personalization'], mlpurple),
    (10, 2.5, 'Insurance', ['Claims processing', 'Pricing models', 'Actuarial ML'], mlgray),
]

for x, y, title, items, color in apps:
    rect = mpatches.FancyBboxPatch((x-1.5, y-1.3), 3, 2.4, boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.15, edgecolor=color, lw=2)
    ax.add_patch(rect)
    ax.text(x, y+0.8, title, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y - 0.1 - i*0.45, f'- {item}', ha='center', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('ai_applications_finance.pdf', bbox_inches='tight', dpi=300)
plt.savefig('ai_applications_finance.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: ai_applications_finance.pdf")
