"""
Step Activation Function Visualization
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Step Function',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/step_function'
}

# Colors matching Beamer template
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

# Set up figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create step function data
x_left = np.linspace(-5, 0, 100)
x_right = np.linspace(0, 5, 100)

y_left = np.zeros_like(x_left)
y_right = np.ones_like(x_right)

# Plot step function
ax.plot(x_left, y_left, color=mlpurple, linewidth=3, label='Step Function')
ax.plot(x_right, y_right, color=mlpurple, linewidth=3)

# Vertical line at x=0 (dashed)
ax.plot([0, 0], [0, 1], color=mlpurple, linewidth=2, linestyle='--')

# Points at discontinuity
ax.scatter([0], [0], s=100, c='white', edgecolors=mlpurple, linewidths=2, zorder=5)
ax.scatter([0], [1], s=100, c=mlpurple, edgecolors=mlpurple, linewidths=2, zorder=5)

# Threshold annotation
ax.annotate('Threshold\n(z = 0)', xy=(0, 0.5), xytext=(1.5, 0.5),
            fontsize=11, ha='left', va='center',
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor=mlgray))

# Output labels
ax.text(-3, 0.15, 'Output = 0\n(Sell)', fontsize=11, ha='center', color=mlorange, fontweight='bold')
ax.text(3, 0.85, 'Output = 1\n(Buy)', fontsize=11, ha='center', color=mlgreen, fontweight='bold')

# Shading
ax.fill_between(x_left, -0.1, 0, alpha=0.2, color=mlorange)
ax.fill_between(x_right, 1, 1.1, alpha=0.2, color=mlgreen)

# Axis labels
ax.set_xlabel('Weighted Sum $z = \\sum w_i x_i + b$', fontsize=12)
ax.set_ylabel('Output $y$', fontsize=12)
ax.set_title('Step Activation Function (Heaviside)', fontsize=14, fontweight='bold', color=mlpurple)

# Grid and formatting
ax.axhline(y=0, color='lightgray', linewidth=0.5)
ax.axhline(y=1, color='lightgray', linewidth=0.5)
ax.axvline(x=0, color='lightgray', linewidth=0.5)
ax.set_xlim(-5, 5)
ax.set_ylim(-0.2, 1.3)
ax.set_yticks([0, 1])
ax.set_yticklabels(['0', '1'])
ax.grid(True, alpha=0.3)

# Formula box (simplified for matplotlib compatibility)
formula_text = r'$f(z) = 1$ if $z \geq 0$, else $f(z) = 0$'
ax.text(0.02, 0.98, formula_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5',
        facecolor='white', edgecolor=mlpurple, alpha=0.9))

plt.tight_layout()
plt.savefig('step_function.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('step_function.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: step_function.pdf")
