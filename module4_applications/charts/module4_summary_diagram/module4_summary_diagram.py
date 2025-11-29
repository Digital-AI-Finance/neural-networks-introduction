"""
Module 4 Summary Diagram
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Module4 Summary Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/module4_summary_diagram'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.5, 'Module 4 Summary: Applications & Modern Perspectives',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Four main topic areas
topics = [
    (3.5, 8.5, 'FINANCE\nAPPLICATIONS', mlblue, [
        'Feature engineering',
        'Walk-forward validation',
        'Backtesting',
        'Risk management',
    ]),
    (10.5, 8.5, 'HISTORICAL\nCONTEXT', mlorange, [
        '1943-2012 timeline',
        'AI winters',
        'Deep learning revolution',
        'Key breakthroughs',
    ]),
    (3.5, 3.5, 'LIMITATIONS\n& CHALLENGES', mlred, [
        'Black box problem',
        'Data requirements',
        'Computational cost',
        'Interpretability',
    ]),
    (10.5, 3.5, 'PRACTICAL\nGUIDANCE', mlgreen, [
        'When to use NNs',
        'Model selection',
        'Bias-variance tradeoff',
        'Best practices',
    ]),
]

for x, y, title, color, items in topics:
    box = FancyBboxPatch((x - 2.3, y - 1.8), 4.6, 3.2, boxstyle="round,pad=0.1",
                          facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 1, title, ha='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y + 0.1 - i * 0.5, '- ' + item, ha='center', fontsize=8, color=mlgray)

# Central connecting element
center_circle = Circle((7, 6), 1.2, fill=True, facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=3)
ax.add_patch(center_circle)
ax.text(7, 6, 'MLP in\nPractice', ha='center', va='center', fontsize=10, fontweight='bold', color=mlpurple)

# Arrows from center to topics
arrow_positions = [
    (7, 7.2, 3.5, 6.7),   # to finance
    (7, 7.2, 10.5, 6.7),  # to history
    (7, 4.8, 3.5, 5.3),   # to limitations
    (7, 4.8, 10.5, 5.3),  # to guidance
]

for x1, y1, x2, y2 in arrow_positions:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color=mlgray, lw=1.5, alpha=0.5))

# Key takeaways at bottom
takeaways_box = FancyBboxPatch((0.5, 0.3), 13, 1.2, boxstyle="round,pad=0.1",
                                facecolor='white', edgecolor=mlpurple, linewidth=2)
ax.add_patch(takeaways_box)

ax.text(7, 1.1, 'Key Takeaways', ha='center', fontsize=11, fontweight='bold', color=mlpurple)
ax.text(7, 0.6, 'NNs are powerful but not always the best choice. Understand the tradeoffs. Start simple. Finance requires careful validation.',
        ha='center', fontsize=9, color=mlgray)

plt.tight_layout()
plt.savefig('module4_summary_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('module4_summary_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: module4_summary_diagram.pdf")
