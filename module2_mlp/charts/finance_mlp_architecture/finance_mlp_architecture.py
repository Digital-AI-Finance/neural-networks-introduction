"""
Finance MLP Architecture - Stock Prediction Network
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

CHART_METADATA = {
    'title': 'Finance MLP Architecture',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_mlp_architecture'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(7, 10.5, 'MLP for Stock Return Prediction',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== INPUT LAYER ====================
input_features = [
    ('Returns$_{t-1}$', 'Past returns'),
    ('Returns$_{t-5}$', '5-day return'),
    ('Volume', 'Trading volume'),
    ('Volatility', 'Price volatility'),
    ('P/E Ratio', 'Valuation'),
    ('Momentum', 'Price trend'),
]

input_x = 1.5
for i, (feature, desc) in enumerate(input_features):
    y = 8 - i * 1.2
    circle = Circle((input_x, y), 0.4, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(input_x - 1.2, y, f'{feature}', ha='right', va='center', fontsize=9, color=mlblue)
    ax.text(input_x - 1.2, y - 0.3, f'({desc})', ha='right', va='center', fontsize=7, color=mlgray)

ax.text(input_x, 9, 'Input Layer', ha='center', fontsize=11, fontweight='bold', color=mlblue)
ax.text(input_x, 8.5, '(Financial Features)', ha='center', fontsize=9, color=mlgray)

# ==================== HIDDEN LAYER 1 ====================
hidden1_x = 5
hidden1_neurons = 8
for i in range(hidden1_neurons):
    y = 8.5 - i * 0.9
    circle = Circle((hidden1_x, y), 0.35, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
    ax.add_patch(circle)

ax.text(hidden1_x, 9, 'Hidden 1', ha='center', fontsize=11, fontweight='bold', color=mlorange)
ax.text(hidden1_x, 8.5, '(8 neurons, ReLU)', ha='center', fontsize=9, color=mlgray)

# ==================== HIDDEN LAYER 2 ====================
hidden2_x = 8.5
hidden2_neurons = 4
for i in range(hidden2_neurons):
    y = 6.5 - i * 1.3
    circle = Circle((hidden2_x, y), 0.35, fill=True, facecolor='#D8BFD8', edgecolor=mlpurple, linewidth=2)
    ax.add_patch(circle)

ax.text(hidden2_x, 9, 'Hidden 2', ha='center', fontsize=11, fontweight='bold', color=mlpurple)
ax.text(hidden2_x, 8.5, '(4 neurons, ReLU)', ha='center', fontsize=9, color=mlgray)

# ==================== OUTPUT LAYER ====================
output_x = 12
circle = Circle((output_x, 5), 0.5, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=3)
ax.add_patch(circle)
ax.text(output_x, 5, '$\\hat{r}$', ha='center', va='center', fontsize=12, fontweight='bold')

ax.text(output_x, 9, 'Output', ha='center', fontsize=11, fontweight='bold', color=mlgreen)
ax.text(output_x, 8.5, '(Predicted Return)', ha='center', fontsize=9, color=mlgray)
ax.text(output_x + 1.3, 5, 'Linear\nactivation', ha='left', va='center', fontsize=8, color=mlgray)

# ==================== CONNECTIONS ====================
# Input to Hidden1
for i in range(6):
    y_in = 8 - i * 1.2
    for j in range(8):
        y_h1 = 8.5 - j * 0.9
        ax.plot([input_x + 0.4, hidden1_x - 0.35], [y_in, y_h1],
                color=mlgray, linewidth=0.3, alpha=0.3)

# Hidden1 to Hidden2
for i in range(8):
    y_h1 = 8.5 - i * 0.9
    for j in range(4):
        y_h2 = 6.5 - j * 1.3
        ax.plot([hidden1_x + 0.35, hidden2_x - 0.35], [y_h1, y_h2],
                color=mlgray, linewidth=0.5, alpha=0.4)

# Hidden2 to Output
for i in range(4):
    y_h2 = 6.5 - i * 1.3
    ax.plot([hidden2_x + 0.35, output_x - 0.5], [y_h2, 5],
            color=mlgray, linewidth=0.8, alpha=0.5)

# ==================== INFO BOX ====================
info_text = """Architecture Summary:
- Input: 6 financial features (normalized)
- Hidden 1: 8 neurons with ReLU
- Hidden 2: 4 neurons with ReLU
- Output: 1 (predicted return)
- Loss: Mean Squared Error
- Total parameters: 6x8 + 8 + 8x4 + 4 + 4x1 + 1 = 97"""

ax.text(7, 0.8, info_text, ha='center', va='top', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlpurple, alpha=0.9))

plt.tight_layout()
plt.savefig('finance_mlp_architecture.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_mlp_architecture.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_mlp_architecture.pdf")
