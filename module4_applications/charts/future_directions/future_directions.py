"""
Future Directions in Neural Networks
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Future Directions',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/future_directions'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(7, 10.5, 'Future Directions in Neural Networks',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Central node
center = Circle((7, 5.5), 1.2, fill=True, facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=3)
ax.add_patch(center)
ax.text(7, 5.5, 'Beyond\nMLPs', ha='center', va='center', fontsize=11, fontweight='bold', color=mlpurple)

# Surrounding directions
directions = [
    (2.5, 8, 'ARCHITECTURES', mlblue, [
        'Transformers',
        'Graph Neural Networks',
        'Neural ODEs',
        'Mixture of Experts',
    ]),
    (11.5, 8, 'EFFICIENCY', mlorange, [
        'Model compression',
        'Quantization',
        'Knowledge distillation',
        'Edge deployment',
    ]),
    (2.5, 3, 'LEARNING', mlgreen, [
        'Self-supervised learning',
        'Few-shot learning',
        'Continual learning',
        'Meta-learning',
    ]),
    (11.5, 3, 'APPLICATIONS', mlpurple, [
        'Large Language Models',
        'Generative AI',
        'Scientific discovery',
        'Autonomous systems',
    ]),
]

for x, y, title, color, items in directions:
    box = FancyBboxPatch((x - 2, y - 1.5), 4, 2.8, boxstyle="round,pad=0.1",
                          facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 1, title, ha='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y + 0.2 - i * 0.5, '- ' + item, ha='center', fontsize=8, color=mlgray)

# Arrows from center
arrow_ends = [(4, 7), (10, 7), (4, 4), (10, 4)]
for ex, ey in arrow_ends:
    dx, dy = ex - 7, ey - 5.5
    length = np.sqrt(dx**2 + dy**2)
    start_x = 7 + 1.2 * dx / length
    start_y = 5.5 + 1.2 * dy / length
    ax.annotate('', xy=(ex, ey), xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Bottom note
ax.text(7, 0.5, 'The field is evolving rapidly! MLPs are the foundation for understanding all these advances.',
        ha='center', fontsize=10, color=mlpurple, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

plt.tight_layout()
plt.savefig('future_directions.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('future_directions.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: future_directions.pdf")
