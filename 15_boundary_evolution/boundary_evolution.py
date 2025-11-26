# ==============================================================================
# Chart: Boundary Evolution
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/15_boundary_evolution/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-24
# ==============================================================================

"""
Boundary Evolution

Real trained neural networks showing curved decision boundaries

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/15_boundary_evolution/
"""

CHART_METADATA = {
    'name': 'Boundary Evolution',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/15_boundary_evolution',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-24',
    'description': 'Real trained neural networks showing curved decision boundaries'
}

"""
Chart 15: Decision Boundary Evolution - REAL NEURAL NETWORKS
Actually trains neural networks with different architectures and plots their learned boundaries.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# Colors
mlgreen = '#2ca02c'
mlred = '#d62728'
mlpurple = '#3333b2'
mlblue = '#0066cc'
mlorange = '#ff7f0e'

# Generate XOR-like data
n = 25
# Class 1 (green/buy): upper-left and lower-right
X1 = np.concatenate([
    np.random.normal([0.2, 0.8], 0.12, (n, 2)),
    np.random.normal([0.8, 0.2], 0.12, (n, 2))
])
y1 = np.ones(2*n)

# Class 0 (red/sell): upper-right and lower-left
X0 = np.concatenate([
    np.random.normal([0.2, 0.2], 0.12, (n, 2)),
    np.random.normal([0.8, 0.8], 0.12, (n, 2))
])
y0 = np.zeros(2*n)

# Combine data
X = np.vstack([X1, X0])
y = np.concatenate([y1, y0])

# Standardize (helps neural network training)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create meshgrid for decision boundary visualization
h = 0.01  # step size
x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
mesh_data = np.c_[xx.ravel(), yy.ravel()]
mesh_data_scaled = scaler.transform(mesh_data)

fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))

# ============================================================================
# Panel 1: Logistic Regression (equivalent to 1 neuron)
# ============================================================================
print("Training Model 1: Logistic Regression (1 neuron)...")
model1 = LogisticRegression(random_state=42, max_iter=1000)
model1.fit(X_scaled, y)
acc1 = model1.score(X_scaled, y) * 100

# Predict on mesh
Z1 = model1.predict(mesh_data_scaled).reshape(xx.shape)

ax1 = axes[0]
ax1.contourf(xx, yy, Z1, levels=1, colors=[mlred, mlgreen], alpha=0.2)
ax1.contour(xx, yy, Z1, levels=1, colors=[mlpurple], linewidths=3)
ax1.scatter(X[y==1, 0], X[y==1, 1], c=mlgreen, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax1.scatter(X[y==0, 0], X[y==0, 1], c=mlred, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax1.text(0.5, 0.05, f'Accuracy: {acc1:.0f}%', fontsize=10, ha='center', fontweight='bold',
         color=mlred if acc1 < 60 else mlorange)
ax1.set_title('1 Neuron\n(Logistic)', fontsize=11, fontweight='bold')
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_aspect('equal')

# ============================================================================
# Panel 2: Neural Network with 2 hidden neurons
# ============================================================================
print("Training Model 2: Neural Network (2 neurons)...")
model2 = MLPClassifier(hidden_layer_sizes=(2,), activation='relu',
                       random_state=42, max_iter=2000, learning_rate_init=0.01)
model2.fit(X_scaled, y)
acc2 = model2.score(X_scaled, y) * 100

Z2 = model2.predict(mesh_data_scaled).reshape(xx.shape)

ax2 = axes[1]
ax2.contourf(xx, yy, Z2, levels=1, colors=[mlred, mlgreen], alpha=0.2)
ax2.contour(xx, yy, Z2, levels=1, colors=[mlpurple], linewidths=2)
ax2.scatter(X[y==1, 0], X[y==1, 1], c=mlgreen, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax2.scatter(X[y==0, 0], X[y==0, 1], c=mlred, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax2.text(0.5, 0.05, f'Accuracy: {acc2:.0f}%', fontsize=10, ha='center', fontweight='bold', color=mlorange)
ax2.set_title('2 Neurons\n(Hidden Layer)', fontsize=11, fontweight='bold')
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(y_min, y_max)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_aspect('equal')

# ============================================================================
# Panel 3: Neural Network with 4 hidden neurons
# ============================================================================
print("Training Model 3: Neural Network (4 neurons)...")
model3 = MLPClassifier(hidden_layer_sizes=(4,), activation='relu',
                       random_state=42, max_iter=2000, learning_rate_init=0.01)
model3.fit(X_scaled, y)
acc3 = model3.score(X_scaled, y) * 100

Z3 = model3.predict(mesh_data_scaled).reshape(xx.shape)

ax3 = axes[2]
ax3.contourf(xx, yy, Z3, levels=1, colors=[mlred, mlgreen], alpha=0.2)
ax3.contour(xx, yy, Z3, levels=1, colors=[mlblue], linewidths=3)
ax3.scatter(X[y==1, 0], X[y==1, 1], c=mlgreen, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax3.scatter(X[y==0, 0], X[y==0, 1], c=mlred, s=40, alpha=0.7, edgecolors='k', linewidths=0.5)
ax3.text(0.5, 0.05, f'Accuracy: {acc3:.0f}%', fontsize=10, ha='center', fontweight='bold', color=mlblue)
ax3.set_title('4 Neurons\n(Hidden Layer)', fontsize=11, fontweight='bold')
ax3.set_xlim(x_min, x_max)
ax3.set_ylim(y_min, y_max)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_aspect('equal')

# ============================================================================
# Panel 4: Neural Network with 10 hidden neurons (full network)
# ============================================================================
print("Training Model 4: Neural Network (10 neurons)...")
model4 = MLPClassifier(hidden_layer_sizes=(10,), activation='relu',
                       random_state=42, max_iter=2000, learning_rate_init=0.01)
model4.fit(X_scaled, y)
acc4 = model4.score(X_scaled, y) * 100

Z4 = model4.predict(mesh_data_scaled).reshape(xx.shape)

ax4 = axes[3]
ax4.contourf(xx, yy, Z4, levels=1, colors=[mlred, mlgreen], alpha=0.2)
ax4.contour(xx, yy, Z4, levels=1, colors=[mlgreen], linewidths=3)
ax4.scatter(X[y==1, 0], X[y==1, 1], c=mlgreen, s=40, alpha=0.7, edgecolors='k', linewidths=0.5, label='Buy')
ax4.scatter(X[y==0, 0], X[y==0, 1], c=mlred, s=40, alpha=0.7, edgecolors='k', linewidths=0.5, label='Sell')
ax4.text(0.5, 0.05, f'Accuracy: {acc4:.0f}%', fontsize=10, ha='center', fontweight='bold', color=mlgreen)
ax4.set_title('10 Neurons\n(Curved)', fontsize=11, fontweight='bold')
ax4.set_xlim(x_min, x_max)
ax4.set_ylim(y_min, y_max)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_aspect('equal')

# Add arrow progression
fig.text(0.27, 0.02, '-->', fontsize=16, ha='center', color=mlpurple)
fig.text(0.5, 0.02, '-->', fontsize=16, ha='center', color=mlpurple)
fig.text(0.73, 0.02, '-->', fontsize=16, ha='center', color=mlpurple)

plt.tight_layout()
plt.subplots_adjust(bottom=0.1)
plt.savefig('boundary_evolution.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("\nSaved: 15_boundary_evolution/boundary_evolution.pdf")
print(f"\nTrained Accuracies:")
print(f"  1 Neuron:  {acc1:.1f}%")
print(f"  2 Neurons: {acc2:.1f}%")
print(f"  4 Neurons: {acc3:.1f}%")
print(f"  10 Neurons: {acc4:.1f}%")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/15_boundary_evolution/
