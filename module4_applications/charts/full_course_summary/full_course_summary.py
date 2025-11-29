"""
Full Course Summary - Neural Networks: From Perceptron to Practice
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

CHART_METADATA = {
    'title': 'Full Course Summary',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/full_course_summary'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(8, 11.5, 'Neural Networks: From Perceptron to Practice',
        fontsize=20, fontweight='bold', ha='center', color=mlpurple)
ax.text(8, 10.8, 'Complete Course Summary',
        fontsize=14, ha='center', color=mlgray, style='italic')

# Four modules as connected boxes
modules = [
    (2, 7, 'MODULE 1', 'The Perceptron', mlblue, [
        'Biological inspiration',
        'Single layer classifier',
        'Linear decision boundaries',
        'Convergence theorem',
        'XOR problem limitation',
    ]),
    (6, 7, 'MODULE 2', 'Multi-Layer Perceptrons', mlorange, [
        'Hidden layers',
        'Activation functions',
        'Universal approximation',
        'Forward propagation',
        'Loss functions',
    ]),
    (10, 7, 'MODULE 3', 'Training NNs', mlpurple, [
        'Backpropagation',
        'Gradient descent',
        'Regularization',
        'Overfitting',
        'Hyperparameters',
    ]),
    (14, 7, 'MODULE 4', 'Applications', mlgreen, [
        'Finance applications',
        'Model selection',
        'Limitations',
        'Best practices',
        'Future directions',
    ]),
]

for x, y, title, subtitle, color, items in modules:
    box = FancyBboxPatch((x - 1.8, y - 2.5), 3.6, 4.5, boxstyle="round,pad=0.1",
                          facecolor=f'{color}11', edgecolor=color, linewidth=3)
    ax.add_patch(box)
    ax.text(x, y + 1.7, title, ha='center', fontsize=10, fontweight='bold', color=color)
    ax.text(x, y + 1.1, subtitle, ha='center', fontsize=9, color=mlgray)
    for i, item in enumerate(items):
        ax.text(x, y + 0.3 - i * 0.5, '- ' + item, ha='center', fontsize=7, color=mlgray)

# Arrows between modules
for x in [3.8, 7.8, 11.8]:
    ax.annotate('', xy=(x + 0.4, 7), xytext=(x - 0.4, 7),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=3))

# Historical timeline at bottom
ax.text(8, 3.5, 'Historical Journey: 1943 - Present', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

# Timeline
ax.plot([1, 15], [2.5, 2.5], color=mlgray, linewidth=3)

milestones = [
    (1.5, '1943', 'McCulloch-\nPitts', mlblue),
    (3.5, '1958', 'Perceptron', mlblue),
    (5.5, '1969', 'XOR\nProblem', mlred),
    (7.5, '1986', 'Backprop', mlgreen),
    (9.5, '2006', 'Deep\nBelief', mlorange),
    (11.5, '2012', 'AlexNet', mlgreen),
    (13.5, '2020s', 'Modern\nDL', mlpurple),
]

for x, year, label, color in milestones:
    ax.scatter([x], [2.5], c=color, s=100, zorder=5)
    ax.text(x, 3, year, ha='center', fontsize=8, fontweight='bold', color=color)
    ax.text(x, 1.8, label, ha='center', fontsize=7, color=mlgray)

# Key equations
ax.text(8, 0.8, 'Key Equations: $y = \\sigma(Wx + b)$  |  $L = -\\sum y \\log(\\hat{y})$  |  $w \\leftarrow w - \\eta \\nabla L$',
        ha='center', fontsize=10, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

plt.tight_layout()
plt.savefig('full_course_summary.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('full_course_summary.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: full_course_summary.pdf")
