"""
L1 vs L2 Regularization Comparison
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'L1 L2 Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/l1_l2_comparison'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

# ==================== LEFT: Constraint Regions ====================
ax = axes[0]

theta = np.linspace(0, 2 * np.pi, 200)

# L2: circle
r_l2 = 1
x_l2 = r_l2 * np.cos(theta)
y_l2 = r_l2 * np.sin(theta)
ax.plot(x_l2, y_l2, color=mlblue, linewidth=2, label='L2 (circle)')
ax.fill(x_l2, y_l2, color=mlblue, alpha=0.2)

# L1: diamond
x_l1 = [1, 0, -1, 0, 1]
y_l1 = [0, 1, 0, -1, 0]
ax.plot(x_l1, y_l1, color=mlorange, linewidth=2, label='L1 (diamond)')
ax.fill(x_l1, y_l1, color=mlorange, alpha=0.2)

# Loss contours (ellipses)
for i in range(1, 6):
    ellipse_x = 0.3 * i * np.cos(theta) + 0.8
    ellipse_y = 0.5 * i * np.sin(theta) + 0.6
    ax.plot(ellipse_x, ellipse_y, color=mlgray, linewidth=0.5, alpha=0.5)

# Optimal points
ax.scatter([0.71], [0.71], c=mlblue, s=100, zorder=5, marker='*')
ax.text(0.8, 0.85, 'L2 optimum', fontsize=8, color=mlblue)

ax.scatter([0], [1], c=mlorange, s=100, zorder=5, marker='*')
ax.text(0.1, 1.1, 'L1 optimum\n(sparse!)', fontsize=8, color=mlorange)

ax.axhline(y=0, color=mlgray, linewidth=0.5)
ax.axvline(x=0, color=mlgray, linewidth=0.5)

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('Constraint Regions', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=9)
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')

# ==================== MIDDLE: Weight Distribution ====================
ax = axes[1]

# Simulated weight distributions
np.random.seed(42)
weights_no_reg = np.random.randn(100)
weights_l2 = np.random.randn(100) * 0.5
weights_l1 = np.concatenate([np.zeros(60), np.random.randn(40) * 0.8])
np.random.shuffle(weights_l1)

bins = np.linspace(-3, 3, 30)

ax.hist(weights_no_reg, bins, alpha=0.5, color=mlgray, label='No reg', density=True)
ax.hist(weights_l2, bins, alpha=0.5, color=mlblue, label='L2', density=True)
ax.hist(weights_l1, bins, alpha=0.7, color=mlorange, label='L1', density=True)

ax.axvline(x=0, color='black', linewidth=1, linestyle='--')
ax.set_xlabel('Weight value', fontsize=11)
ax.set_ylabel('Density', fontsize=11)
ax.set_title('Weight Distributions', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(-3, 3)

ax.text(0, 1.5, 'L1 pushes weights\nto exactly 0', fontsize=9, ha='center', color=mlorange)

# ==================== RIGHT: Comparison Table ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'L1 vs L2 Regularization', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

# Table
headers = ['', 'L1 (Lasso)', 'L2 (Ridge)']
rows = [
    ['Penalty', '$\\lambda \\sum |w_i|$', '$\\lambda \\sum w_i^2$'],
    ['Effect', 'Sparse weights', 'Small weights'],
    ['Feature', 'Feature selection', 'All features used'],
    ['Geometry', 'Diamond', 'Circle'],
    ['Use case', 'Many irrelevant\nfeatures', 'All features\nmatter'],
]

# Draw table
col_x = [1, 4, 7.5]
row_y = 7.5

for j, h in enumerate(headers):
    ax.text(col_x[j], row_y, h, fontsize=10, fontweight='bold',
            color=[mlgray, mlorange, mlblue][j])

for i, row in enumerate(rows):
    y = row_y - (i + 1) * 1.2
    for j, cell in enumerate(row):
        color = mlgray if j == 0 else [mlorange, mlblue][j - 1]
        ax.text(col_x[j], y, cell, fontsize=9, color=color, va='center')

# Bottom note
ax.text(5, 0.5, 'Elastic Net combines both: $\\lambda_1 \\sum |w_i| + \\lambda_2 \\sum w_i^2$',
        ha='center', fontsize=9, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

fig.suptitle('L1 vs L2: Different Regularization Philosophies',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('l1_l2_comparison.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('l1_l2_comparison.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: l1_l2_comparison.pdf")
