"""
Perceptron Convergence Theorem - Geometric Intuition
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Wedge

CHART_METADATA = {
    'title': 'Perceptron Convergence Proof',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/perceptron_convergence_proof'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Geometric Intuition ====================
ax = axes[0]

# Setup
ax.set_xlim(-2, 3)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')

# Origin
ax.scatter([0], [0], s=100, c='black', zorder=10)
ax.text(0.1, -0.2, 'Origin', fontsize=9)

# Optimal weight vector w*
w_star = np.array([1.5, 1.5])
ax.annotate('', xy=w_star, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=3))
ax.text(1.6, 1.6, '$w^*$\n(optimal)', fontsize=11, color=mlgreen, fontweight='bold')

# Current weight vector w(t)
w_t = np.array([0.5, 2.5])
ax.annotate('', xy=w_t, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=2))
ax.text(0.3, 2.6, '$w^{(t)}$\n(current)', fontsize=10, color=mlorange)

# Angle between them
theta = np.arctan2(w_star[1], w_star[0])
angle = Wedge((0, 0), 0.5, 0, np.degrees(np.arctan2(w_t[1], w_t[0])),
              facecolor=mlpurple, alpha=0.3)
ax.add_patch(angle)

# Key insight arrows
ax.annotate('Proof shows:\n1. $w^{(t)} \\cdot w^*$ grows\n2. $\\|w^{(t)}\\|$ bounded',
            xy=(1, 0.5), xytext=(2, 0.5), fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple, alpha=0.9))

ax.set_xlabel('$w_1$', fontsize=12)
ax.set_ylabel('$w_2$', fontsize=12)
ax.set_title('Geometric Intuition', fontsize=12, fontweight='bold', color=mlpurple)
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)

# ==================== RIGHT: Theorem Statement ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Perceptron Convergence Theorem', fontsize=14, fontweight='bold',
        ha='center', color=mlpurple)

# Theorem box
theorem_text = """Theorem (Novikoff, 1962):

If training data is linearly separable with margin gamma > 0,
then the perceptron learning algorithm makes at most

(R / gamma)^2

mistakes before converging.

Where:
- R = maximum norm of any input
- w* = any separating hyperplane
- gamma = margin (minimum distance to boundary)"""

ax.text(5, 5, theorem_text, ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#F0F0F0', edgecolor=mlpurple, linewidth=2))

# Implications
implications = """Implications:
- Convergence is GUARANTEED for separable data
- Number of mistakes is FINITE
- Bound depends on data geometry (margin)
- Does NOT guarantee finding optimal solution"""

ax.text(5, 0.8, implications, ha='center', va='top', fontsize=9, color=mlgray,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlgray, alpha=0.9))

fig.suptitle('Perceptron Convergence: Why It Always Works (for Separable Data)',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('perceptron_convergence_proof.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('perceptron_convergence_proof.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: perceptron_convergence_proof.pdf")
