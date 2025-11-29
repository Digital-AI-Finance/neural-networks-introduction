"""
Bias-Variance Tradeoff Visualization
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Bias Variance Tradeoff',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/bias_variance_tradeoff'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Bias-Variance Curves ====================
ax = axes[0]

complexity = np.linspace(0.5, 5, 100)

# Bias squared (decreases with complexity)
bias_sq = 2 / complexity

# Variance (increases with complexity)
variance = 0.1 * complexity ** 1.8

# Total error
total_error = bias_sq + variance + 0.1  # irreducible error

ax.plot(complexity, bias_sq, color=mlblue, linewidth=2, label='Bias$^2$')
ax.plot(complexity, variance, color=mlorange, linewidth=2, label='Variance')
ax.plot(complexity, total_error, color=mlred, linewidth=3, label='Total Error')
ax.axhline(y=0.1, color=mlgray, linestyle='--', linewidth=1, label='Irreducible Error')

# Optimal complexity point
opt_idx = np.argmin(total_error)
ax.axvline(x=complexity[opt_idx], color=mlgreen, linewidth=2, linestyle='--')
ax.scatter([complexity[opt_idx]], [total_error[opt_idx]], c=mlgreen, s=150, marker='*', zorder=5)
ax.text(complexity[opt_idx] + 0.1, total_error[opt_idx] + 0.3, 'Optimal\nComplexity',
        fontsize=9, color=mlgreen)

ax.set_xlabel('Model Complexity', fontsize=11)
ax.set_ylabel('Error', fontsize=11)
ax.set_title('Bias-Variance Tradeoff', fontsize=12, fontweight='bold', color=mlpurple)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.5, 5)
ax.set_ylim(0, 4)

# Region labels
ax.text(1.2, 3.5, 'Underfitting\n(High Bias)', fontsize=9, ha='center', color=mlblue)
ax.text(4.2, 3.5, 'Overfitting\n(High Variance)', fontsize=9, ha='center', color=mlorange)

# ==================== RIGHT: Visual Explanation ====================
ax = axes[1]
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6, 9.5, 'Understanding Bias vs Variance', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

# Dartboard analogy
# High Bias, Low Variance
circle1 = plt.Circle((2.5, 6), 1.5, fill=False, color=mlgray, linewidth=2)
ax.add_patch(circle1)
ax.scatter([2.2, 2.3, 2.6, 2.4, 2.5], [5.0, 5.1, 5.2, 4.9, 5.0], c=mlblue, s=50)
ax.scatter([2.5], [6], c=mlred, s=100, marker='x')  # target
ax.text(2.5, 4, 'High Bias\nLow Variance', ha='center', fontsize=9, color=mlblue)
ax.text(2.5, 3.4, '(Consistently wrong)', ha='center', fontsize=8, color=mlgray)

# Low Bias, High Variance
circle2 = plt.Circle((6, 6), 1.5, fill=False, color=mlgray, linewidth=2)
ax.add_patch(circle2)
ax.scatter([5.2, 6.8, 5.5, 6.5, 5.0], [6.8, 5.5, 5.2, 6.5, 6.0], c=mlorange, s=50)
ax.scatter([6], [6], c=mlred, s=100, marker='x')  # target
ax.text(6, 4, 'Low Bias\nHigh Variance', ha='center', fontsize=9, color=mlorange)
ax.text(6, 3.4, '(Scattered around target)', ha='center', fontsize=8, color=mlgray)

# Low Bias, Low Variance (ideal)
circle3 = plt.Circle((9.5, 6), 1.5, fill=False, color=mlgray, linewidth=2)
ax.add_patch(circle3)
ax.scatter([9.4, 9.6, 9.5, 9.45, 9.55], [6.1, 5.9, 6.05, 5.95, 6.0], c=mlgreen, s=50)
ax.scatter([9.5], [6], c=mlred, s=100, marker='x')  # target
ax.text(9.5, 4, 'Low Bias\nLow Variance', ha='center', fontsize=9, color=mlgreen)
ax.text(9.5, 3.4, '(Ideal!)', ha='center', fontsize=8, color=mlgreen)

# Formulas
ax.text(6, 1.5, 'Total Error = Bias$^2$ + Variance + Irreducible Noise',
        ha='center', fontsize=11, color=mlpurple,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=mlpurple))

ax.text(6, 0.5, 'We can control Bias and Variance through model complexity',
        ha='center', fontsize=9, color=mlgray)

fig.suptitle('Bias-Variance Tradeoff: The Fundamental Challenge',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('bias_variance_tradeoff.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('bias_variance_tradeoff.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: bias_variance_tradeoff.pdf")
