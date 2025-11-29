"""
When NOT to Use Neural Networks
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

CHART_METADATA = {
    'title': 'When Not To Use Nn',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/when_not_to_use_nn'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(7, 10.5, 'When NOT to Use Neural Networks',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Subtitle
ax.text(7, 9.8, '(Sometimes simpler is better)',
        fontsize=12, ha='center', color=mlgray, style='italic')

# Don't use when...
dont_use = [
    ('Small Dataset', 'N < 1000 samples\nNNs will overfit; use linear models, trees', mlred),
    ('Interpretability Required', 'Need to explain decisions\n(medical, legal, finance)', mlred),
    ('Tabular Data', 'Structured data with few features\nGradient boosting often wins', mlorange),
    ('Simple Relationships', 'Linear or nearly linear patterns\nLinear regression works fine', mlorange),
    ('Limited Compute', 'Edge devices, real-time constraints\nSimpler models are faster', mlorange),
    ('Domain Knowledge Exists', 'Physics, rules are known\nEncode them directly', mlblue),
]

y_pos = 8.5
for title, desc, color in dont_use:
    box = FancyBboxPatch((0.5, y_pos - 0.8), 6.5, 1.2, boxstyle="round,pad=0.05",
                          facecolor=f'{color}11', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(0.7, y_pos, title, fontsize=10, fontweight='bold', color=color, va='center')
    ax.text(3.5, y_pos - 0.4, desc, fontsize=8, color=mlgray, va='center', ha='left')
    y_pos -= 1.4

# DO use when...
ax.text(11, 8.8, 'DO Use NNs When:', fontsize=12, fontweight='bold', color=mlgreen)

do_use = [
    'Large dataset (N > 10,000)',
    'Complex patterns (images, text, audio)',
    'High-dimensional inputs',
    'State-of-the-art needed',
    'Ample compute available',
]

y_pos = 8
for item in do_use:
    ax.text(8, y_pos, '+ ' + item, fontsize=9, color=mlgray)
    y_pos -= 0.7

# Decision flowchart summary
summary_box = FancyBboxPatch((0.5, 0.3), 13, 1.5, boxstyle="round,pad=0.1",
                              facecolor='white', edgecolor=mlpurple, linewidth=2)
ax.add_patch(summary_box)

ax.text(7, 1.3, 'Decision Rule: Start simple, add complexity only when needed',
        ha='center', fontsize=11, fontweight='bold', color=mlpurple)
ax.text(7, 0.7, 'Linear Model  ->  Decision Trees/Boosting  ->  Neural Networks',
        ha='center', fontsize=10, color=mlgray)

# Alternatives box
alt_box = FancyBboxPatch((8, 2.5), 5.5, 4, boxstyle="round,pad=0.1",
                          facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(alt_box)

ax.text(10.75, 6, 'Strong Alternatives:', fontsize=10, fontweight='bold', color=mlgreen)
alternatives = [
    'XGBoost / LightGBM',
    'Random Forest',
    'Logistic/Linear Regression',
    'Support Vector Machines',
    'Bayesian methods',
]
y_pos = 5.3
for alt in alternatives:
    ax.text(8.3, y_pos, '- ' + alt, fontsize=9, color=mlgray)
    y_pos -= 0.6

plt.tight_layout()
plt.savefig('when_not_to_use_nn.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('when_not_to_use_nn.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: when_not_to_use_nn.pdf")
