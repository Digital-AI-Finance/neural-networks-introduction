CHART_METADATA = {
    'title': 'Ethical Considerations',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/ethical_considerations'
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

ax.text(6, 8.5, 'Ethical Considerations in AI/ML for Finance', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

topics = [
    (2, 6.5, 'Fairness & Bias', ['Credit discrimination', 'Protected attributes', 'Disparate impact'], mlred),
    (6, 6.5, 'Transparency', ['Black box models', 'Explainability', 'Audit trails'], mlorange),
    (10, 6.5, 'Privacy', ['Data protection', 'Customer consent', 'GDPR compliance'], mlblue),
    (2, 3, 'Market Integrity', ['Flash crashes', 'Market manipulation', 'Systemic risk'], mlpurple),
    (6, 3, 'Accountability', ['Model governance', 'Human oversight', 'Liability'], mlgreen),
    (10, 3, 'Job Displacement', ['Automation impact', 'Skill requirements', 'Social effects'], mlgray),
]

for x, y, title, items, color in topics:
    rect = mpatches.FancyBboxPatch((x-1.5, y-1.3), 3, 2.4, boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.15, edgecolor=color, lw=2)
    ax.add_patch(rect)
    ax.text(x, y+0.8, title, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y - 0.1 - i*0.45, f'- {item}', ha='center', va='center', fontsize=9)

ax.text(6, 0.5, 'Responsible AI: Balance innovation with societal impact',
        ha='center', fontsize=11, color=mlgray, style='italic')

plt.tight_layout()
plt.savefig('ethical_considerations.pdf', bbox_inches='tight', dpi=300)
plt.savefig('ethical_considerations.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: ethical_considerations.pdf")
