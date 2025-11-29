"""
Neural Networks: Limitations and Criticisms
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Limitations And Criticisms',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/limitations_and_criticisms'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(7, 10.5, 'Neural Networks: Limitations & Criticisms',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Limitations
limitations = [
    ('Black Box Problem', mlred, 3.5, 8, [
        'Hard to interpret decisions',
        'Cannot explain "why"',
        'Problematic for regulated industries',
    ]),
    ('Data Hungry', mlorange, 10.5, 8, [
        'Need lots of labeled data',
        'Small data = overfitting',
        'Labeling is expensive',
    ]),
    ('Computational Cost', mlorange, 3.5, 4.5, [
        'Training is expensive',
        'Large models need GPUs',
        'Environmental concerns',
    ]),
    ('Brittleness', mlred, 10.5, 4.5, [
        'Adversarial examples',
        'Distribution shift',
        'Unreliable uncertainty',
    ]),
]

for title, color, x, y, items in limitations:
    box = FancyBboxPatch((x - 2.2, y - 1.8), 4.4, 2.8, boxstyle="round,pad=0.1",
                          facecolor=f'{color}11', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.7, title, ha='center', fontsize=11, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y - 0.1 - i * 0.5, '- ' + item, ha='center', fontsize=9, color=mlgray)

# Central balance
ax.text(7, 6.25, 'vs', ha='center', fontsize=20, fontweight='bold', color=mlgray)

# Counterpoint box
counter_box = FancyBboxPatch((4.5, 0.5), 5, 2, boxstyle="round,pad=0.1",
                              facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(counter_box)

ax.text(7, 2, 'Despite Limitations:', ha='center', fontsize=11, fontweight='bold', color=mlgreen)
ax.text(7, 1.3, 'Neural networks achieve state-of-the-art on\nmany practical tasks (vision, NLP, games, ...)',
        ha='center', fontsize=9, color=mlgray)

# Arrows
ax.annotate('', xy=(5.5, 6.25), xytext=(4.5, 6.25),
            arrowprops=dict(arrowstyle='<-', color=mlred, lw=2))
ax.annotate('', xy=(8.5, 6.25), xytext=(9.5, 6.25),
            arrowprops=dict(arrowstyle='<-', color=mlred, lw=2))

plt.tight_layout()
plt.savefig('limitations_and_criticisms.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('limitations_and_criticisms.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: limitations_and_criticisms.pdf")
