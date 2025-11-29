"""
Module 1 Summary Concept Map
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

CHART_METADATA = {
    'title': 'Module1 Summary Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/module1_summary_diagram'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Module 1 Summary: The Birth of Neural Computing',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Central concept: Perceptron
perceptron_box = FancyBboxPatch((5, 4.5), 4, 1.5, boxstyle="round,pad=0.1",
                                  facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=3)
ax.add_patch(perceptron_box)
ax.text(7, 5.25, 'PERCEPTRON', ha='center', va='center', fontsize=14, fontweight='bold', color=mlpurple)
ax.text(7, 4.85, '$y = f(\\sum w_i x_i + b)$', ha='center', va='center', fontsize=10, color=mlgray)

# Four corners: Key concepts
concepts = [
    {'pos': (1.5, 7.5), 'title': 'Biological\nInspiration', 'desc': 'McCulloch-Pitts\n(1943)', 'color': mlblue},
    {'pos': (12.5, 7.5), 'title': 'Mathematical\nModel', 'desc': 'Weighted sum +\nthreshold', 'color': mlblue},
    {'pos': (1.5, 2), 'title': 'Learning\nAlgorithm', 'desc': 'Update weights\non errors', 'color': mlgreen},
    {'pos': (12.5, 2), 'title': 'Limitations', 'desc': 'XOR problem\nNot universal', 'color': mlred}
]

for concept in concepts:
    x, y = concept['pos']
    box = FancyBboxPatch((x - 1.2, y - 0.9), 2.4, 1.8, boxstyle="round,pad=0.1",
                          facecolor='white', edgecolor=concept['color'], linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.3, concept['title'], ha='center', va='center',
            fontsize=11, fontweight='bold', color=concept['color'])
    ax.text(x, y - 0.3, concept['desc'], ha='center', va='center',
            fontsize=9, color=mlgray)

# Arrows from corners to center
arrow_params = dict(arrowstyle='->', color=mlgray, lw=1.5, connectionstyle="arc3,rad=0.2")

ax.annotate('', xy=(5, 5.5), xytext=(2.7, 7), arrowprops=arrow_params)
ax.annotate('', xy=(9, 5.5), xytext=(11.3, 7), arrowprops=arrow_params)
ax.annotate('', xy=(5, 5), xytext=(2.7, 2.5), arrowprops=arrow_params)
ax.annotate('', xy=(9, 5), xytext=(11.3, 2.5), arrowprops=arrow_params)

# Timeline at bottom
ax.plot([1, 13], [0.8, 0.8], color=mlpurple, linewidth=2)
timeline_events = [
    (1.5, '1943\nMcCulloch-Pitts'),
    (4, '1949\nHebb'),
    (6.5, '1958\nPerceptron'),
    (9, '1969\nMinsky-Papert'),
    (11.5, 'AI Winter\nbegins')
]

for x, label in timeline_events:
    ax.scatter([x], [0.8], s=80, c=mlpurple, zorder=5)
    ax.text(x, 0.2, label, ha='center', fontsize=8, color=mlgray)

# Key takeaways
takeaways = [
    "Key Takeaways:",
    "1. Single perceptron = linear classifier",
    "2. Can learn linearly separable patterns",
    "3. Cannot solve XOR (need multiple layers)",
    "4. Foundation for all neural networks"
]

takeaway_text = '\n'.join(takeaways)
ax.text(7, 3, takeaway_text, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0F0F0', edgecolor=mlgray, alpha=0.9))

# Finance connection
ax.text(7, 1.8, 'Finance Application: Simple stock screening (buy/sell based on single threshold)',
        ha='center', fontsize=9, style='italic', color=mlorange)

plt.tight_layout()
plt.savefig('module1_summary_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('module1_summary_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: module1_summary_diagram.pdf")
