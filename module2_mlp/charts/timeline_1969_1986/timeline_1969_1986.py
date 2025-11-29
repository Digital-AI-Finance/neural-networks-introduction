"""
Timeline 1969-1986: The First AI Winter and MLP Revival
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

CHART_METADATA = {
    'title': 'Timeline 1969 1986',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/timeline_1969_1986'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(1968, 1988)
ax.set_ylim(0, 10)

# Title
ax.text(1978, 9.5, 'From Darkness to Light: 1969-1986',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Timeline base
ax.axhline(y=5, color=mlgray, linewidth=3, alpha=0.5)

# Events
events = [
    (1969, 'Minsky-Papert\n"Perceptrons"', mlred, 7,
     'Proved perceptrons cannot\nsolve XOR problem'),
    (1970, 'Funding Collapse', mlred, 3,
     'DARPA cuts\nAI funding'),
    (1974, 'Werbos\nBackprop (thesis)', mlblue, 7,
     'First backpropagation\n(largely ignored)'),
    (1979, 'Neocognitron\n(Fukushima)', mlblue, 3,
     'Early convolutional\narchitecture'),
    (1982, 'Hopfield\nNetworks', mlorange, 7,
     'Recurrent networks\nrevive interest'),
    (1985, 'Boltzmann\nMachines', mlorange, 3,
     'Hinton & Sejnowski\nenergy-based learning'),
    (1986, 'Backprop Paper\nRumelhart et al.', mlgreen, 7,
     'Nature paper revives\nneural networks!'),
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
    desc_y = y + 1.2 if y > 5 else y - 1.2
    ax.text(year, desc_y, desc, ha='center',
            va='bottom' if y > 5 else 'top',
            fontsize=8, color=mlgray)

# Era labels
ax.fill_between([1969, 1982], 0, 1, alpha=0.2, color=mlred)
ax.text(1975.5, 0.5, 'First AI Winter (1969-1982)', ha='center', fontsize=10, color=mlred)

ax.fill_between([1982, 1988], 0, 1, alpha=0.2, color=mlgreen)
ax.text(1985, 0.5, 'Revival Era', ha='center', fontsize=10, color=mlgreen)

# Year markers
for year in range(1970, 1988, 2):
    ax.text(year, 4.7, str(year), ha='center', fontsize=8, color=mlgray)

# Key insight box
insight_text = """Key Turning Point (1986):
Rumelhart, Hinton & Williams published "Learning representations
by back-propagating errors" in Nature. This paper:
- Made backpropagation accessible and practical
- Showed MLPs could learn internal representations
- Launched the connectionist movement
- Led to modern deep learning"""

ax.text(1978, 1.8, insight_text, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlgreen, linewidth=2))

ax.axis('off')

plt.tight_layout()
plt.savefig('timeline_1969_1986.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('timeline_1969_1986.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: timeline_1969_1986.pdf")
