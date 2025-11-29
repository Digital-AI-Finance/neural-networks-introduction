"""
Linear vs Non-Linear Patterns Comparison
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Linear Vs Nonlinear Patterns',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/linear_vs_nonlinear_patterns'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

# Set up figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(14, 5))

np.random.seed(42)
n_points = 50

# ==================== LINEARLY SEPARABLE ====================
ax = axes[0]

# Two well-separated clusters
x1_class1 = np.random.randn(n_points) * 0.5 + 2
y1_class1 = np.random.randn(n_points) * 0.5 + 2

x1_class0 = np.random.randn(n_points) * 0.5 + 0
y1_class0 = np.random.randn(n_points) * 0.5 + 0

ax.scatter(x1_class1, y1_class1, c=mlgreen, s=60, marker='o', edgecolors='white', linewidths=1)
ax.scatter(x1_class0, y1_class0, c=mlorange, s=60, marker='s', edgecolors='white', linewidths=1)

# Decision boundary
x_line = np.linspace(-1, 3.5, 100)
y_line = -x_line + 2
ax.plot(x_line, y_line, color=mlpurple, linewidth=2.5)

ax.set_title('Linearly Separable', fontsize=12, fontweight='bold', color=mlgreen)
ax.text(0.5, -0.15, 'Perceptron CAN solve', transform=ax.transAxes, fontsize=10,
        ha='center', color=mlgreen, fontweight='bold')
ax.set_xlim(-1.5, 3.5)
ax.set_ylim(-1.5, 3.5)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# ==================== XOR (NOT LINEARLY SEPARABLE) ====================
ax = axes[1]

# XOR pattern
xor_data = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]

for x, y, label in xor_data:
    color = mlgreen if label == 1 else mlorange
    marker = 'o' if label == 1 else 's'
    ax.scatter([x], [y], c=color, s=300, marker=marker, edgecolors='white', linewidths=2, zorder=5)

# Try various lines (all fail)
for angle in [0, 45, 90, 135]:
    rad = np.radians(angle)
    x_line = np.linspace(-0.5, 1.5, 100)
    y_line = np.tan(rad) * (x_line - 0.5) + 0.5
    ax.plot(x_line, y_line, color=mlred, linewidth=1.5, linestyle='--', alpha=0.4)

ax.set_title('XOR Pattern', fontsize=12, fontweight='bold', color=mlred)
ax.text(0.5, -0.15, 'Perceptron CANNOT solve', transform=ax.transAxes, fontsize=10,
        ha='center', color=mlred, fontweight='bold')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# ==================== CIRCULAR PATTERN ====================
ax = axes[2]

# Inner circle (class 0)
theta = np.random.uniform(0, 2 * np.pi, n_points)
r_inner = np.random.uniform(0, 0.8, n_points)
x_inner = r_inner * np.cos(theta)
y_inner = r_inner * np.sin(theta)

# Outer ring (class 1)
theta = np.random.uniform(0, 2 * np.pi, n_points)
r_outer = np.random.uniform(1.5, 2.2, n_points)
x_outer = r_outer * np.cos(theta)
y_outer = r_outer * np.sin(theta)

ax.scatter(x_inner, y_inner, c=mlorange, s=60, marker='s', edgecolors='white', linewidths=1)
ax.scatter(x_outer, y_outer, c=mlgreen, s=60, marker='o', edgecolors='white', linewidths=1)

# Circular boundary (can't be drawn with single line)
circle = plt.Circle((0, 0), 1.15, fill=False, color=mlpurple, linewidth=2.5, linestyle='--')
ax.add_patch(circle)

ax.set_title('Circular Pattern', fontsize=12, fontweight='bold', color=mlred)
ax.text(0.5, -0.15, 'Perceptron CANNOT solve', transform=ax.transAxes, fontsize=10,
        ha='center', color=mlred, fontweight='bold')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# Main title
fig.suptitle('Linear vs Non-Linear Decision Boundaries', fontsize=14, fontweight='bold',
             color=mlpurple, y=1.05)

# Bottom note
fig.text(0.5, 0.02, 'A single perceptron can only draw linear boundaries (straight lines/hyperplanes)',
         ha='center', fontsize=10, style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('linear_vs_nonlinear_patterns.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('linear_vs_nonlinear_patterns.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: linear_vs_nonlinear_patterns.pdf")
