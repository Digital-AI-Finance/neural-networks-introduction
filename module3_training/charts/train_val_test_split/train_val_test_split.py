"""
Train/Validation/Test Split Visualization
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

CHART_METADATA = {
    'title': 'Train Val Test Split',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/train_val_test_split'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Data Splitting: Train / Validation / Test',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== DATA BAR ====================
# Full dataset
ax.text(0.5, 7.8, 'Full Dataset', fontsize=11, fontweight='bold', color=mlpurple)

# Training set (60%)
train_rect = Rectangle((0.5, 6.8), 7.8, 0.8,
                        facecolor=mlblue, edgecolor='white', linewidth=2, alpha=0.8)
ax.add_patch(train_rect)
ax.text(4.4, 7.2, 'Training Set (60-80%)', ha='center', va='center',
        fontsize=10, color='white', fontweight='bold')

# Validation set (20%)
val_rect = Rectangle((8.3, 6.8), 2.6, 0.8,
                      facecolor=mlorange, edgecolor='white', linewidth=2, alpha=0.8)
ax.add_patch(val_rect)
ax.text(9.6, 7.2, 'Validation\n(10-20%)', ha='center', va='center',
        fontsize=9, color='white', fontweight='bold')

# Test set (20%)
test_rect = Rectangle((10.9, 6.8), 2.6, 0.8,
                       facecolor=mlgreen, edgecolor='white', linewidth=2, alpha=0.8)
ax.add_patch(test_rect)
ax.text(12.2, 7.2, 'Test\n(10-20%)', ha='center', va='center',
        fontsize=9, color='white', fontweight='bold')

# ==================== PURPOSE BOXES ====================
purposes = [
    (4.4, 'Training Set', mlblue, [
        'Learn model parameters',
        'Update weights via backprop',
        'Used EVERY epoch',
    ]),
    (9.6, 'Validation Set', mlorange, [
        'Tune hyperparameters',
        'Early stopping decisions',
        'Model selection',
    ]),
    (12.2, 'Test Set', mlgreen, [
        'Final evaluation ONLY',
        'Never used during training',
        'Report this performance',
    ]),
]

for x, title, color, points in purposes:
    box = FancyBboxPatch((x - 1.8, 3.2), 3.6, 3,
                          boxstyle="round,pad=0.1", facecolor='white',
                          edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, 5.9, title, ha='center', fontsize=10, fontweight='bold', color=color)
    for i, point in enumerate(points):
        ax.text(x, 5.2 - i * 0.6, '- ' + point, ha='center', fontsize=8, color=mlgray)

# Arrows from bar to boxes
for x in [4.4, 9.6, 12.2]:
    ax.annotate('', xy=(x, 6.2), xytext=(x, 6.7),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))

# ==================== WORKFLOW ====================
ax.text(7, 2.5, 'Typical Workflow', fontsize=11, fontweight='bold', ha='center', color=mlpurple)

workflow = [
    '1. Split data BEFORE any preprocessing (prevent data leakage)',
    '2. Train on training set, evaluate on validation set',
    '3. Iterate: adjust hyperparameters based on validation performance',
    '4. Final model: evaluate ONCE on test set (report this!)',
]

for i, step in enumerate(workflow):
    ax.text(7, 1.8 - i * 0.5, step, ha='center', fontsize=9, color=mlgray)

# Warning
ax.text(7, -0.2, 'WARNING: Never optimize based on test set performance (data leakage)!',
        ha='center', fontsize=10, color='red', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE4E4', edgecolor='red'))

plt.tight_layout()
plt.savefig('train_val_test_split.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('train_val_test_split.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: train_val_test_split.pdf")
