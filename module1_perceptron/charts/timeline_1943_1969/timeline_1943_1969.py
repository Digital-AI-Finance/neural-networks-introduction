"""
Historical Timeline 1943-1969
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Timeline 1943 1969',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/timeline_1943_1969'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'
mllavender = '#ADADE0'

# Set up figure
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(1940, 1975)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(1957.5, 9.5, 'Neural Networks: The Early Years (1943-1969)',
        fontsize=18, fontweight='bold', ha='center', color=mlpurple)

# Timeline base line
ax.plot([1942, 1972], [5, 5], color=mlpurple, linewidth=4, zorder=1)

# Year markers
years = [1943, 1949, 1957, 1958, 1960, 1969]
for year in years:
    ax.plot([year, year], [4.7, 5.3], color=mlpurple, linewidth=2)
    ax.text(year, 4.2, str(year), ha='center', fontsize=11, fontweight='bold')

# Events
events = [
    {
        'year': 1943, 'y': 7, 'color': mlblue,
        'title': 'McCulloch-Pitts',
        'subtitle': 'Mathematical Neuron Model',
        'desc': 'First mathematical model\nof neural computation'
    },
    {
        'year': 1949, 'y': 2.5, 'color': mlgreen,
        'title': 'Hebbian Learning',
        'subtitle': 'Donald Hebb',
        'desc': '"Neurons that fire\ntogether, wire together"'
    },
    {
        'year': 1957, 'y': 7.5, 'color': mlorange,
        'title': 'Perceptron',
        'subtitle': 'Frank Rosenblatt',
        'desc': 'First learning machine\n(Mark I Perceptron)'
    },
    {
        'year': 1958, 'y': 2, 'color': mlorange,
        'title': 'NYT Headline',
        'subtitle': 'Media Hype',
        'desc': '"Navy device learns\nby doing"'
    },
    {
        'year': 1960, 'y': 7, 'color': mlblue,
        'title': 'ADALINE',
        'subtitle': 'Widrow & Hoff',
        'desc': 'Delta rule\n(Gradient descent)'
    },
    {
        'year': 1969, 'y': 2.5, 'color': mlred,
        'title': 'Perceptrons Book',
        'subtitle': 'Minsky & Papert',
        'desc': 'Proved limitations\nAI Winter begins'
    }
]

for event in events:
    year = event['year']
    y = event['y']
    color = event['color']

    # Connection line
    if y > 5:
        ax.plot([year, year], [5.3, y - 0.8], color=color, linewidth=2, linestyle='--')
    else:
        ax.plot([year, year], [4.7, y + 1], color=color, linewidth=2, linestyle='--')

    # Event box
    box_width = 4.5
    box_height = 2 if y > 5 else 2
    box_x = year - box_width / 2
    box_y = y - 0.5 if y > 5 else y - 0.5

    box = FancyBboxPatch((box_x, box_y), box_width, box_height,
                          boxstyle="round,pad=0.05", facecolor='white',
                          edgecolor=color, linewidth=2)
    ax.add_patch(box)

    # Event text
    ax.text(year, y + 0.4, event['title'], ha='center', fontsize=11,
            fontweight='bold', color=color)
    ax.text(year, y, event['subtitle'], ha='center', fontsize=9,
            color=mlgray, style='italic')
    ax.text(year, y - 0.6, event['desc'], ha='center', fontsize=8,
            color='black')

    # Marker dot
    ax.scatter([year], [5], s=150, c=color, zorder=5, edgecolors='white', linewidths=2)

# Era labels
ax.text(1951, 8.8, 'Birth of\nCybernetics', fontsize=10, ha='center',
        color=mlgray, style='italic')
ax.text(1958.5, 8.8, 'The Golden\nAge', fontsize=10, ha='center',
        color=mlgray, style='italic')
ax.text(1969, 1, 'AI Winter\nBegins', fontsize=10, ha='center',
        color=mlred, fontweight='bold')

# Arrow showing progression
ax.annotate('', xy=(1971, 5), xytext=(1969.5, 5),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=2))
ax.text(1972, 5, '?', fontsize=16, ha='left', va='center', color=mlred, fontweight='bold')

# Bottom note
ax.text(1957.5, 0.5, 'From mathematical model to practical machine to fundamental limitations',
        fontsize=11, ha='center', style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('timeline_1943_1969.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('timeline_1943_1969.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: timeline_1943_1969.pdf")
