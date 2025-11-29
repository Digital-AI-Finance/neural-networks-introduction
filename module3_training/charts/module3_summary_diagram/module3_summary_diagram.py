"""
Module 3 Summary Diagram - Training Neural Networks
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

CHART_METADATA = {
    'title': 'Module3 Summary Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/module3_summary_diagram'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.5, 'Module 3 Summary: Training Neural Networks',
        fontsize=18, fontweight='bold', ha='center', color=mlpurple)

# ==================== CENTRAL TRAINING LOOP ====================
center_box = FancyBboxPatch((5.5, 5.5), 3, 1.5, boxstyle="round,pad=0.1",
                             facecolor='#E6E6FA', edgecolor=mlpurple, linewidth=3)
ax.add_patch(center_box)
ax.text(7, 6.5, 'TRAINING LOOP', ha='center', va='center',
        fontsize=12, fontweight='bold', color=mlpurple)
ax.text(7, 5.9, 'Forward + Backward + Update', ha='center', va='center',
        fontsize=9, color=mlgray)

# ==================== SURROUNDING CONCEPTS ====================
concepts = [
    # (x, y, title, items, color)
    (2, 9.5, 'BACKPROPAGATION', ['Chain rule', 'Gradient flow', 'Computational graph'], mlblue),
    (7, 9.5, 'GRADIENT DESCENT', ['SGD, Mini-batch', 'Momentum', 'Adam optimizer'], mlorange),
    (12, 9.5, 'LOSS FUNCTIONS', ['MSE (regression)', 'Cross-entropy', 'Custom losses'], mlgreen),
    (2, 3, 'INITIALIZATION', ['Xavier/Glorot', 'He initialization', 'Avoid vanishing grad'], mlblue),
    (7, 1, 'REGULARIZATION', ['L1/L2 penalty', 'Dropout', 'Early stopping'], mlred),
    (12, 3, 'HYPERPARAMETERS', ['Learning rate', 'Batch size', 'Architecture'], mlorange),
]

for x, y, title, items, color in concepts:
    box = FancyBboxPatch((x - 1.8, y - 1.2), 3.6, 2.2, boxstyle="round,pad=0.1",
                          facecolor=f'{color}22', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.7, title, ha='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y + 0.1 - i * 0.4, '- ' + item, ha='center', fontsize=8, color=mlgray)

# ==================== ARROWS TO CENTER ====================
arrow_positions = [
    (2, 8, 4, 6.5),
    (7, 8, 7, 7.2),
    (12, 8, 10, 6.5),
    (2, 4, 4, 6),
    (7, 2.3, 7, 5.3),
    (12, 4, 10, 6),
]

for x1, y1, x2, y2 in arrow_positions:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5, alpha=0.5))

# ==================== KEY TAKEAWAYS ====================
takeaways_box = FancyBboxPatch((0.5, -0.5), 13, 1.5, boxstyle="round,pad=0.1",
                                facecolor='white', edgecolor=mlpurple, linewidth=2)
ax.add_patch(takeaways_box)

ax.text(7, 0.7, 'Key Takeaways', ha='center', fontsize=11, fontweight='bold', color=mlpurple)
takeaways = ('1. Backprop = Chain rule applied systematically  |  '
             '2. Learning rate is the most critical hyperparameter  |  '
             '3. Regularization prevents overfitting')
ax.text(7, 0.1, takeaways, ha='center', fontsize=9, color=mlgray)

plt.tight_layout()
plt.savefig('module3_summary_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('module3_summary_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: module3_summary_diagram.pdf")
