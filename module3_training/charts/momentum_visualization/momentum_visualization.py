"""
Momentum Optimization Visualization
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Momentum Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/momentum_visualization'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

np.random.seed(42)

# Create elongated loss surface
x = np.linspace(-3, 3, 100)
y = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(x, y)
Z = 0.5 * X**2 + 5 * Y**2  # Elongated valley

# ==================== LEFT: Without Momentum ====================
ax = axes[0]

ax.contour(X, Y, Z, levels=20, colors=mlgray, alpha=0.5)
ax.contourf(X, Y, Z, levels=20, cmap='Blues', alpha=0.3)

# Path without momentum (oscillates in narrow dimension)
path_x = [-2.5]
path_y = [1.2]
lr = 0.15
for _ in range(30):
    grad_x = path_x[-1]
    grad_y = 10 * path_y[-1]
    path_x.append(path_x[-1] - lr * grad_x)
    path_y.append(path_y[-1] - lr * grad_y)

ax.plot(path_x, path_y, 'o-', color=mlblue, linewidth=2, markersize=4, label='GD path')
ax.scatter([0], [0], c=mlgreen, s=200, marker='*', zorder=10, label='Minimum')

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('Without Momentum', fontsize=12, fontweight='bold', color=mlblue)
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(-3, 3)
ax.set_ylim(-1.5, 1.5)

ax.text(0, -1.3, 'Oscillates in steep direction\nSlow progress in flat direction',
        fontsize=9, ha='center', color=mlblue)

# ==================== RIGHT: With Momentum ====================
ax = axes[1]

ax.contour(X, Y, Z, levels=20, colors=mlgray, alpha=0.5)
ax.contourf(X, Y, Z, levels=20, cmap='Oranges', alpha=0.3)

# Path with momentum (smoother, faster)
path_x = [-2.5]
path_y = [1.2]
vel_x, vel_y = 0, 0
lr = 0.15
momentum = 0.9
for _ in range(20):
    grad_x = path_x[-1]
    grad_y = 10 * path_y[-1]
    vel_x = momentum * vel_x - lr * grad_x
    vel_y = momentum * vel_y - lr * grad_y
    path_x.append(path_x[-1] + vel_x)
    path_y.append(path_y[-1] + vel_y)

ax.plot(path_x, path_y, 'o-', color=mlorange, linewidth=2, markersize=4, label='Momentum path')
ax.scatter([0], [0], c=mlgreen, s=200, marker='*', zorder=10, label='Minimum')

ax.set_xlabel('$w_1$', fontsize=11)
ax.set_ylabel('$w_2$', fontsize=11)
ax.set_title('With Momentum ($\\beta = 0.9$)', fontsize=12, fontweight='bold', color=mlorange)
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(-3, 3)
ax.set_ylim(-1.5, 1.5)

ax.text(0, -1.3, 'Dampens oscillations\nAccelerates in consistent direction',
        fontsize=9, ha='center', color=mlorange)

# Physics analogy and formula
fig.text(0.5, 0.02,
         'Momentum Update: $v_t = \\beta v_{t-1} + \\eta \\nabla L$,  $w_t = w_{t-1} - v_t$  '
         '(Like a ball rolling downhill with inertia)',
         ha='center', fontsize=10, color=mlpurple)

fig.suptitle('Momentum: Accelerating Gradient Descent',
             fontsize=14, fontweight='bold', color=mlpurple, y=0.98)

plt.tight_layout(rect=[0, 0.06, 1, 0.95])
plt.savefig('momentum_visualization.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('momentum_visualization.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: momentum_visualization.pdf")
