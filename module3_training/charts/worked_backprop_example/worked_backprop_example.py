CHART_METADATA = {
    'title': 'Worked Backprop Example',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/worked_backprop_example'
}

import matplotlib.pyplot as plt
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Worked Example: Backpropagation', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

# Network diagram
# Input
ax.text(1, 7, '$x = 2$', fontsize=12, ha='center', color=mlblue)
circle_x = plt.Circle((1, 6), 0.3, color=mlblue, alpha=0.7)
ax.add_patch(circle_x)

# Weight w1
ax.annotate('', xy=(2.7, 6), xytext=(1.3, 6), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(2, 6.4, '$w_1 = 0.5$', fontsize=10, ha='center')

# Hidden h
circle_h = plt.Circle((3.5, 6), 0.3, color=mlpurple, alpha=0.7)
ax.add_patch(circle_h)
ax.text(3.5, 6, 'h', fontsize=10, ha='center', color='white')
ax.text(3.5, 5.2, '$h = \\sigma(w_1 \\cdot x)$', fontsize=9, ha='center')
ax.text(3.5, 4.7, '$= \\sigma(1) = 0.73$', fontsize=9, ha='center', color=mlpurple)

# Weight w2
ax.annotate('', xy=(5.2, 6), xytext=(3.8, 6), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(4.5, 6.4, '$w_2 = 0.8$', fontsize=10, ha='center')

# Output y_hat
circle_y = plt.Circle((6, 6), 0.3, color=mlgreen, alpha=0.7)
ax.add_patch(circle_y)
ax.text(6, 6, '$\\hat{y}$', fontsize=10, ha='center', color='white')
ax.text(6, 5.2, '$\\hat{y} = \\sigma(w_2 \\cdot h)$', fontsize=9, ha='center')
ax.text(6, 4.7, '$= \\sigma(0.58) = 0.64$', fontsize=9, ha='center', color=mlgreen)

# Loss
ax.annotate('', xy=(7.7, 6), xytext=(6.3, 6), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
circle_L = plt.Circle((8.5, 6), 0.4, color=mlred, alpha=0.7)
ax.add_patch(circle_L)
ax.text(8.5, 6, 'L', fontsize=12, ha='center', color='white')
ax.text(8.5, 5.2, '$L = (\\hat{y} - y)^2$', fontsize=9, ha='center')
ax.text(8.5, 4.7, '$y = 1$, $L = 0.13$', fontsize=9, ha='center', color=mlred)

# Backprop calculations
ax.text(10.5, 9, 'Backward Pass:', fontsize=12, fontweight='bold', color=mlred)

calcs = [
    '$\\frac{\\partial L}{\\partial \\hat{y}} = 2(\\hat{y} - y) = -0.72$',
    '$\\frac{\\partial \\hat{y}}{\\partial w_2} = h \\cdot \\sigma\'(\\cdot) = 0.17$',
    '$\\frac{\\partial L}{\\partial w_2} = -0.72 \\times 0.17 = -0.12$',
    '',
    '$\\frac{\\partial L}{\\partial h} = w_2 \\cdot \\sigma\'(\\cdot) \\cdot \\frac{\\partial L}{\\partial \\hat{y}}$',
    '$\\frac{\\partial L}{\\partial w_1} = x \\cdot \\sigma\'(\\cdot) \\cdot \\frac{\\partial L}{\\partial h}$',
]

for i, calc in enumerate(calcs):
    ax.text(10, 7.8 - i * 0.7, calc, fontsize=10, ha='left', color=mlred if i < 3 else mlpurple)

# Update rule
ax.text(1, 2.5, 'Weight Updates:', fontsize=12, fontweight='bold', color=mlgreen)
ax.text(1, 1.8, '$w_2^{new} = w_2 - \\eta \\cdot \\frac{\\partial L}{\\partial w_2} = 0.8 - 0.1 \\times (-0.12) = 0.812$', fontsize=10)
ax.text(1, 1.1, '$w_1^{new} = w_1 - \\eta \\cdot \\frac{\\partial L}{\\partial w_1}$ (similar calculation)', fontsize=10)

# Learning rate
ax.text(1, 0.4, '$\\eta = 0.1$ (learning rate)', fontsize=10, color=mlgray)

plt.tight_layout()
plt.savefig('worked_backprop_example.pdf', bbox_inches='tight', dpi=300)
plt.savefig('worked_backprop_example.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: worked_backprop_example.pdf")
