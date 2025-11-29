"""
Complete Neural Networks Timeline 1943-2024
Module 4: From Theory to Practice
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'Full Timeline 1943 2024',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/full_timeline_1943_2024'
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
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(1940, 2030)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(1985, 11.5, 'Neural Networks: 80 Years of Progress (1943-2024)',
        fontsize=18, fontweight='bold', ha='center', color=mlpurple)

# Timeline base line
ax.plot([1942, 2026], [6, 6], color=mlpurple, linewidth=4, zorder=1)

# Era backgrounds
eras = [
    {'start': 1943, 'end': 1969, 'color': mlblue, 'label': 'Birth', 'y': 11},
    {'start': 1969, 'end': 1986, 'color': mlred, 'label': 'AI Winter 1', 'y': 11},
    {'start': 1986, 'end': 1998, 'color': mlgreen, 'label': 'Renaissance', 'y': 11},
    {'start': 1998, 'end': 2006, 'color': mlorange, 'label': 'AI Winter 2', 'y': 11},
    {'start': 2006, 'end': 2024, 'color': mlpurple, 'label': 'Deep Learning', 'y': 11}
]

for era in eras:
    ax.axvspan(era['start'], era['end'], ymin=0.5, ymax=0.58, alpha=0.3, color=era['color'])
    ax.text((era['start'] + era['end']) / 2, 6.5, era['label'], fontsize=9,
            ha='center', color=era['color'], fontweight='bold')

# Key events (smaller boxes due to density)
events = [
    {'year': 1943, 'y': 8, 'color': mlblue, 'text': 'McCulloch-Pitts'},
    {'year': 1949, 'y': 4, 'color': mlblue, 'text': 'Hebb'},
    {'year': 1958, 'y': 8.5, 'color': mlblue, 'text': 'Perceptron'},
    {'year': 1969, 'y': 3.5, 'color': mlred, 'text': 'Minsky-Papert'},
    {'year': 1982, 'y': 8, 'color': mlgreen, 'text': 'Hopfield'},
    {'year': 1986, 'y': 4, 'color': mlgreen, 'text': 'Backprop'},
    {'year': 1989, 'y': 8.5, 'color': mlgreen, 'text': 'LeNet'},
    {'year': 1997, 'y': 3.5, 'color': mlgreen, 'text': 'LSTM'},
    {'year': 2006, 'y': 8, 'color': mlpurple, 'text': 'DBN'},
    {'year': 2012, 'y': 9, 'color': mlpurple, 'text': 'AlexNet'},
    {'year': 2017, 'y': 3.5, 'color': mlpurple, 'text': 'Transformer'},
    {'year': 2020, 'y': 8.5, 'color': mlpurple, 'text': 'GPT-3'},
    {'year': 2023, 'y': 4, 'color': mlpurple, 'text': 'GPT-4/Claude'}
]

for event in events:
    # Vertical line
    y_end = event['y'] - 0.3 if event['y'] > 6 else event['y'] + 0.6
    ax.plot([event['year'], event['year']], [6, y_end], color=event['color'],
            linewidth=1, linestyle='--', alpha=0.7)

    # Dot on timeline
    ax.scatter([event['year']], [6], s=80, c=event['color'], zorder=5,
               edgecolors='white', linewidths=1)

    # Text label
    va = 'bottom' if event['y'] > 6 else 'top'
    ax.text(event['year'], event['y'], event['text'], fontsize=8, ha='center', va=va,
            color=event['color'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=event['color'], alpha=0.9))

# Year markers
for year in [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]:
    ax.plot([year, year], [5.7, 6.3], color=mlgray, linewidth=1)
    ax.text(year, 5.3, str(year), ha='center', fontsize=9, color=mlgray)

# Finance application timeline at bottom
finance_events = [
    {'year': 1980, 'text': 'Black-Scholes\n(1973)'},
    {'year': 1995, 'text': 'Early NN\nTrading'},
    {'year': 2010, 'text': 'HFT\nExpansion'},
    {'year': 2020, 'text': 'AI Hedge\nFunds'}
]

ax.text(1985, 1.5, 'Finance Applications:', fontsize=10, fontweight='bold', color=mlorange)
for fe in finance_events:
    ax.text(fe['year'], 0.8, fe['text'], fontsize=8, ha='center', color=mlorange)
    ax.scatter([fe['year']], [1.3], s=50, c=mlorange, marker='s')

ax.plot([1975, 2025], [1.3, 1.3], color=mlorange, linewidth=2, alpha=0.5)

# Key insights
insights_text = """Key Patterns:
1. Two "AI Winters" followed hype cycles
2. Compute and data enabled breakthroughs
3. Each era built on previous foundations
4. Finance adoption lagged research by 5-10 years"""

ax.text(0.02, 0.02, insights_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

plt.tight_layout()
plt.savefig('full_timeline_1943_2024.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('full_timeline_1943_2024.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: full_timeline_1943_2024.pdf")
