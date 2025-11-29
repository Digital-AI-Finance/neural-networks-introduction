"""
Walk-Forward Validation for Time Series
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch

CHART_METADATA = {
    'title': 'Finance Walk Forward Validation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_walk_forward_validation'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# ==================== TOP: Standard (Wrong) Cross-Validation ====================
ax = axes[0]
ax.set_xlim(0, 14)
ax.set_ylim(0, 5)
ax.axis('off')

ax.text(7, 4.5, 'Standard K-Fold Cross-Validation (WRONG for Time Series!)',
        fontsize=12, fontweight='bold', ha='center', color='red')

# Time axis
ax.annotate('', xy=(12.5, 2.5), xytext=(1.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.text(13, 2.5, 'Time', fontsize=10, color=mlgray, va='center')

# Folds with random splits
fold_data = [
    [(0.2, mlblue), (0.2, mlorange), (0.2, mlblue), (0.2, mlblue), (0.2, mlorange)],
    [(0.2, mlorange), (0.2, mlblue), (0.2, mlorange), (0.2, mlblue), (0.2, mlblue)],
]

for fold_idx, fold in enumerate(fold_data):
    y = 3.2 - fold_idx * 0.8
    x = 2
    ax.text(1.3, y + 0.15, f'Fold {fold_idx + 1}', fontsize=8, color=mlgray, va='center')
    for width, color in fold:
        rect = Rectangle((x, y), width * 10, 0.5,
                         facecolor=color, alpha=0.7, edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        x += width * 10

# Legend
ax.text(2, 1.5, 'Train', fontsize=9, color=mlblue)
ax.add_patch(Rectangle((2.8, 1.4), 0.3, 0.3, facecolor=mlblue, alpha=0.7))
ax.text(4, 1.5, 'Test', fontsize=9, color=mlorange)
ax.add_patch(Rectangle((4.7, 1.4), 0.3, 0.3, facecolor=mlorange, alpha=0.7))

ax.text(7, 0.8, 'Problem: Test data can appear BEFORE training data (data leakage!)',
        fontsize=10, ha='center', color='red')

# ==================== BOTTOM: Walk-Forward Validation ====================
ax = axes[1]
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(7, 5.5, 'Walk-Forward Validation (CORRECT for Time Series)',
        fontsize=12, fontweight='bold', ha='center', color=mlgreen)

# Time axis
ax.annotate('', xy=(12.5, 3), xytext=(1.5, 3),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.text(13, 3, 'Time', fontsize=10, color=mlgray, va='center')

# Walk-forward folds
folds = [
    (2, 4, 4, 6),  # train_start, train_end, test_start, test_end
    (2, 6, 6, 8),
    (2, 8, 8, 10),
    (2, 10, 10, 12),
]

for fold_idx, (ts, te, vs, ve) in enumerate(folds):
    y = 4.3 - fold_idx * 0.7
    ax.text(1.3, y + 0.15, f'Fold {fold_idx + 1}', fontsize=8, color=mlgray, va='center')

    # Training portion
    rect = Rectangle((ts, y), te - ts, 0.4,
                     facecolor=mlblue, alpha=0.7, edgecolor='white', linewidth=1)
    ax.add_patch(rect)

    # Test portion
    rect = Rectangle((vs, y), ve - vs, 0.4,
                     facecolor=mlorange, alpha=0.7, edgecolor='white', linewidth=1)
    ax.add_patch(rect)

# Legend
ax.text(2, 1.3, 'Train', fontsize=9, color=mlblue)
ax.add_patch(Rectangle((2.8, 1.2), 0.3, 0.3, facecolor=mlblue, alpha=0.7))
ax.text(4, 1.3, 'Test', fontsize=9, color=mlorange)
ax.add_patch(Rectangle((4.7, 1.2), 0.3, 0.3, facecolor=mlorange, alpha=0.7))

ax.text(7, 0.6, 'Key: Training data ALWAYS comes before test data (respects time order)',
        fontsize=10, ha='center', color=mlgreen)

fig.suptitle('Time Series Validation: Respecting Temporal Order',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('finance_walk_forward_validation.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_walk_forward_validation.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_walk_forward_validation.pdf")
