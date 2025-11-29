"""
Gradient Descent on Contour Plot
Module 3: Learning from Mistakes
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Gradient Descent Contour',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/gradient_descent_contour'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 8))

# Create loss surface (quadratic bowl)
w1 = np.linspace(-3, 3, 100)
w2 = np.linspace(-3, 3, 100)
W1, W2 = np.meshgrid(w1, w2)

# Loss function: elongated bowl
L = 0.5 * W1**2 + 2 * W2**2

# Contour plot
contours = ax.contour(W1, W2, L, levels=15, colors=mlgray, linewidths=0.5)
contourf = ax.contourf(W1, W2, L, levels=15, cmap='Blues', alpha=0.3)

# Gradient descent path
np.random.seed(42)
path_w1 = [2.5]
path_w2 = [2.0]
learning_rate = 0.15

for i in range(20):
    # Gradient
    grad_w1 = path_w1[-1]
    grad_w2 = 4 * path_w2[-1]

    # Update
    new_w1 = path_w1[-1] - learning_rate * grad_w1
    new_w2 = path_w2[-1] - learning_rate * grad_w2

    path_w1.append(new_w1)
    path_w2.append(new_w2)

    # Stop if close to minimum
    if abs(new_w1) < 0.01 and abs(new_w2) < 0.01:
        break

# Plot gradient descent path
ax.plot(path_w1, path_w2, 'o-', color=mlpurple, linewidth=2, markersize=6,
        label='Gradient Descent Path')

# Mark start and end
ax.scatter([path_w1[0]], [path_w2[0]], s=200, c=mlred, marker='*',
           edgecolors='white', linewidths=2, zorder=5, label='Start')
ax.scatter([path_w1[-1]], [path_w2[-1]], s=200, c=mlgreen, marker='*',
           edgecolors='white', linewidths=2, zorder=5, label='Minimum')

# Add gradient arrows at some points
for i in [0, 3, 7]:
    if i < len(path_w1) - 1:
        dx = path_w1[i + 1] - path_w1[i]
        dy = path_w2[i + 1] - path_w2[i]
        ax.annotate('', xy=(path_w1[i] + dx * 0.7, path_w2[i] + dy * 0.7),
                    xytext=(path_w1[i], path_w2[i]),
                    arrowprops=dict(arrowstyle='->', color=mlorange, lw=2))

# Labels and title
ax.set_xlabel('Weight $w_1$', fontsize=12)
ax.set_ylabel('Weight $w_2$', fontsize=12)
ax.set_title('Gradient Descent: Finding the Minimum', fontsize=14, fontweight='bold', color=mlpurple)

# Add colorbar
cbar = plt.colorbar(contourf, ax=ax, label='Loss L(w)')
cbar.ax.set_ylabel('Loss Value', fontsize=10)

# Annotations
ax.text(2.5, 2.3, 'Start:\nHigh Loss', fontsize=9, ha='center', color=mlred)
ax.text(0, -0.7, 'Minimum:\nLow Loss', fontsize=9, ha='center', color=mlgreen)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Grid
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')

# Add equation
eq_text = '$w_{new} = w_{old} - \\eta \\nabla L(w)$'
ax.text(0.98, 0.02, eq_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, alpha=0.9))

plt.tight_layout()
plt.savefig('gradient_descent_contour.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('gradient_descent_contour.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: gradient_descent_contour.pdf")
