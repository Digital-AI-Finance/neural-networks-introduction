CHART_METADATA = {
    'title': 'Loss Function Concept',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/loss_function_concept'
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

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# Left: Concept diagram
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8)
ax1.axis('off')

# Input box
rect1 = plt.Rectangle((0.5, 5), 2, 1.5, fill=True, color=mlblue, alpha=0.7)
ax1.add_patch(rect1)
ax1.text(1.5, 5.75, 'Input\n$x$', ha='center', va='center', fontsize=10, color='white')

# Model box
rect2 = plt.Rectangle((3.5, 5), 2, 1.5, fill=True, color=mlpurple, alpha=0.7)
ax1.add_patch(rect2)
ax1.text(4.5, 5.75, 'Model\n$f(x; w)$', ha='center', va='center', fontsize=10, color='white')

# Prediction
rect3 = plt.Rectangle((6.5, 5), 2, 1.5, fill=True, color=mlgreen, alpha=0.7)
ax1.add_patch(rect3)
ax1.text(7.5, 5.75, 'Prediction\n$\\hat{y}$', ha='center', va='center', fontsize=10, color='white')

# True label
rect4 = plt.Rectangle((6.5, 2), 2, 1.5, fill=True, color=mlorange, alpha=0.7)
ax1.add_patch(rect4)
ax1.text(7.5, 2.75, 'True Label\n$y$', ha='center', va='center', fontsize=10, color='white')

# Loss function
circle = plt.Circle((4.5, 2.75), 0.8, fill=True, color=mlred, alpha=0.7)
ax1.add_patch(circle)
ax1.text(4.5, 2.75, '$L$', ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# Arrows
ax1.annotate('', xy=(3.4, 5.75), xytext=(2.6, 5.75), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.annotate('', xy=(6.4, 5.75), xytext=(5.6, 5.75), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.annotate('', xy=(5.3, 2.75), xytext=(6.4, 2.75), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.annotate('', xy=(5.0, 3.4), xytext=(7.0, 4.9), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax1.text(5, 7.5, 'Loss Function: Measures Prediction Error', fontsize=12, fontweight='bold', ha='center')
ax1.text(2.5, 1, '$L(\\hat{y}, y) = $ Error between prediction and truth', fontsize=10, ha='left')

# Right: Loss landscape
ax2 = axes[1]
w = np.linspace(-3, 3, 100)
loss = w**2 + 0.5
ax2.plot(w, loss, color=mlpurple, lw=3)
ax2.fill_between(w, loss, alpha=0.2, color=mlpurple)

# Mark minimum
ax2.plot(0, 0.5, 'o', color=mlgreen, markersize=12, zorder=5)
ax2.annotate('Minimum\n(Optimal $w$)', xy=(0, 0.5), xytext=(1.5, 3),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5),
            fontsize=10, color=mlgreen)

# Mark current point
ax2.plot(2, 4.5, 'o', color=mlred, markersize=10, zorder=5)
ax2.annotate('Current $w$', xy=(2, 4.5), xytext=(2.5, 6),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=1.5),
            fontsize=10, color=mlred)

ax2.set_xlabel('Weight $w$', fontsize=11)
ax2.set_ylabel('Loss $L(w)$', fontsize=11)
ax2.set_title('Loss as Function of Weights', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-3, 3)
ax2.set_ylim(0, 10)

plt.tight_layout()
plt.savefig('loss_function_concept.pdf', bbox_inches='tight', dpi=300)
plt.savefig('loss_function_concept.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: loss_function_concept.pdf")
