CHART_METADATA = {
    'title': 'Architecture Family Tree',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/architecture_family_tree'
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

ax.text(7, 9.5, 'Neural Network Architecture Family Tree', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

# Root
ax.text(7, 8, 'Perceptron (1958)', fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor=mlblue, alpha=0.3))
ax.plot([7, 7], [7.6, 7], 'k-', lw=1.5)

# MLP branch
ax.plot([7, 3], [7, 6], 'k-', lw=1.5)
ax.text(3, 5.8, 'MLP (1986)', fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor=mlpurple, alpha=0.3))

# CNN branch
ax.plot([7, 7], [7, 6], 'k-', lw=1.5)
ax.text(7, 5.8, 'CNN (1989)', fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor=mlgreen, alpha=0.3))
ax.plot([7, 7], [5.4, 4.5], 'k-', lw=1.5)
ax.text(7, 4.3, 'AlexNet (2012)', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor=mlgreen, alpha=0.2))
ax.plot([7, 5.5], [4, 3], 'k-', lw=1)
ax.plot([7, 8.5], [4, 3], 'k-', lw=1)
ax.text(5.5, 2.8, 'VGG (2014)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlgreen, alpha=0.15))
ax.text(8.5, 2.8, 'ResNet (2015)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlgreen, alpha=0.15))

# RNN branch
ax.plot([7, 11], [7, 6], 'k-', lw=1.5)
ax.text(11, 5.8, 'RNN (1986)', fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor=mlorange, alpha=0.3))
ax.plot([11, 11], [5.4, 4.5], 'k-', lw=1.5)
ax.text(11, 4.3, 'LSTM (1997)', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor=mlorange, alpha=0.2))
ax.plot([11, 11], [4, 3], 'k-', lw=1)
ax.text(11, 2.8, 'GRU (2014)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlorange, alpha=0.15))

# Transformer branch
ax.plot([11, 13], [4, 3], 'k-', lw=1)
ax.text(13, 2.8, 'Transformer\n(2017)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlred, alpha=0.3))
ax.plot([13, 13], [2.3, 1.3], 'k-', lw=1)
ax.text(13, 1.1, 'GPT/BERT', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlred, alpha=0.2))

# Autoencoder branch
ax.plot([3, 3], [5.4, 4.5], 'k-', lw=1.5)
ax.text(3, 4.3, 'Autoencoder', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor=mlpurple, alpha=0.2))
ax.plot([3, 1.5], [4, 3], 'k-', lw=1)
ax.plot([3, 4.5], [4, 3], 'k-', lw=1)
ax.text(1.5, 2.8, 'VAE (2013)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlpurple, alpha=0.15))
ax.text(4.5, 2.8, 'GAN (2014)', fontsize=8, ha='center', bbox=dict(boxstyle='round', facecolor=mlpurple, alpha=0.15))

# Legend
ax.text(1, 1, 'Feedforward', fontsize=9, color=mlpurple, bbox=dict(boxstyle='round', facecolor=mlpurple, alpha=0.2))
ax.text(4, 1, 'Convolutional', fontsize=9, color=mlgreen, bbox=dict(boxstyle='round', facecolor=mlgreen, alpha=0.2))
ax.text(7.5, 1, 'Recurrent', fontsize=9, color=mlorange, bbox=dict(boxstyle='round', facecolor=mlorange, alpha=0.2))
ax.text(10.5, 1, 'Attention', fontsize=9, color=mlred, bbox=dict(boxstyle='round', facecolor=mlred, alpha=0.2))

plt.tight_layout()
plt.savefig('architecture_family_tree.pdf', bbox_inches='tight', dpi=300)
plt.savefig('architecture_family_tree.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: architecture_family_tree.pdf")
