"""
Timeline 1986-2012: From Revival to Deep Learning
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Timeline 1986 2012',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/timeline_1986_2012'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(1984, 2014)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(1999, 9.5, 'Neural Networks: 1986-2012',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Timeline base
ax.axhline(y=5, color=mlgray, linewidth=3, alpha=0.5)

# Events
events = [
    (1986, 'Backprop Paper', mlgreen, 7, 'Rumelhart et al.\nNature paper'),
    (1989, 'Cybenko\nUniversal Approx.', mlblue, 3, 'MLP can approximate\nany function'),
    (1997, 'LSTM', mlorange, 7, 'Hochreiter & Schmidhuber\nLong-term memory'),
    (1998, 'LeNet-5', mlblue, 3, 'LeCun - CNNs for\nhandwriting'),
    (2006, 'Deep Belief\nNetworks', mlgreen, 7, 'Hinton - Pre-training\nbreakthrough'),
    (2009, 'GPU Training', mlorange, 3, 'Raina et al.\n100x speedup'),
    (2012, 'AlexNet', mlgreen, 7, 'ImageNet victory\nDeep Learning era begins'),
]

for year, label, color, y, desc in events:
    # Vertical line to timeline
    ax.plot([year, year], [5, y], color=color, linewidth=2)

    # Event marker
    ax.scatter([year], [5], c=color, s=100, zorder=5)

    # Label
    ax.text(year, y + (0.3 if y > 5 else -0.3), label,
            ha='center', va='bottom' if y > 5 else 'top',
            fontsize=9, fontweight='bold', color=color)

    # Description
    desc_y = y + 1 if y > 5 else y - 1
    ax.text(year, desc_y, desc, ha='center',
            va='bottom' if y > 5 else 'top',
            fontsize=7, color=mlgray)

# Era backgrounds
ax.fill_between([1986, 1998], 0, 1, alpha=0.2, color=mlgreen)
ax.text(1992, 0.5, 'Connectionism Era', ha='center', fontsize=9, color=mlgreen)

ax.fill_between([1998, 2006], 0, 1, alpha=0.2, color=mlgray)
ax.text(2002, 0.5, 'Second AI Winter', ha='center', fontsize=9, color=mlgray)

ax.fill_between([2006, 2014], 0, 1, alpha=0.2, color=mlblue)
ax.text(2010, 0.5, 'Deep Learning Revival', ha='center', fontsize=9, color=mlblue)

# Year markers
for year in range(1985, 2015, 5):
    ax.text(year, 4.7, str(year), ha='center', fontsize=8, color=mlgray)

# Key insight box
insight = """Key Turning Points:
- 1986: Backpropagation makes training practical
- 2006: Deep pre-training solves vanishing gradients
- 2012: GPUs + Big Data + Deep Networks = Revolution"""

ax.text(1999, 1.8, insight, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlpurple, linewidth=2))

plt.tight_layout()
plt.savefig('timeline_1986_2012.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('timeline_1986_2012.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: timeline_1986_2012.pdf")
