# ==============================================================================
# Chart: Gradient Descent
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/08_gradient_descent/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Gradient Descent

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/08_gradient_descent/
"""

CHART_METADATA = {
    'name': 'Gradient Descent',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/08_gradient_descent',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Gradient Descent: Learning by Stepping Downhill', fontsize=16, fontweight='bold')

# LEFT: 1D visualization (simple bowl)
x = np.linspace(-5, 5, 100)
loss = x**2 + 3  # Simple quadratic loss function

ax1.plot(x, loss, 'b-', linewidth=3, label='Loss Function')
ax1.set_xlabel('Weight Value', fontsize=12)
ax1.set_ylabel('Loss (Error)', fontsize=12)
ax1.set_title('Gradient Descent in 1D\n(Simplified View)', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Simulate gradient descent steps
learning_rate = 0.3
start_point = 4.5
steps = 8

positions = [start_point]
current = start_point
for i in range(steps):
    gradient = 2 * current  # Derivative of x^2
    current = current - learning_rate * gradient
    positions.append(current)

# Plot the path
for i in range(len(positions) - 1):
    pos = positions[i]
    next_pos = positions[i + 1]
    loss_val = pos**2 + 3
    next_loss = next_pos**2 + 3

    # Draw the point
    ax1.plot(pos, loss_val, 'ro', markersize=10, zorder=5)

    # Draw arrow to next point
    ax1.annotate('', xy=(next_pos, next_loss), xytext=(pos, loss_val),
                arrowprops=dict(arrowstyle='->', lw=2, color='red', alpha=0.7))

    # Label first few steps
    if i < 3:
        ax1.text(pos, loss_val + 2, f'Step {i}', fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))

# Mark the final position
final_pos = positions[-1]
final_loss = final_pos**2 + 3
ax1.plot(final_pos, final_loss, 'g*', markersize=20, zorder=5, label='Minimum Found')
ax1.text(final_pos, final_loss - 2, 'Converged!', fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

ax1.legend(loc='upper right', fontsize=10)

# Add annotation box
annotation = 'Algorithm:\n1. Calculate gradient\n2. Step in opposite direction\n3. Repeat until converged'
ax1.text(-4, 20, annotation, fontsize=9, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# RIGHT: Loss over iterations
ax2.set_xlabel('Training Iteration', fontsize=12)
ax2.set_ylabel('Loss (Error)', fontsize=12)
ax2.set_title('Loss Decreases During Training\n(Network Improves Over Time)', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Simulate realistic loss curve
iterations = np.arange(0, 100)
# Exponential decay with some noise
loss_curve = 5 * np.exp(-iterations / 20) + 0.5 + 0.1 * np.random.randn(len(iterations)) * np.exp(-iterations / 30)
loss_curve = np.maximum(loss_curve, 0.5)  # Floor at 0.5

ax2.plot(iterations, loss_curve, 'b-', linewidth=2, alpha=0.7)
ax2.fill_between(iterations, loss_curve, alpha=0.3)

# Mark key points
ax2.plot(0, loss_curve[0], 'ro', markersize=12, label='Start (Random Weights)', zorder=5)
ax2.plot(99, loss_curve[99], 'g*', markersize=15, label='End (Optimized Weights)', zorder=5)

# Add phases
ax2.axvspan(0, 20, alpha=0.1, color='red', label='Fast Learning')
ax2.axvspan(20, 60, alpha=0.1, color='yellow')
ax2.axvspan(60, 100, alpha=0.1, color='green')

ax2.text(10, 4, 'Rapid\nImprovement', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.6))
ax2.text(40, 2, 'Steady\nProgress', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))
ax2.text(80, 1, 'Fine\nTuning', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

ax2.legend(loc='upper right', fontsize=9)

# Add learning rate note
formula_text = r'Update rule: $w_{new} = w_{old} - \eta \frac{\partial L}{\partial w}$'
formula_text += '\n' + r'($\eta$ = learning rate)'
ax2.text(50, 5, formula_text, fontsize=10, ha='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('gradient_descent.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: gradient_descent.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/08_gradient_descent/
