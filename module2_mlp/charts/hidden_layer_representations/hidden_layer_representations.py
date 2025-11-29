"""
Hidden Layer Representations - Feature Learning
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Hidden Layer Representations',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/hidden_layer_representations'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

np.random.seed(42)

# ==================== LEFT: Original Feature Space ====================
ax = axes[0]

# Generate circular data (not linearly separable)
n = 100
theta_inner = np.random.uniform(0, 2*np.pi, n//2)
r_inner = np.random.uniform(0, 1, n//2)
x1_inner = r_inner * np.cos(theta_inner)
x2_inner = r_inner * np.sin(theta_inner)

theta_outer = np.random.uniform(0, 2*np.pi, n//2)
r_outer = np.random.uniform(1.5, 2.5, n//2)
x1_outer = r_outer * np.cos(theta_outer)
x2_outer = r_outer * np.sin(theta_outer)

ax.scatter(x1_inner, x2_inner, c=mlgreen, s=40, alpha=0.7, label='Class 1')
ax.scatter(x1_outer, x2_outer, c=mlorange, s=40, alpha=0.7, label='Class 2')

ax.set_xlabel('$x_1$', fontsize=11)
ax.set_ylabel('$x_2$', fontsize=11)
ax.set_title('Input Space\n(Not Linearly Separable)', fontsize=11, fontweight='bold', color=mlblue)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# ==================== MIDDLE: Hidden Layer Features ====================
ax = axes[1]

# Transform: hidden layer learns radial features
# h1 = sqrt(x1^2 + x2^2) - distance from origin
# h2 = atan2(x2, x1) - angle (periodic feature)
h1_inner = np.sqrt(x1_inner**2 + x2_inner**2)
h2_inner = np.sin(np.arctan2(x2_inner, x1_inner)) + np.random.normal(0, 0.1, len(x1_inner))

h1_outer = np.sqrt(x1_outer**2 + x2_outer**2)
h2_outer = np.sin(np.arctan2(x2_outer, x1_outer)) + np.random.normal(0, 0.1, len(x1_outer))

ax.scatter(h1_inner, h2_inner, c=mlgreen, s=40, alpha=0.7)
ax.scatter(h1_outer, h2_outer, c=mlorange, s=40, alpha=0.7)

# Decision boundary in hidden space
ax.axvline(x=1.25, color=mlpurple, linewidth=2, linestyle='--', label='Decision boundary')
ax.fill_betweenx([-2, 2], 0, 1.25, alpha=0.15, color=mlgreen)
ax.fill_betweenx([-2, 2], 1.25, 3, alpha=0.15, color=mlorange)

ax.set_xlabel('$h_1$ (learned: radius)', fontsize=11)
ax.set_ylabel('$h_2$ (learned: angle)', fontsize=11)
ax.set_title('Hidden Layer Space\n(Linearly Separable!)', fontsize=11, fontweight='bold', color=mlorange)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 3)
ax.set_ylim(-1.5, 1.5)

# ==================== RIGHT: What Hidden Layer Learns ====================
ax = axes[2]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9, 'What Hidden Layers Learn', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

# Key insight boxes
insights = [
    ('Raw Features', '$x_1, x_2$\nOriginal inputs', mlblue, 8),
    ('Hidden Features', '$h_1 = f(W \\cdot x)$\nLearned combinations', mlorange, 6),
    ('Useful Patterns', 'Radius, angles,\nedges, textures...', mlgreen, 4),
    ('Linear Separability', 'Transform until\nclasses separable', mlpurple, 2),
]

for label, text, color, y in insights:
    ax.text(2, y, label + ':', fontsize=10, fontweight='bold', color=color, va='center')
    ax.text(5.5, y, text, fontsize=9, color=mlgray, va='center')

# Arrow showing transformation
ax.annotate('', xy=(8, 3), xytext=(8, 7),
            arrowprops=dict(arrowstyle='->', color=mlpurple, lw=2))
ax.text(8.5, 5, 'Network\nlearns\nthis!', fontsize=9, color=mlpurple, va='center')

fig.suptitle('Hidden Layers: Learning Useful Representations',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('hidden_layer_representations.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('hidden_layer_representations.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: hidden_layer_representations.pdf")
