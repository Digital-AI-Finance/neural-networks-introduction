CHART_METADATA = {
    'title': 'ImageNet Error Rates',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/imagenet_error_rates'
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

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# ImageNet Top-5 error rates
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
errors = [28.2, 25.8, 16.4, 11.7, 6.7, 3.6, 2.99, 2.25]
models = ['Traditional', 'Traditional', 'AlexNet', 'ZFNet', 'VGGNet/GoogLeNet', 'ResNet', 'ResNet-152', 'SENet']

# Human-level performance
human_error = 5.1

# Color by type
colors = [mlgray, mlgray, mlred, mlorange, mlblue, mlpurple, mlpurple, mlgreen]

bars = ax.bar(years, errors, color=colors, alpha=0.8, width=0.7)

# Human baseline
ax.axhline(y=human_error, color=mlred, linestyle='--', lw=2, label=f'Human Performance ({human_error}%)')
ax.fill_between([2009, 2018], 0, human_error, alpha=0.1, color=mlgreen)

# Add labels
for year, error, model, bar in zip(years, errors, models, bars):
    ax.text(year, error + 0.8, f'{error}%', ha='center', fontsize=9, fontweight='bold')
    ax.text(year, -2.5, model, ha='center', fontsize=8, rotation=45, va='top')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Top-5 Error Rate (%)', fontsize=12)
ax.set_title('ImageNet Classification Challenge: Error Rates Over Time', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3, axis='y')
ax.set_xlim(2009, 2018)
ax.set_ylim(0, 32)

# Annotation
ax.annotate('Deep Learning\nBreakthrough', xy=(2012, 16.4), xytext=(2013.5, 22),
            arrowprops=dict(arrowstyle='->', color=mlred, lw=1.5),
            fontsize=10, color=mlred, fontweight='bold')

ax.annotate('Surpasses\nHuman Level', xy=(2015, 3.6), xytext=(2013, 8),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=1.5),
            fontsize=10, color=mlgreen, fontweight='bold')

plt.tight_layout()
plt.savefig('imagenet_error_rates.pdf', bbox_inches='tight', dpi=300)
plt.savefig('imagenet_error_rates.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: imagenet_error_rates.pdf")
