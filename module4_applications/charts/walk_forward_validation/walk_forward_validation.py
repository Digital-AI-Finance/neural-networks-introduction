CHART_METADATA = {
    'title': 'Walk Forward Validation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/walk_forward_validation'
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

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

ax.text(6, 7.5, 'Walk-Forward Validation for Time Series', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

# Time axis
ax.axhline(y=1, xmin=0.05, xmax=0.95, color=mlgray, lw=2)
ax.text(6, 0.3, 'Time', ha='center', fontsize=11)

# Folds
folds = [
    (1, 3, 4, 'Fold 1'),  # train_start, train_end, test_end, label
    (1, 4, 5, 'Fold 2'),
    (1, 5, 6, 'Fold 3'),
    (1, 6, 7, 'Fold 4'),
    (1, 7, 8, 'Fold 5'),
]

y_positions = [6, 5.2, 4.4, 3.6, 2.8]

for (train_start, train_end, test_end, label), y in zip(folds, y_positions):
    # Training set
    ax.add_patch(plt.Rectangle((train_start, y-0.25), train_end-train_start, 0.5,
                                facecolor=mlblue, alpha=0.7))
    # Validation/test set
    ax.add_patch(plt.Rectangle((train_end, y-0.25), test_end-train_end, 0.5,
                                facecolor=mlorange, alpha=0.7))
    # Label
    ax.text(0.5, y, label, ha='center', va='center', fontsize=9)

# Legend
ax.add_patch(plt.Rectangle((9, 5.5), 0.8, 0.4, facecolor=mlblue, alpha=0.7))
ax.text(10, 5.7, 'Training', fontsize=10, va='center')
ax.add_patch(plt.Rectangle((9, 4.8), 0.8, 0.4, facecolor=mlorange, alpha=0.7))
ax.text(10, 5.0, 'Test', fontsize=10, va='center')

# Key insight
ax.text(6, 1.8, 'Training window grows, test window moves forward', ha='center', fontsize=11, color=mlgreen)
ax.text(6, 1.3, 'No future data leaks into training', ha='center', fontsize=10, color=mlgray)

plt.tight_layout()
plt.savefig('walk_forward_validation.pdf', bbox_inches='tight', dpi=300)
plt.savefig('walk_forward_validation.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: walk_forward_validation.pdf")
