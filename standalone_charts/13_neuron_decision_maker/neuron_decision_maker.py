# ==============================================================================
# Chart: Neuron Decision Maker
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/13_neuron_decision_maker/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Neuron Decision Maker

Buy/sell threshold decision visualization

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/13_neuron_decision_maker/
"""

CHART_METADATA = {
    'name': 'Neuron Decision Maker',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/13_neuron_decision_maker',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Buy/sell threshold decision visualization'
}

"""
Chart 13: Neuron as Decision Maker
Single neuron making buy/sell decision with threshold visualization.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Colors
mlgreen = '#2ca02c'
mlred = '#d62728'
mlpurple = '#3333b2'
mlblue = '#0066cc'
mlorange = '#ff7f0e'

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: Single neuron decision boundary
ax1 = axes[0]

# Generate market scenarios
n = 30
# Good signals (buy)
good_price = np.random.uniform(0.4, 1.0, n)
good_volume = np.random.uniform(0.5, 1.0, n)
# Bad signals (sell)
bad_price = np.random.uniform(0, 0.6, n)
bad_volume = np.random.uniform(0, 0.5, n)

ax1.scatter(good_price, good_volume, c=mlgreen, s=100, alpha=0.7, label='BUY signal', marker='^')
ax1.scatter(bad_price, bad_volume, c=mlred, s=100, alpha=0.7, label='SELL signal', marker='v')

# Decision boundary line: w1*x1 + w2*x2 = threshold
# Let's say: 0.6*price + 0.4*volume = 0.5
x_bound = np.linspace(0, 1, 100)
y_bound = (0.5 - 0.6*x_bound) / 0.4

ax1.plot(x_bound, y_bound, color=mlpurple, linewidth=3, label='Decision boundary')
ax1.fill_between(x_bound, y_bound, 1.2, alpha=0.15, color=mlgreen)
ax1.fill_between(x_bound, -0.1, y_bound, alpha=0.15, color=mlred)

# Annotations
ax1.annotate('BUY ZONE', xy=(0.8, 0.85), fontsize=12, color=mlgreen, fontweight='bold', ha='center')
ax1.annotate('SELL ZONE', xy=(0.2, 0.15), fontsize=12, color=mlred, fontweight='bold', ha='center')

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_xlabel('Normalized Price Signal', fontsize=11)
ax1.set_ylabel('Normalized Volume Signal', fontsize=11)
ax1.set_title('One Neuron = One Decision Line', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)

# Right: Weighted sum visualization
ax2 = axes[1]
ax2.axis('off')

# Draw neuron diagram
circle = plt.Circle((0.5, 0.5), 0.15, fill=False, color=mlpurple, linewidth=3)
ax2.add_patch(circle)

# Input arrows
ax2.annotate('', xy=(0.35, 0.55), xytext=(0.1, 0.75),
            arrowprops=dict(arrowstyle='->', color=mlblue, lw=2))
ax2.annotate('', xy=(0.35, 0.45), xytext=(0.1, 0.25),
            arrowprops=dict(arrowstyle='->', color=mlorange, lw=2))

# Output arrow
ax2.annotate('', xy=(0.85, 0.5), xytext=(0.65, 0.5),
            arrowprops=dict(arrowstyle='->', color=mlpurple, lw=3))

# Labels
ax2.text(0.05, 0.78, 'Price = 0.8', fontsize=11, color=mlblue, fontweight='bold')
ax2.text(0.05, 0.22, 'Volume = 0.6', fontsize=11, color=mlorange, fontweight='bold')
ax2.text(0.18, 0.65, 'w1 = 0.6', fontsize=10, color=mlblue)
ax2.text(0.18, 0.35, 'w2 = 0.4', fontsize=10, color=mlorange)

# Inside neuron
ax2.text(0.5, 0.52, 'Sum', fontsize=10, ha='center', va='center')
ax2.text(0.5, 0.45, '0.72', fontsize=11, ha='center', va='center', fontweight='bold', color=mlpurple)

# Output
ax2.text(0.88, 0.5, 'Output', fontsize=10, ha='left', va='center')
ax2.text(0.88, 0.42, '0.67', fontsize=12, ha='left', va='center', fontweight='bold', color=mlgreen)

# Calculation box
calc_text = ('Calculation:\n'
             '(0.6 x 0.8) + (0.4 x 0.6) = 0.72\n'
             'sigmoid(0.72) = 0.67\n'
             '0.67 > 0.5  -->  BUY')
ax2.text(0.5, 0.1, calc_text, fontsize=10, ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, alpha=0.9),
        family='monospace')

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_title('How the Neuron Decides', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('neuron_decision_maker.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 13_neuron_decision_maker/neuron_decision_maker.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/13_neuron_decision_maker/
