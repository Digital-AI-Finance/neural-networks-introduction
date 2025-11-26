# ==============================================================================
# Chart: Decision Boundary Concept
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/12_decision_boundary_concept/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Decision Boundary Concept

Linear vs curved decision boundaries comparison

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/12_decision_boundary_concept/
"""

CHART_METADATA = {
    'name': 'Decision Boundary Concept',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/12_decision_boundary_concept',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Linear vs curved decision boundaries comparison'
}

"""
Chart 12: Decision Boundary Concept
Shows linear vs non-linear boundaries - what a learning system must achieve.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Colors
mlgreen = '#2ca02c'
mlred = '#d62728'
mlpurple = '#3333b2'
mlblue = '#0066cc'

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Generate data for all plots
n = 40
theta = np.linspace(0, 2*np.pi, n)

# Plot 1: Linearly separable (easy case)
ax1 = axes[0]
# Two clusters clearly separated
up_x1 = np.random.normal(2, 0.4, n)
up_y1 = np.random.normal(2, 0.4, n)
down_x1 = np.random.normal(0, 0.4, n)
down_y1 = np.random.normal(0, 0.4, n)

ax1.scatter(up_x1, up_y1, c=mlgreen, s=60, alpha=0.7, label='Buy')
ax1.scatter(down_x1, down_y1, c=mlred, s=60, alpha=0.7, label='Sell')

# Linear boundary
x_line = np.linspace(-1, 3, 100)
ax1.plot(x_line, x_line, color=mlpurple, linewidth=3, linestyle='-', label='Simple Rule')
ax1.fill_between(x_line, x_line, 4, alpha=0.1, color=mlgreen)
ax1.fill_between(x_line, -1, x_line, alpha=0.1, color=mlred)

ax1.set_xlim(-1, 3)
ax1.set_ylim(-1, 3)
ax1.set_xlabel('Feature 1 (Volume)', fontsize=10)
ax1.set_ylabel('Feature 2 (Sentiment)', fontsize=10)
ax1.set_title('Easy: Linear Boundary Works', fontsize=11, fontweight='bold')
ax1.legend(loc='lower right', fontsize=8)
ax1.grid(True, alpha=0.3)

# Plot 2: Non-linearly separable (XOR-like)
ax2 = axes[1]
# XOR pattern
up_x2 = np.concatenate([np.random.normal(0, 0.3, n//2), np.random.normal(2, 0.3, n//2)])
up_y2 = np.concatenate([np.random.normal(2, 0.3, n//2), np.random.normal(0, 0.3, n//2)])
down_x2 = np.concatenate([np.random.normal(0, 0.3, n//2), np.random.normal(2, 0.3, n//2)])
down_y2 = np.concatenate([np.random.normal(0, 0.3, n//2), np.random.normal(2, 0.3, n//2)])

ax2.scatter(up_x2, up_y2, c=mlgreen, s=60, alpha=0.7, label='Buy')
ax2.scatter(down_x2, down_y2, c=mlred, s=60, alpha=0.7, label='Sell')

# Failed linear attempts
ax2.plot([-0.5, 2.5], [1, 1], color=mlpurple, linewidth=2, linestyle='--', alpha=0.5)
ax2.plot([1, 1], [-0.5, 2.5], color=mlpurple, linewidth=2, linestyle='--', alpha=0.5)
ax2.annotate('X', xy=(1, 1), fontsize=20, color=mlred, fontweight='bold', ha='center', va='center')

ax2.set_xlim(-0.5, 2.5)
ax2.set_ylim(-0.5, 2.5)
ax2.set_xlabel('Feature 1 (Volume)', fontsize=10)
ax2.set_ylabel('Feature 2 (Sentiment)', fontsize=10)
ax2.set_title('Hard: No Line Works!', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Plot 3: Non-linear boundary solution
ax3 = axes[2]
ax3.scatter(up_x2, up_y2, c=mlgreen, s=60, alpha=0.7, label='Buy')
ax3.scatter(down_x2, down_y2, c=mlred, s=60, alpha=0.7, label='Sell')

# Draw curved boundaries
theta1 = np.linspace(0, 2*np.pi, 100)
ax3.plot(0.6*np.cos(theta1), 2 + 0.6*np.sin(theta1), color=mlblue, linewidth=3)
ax3.plot(2 + 0.6*np.cos(theta1), 0.6*np.sin(theta1), color=mlblue, linewidth=3)
ax3.plot(0.6*np.cos(theta1), 0.6*np.sin(theta1), color=mlblue, linewidth=3)
ax3.plot(2 + 0.6*np.cos(theta1), 2 + 0.6*np.sin(theta1), color=mlblue, linewidth=3)

ax3.annotate('Neural Network\nLearns This!', xy=(1, 1), fontsize=10, color=mlblue,
            fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlblue, alpha=0.9))

ax3.set_xlim(-0.5, 2.5)
ax3.set_ylim(-0.5, 2.5)
ax3.set_xlabel('Feature 1 (Volume)', fontsize=10)
ax3.set_ylabel('Feature 2 (Sentiment)', fontsize=10)
ax3.set_title('Solution: Curved Boundaries', fontsize=11, fontweight='bold')
ax3.legend(loc='lower right', fontsize=8)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('decision_boundary_concept.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Saved: 12_decision_boundary_concept/decision_boundary_concept.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/12_decision_boundary_concept/
