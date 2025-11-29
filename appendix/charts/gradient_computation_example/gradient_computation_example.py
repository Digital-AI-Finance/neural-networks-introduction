"""
Gradient Computation: Worked Example
Appendix: Mathematical Foundations
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Gradient Computation Example',
    'url': 'https://github.com/QuantLet/NeuralNetworks/tree/main/appendix/charts/gradient_computation_example'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.5, 'Gradient Computation: Worked Example',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)
ax.text(7, 10.9, 'Simple network: 2 inputs, 1 hidden neuron, 1 output',
        fontsize=11, ha='center', color=mlgray)

# Network diagram
# Input
ax.text(1, 7.5, '$x_1 = 0.5$', fontsize=10, ha='center', color=mlblue)
ax.text(1, 5.5, '$x_2 = 0.3$', fontsize=10, ha='center', color=mlblue)

# Hidden
circle_h = Circle((5, 6.5), 0.5, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax.add_patch(circle_h)
ax.text(5, 6.5, '$h$', ha='center', va='center', fontsize=12, fontweight='bold')

# Output
circle_o = Circle((9, 6.5), 0.5, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(circle_o)
ax.text(9, 6.5, '$\\hat{y}$', ha='center', va='center', fontsize=12, fontweight='bold')

# Arrows with weights
ax.annotate('', xy=(4.5, 6.5), xytext=(1.5, 7.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))
ax.text(2.8, 7.3, '$w_1=0.4$', fontsize=9, color=mlorange)

ax.annotate('', xy=(4.5, 6.5), xytext=(1.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))
ax.text(2.8, 5.7, '$w_2=0.6$', fontsize=9, color=mlorange)

ax.annotate('', xy=(8.5, 6.5), xytext=(5.5, 6.5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))
ax.text(7, 6.9, '$w_3=0.8$', fontsize=9, color=mlgreen)

# Target
ax.text(11.5, 6.5, '$y = 1$', fontsize=10, ha='center', color=mlred)

# Calculations
calc_box = FancyBboxPatch((0.5, 0.3), 13, 4.5, boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor=mlpurple, linewidth=2)
ax.add_patch(calc_box)

ax.text(7, 4.5, 'Step-by-Step Calculation', fontsize=11, fontweight='bold',
        ha='center', color=mlpurple)

# Forward pass
ax.text(0.8, 3.8, 'FORWARD:', fontsize=10, fontweight='bold', color=mlblue)
ax.text(2.5, 3.8, '$z_h = w_1 x_1 + w_2 x_2 = 0.4(0.5) + 0.6(0.3) = 0.38$', fontsize=9, color=mlgray)
ax.text(2.5, 3.3, '$h = \\sigma(z_h) = \\sigma(0.38) = 0.594$', fontsize=9, color=mlgray)
ax.text(2.5, 2.8, '$z_o = w_3 h = 0.8(0.594) = 0.475$', fontsize=9, color=mlgray)
ax.text(2.5, 2.3, '$\\hat{y} = \\sigma(z_o) = \\sigma(0.475) = 0.617$', fontsize=9, color=mlgray)

# Backward pass
ax.text(8.5, 3.8, 'BACKWARD:', fontsize=10, fontweight='bold', color=mlred)
ax.text(10.2, 3.8, '$L = \\frac{1}{2}(y - \\hat{y})^2 = 0.073$', fontsize=9, color=mlgray)
ax.text(10.2, 3.3, '$\\delta_o = (\\hat{y} - y) \\cdot \\sigma\'(z_o) = -0.091$', fontsize=9, color=mlgray)
ax.text(10.2, 2.8, '$\\delta_h = \\delta_o \\cdot w_3 \\cdot \\sigma\'(z_h) = -0.017$', fontsize=9, color=mlgray)

# Gradients
ax.text(0.8, 1.5, 'GRADIENTS:', fontsize=10, fontweight='bold', color=mlgreen)
ax.text(3, 1.5, '$\\frac{\\partial L}{\\partial w_3} = \\delta_o \\cdot h = -0.054$', fontsize=9, color=mlgray)
ax.text(6, 1.5, '$\\frac{\\partial L}{\\partial w_1} = \\delta_h \\cdot x_1 = -0.009$', fontsize=9, color=mlgray)
ax.text(9, 1.5, '$\\frac{\\partial L}{\\partial w_2} = \\delta_h \\cdot x_2 = -0.005$', fontsize=9, color=mlgray)

# Update
ax.text(0.8, 0.8, 'UPDATE ($\\eta=0.1$):', fontsize=10, fontweight='bold', color=mlpurple)
ax.text(4.5, 0.8, '$w_3 \\leftarrow 0.8 - 0.1(-0.054) = 0.805$', fontsize=9, color=mlgray)

plt.tight_layout()
plt.savefig('gradient_computation_example.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('gradient_computation_example.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: gradient_computation_example.pdf")
