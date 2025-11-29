"""
McCulloch-Pitts Neuron Diagram (1943)
Module 1: The Birth of Neural Computing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

CHART_METADATA = {
    'title': 'Mcculloch Pitts Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/mcculloch_pitts_diagram'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(6, 7.5, 'McCulloch-Pitts Neuron (1943): Binary Threshold Logic',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Inputs (binary)
input_y = [5.5, 4, 2.5]
input_labels = ['$x_1$ (0 or 1)', '$x_2$ (0 or 1)', '$x_3$ (0 or 1)']

for i, (y, label) in enumerate(zip(input_y, input_labels)):
    circle = Circle((1.5, y), 0.4, fill=True, facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
    ax.add_patch(circle)
    ax.text(0.3, y, label, ha='right', va='center', fontsize=10, color=mlblue)

    # Arrow to threshold unit
    ax.annotate('', xy=(5.3, 4), xytext=(2, y),
                arrowprops=dict(arrowstyle='->', color=mlblue, lw=1.5))

# Threshold unit
threshold_circle = Circle((6, 4), 0.8, fill=True, facecolor='#FFE4B5', edgecolor=mlorange, linewidth=3)
ax.add_patch(threshold_circle)
ax.text(6, 4, '$\\theta$', ha='center', va='center', fontsize=18, fontweight='bold', color=mlorange)

# Output arrow
ax.annotate('', xy=(10, 4), xytext=(6.8, 4),
            arrowprops=dict(arrowstyle='->', color=mlgreen, lw=3))

# Output
output_circle = Circle((10.5, 4), 0.4, fill=True, facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(output_circle)
ax.text(10.5, 4, '$y$', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(11.5, 4, '(0 or 1)', ha='left', va='center', fontsize=10, color=mlgreen)

# Logic rule
rule_text = """McCulloch-Pitts Rule:
$y = 1$ if $\\sum x_i \\geq \\theta$
$y = 0$ otherwise

Key Properties:
- All inputs are binary (0 or 1)
- All weights are equal (=1)
- Single threshold parameter
- No learning (fixed weights)"""

ax.text(6, 1.5, rule_text, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlpurple, alpha=0.9))

# Example
ax.text(9, 6, 'Example (AND gate):\n$\\theta = 2$\n(1,1) -> 1\n(1,0) -> 0\n(0,1) -> 0\n(0,0) -> 0',
        fontsize=9, ha='left', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor=mlgray, alpha=0.9))

# Historical note
ax.text(6, 0.3, 'Warren McCulloch and Walter Pitts: "A Logical Calculus of Ideas Immanent in Nervous Activity" (1943)',
        ha='center', fontsize=9, style='italic', color=mlgray)

plt.tight_layout()
plt.savefig('mcculloch_pitts_diagram.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('mcculloch_pitts_diagram.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: mcculloch_pitts_diagram.pdf")
