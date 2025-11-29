"""
Mark I Perceptron Hardware Diagram (Conceptual)
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

CHART_METADATA = {
    'title': 'Mark1 Perceptron Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mark1_perceptron_diagram'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Mark I Perceptron (1958): First Neural Network Hardware',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== INPUT: Photocells ====================
# Grid of photocells (20x20 = 400)
input_box = FancyBboxPatch((0.5, 3), 3, 4, boxstyle="round,pad=0.05",
                            facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
ax.add_patch(input_box)

# Draw mini grid
for i in range(5):
    for j in range(5):
        rect = Rectangle((0.8 + i * 0.5, 3.3 + j * 0.7), 0.4, 0.6,
                          fill=True, facecolor='lightgray', edgecolor=mlgray, linewidth=0.5)
        ax.add_patch(rect)

ax.text(2, 7.3, '400 Photocells', ha='center', fontsize=10, fontweight='bold', color=mlblue)
ax.text(2, 2.5, 'Input Image\n(20x20 pixels)', ha='center', fontsize=9, color=mlgray)

# ==================== WEIGHTS: Potentiometers ====================
weights_box = FancyBboxPatch((4.5, 3), 3, 4, boxstyle="round,pad=0.05",
                              facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax.add_patch(weights_box)

# Draw potentiometer symbols
for i in range(4):
    y = 3.5 + i * 0.9
    ax.plot([5, 6.5], [y, y], color=mlorange, linewidth=2)
    circle = Circle((5.75, y), 0.15, fill=True, facecolor='white', edgecolor=mlorange, linewidth=1)
    ax.add_patch(circle)

ax.text(6, 7.3, 'Adjustable Weights', ha='center', fontsize=10, fontweight='bold', color=mlorange)
ax.text(6, 2.5, 'Potentiometers\n(512 variable resistors)', ha='center', fontsize=9, color=mlgray)

# ==================== PROCESSING: Threshold ====================
process_box = FancyBboxPatch((8.5, 3.5), 2.5, 3, boxstyle="round,pad=0.05",
                              facecolor='#D8BFD8', edgecolor=mlpurple, linewidth=2)
ax.add_patch(process_box)

ax.text(9.75, 5.5, '$\\Sigma$', ha='center', va='center', fontsize=24, fontweight='bold', color=mlpurple)
ax.text(9.75, 4.2, 'Threshold', ha='center', fontsize=10, color=mlpurple)

ax.text(9.75, 7.3, 'Summation &\nThreshold Unit', ha='center', fontsize=10, fontweight='bold', color=mlpurple)
ax.text(9.75, 2.5, 'Electric motor\ncontrolled', ha='center', fontsize=9, color=mlgray)

# ==================== OUTPUT ====================
output_box = FancyBboxPatch((11.5, 4), 2, 2, boxstyle="round,pad=0.05",
                             facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(output_box)
ax.text(12.5, 5, 'Output\n0 or 1', ha='center', va='center', fontsize=11, fontweight='bold', color=mlgreen)

ax.text(12.5, 7.3, 'Binary Output', ha='center', fontsize=10, fontweight='bold', color=mlgreen)
ax.text(12.5, 3.5, 'Light bulb\nindicator', ha='center', fontsize=9, color=mlgray)

# ==================== ARROWS ====================
ax.annotate('', xy=(4.4, 5), xytext=(3.6, 5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.annotate('', xy=(8.4, 5), xytext=(7.6, 5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))
ax.annotate('', xy=(11.4, 5), xytext=(11.1, 5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# ==================== INFO BOX ====================
info_text = """Specifications (1958):
- Weight: ~2 tons
- Size: Room-sized
- 400 photocells (sensory units)
- 512 motor-driven potentiometers (weights)
- Could recognize simple shapes
- Training: Electric motors adjusted weights"""

ax.text(7, 0.8, info_text, ha='center', va='top', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlgray, alpha=0.9))

# Historical note
ax.text(7, 0.1, 'Frank Rosenblatt, Cornell Aeronautical Laboratory - Funded by U.S. Navy',
        ha='center', fontsize=9, style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('mark1_perceptron_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('mark1_perceptron_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: mark1_perceptron_diagram.pdf")
