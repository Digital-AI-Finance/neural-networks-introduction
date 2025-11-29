CHART_METADATA = {
    'title': 'L1 Vs L2',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/l1_vs_l2'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))

# L1 constraint region
ax1 = axes[0]
t = np.linspace(0, 2*np.pi, 100)
# Diamond shape for L1
l1_x = np.concatenate([np.linspace(0, 1, 25), np.linspace(1, 0, 25), np.linspace(0, -1, 25), np.linspace(-1, 0, 25)])
l1_y = np.concatenate([np.linspace(1, 0, 25), np.linspace(0, -1, 25), np.linspace(-1, 0, 25), np.linspace(0, 1, 25)])
ax1.fill(l1_x, l1_y, alpha=0.3, color=mlblue)
ax1.plot(l1_x, l1_y, color=mlblue, lw=2)
# Loss contours
for r in [0.5, 1.0, 1.5, 2.0]:
    circle = plt.Circle((1.5, 1.5), r, fill=False, color=mlgray, linestyle='--', alpha=0.5)
    ax1.add_patch(circle)
ax1.plot(0, 1, 'ro', markersize=12)
ax1.annotate('Solution\n(sparse)', xy=(0, 1), xytext=(0.5, 1.8), fontsize=9, color=mlred,
            arrowprops=dict(arrowstyle='->', color=mlred))
ax1.set_xlim(-2, 2.5)
ax1.set_ylim(-2, 2.5)
ax1.set_aspect('equal')
ax1.set_title('L1 (Lasso): $|w_1| + |w_2| \\leq c$', fontsize=11, fontweight='bold')
ax1.set_xlabel('$w_1$')
ax1.set_ylabel('$w_2$')
ax1.axhline(y=0, color='k', lw=0.5)
ax1.axvline(x=0, color='k', lw=0.5)

# L2 constraint region
ax2 = axes[1]
circle_l2 = plt.Circle((0, 0), 1, fill=True, alpha=0.3, color=mlgreen)
ax2.add_patch(circle_l2)
circle_l2_border = plt.Circle((0, 0), 1, fill=False, color=mlgreen, lw=2)
ax2.add_patch(circle_l2_border)
for r in [0.5, 1.0, 1.5, 2.0]:
    circle = plt.Circle((1.5, 1.5), r, fill=False, color=mlgray, linestyle='--', alpha=0.5)
    ax2.add_patch(circle)
ax2.plot(0.5, 0.866, 'go', markersize=12)
ax2.annotate('Solution\n(small)', xy=(0.5, 0.866), xytext=(1.2, 1.8), fontsize=9, color=mlgreen,
            arrowprops=dict(arrowstyle='->', color=mlgreen))
ax2.set_xlim(-2, 2.5)
ax2.set_ylim(-2, 2.5)
ax2.set_aspect('equal')
ax2.set_title('L2 (Ridge): $w_1^2 + w_2^2 \\leq c$', fontsize=11, fontweight='bold')
ax2.set_xlabel('$w_1$')
ax2.axhline(y=0, color='k', lw=0.5)
ax2.axvline(x=0, color='k', lw=0.5)

# Comparison
ax3 = axes[2]
ax3.axis('off')
comparison = [
    ('Property', 'L1 (Lasso)', 'L2 (Ridge)'),
    ('Constraint', 'Diamond', 'Circle'),
    ('Sparsity', 'Yes (zeros)', 'No'),
    ('Feature Selection', 'Automatic', 'No'),
    ('Correlated Features', 'Picks one', 'Shrinks all'),
    ('Computational', 'Harder', 'Easier'),
]
y_pos = 0.9
for row in comparison:
    for i, (text, color) in enumerate(zip(row, [mlgray, mlblue, mlgreen])):
        weight = 'bold' if y_pos > 0.85 else 'normal'
        ax3.text(0.1 + i*0.35, y_pos, text, fontsize=10, color=color, fontweight=weight)
    y_pos -= 0.12

ax3.set_title('L1 vs L2 Comparison', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('l1_vs_l2.pdf', bbox_inches='tight', dpi=300)
plt.savefig('l1_vs_l2.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: l1_vs_l2.pdf")
