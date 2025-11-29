"""
Perceptron Learning Convergence Plot
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Convergence Plot',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/convergence_plot'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 6))

# Simulate perceptron learning
np.random.seed(42)
iterations = 50
errors = []
cumulative_mistakes = 0

# Simulate decreasing errors with some noise
for i in range(iterations):
    # Error rate decreases over time
    base_error = max(0, 15 - i * 0.4 + np.random.randn() * 2)
    errors.append(base_error)

# Smooth the curve slightly
from scipy.ndimage import gaussian_filter1d
errors_smooth = gaussian_filter1d(errors, sigma=2)
errors_smooth = np.maximum(errors_smooth, 0)

# Plot
ax.plot(range(1, iterations + 1), errors_smooth, color=mlpurple, linewidth=2.5,
        label='Number of Misclassifications')
ax.fill_between(range(1, iterations + 1), errors_smooth, alpha=0.3, color=mlpurple)

# Mark convergence point
converge_idx = 35
ax.axvline(x=converge_idx, color=mlgreen, linestyle='--', linewidth=2, label='Convergence')
ax.scatter([converge_idx], [errors_smooth[converge_idx - 1]], s=150, c=mlgreen,
           zorder=5, edgecolors='white', linewidths=2)

# Annotations
ax.annotate('Convergence!\nZero errors', xy=(converge_idx, errors_smooth[converge_idx - 1]),
            xytext=(converge_idx + 5, 6), fontsize=11, color=mlgreen, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5))

ax.text(10, 12, 'Errors decrease\nas weights adjust', fontsize=10, color=mlgray, style='italic')

# Labels
ax.set_xlabel('Iteration', fontsize=12)
ax.set_ylabel('Number of Misclassified Samples', fontsize=12)
ax.set_title('Perceptron Learning: Convergence', fontsize=14, fontweight='bold', color=mlpurple)

# Formatting
ax.set_xlim(0, iterations + 2)
ax.set_ylim(-0.5, 18)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

# Add theorem reference
theorem_text = "Convergence Theorem: If data is linearly\nseparable, perceptron converges in finite steps"
ax.text(0.02, 0.02, theorem_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor=mlgray, alpha=0.9))

plt.tight_layout()
plt.savefig('convergence_plot.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('convergence_plot.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: convergence_plot.pdf")
