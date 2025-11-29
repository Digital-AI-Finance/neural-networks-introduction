"""
2D Decision Boundary Visualization
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Decision Boundary 2D',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/decision_boundary_2d'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 8))

# Generate sample data (two classes)
np.random.seed(42)
n_samples = 30

# Class 1: "Buy" stocks (upper right)
x1_buy = np.random.randn(n_samples) * 0.8 + 2.5
x2_buy = np.random.randn(n_samples) * 0.8 + 2.5

# Class 0: "Sell" stocks (lower left)
x1_sell = np.random.randn(n_samples) * 0.8 + 0.5
x2_sell = np.random.randn(n_samples) * 0.8 + 0.5

# Plot data points
ax.scatter(x1_buy, x2_buy, c=mlgreen, s=100, marker='o', label='Buy (y=1)',
           edgecolors='white', linewidths=1.5, zorder=5)
ax.scatter(x1_sell, x2_sell, c=mlorange, s=100, marker='s', label='Sell (y=0)',
           edgecolors='white', linewidths=1.5, zorder=5)

# Decision boundary: w1*x1 + w2*x2 + b = 0
# Using w1=1, w2=1, b=-3 -> x2 = -x1 + 3
x_line = np.linspace(-0.5, 4.5, 100)
y_line = -x_line + 3

ax.plot(x_line, y_line, color=mlpurple, linewidth=3, label='Decision Boundary', zorder=4)

# Fill regions
ax.fill_between(x_line, y_line, 5, alpha=0.15, color=mlgreen, label='Buy Region')
ax.fill_between(x_line, -1, y_line, alpha=0.15, color=mlorange, label='Sell Region')

# Normal vector (weight vector)
mid_x, mid_y = 1.5, 1.5
ax.annotate('', xy=(mid_x + 0.8, mid_y + 0.8), xytext=(mid_x, mid_y),
            arrowprops=dict(arrowstyle='->', color=mlblue, lw=2))
ax.text(mid_x + 1, mid_y + 1, '$\\mathbf{w}$', fontsize=14, color=mlblue, fontweight='bold')

# Boundary equation
ax.text(3.5, 0.3, '$w_1 x_1 + w_2 x_2 + b = 0$', fontsize=11,
        color=mlpurple, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, alpha=0.9))

# Labels for regions
ax.text(3.2, 3.8, 'Predict: BUY\n$z > 0$', fontsize=11, ha='center',
        color=mlgreen, fontweight='bold')
ax.text(0.3, 0.2, 'Predict: SELL\n$z < 0$', fontsize=11, ha='center',
        color=mlorange, fontweight='bold')

# Axis labels
ax.set_xlabel('$x_1$ (e.g., Normalized P/E Ratio)', fontsize=12)
ax.set_ylabel('$x_2$ (e.g., Momentum)', fontsize=12)
ax.set_title('Perceptron Decision Boundary in 2D', fontsize=14, fontweight='bold', color=mlpurple)

# Formatting
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.set_aspect('equal')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

# Add equation explanation
explanation = "The perceptron draws a line\n(hyperplane in higher dimensions)\nthat separates the two classes"
ax.text(0.98, 0.02, explanation, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', horizontalalignment='right', style='italic',
        color=mlgray)

plt.tight_layout()
plt.savefig('decision_boundary_2d.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('decision_boundary_2d.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: decision_boundary_2d.pdf")
