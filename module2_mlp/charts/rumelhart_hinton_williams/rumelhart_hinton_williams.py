"""
Rumelhart, Hinton & Williams - The Backprop Pioneers
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

CHART_METADATA = {
    'title': 'Rumelhart Hinton Williams',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/rumelhart_hinton_williams'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'The 1986 Breakthrough: Rumelhart, Hinton & Williams',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Three scientist boxes
scientists = [
    ('David Rumelhart', 'UC San Diego', 'Cognitive Science\nPDP Framework', 2.3),
    ('Geoffrey Hinton', 'CMU/Toronto', 'Boltzmann Machines\n"Godfather of DL"', 7),
    ('Ronald Williams', 'Northeastern', 'REINFORCE Algorithm\nRL Pioneer', 11.7),
]

for name, affil, contrib, x in scientists:
    box = FancyBboxPatch((x - 1.8, 6), 3.6, 2.5, boxstyle="round,pad=0.1",
                          facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=2)
    ax.add_patch(box)
    ax.text(x, 8.2, name, ha='center', fontsize=11, fontweight='bold', color=mlpurple)
    ax.text(x, 7.5, affil, ha='center', fontsize=9, color=mlblue)
    ax.text(x, 6.7, contrib, ha='center', fontsize=8, color=mlgray)

# Paper box
paper_box = FancyBboxPatch((3.5, 3.5), 7, 2, boxstyle="round,pad=0.1",
                            facecolor='#FFE4B5', edgecolor=mlorange, linewidth=3)
ax.add_patch(paper_box)

ax.text(7, 5, 'Nature (1986)', ha='center', fontsize=12, fontweight='bold', color=mlorange)
ax.text(7, 4.3, '"Learning representations by back-propagating errors"',
        ha='center', fontsize=10, style='italic')
ax.text(7, 3.7, 'Vol. 323, pp. 533-536', ha='center', fontsize=9, color=mlgray)

# Arrows from scientists to paper
for x in [2.3, 7, 11.7]:
    ax.annotate('', xy=(x, 5.5), xytext=(x, 6),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))

# Key contributions
contributions = [
    'Made backpropagation accessible',
    'Demonstrated hidden representations',
    'Showed MLPs learn meaningful features',
    'Provided practical training algorithms',
    'Launched the connectionist revolution',
]

ax.text(7, 2.8, 'Key Contributions:', ha='center', fontsize=11, fontweight='bold', color=mlgreen)

y_start = 2.2
for i, contrib in enumerate(contributions):
    ax.text(7, y_start - i * 0.4, '- ' + contrib, ha='center', fontsize=9, color=mlgray)

# Impact note
ax.text(7, 0.3, 'This paper is one of the most cited in all of computer science (100,000+ citations)',
        ha='center', fontsize=10, color=mlpurple, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

plt.tight_layout()
plt.savefig('rumelhart_hinton_williams.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('rumelhart_hinton_williams.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: rumelhart_hinton_williams.pdf")
