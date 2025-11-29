"""
Deep Learning Revolution - Why Now?
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Deep Learning Revolution',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/deep_learning_revolution'
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
ax.text(7, 10.5, 'The Deep Learning Revolution: Why Now?',
        fontsize=18, fontweight='bold', ha='center', color=mlpurple)

# Three pillars
pillars = [
    (2.5, 6, 'BIG DATA', mlblue, [
        'ImageNet (14M images)',
        'Internet-scale datasets',
        'User-generated content',
        'Sensor data explosion',
    ]),
    (7, 6, 'COMPUTE', mlorange, [
        'GPU parallel processing',
        'Cloud computing',
        'TPUs, specialized hardware',
        '1000x speedup since 2012',
    ]),
    (11.5, 6, 'ALGORITHMS', mlgreen, [
        'ReLU activation',
        'Dropout regularization',
        'Batch normalization',
        'Better architectures',
    ]),
]

for x, y, title, color, items in pillars:
    # Pillar shape
    box = FancyBboxPatch((x - 1.8, y - 3), 3.6, 5, boxstyle="round,pad=0.1",
                          facecolor=f'{color}22', edgecolor=color, linewidth=3)
    ax.add_patch(box)
    ax.text(x, y + 1.5, title, ha='center', fontsize=12, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y + 0.5 - i * 0.6, '- ' + item, ha='center', fontsize=9, color=mlgray)

# Arrows converging to center
for x in [2.5, 7, 11.5]:
    ax.annotate('', xy=(7, 2.2), xytext=(x, 2.8),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Result
result_box = FancyBboxPatch((4.5, 0.5), 5, 1.5, boxstyle="round,pad=0.1",
                             facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=3)
ax.add_patch(result_box)
ax.text(7, 1.5, 'DEEP LEARNING', ha='center', fontsize=14, fontweight='bold', color=mlpurple)
ax.text(7, 0.9, 'Superhuman performance in many tasks', ha='center', fontsize=10, color=mlgray)

# Timeline annotations
ax.text(7, 9.5, '2012: AlexNet wins ImageNet by huge margin', ha='center', fontsize=10,
        color=mlgreen, style='italic')

plt.tight_layout()
plt.savefig('deep_learning_revolution.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('deep_learning_revolution.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: deep_learning_revolution.pdf")
