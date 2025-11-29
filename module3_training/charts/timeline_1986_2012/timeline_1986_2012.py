CHART_METADATA = {
    'title': 'Timeline 1986 2012',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/timeline_1986_2012'
}

import matplotlib.pyplot as plt
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(14, 5))
ax.set_xlim(1984, 2014)
ax.set_ylim(0, 10)
ax.axis('off')

# Timeline base
ax.axhline(y=5, color=mlgray, lw=3, alpha=0.5)

# Events
events = [
    (1986, 'Backpropagation\nRumelhart et al.', mlpurple, 7),
    (1989, 'LeNet\nLeCun', mlblue, 3),
    (1991, 'LSTM\nHochreiter', mlgreen, 7),
    (1995, 'SVM dominance\nbegins', mlgray, 3),
    (1998, 'LeNet-5\ndigit recognition', mlblue, 7),
    (2006, 'Deep Belief Nets\nHinton', mlpurple, 3),
    (2009, 'GPU training\nbreakthroughs', mlorange, 7),
    (2012, 'AlexNet\nImageNet victory', mlred, 3),
]

for year, label, color, y_pos in events:
    ax.plot(year, 5, 'o', color=color, markersize=15, zorder=5)
    ax.plot([year, year], [5, y_pos], '-', color=color, lw=2)
    ax.text(year, y_pos + (0.5 if y_pos > 5 else -0.5), label, ha='center',
            va='bottom' if y_pos > 5 else 'top', fontsize=9, color=color, fontweight='bold')

# Year labels
for year in range(1986, 2014, 2):
    ax.text(year, 4.3, str(year), ha='center', fontsize=8, color=mlgray)

# Period labels
ax.axvspan(1986, 1995, alpha=0.1, color=mlpurple)
ax.axvspan(1995, 2006, alpha=0.1, color=mlgray)
ax.axvspan(2006, 2014, alpha=0.1, color=mlgreen)

ax.text(1990.5, 9.5, 'Early Neural Networks', ha='center', fontsize=10, color=mlpurple)
ax.text(2000.5, 9.5, 'AI Winter / SVM Era', ha='center', fontsize=10, color=mlgray)
ax.text(2010, 9.5, 'Deep Learning Revival', ha='center', fontsize=10, color=mlgreen)

ax.set_title('Neural Network History: 1986-2012', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('timeline_1986_2012.pdf', bbox_inches='tight', dpi=300)
plt.savefig('timeline_1986_2012.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: timeline_1986_2012.pdf")
