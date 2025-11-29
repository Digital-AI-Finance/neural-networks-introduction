CHART_METADATA = {
    'title': 'MSE Gradient',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mse_gradient'
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

# Left: MSE loss surface
ax1 = axes[0]
w = np.linspace(-3, 3, 100)
y_true = 1.5
mse = (w - y_true)**2

ax1.plot(w, mse, color=mlpurple, lw=3, label='MSE Loss')
ax1.fill_between(w, mse, alpha=0.2, color=mlpurple)

# Show gradient at different points
points = [-1.5, 0.5, 2.5]
for p in points:
    loss_p = (p - y_true)**2
    grad = 2 * (p - y_true)
    # Draw tangent line
    tangent_x = np.linspace(p - 1, p + 1, 50)
    tangent_y = loss_p + grad * (tangent_x - p)
    ax1.plot(tangent_x, tangent_y, '--', color=mlred, lw=1.5, alpha=0.7)
    ax1.plot(p, loss_p, 'o', color=mlred, markersize=8)
    ax1.annotate(f'$\\nabla={grad:.1f}$', xy=(p, loss_p), xytext=(p, loss_p + 2),
                fontsize=9, ha='center', color=mlred)

ax1.axvline(x=y_true, color=mlgreen, linestyle='--', lw=2, label=f'$y={y_true}$ (target)')
ax1.plot(y_true, 0, '*', color=mlgreen, markersize=15)

ax1.set_xlabel('Prediction $\\hat{y}$', fontsize=11)
ax1.set_ylabel('MSE Loss', fontsize=11)
ax1.set_title('MSE: $(\\hat{y} - y)^2$', fontsize=12, fontweight='bold')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-0.5, 12)

# Right: Gradient direction
ax2 = axes[1]
pred = np.linspace(-2, 4, 100)
gradient = 2 * (pred - y_true)

ax2.plot(pred, gradient, color=mlred, lw=3)
ax2.axhline(y=0, color=mlgray, linestyle='-', lw=1)
ax2.axvline(x=y_true, color=mlgreen, linestyle='--', lw=2)

ax2.fill_between(pred[pred < y_true], gradient[pred < y_true], 0, alpha=0.3, color=mlblue, label='Gradient < 0 (increase $\\hat{y}$)')
ax2.fill_between(pred[pred > y_true], gradient[pred > y_true], 0, alpha=0.3, color=mlorange, label='Gradient > 0 (decrease $\\hat{y}$)')

ax2.set_xlabel('Prediction $\\hat{y}$', fontsize=11)
ax2.set_ylabel('Gradient $\\frac{\\partial L}{\\partial \\hat{y}}$', fontsize=11)
ax2.set_title('MSE Gradient: $2(\\hat{y} - y)$', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-2, 4)

plt.tight_layout()
plt.savefig('mse_gradient.pdf', bbox_inches='tight', dpi=300)
plt.savefig('mse_gradient.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: mse_gradient.pdf")
