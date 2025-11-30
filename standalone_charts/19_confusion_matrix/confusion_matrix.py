# ==============================================================================
# Chart: Confusion Matrix
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/19_confusion_matrix/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Confusion Matrix

Classification performance metrics visualization

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/19_confusion_matrix/
"""

CHART_METADATA = {
    'name': 'Confusion Matrix',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/19_confusion_matrix',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Classification performance metrics visualization'
}

"""
Chart 19: Confusion Matrix
2x2 matrix showing precision/recall trade-off for trading decisions.
"""

import numpy as np
import matplotlib.pyplot as plt

# Colors
mlpurple = '#3333b2'
mlblue = '#0066cc'
mlgreen = '#2ca02c'
mlorange = '#ff7f0e'
mlred = '#d62728'
mlgray = '#7f7f7f'

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel 1: Confusion Matrix
ax1 = axes[0]

# Matrix values (realistic for 70% accuracy)
# Actual: 50 up days, 50 down days
# Predicted correctly: ~70% each
tp = 36  # True Positive: Predicted UP, Actual UP
fn = 14  # False Negative: Predicted DOWN, Actual UP
fp = 16  # False Positive: Predicted UP, Actual DOWN
tn = 34  # True Negative: Predicted DOWN, Actual DOWN

matrix = np.array([[tp, fn], [fp, tn]])

# Create confusion matrix visualization
im = ax1.imshow([[0, 0], [0, 0]], cmap='Blues', alpha=0)

# Draw cells manually with colors
# True Positive (good)
ax1.add_patch(plt.Rectangle((-.5, -.5), 1, 1, fill=True, facecolor=mlgreen, alpha=0.3))
# True Negative (good)
ax1.add_patch(plt.Rectangle((.5, .5), 1, 1, fill=True, facecolor=mlgreen, alpha=0.3))
# False Positive (bad)
ax1.add_patch(plt.Rectangle((-.5, .5), 1, 1, fill=True, facecolor=mlred, alpha=0.2))
# False Negative (bad)
ax1.add_patch(plt.Rectangle((.5, -.5), 1, 1, fill=True, facecolor=mlorange, alpha=0.2))

# Add values
ax1.text(0, 0, f'{tp}', fontsize=28, ha='center', va='center', fontweight='bold', color=mlgreen)
ax1.text(1, 0, f'{fn}', fontsize=28, ha='center', va='center', fontweight='bold', color=mlorange)
ax1.text(0, 1, f'{fp}', fontsize=28, ha='center', va='center', fontweight='bold', color=mlred)
ax1.text(1, 1, f'{tn}', fontsize=28, ha='center', va='center', fontweight='bold', color=mlgreen)

# Add labels
ax1.text(0, -0.35, 'True\nPositive', fontsize=9, ha='center', va='center', color=mlgreen)
ax1.text(1, -0.35, 'False\nNegative', fontsize=9, ha='center', va='center', color=mlorange)
ax1.text(0, 1.35, 'False\nPositive', fontsize=9, ha='center', va='center', color=mlred)
ax1.text(1, 1.35, 'True\nNegative', fontsize=9, ha='center', va='center', color=mlgreen)

ax1.set_xticks([0, 1])
ax1.set_yticks([0, 1])
ax1.set_xticklabels(['Predicted\nUP', 'Predicted\nDOWN'], fontsize=10)
ax1.set_yticklabels(['Actual\nUP', 'Actual\nDOWN'], fontsize=10)
ax1.set_xlim(-0.5, 1.5)
ax1.set_ylim(-0.5, 1.5)
ax1.set_title('Trading Confusion Matrix\n(100 test days)', fontsize=12, fontweight='bold')

# Add grid
for i in range(2):
    ax1.axhline(y=i-0.5, color=mlgray, linewidth=2)
    ax1.axvline(x=i-0.5, color=mlgray, linewidth=2)
ax1.axhline(y=1.5, color=mlgray, linewidth=2)
ax1.axvline(x=1.5, color=mlgray, linewidth=2)

# Panel 2: Metrics breakdown
ax2 = axes[1]
ax2.axis('off')

# Calculate metrics
accuracy = (tp + tn) / (tp + tn + fp + fn) * 100
precision = tp / (tp + fp) * 100
recall = tp / (tp + fn) * 100
f1 = 2 * (precision * recall) / (precision + recall) / 100

# Metrics boxes
y_pos = 0.85
box_height = 0.18

# Accuracy
ax2.add_patch(plt.Rectangle((0.05, y_pos), 0.4, box_height, fill=True,
              facecolor=mlblue, alpha=0.2, edgecolor=mlblue, linewidth=2))
ax2.text(0.25, y_pos + 0.12, 'ACCURACY', fontsize=11, ha='center', fontweight='bold', color=mlblue)
ax2.text(0.25, y_pos + 0.04, f'{accuracy:.0f}%', fontsize=18, ha='center', fontweight='bold', color=mlblue)

# Precision
ax2.add_patch(plt.Rectangle((0.55, y_pos), 0.4, box_height, fill=True,
              facecolor=mlpurple, alpha=0.2, edgecolor=mlpurple, linewidth=2))
ax2.text(0.75, y_pos + 0.12, 'PRECISION', fontsize=11, ha='center', fontweight='bold', color=mlpurple)
ax2.text(0.75, y_pos + 0.04, f'{precision:.0f}%', fontsize=18, ha='center', fontweight='bold', color=mlpurple)

y_pos = 0.58
# Recall
ax2.add_patch(plt.Rectangle((0.05, y_pos), 0.4, box_height, fill=True,
              facecolor=mlorange, alpha=0.2, edgecolor=mlorange, linewidth=2))
ax2.text(0.25, y_pos + 0.12, 'RECALL', fontsize=11, ha='center', fontweight='bold', color=mlorange)
ax2.text(0.25, y_pos + 0.04, f'{recall:.0f}%', fontsize=18, ha='center', fontweight='bold', color=mlorange)

# F1
ax2.add_patch(plt.Rectangle((0.55, y_pos), 0.4, box_height, fill=True,
              facecolor=mlgreen, alpha=0.2, edgecolor=mlgreen, linewidth=2))
ax2.text(0.75, y_pos + 0.12, 'F1 SCORE', fontsize=11, ha='center', fontweight='bold', color=mlgreen)
ax2.text(0.75, y_pos + 0.04, f'{f1:.2f}', fontsize=18, ha='center', fontweight='bold', color=mlgreen)

# Explanations
explanations = [
    ('Accuracy:', 'Overall correct predictions', f'{tp+tn}/{tp+tn+fp+fn}'),
    ('Precision:', 'When we say BUY, how often right?', f'{tp}/{tp+fp}'),
    ('Recall:', 'Of all UP days, how many caught?', f'{tp}/{tp+fn}'),
    ('F1 Score:', 'Balance of precision & recall', 'harmonic mean'),
]

y_start = 0.45
for i, (metric, desc, formula) in enumerate(explanations):
    ax2.text(0.05, y_start - i*0.1, metric, fontsize=10, fontweight='bold', color=mlgray)
    ax2.text(0.25, y_start - i*0.1, desc, fontsize=9, color=mlgray)
    ax2.text(0.85, y_start - i*0.1, formula, fontsize=9, color=mlpurple, ha='right')

# Business insight
ax2.text(0.5, 0.02, 'Trading Insight: 69% precision means ~1/3 of BUY signals are wrong!',
        fontsize=10, ha='center', fontweight='bold', color=mlred,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlred, alpha=0.8))

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_title('Performance Metrics Explained', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('confusion_matrix.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 19_confusion_matrix/confusion_matrix.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/19_confusion_matrix/
