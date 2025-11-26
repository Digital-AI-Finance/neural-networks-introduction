# ==============================================================================
# Chart: Loss Landscape
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/07_loss_landscape/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Loss Landscape

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/07_loss_landscape/
"""

CHART_METADATA = {
    'name': 'Loss Landscape',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/07_loss_landscape',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Set up the figure
fig = plt.figure(figsize=(14, 6))

# LEFT: 3D Loss Surface
ax1 = fig.add_subplot(121, projection='3d')

# Create a loss landscape (simplified for visualization)
w1 = np.linspace(-3, 3, 100)
w2 = np.linspace(-3, 3, 100)
W1, W2 = np.meshgrid(w1, w2)

# Create a complex loss surface with a global minimum
# Using a combination of quadratic and sinusoidal terms
Loss = (W1**2 + W2**2) / 10 + 0.5 * np.sin(W1) * np.sin(W2) + 2

# Find the minimum for marking
min_idx = np.unravel_index(np.argmin(Loss), Loss.shape)
min_w1, min_w2 = W1[min_idx], W2[min_idx]
min_loss = Loss[min_idx]

# Plot the surface
surf = ax1.plot_surface(W1, W2, Loss, cmap='viridis', alpha=0.8, edgecolor='none')

# Mark the minimum
ax1.scatter([min_w1], [min_w2], [min_loss], color='red', s=200, marker='*',
            edgecolors='darkred', linewidth=2, zorder=10, label='Optimal Weights')

ax1.set_xlabel('Weight $w_1$', fontsize=11, labelpad=10)
ax1.set_ylabel('Weight $w_2$', fontsize=11, labelpad=10)
ax1.set_zlabel('Loss (Error)', fontsize=11, labelpad=10)
ax1.set_title('Loss Landscape in 3D\n(Error as a function of weights)', fontsize=12, fontweight='bold')
ax1.view_init(elev=25, azim=45)

# Add colorbar
cbar = fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)
cbar.set_label('Loss Value', fontsize=9)

# RIGHT: Contour plot (top-down view)
ax2 = fig.add_subplot(122)

# Create contour plot
contour = ax2.contour(W1, W2, Loss, levels=20, cmap='viridis', linewidths=1.5)
contourf = ax2.contourf(W1, W2, Loss, levels=20, cmap='viridis', alpha=0.6)

# Mark the minimum
ax2.scatter([min_w1], [min_w2], color='red', s=300, marker='*',
            edgecolors='darkred', linewidth=2, zorder=10, label='Global Minimum')

# Add some gradient descent paths (simulated)
# Starting point 1
start1 = [-2.5, 2.5]
path1_w1 = np.array([-2.5, -2.0, -1.5, -1.0, -0.5, min_w1])
path1_w2 = np.array([2.5, 2.0, 1.5, 1.0, 0.5, min_w2])
ax2.plot(path1_w1, path1_w2, 'ro-', linewidth=2, markersize=5, alpha=0.7, label='Learning Path 1')
ax2.scatter(start1[0], start1[1], color='red', s=150, marker='o', edgecolors='darkred', linewidth=2)

# Starting point 2
start2 = [2.0, -2.0]
path2_w1 = np.array([2.0, 1.5, 1.0, 0.5, 0.0, min_w1])
path2_w2 = np.array([-2.0, -1.5, -1.0, -0.5, 0.0, min_w2])
ax2.plot(path2_w1, path2_w2, 'bo-', linewidth=2, markersize=5, alpha=0.7, label='Learning Path 2')
ax2.scatter(start2[0], start2[1], color='blue', s=150, marker='o', edgecolors='darkblue', linewidth=2)

ax2.set_xlabel('Weight $w_1$', fontsize=11)
ax2.set_ylabel('Weight $w_2$', fontsize=11)
ax2.set_title('Contour View: Loss Landscape\n(Gradient descent paths shown)', fontsize=12, fontweight='bold')
ax2.legend(loc='upper right', fontsize=8)
ax2.grid(True, alpha=0.3)

# Add colorbar
cbar2 = fig.colorbar(contourf, ax=ax2)
cbar2.set_label('Loss Value', fontsize=9)

# Add explanation text
explanation = 'Goal: Find the weights that minimize the loss\n(The red star shows the optimal solution)'
fig.text(0.5, 0.02, explanation, ha='center', fontsize=10, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('loss_landscape.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: loss_landscape.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/07_loss_landscape/
