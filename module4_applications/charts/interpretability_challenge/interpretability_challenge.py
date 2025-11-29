"""
The Interpretability Challenge
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Interpretability Challenge',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/interpretability_challenge'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Interpretable vs Black Box ====================
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'Model Interpretability Spectrum', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

# Spectrum bar
ax.fill_between([1, 9], [7.5, 7.5], [8, 8], color=mlgray, alpha=0.3)

# Gradient from green (interpretable) to red (black box)
for i in range(80):
    x = 1 + i * 0.1
    r = i / 80
    color = (r, 1-r, 0)  # Green to red
    ax.fill_between([x, x + 0.1], [7.5, 7.5], [8, 8], color=color, alpha=0.5)

ax.text(1, 8.3, 'Interpretable', fontsize=9, color=mlgreen, ha='left')
ax.text(9, 8.3, 'Black Box', fontsize=9, color=mlred, ha='right')

# Models on spectrum
models = [
    (1.5, 'Linear\nRegression', mlgreen),
    (3, 'Decision\nTree', mlgreen),
    (5, 'Random\nForest', mlorange),
    (6.5, 'SVM', mlorange),
    (8, 'Deep\nNeural Net', mlred),
]

for x, name, color in models:
    ax.plot([x, x], [7.5, 6.5], color=color, linewidth=2)
    ax.scatter([x], [7.75], c=color, s=100, zorder=5)
    ax.text(x, 6.2, name, ha='center', fontsize=8, color=color)

# Why it matters
ax.text(5, 4.5, 'Why Interpretability Matters:', fontsize=11, fontweight='bold',
        ha='center', color=mlpurple)

reasons = [
    '1. Trust: Users need to understand predictions',
    '2. Debugging: Find and fix errors',
    '3. Compliance: Regulations (GDPR, finance)',
    '4. Fairness: Detect bias in decisions',
    '5. Science: Gain insights from models',
]

y_pos = 3.8
for reason in reasons:
    ax.text(1, y_pos, reason, fontsize=9, color=mlgray)
    y_pos -= 0.7

# ==================== RIGHT: Explainability Techniques ====================
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'Making NNs More Interpretable', fontsize=12, fontweight='bold',
        ha='center', color=mlpurple)

techniques = [
    ('Feature Importance', 'Which inputs matter most?', mlblue),
    ('SHAP Values', 'Attribution per feature', mlorange),
    ('LIME', 'Local linear approximations', mlgreen),
    ('Attention Visualization', 'What the model "looks at"', mlpurple),
    ('Gradient-based Methods', 'Sensitivity analysis', mlblue),
]

y_pos = 8
for name, desc, color in techniques:
    box = FancyBboxPatch((0.5, y_pos - 0.6), 9, 1.2, boxstyle="round,pad=0.05",
                          facecolor=f'{color}11', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(0.8, y_pos, name, fontsize=10, fontweight='bold', color=color, va='center')
    ax.text(4.5, y_pos, desc, fontsize=9, color=mlgray, va='center')
    y_pos -= 1.5

# Warning
ax.text(5, 1, 'Trade-off: More interpretable models often have lower accuracy\n'
              'Choose based on application requirements!',
        ha='center', fontsize=9, color=mlred,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor=mlred))

fig.suptitle('The Interpretability Challenge in Neural Networks',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('interpretability_challenge.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('interpretability_challenge.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: interpretability_challenge.pdf")
