CHART_METADATA = {
    'title': 'Mini Batch Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mini_batch_visualization'
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

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

np.random.seed(42)

# Create contour for loss landscape
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2) + 0.5 * np.sin(3*X) * np.cos(3*Y)

# Batch Gradient Descent
ax1 = axes[0]
ax1.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
path_x = np.linspace(2.5, 0, 20)
path_y = 2.5 * np.exp(-0.15 * np.arange(20))
ax1.plot(path_x, path_y, 'o-', color=mlblue, markersize=4, lw=2)
ax1.plot(0, 0, 'r*', markersize=15)
ax1.set_title('Batch GD\n(All data)', fontsize=11, fontweight='bold')
ax1.set_xlabel('$w_1$')
ax1.set_ylabel('$w_2$')
ax1.text(0, -2.5, 'Smooth, slow', ha='center', fontsize=9, color=mlblue)

# Mini-batch Gradient Descent
ax2 = axes[1]
ax2.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
path_x = [2.5]
path_y = [2.5]
for i in range(25):
    path_x.append(path_x[-1] - 0.12 + np.random.randn() * 0.15)
    path_y.append(path_y[-1] - 0.12 + np.random.randn() * 0.15)
ax2.plot(path_x, path_y, 'o-', color=mlgreen, markersize=3, lw=1.5, alpha=0.8)
ax2.plot(0, 0, 'r*', markersize=15)
ax2.set_title('Mini-batch GD\n(32-256 samples)', fontsize=11, fontweight='bold')
ax2.set_xlabel('$w_1$')
ax2.text(0, -2.5, 'Good balance', ha='center', fontsize=9, color=mlgreen)

# Stochastic Gradient Descent
ax3 = axes[2]
ax3.contour(X, Y, Z, levels=15, colors=mlgray, alpha=0.5)
path_x = [2.5]
path_y = [2.5]
for i in range(40):
    path_x.append(path_x[-1] - 0.08 + np.random.randn() * 0.4)
    path_y.append(path_y[-1] - 0.08 + np.random.randn() * 0.4)
ax3.plot(path_x, path_y, 'o-', color=mlorange, markersize=2, lw=1, alpha=0.7)
ax3.plot(0, 0, 'r*', markersize=15)
ax3.set_title('SGD\n(1 sample)', fontsize=11, fontweight='bold')
ax3.set_xlabel('$w_1$')
ax3.text(0, -2.5, 'Noisy, fast', ha='center', fontsize=9, color=mlorange)

for ax in axes:
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')

plt.suptitle('Gradient Descent: Batch Size Comparison', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('mini_batch_visualization.pdf', bbox_inches='tight', dpi=300)
plt.savefig('mini_batch_visualization.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: mini_batch_visualization.pdf")
