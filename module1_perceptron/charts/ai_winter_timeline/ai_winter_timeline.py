"""
First AI Winter Timeline (1969-1982)
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

CHART_METADATA = {
    'title': 'AI Winter Timeline',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/ai_winter_timeline'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(1965, 1990)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(1977.5, 9.5, 'The First AI Winter (1969-1982)', fontsize=18, fontweight='bold',
        ha='center', color=mlred)

# Timeline base
ax.plot([1967, 1987], [5, 5], color=mlgray, linewidth=4, zorder=1)

# Year markers
for year in range(1968, 1988, 2):
    ax.plot([year, year], [4.8, 5.2], color=mlgray, linewidth=1)
    ax.text(year, 4.4, str(year), ha='center', fontsize=9, color=mlgray)

# "Interest/Funding" curve
years = np.linspace(1967, 1987, 100)
# High before 1969, crash, then slow recovery
interest = np.where(years < 1969,
                    8 - 0.1 * (years - 1967),
                    np.where(years < 1982,
                             2 + 0.5 * np.sin((years - 1969) * 0.3),
                             2 + 0.5 * (years - 1982)))

ax.fill_between(years, 5, 5 + (interest - 5) * 0.3, alpha=0.3, color=mlblue)
ax.plot(years, 5 + (interest - 5) * 0.3, color=mlblue, linewidth=2, label='Interest/Funding')

# Key events
events = [
    {'year': 1969, 'y': 7.5, 'text': '1969:\nMinsky-Papert\n"Perceptrons"', 'color': mlred},
    {'year': 1974, 'y': 3, 'text': '1974:\nWerbos thesis\n(ignored)', 'color': mlgray},
    {'year': 1982, 'y': 7.5, 'text': '1982:\nHopfield\nNetworks', 'color': mlgreen},
]

for event in events:
    # Vertical line
    y_end = event['y'] - 0.5 if event['y'] > 5 else event['y'] + 0.8
    ax.plot([event['year'], event['year']], [5, y_end], color=event['color'],
            linewidth=2, linestyle='--')

    # Event text
    va = 'bottom' if event['y'] > 5 else 'top'
    ax.text(event['year'], event['y'], event['text'], ha='center', va=va,
            fontsize=10, color=event['color'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=event['color'], alpha=0.9))

    # Dot
    ax.scatter([event['year']], [5], s=120, c=event['color'], zorder=5,
               edgecolors='white', linewidths=2)

# Consequences box
consequences = [
    "Consequences of the AI Winter:",
    "- Federal funding for neural networks nearly eliminated",
    "- Researchers left the field or went 'underground'",
    "- Symbolic AI (expert systems) became dominant",
    "- Key ideas survived but progress slowed dramatically"
]

consequence_text = '\n'.join(consequences)
ax.text(1977.5, 1.5, consequence_text, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE4E1', edgecolor=mlred, alpha=0.9))

# Era labels
ax.text(1968, 8.5, 'Golden Age', fontsize=11, color=mlgreen, fontweight='bold')
ax.annotate('', xy=(1968.5, 8.3), xytext=(1967, 8.3),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5))

ax.text(1975.5, 8.5, 'AI Winter', fontsize=11, color=mlred, fontweight='bold', ha='center')
ax.annotate('', xy=(1981, 8.3), xytext=(1970, 8.3),
            arrowprops=dict(arrowstyle='-', color=mlred, lw=1.5))

ax.text(1985, 8.5, 'Recovery', fontsize=11, color=mlgreen, fontweight='bold')
ax.annotate('', xy=(1987, 8.3), xytext=(1983, 8.3),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5))

plt.tight_layout()
plt.savefig('ai_winter_timeline.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('ai_winter_timeline.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: ai_winter_timeline.pdf")
