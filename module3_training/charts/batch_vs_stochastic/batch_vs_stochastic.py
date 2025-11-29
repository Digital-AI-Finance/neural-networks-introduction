"""
Batch vs Stochastic Gradient Descent
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Batch Vs Stochastic',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/batch_vs_stochastic'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

np.random.seed(42)

# ==================== LEFT: Full Batch GD ====================
ax = axes[0]

# Contour plot
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

ax.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
ax.contourf(X, Y, Z, levels=15, cmap='Blues', alpha=0.3)

# Smooth path
path_x = [1.8]
path_y = [1.5]
for _ in range(15):
    path_x.append(path_x[-1] * 0.8)
    path_y.append(path_y[-1] * 0.8)

ax.plot(path_x, path_y, 'o-', color=mlblue, linewidth=2, markersize=4)
ax.scatter([0], [0], c=mlgreen, s=150, marker='*', zorder=10)

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('Full Batch GD', fontsize=12, fontweight='bold', color=mlblue)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.text(0, -1.7, 'Smooth but slow\n(uses ALL data)', fontsize=9, ha='center', color=mlblue)

# ==================== MIDDLE: Mini-Batch GD ====================
ax = axes[1]

ax.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
ax.contourf(X, Y, Z, levels=15, cmap='Oranges', alpha=0.3)

# Slightly noisy path
path_x = [1.8]
path_y = [1.5]
for _ in range(20):
    path_x.append(path_x[-1] * 0.85 + np.random.randn() * 0.1)
    path_y.append(path_y[-1] * 0.85 + np.random.randn() * 0.1)

ax.plot(path_x, path_y, 'o-', color=mlorange, linewidth=2, markersize=4)
ax.scatter([0], [0], c=mlgreen, s=150, marker='*', zorder=10)

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('Mini-Batch GD', fontsize=12, fontweight='bold', color=mlorange)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.text(0, -1.7, 'Best of both worlds\n(batch size 32-256)', fontsize=9, ha='center', color=mlorange)

# ==================== RIGHT: Stochastic GD ====================
ax = axes[2]

ax.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
ax.contourf(X, Y, Z, levels=15, cmap='Greens', alpha=0.3)

# Very noisy path
path_x = [1.8]
path_y = [1.5]
for _ in range(30):
    path_x.append(path_x[-1] * 0.9 + np.random.randn() * 0.25)
    path_y.append(path_y[-1] * 0.9 + np.random.randn() * 0.25)

ax.plot(path_x, path_y, 'o-', color=mlgreen, linewidth=1.5, markersize=3)
ax.scatter([0], [0], c='red', s=150, marker='*', zorder=10)

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('Stochastic GD', fontsize=12, fontweight='bold', color=mlgreen)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.text(0, -1.7, 'Noisy but fast\n(one sample at a time)', fontsize=9, ha='center', color=mlgreen)

# Summary table at bottom
fig.text(0.5, 0.02,
         'Full Batch: Stable gradients, slow updates  |  Mini-Batch: Good balance, standard choice  |  SGD: Fast updates, noisy gradients',
         ha='center', fontsize=9, color=mlpurple)

fig.suptitle('Gradient Descent Variants: Trading Off Speed vs Stability',
             fontsize=14, fontweight='bold', color=mlpurple, y=0.98)

plt.tight_layout(rect=[0, 0.06, 1, 0.95])
plt.savefig('batch_vs_stochastic.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('batch_vs_stochastic.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: batch_vs_stochastic.pdf")
