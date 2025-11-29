"""
3D Loss Landscape Visualization
Module 3: Training Neural Networks
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

CHART_METADATA = {
    'title': 'Loss Landscape 3D',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/loss_landscape_3d'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig = plt.figure(figsize=(14, 6))

# ==================== LEFT: Simple Convex Loss ====================
ax1 = fig.add_subplot(121, projection='3d')

w1 = np.linspace(-3, 3, 50)
w2 = np.linspace(-3, 3, 50)
W1, W2 = np.meshgrid(w1, w2)

# Simple convex loss (bowl shape)
L_convex = W1**2 + W2**2

surf1 = ax1.plot_surface(W1, W2, L_convex, cmap='coolwarm', alpha=0.8, edgecolor='none')

# Mark global minimum
ax1.scatter([0], [0], [0], c=mlgreen, s=100, marker='*', zorder=10, label='Global minimum')

ax1.set_xlabel('$w_1$', fontsize=11)
ax1.set_ylabel('$w_2$', fontsize=11)
ax1.set_zlabel('Loss $L$', fontsize=11)
ax1.set_title('Convex Loss Surface\n(Single Layer)', fontsize=12, fontweight='bold', color=mlblue)
ax1.view_init(elev=30, azim=45)

# ==================== RIGHT: Non-Convex Loss ====================
ax2 = fig.add_subplot(122, projection='3d')

# Non-convex loss (multiple minima)
L_nonconvex = (np.sin(W1 * 2) * np.sin(W2 * 2) + 0.1 * (W1**2 + W2**2) +
               0.5 * np.exp(-((W1-1)**2 + (W2-1)**2)))

surf2 = ax2.plot_surface(W1, W2, L_nonconvex, cmap='coolwarm', alpha=0.8, edgecolor='none')

# Mark local minima
local_mins = [(-1.5, -1.5), (0, 0), (1.5, 1.5)]
for x, y in local_mins:
    z = np.sin(x * 2) * np.sin(y * 2) + 0.1 * (x**2 + y**2)
    ax2.scatter([x], [y], [z], c=mlorange, s=80, marker='o', zorder=10)

ax2.scatter([0], [0], [0], c=mlgreen, s=100, marker='*', zorder=10, label='Global minimum')

ax2.set_xlabel('$w_1$', fontsize=11)
ax2.set_ylabel('$w_2$', fontsize=11)
ax2.set_zlabel('Loss $L$', fontsize=11)
ax2.set_title('Non-Convex Loss Surface\n(Deep Network)', fontsize=12, fontweight='bold', color=mlorange)
ax2.view_init(elev=30, azim=45)

# Legend and annotations
fig.text(0.25, 0.02, 'Easy: One global minimum\nGradient descent always finds it',
         ha='center', fontsize=9, color=mlblue)
fig.text(0.75, 0.02, 'Hard: Many local minima\nMay get stuck in suboptimal solutions',
         ha='center', fontsize=9, color=mlorange)

fig.suptitle('Loss Landscape: Why Deep Networks Are Hard to Train',
             fontsize=14, fontweight='bold', color=mlpurple, y=0.98)

plt.tight_layout(rect=[0, 0.08, 1, 0.95])
plt.savefig('loss_landscape_3d.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('loss_landscape_3d.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: loss_landscape_3d.pdf")
