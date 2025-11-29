CHART_METADATA = {
    'title': 'EMH Visualization',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/emh_visualization'
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

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))

np.random.seed(42)

# Weak form efficiency
ax1 = axes[0]
t = np.arange(100)
price = 100 + np.cumsum(np.random.randn(100))
ax1.plot(t, price, color=mlblue, lw=2)
ax1.fill_between(t[60:], price[60:]-5, price[60:]+5, alpha=0.3, color=mlred, label='Cannot predict')
ax1.set_title('Weak Form EMH', fontsize=11, fontweight='bold')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price')
ax1.text(50, price.min()-5, 'Past prices cannot\npredict future returns', ha='center', fontsize=9, color=mlred)
ax1.grid(True, alpha=0.3)

# Semi-strong form
ax2 = axes[1]
price2 = 100 + np.cumsum(np.random.randn(100) * 0.8)
# News event
price2[50:] = price2[50:] + 10  # Jump on news
ax2.plot(t, price2, color=mlgreen, lw=2)
ax2.axvline(x=50, color=mlred, linestyle='--', lw=2)
ax2.annotate('News\nRelease', xy=(50, price2[50]), xytext=(60, price2[50]+15),
            arrowprops=dict(arrowstyle='->', color=mlred), fontsize=9, color=mlred)
ax2.set_title('Semi-Strong Form EMH', fontsize=11, fontweight='bold')
ax2.set_xlabel('Time')
ax2.text(50, price2.min()-5, 'Prices instantly reflect\nall public information', ha='center', fontsize=9, color=mlgreen)
ax2.grid(True, alpha=0.3)

# Strong form
ax3 = axes[2]
price3 = 100 + np.cumsum(np.random.randn(100) * 0.7)
ax3.plot(t, price3, color=mlpurple, lw=2)
# Insider trading impossible
ax3.axhspan(price3.min()-3, price3.max()+3, alpha=0.1, color=mlpurple)
ax3.set_title('Strong Form EMH', fontsize=11, fontweight='bold')
ax3.set_xlabel('Time')
ax3.text(50, price3.min()-5, 'Even insider info\nalready priced in', ha='center', fontsize=9, color=mlpurple)
ax3.grid(True, alpha=0.3)

plt.suptitle('Efficient Market Hypothesis (EMH) Forms', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('emh_visualization.pdf', bbox_inches='tight', dpi=300)
plt.savefig('emh_visualization.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: emh_visualization.pdf")
