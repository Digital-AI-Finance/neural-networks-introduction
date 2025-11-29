CHART_METADATA = {
    'title': 'Regularization Effect',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/regularization_effect'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))

np.random.seed(42)
x = np.linspace(0, 10, 20)
y_true = 2 + 0.5 * x
y_noisy = y_true + np.random.randn(len(x)) * 1.5
x_smooth = np.linspace(0, 10, 100)

# No regularization (overfitting)
ax1 = axes[0]
ax1.scatter(x, y_noisy, color=mlblue, s=50, alpha=0.7)
# Overfit polynomial
poly_coeffs = np.polyfit(x, y_noisy, 15)
y_overfit = np.polyval(poly_coeffs, x_smooth)
ax1.plot(x_smooth, y_overfit, color=mlred, lw=2)
ax1.plot(x_smooth, 2 + 0.5 * x_smooth, '--', color=mlgray, lw=1.5, label='True')
ax1.set_title('No Regularization\n(Overfitting)', fontsize=11, fontweight='bold', color=mlred)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_ylim(-5, 15)
ax1.grid(True, alpha=0.3)

# With regularization (good fit)
ax2 = axes[1]
ax2.scatter(x, y_noisy, color=mlblue, s=50, alpha=0.7)
poly_coeffs = np.polyfit(x, y_noisy, 1)
y_good = np.polyval(poly_coeffs, x_smooth)
ax2.plot(x_smooth, y_good, color=mlgreen, lw=2)
ax2.plot(x_smooth, 2 + 0.5 * x_smooth, '--', color=mlgray, lw=1.5, label='True')
ax2.set_title('With Regularization\n(Good Fit)', fontsize=11, fontweight='bold', color=mlgreen)
ax2.set_xlabel('x')
ax2.set_ylim(-5, 15)
ax2.grid(True, alpha=0.3)

# Too much regularization (underfitting)
ax3 = axes[2]
ax3.scatter(x, y_noisy, color=mlblue, s=50, alpha=0.7)
ax3.axhline(y=np.mean(y_noisy), color=mlorange, lw=2)
ax3.plot(x_smooth, 2 + 0.5 * x_smooth, '--', color=mlgray, lw=1.5, label='True')
ax3.set_title('Too Much Regularization\n(Underfitting)', fontsize=11, fontweight='bold', color=mlorange)
ax3.set_xlabel('x')
ax3.set_ylim(-5, 15)
ax3.grid(True, alpha=0.3)

plt.suptitle('Effect of Regularization Strength', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('regularization_effect.pdf', bbox_inches='tight', dpi=300)
plt.savefig('regularization_effect.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: regularization_effect.pdf")
