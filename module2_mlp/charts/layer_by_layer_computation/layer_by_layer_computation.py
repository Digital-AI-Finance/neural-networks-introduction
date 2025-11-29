"""
Layer-by-Layer Forward Computation
Module 2: Multi-Layer Perceptrons
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle

CHART_METADATA = {
    'title': 'Layer By Layer Computation',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/layer_by_layer_computation'
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
ax.text(7, 9.5, 'Forward Pass: Layer-by-Layer Computation',
        fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# ==================== LAYER 0: INPUT ====================
input_box = FancyBboxPatch((0.5, 3), 2.5, 4, boxstyle="round,pad=0.1",
                            facecolor='#E6E6FA', edgecolor=mlblue, linewidth=2)
ax.add_patch(input_box)
ax.text(1.75, 7.3, 'Layer 0: Input', ha='center', fontsize=10, fontweight='bold', color=mlblue)

ax.text(1.75, 6, '$x_1 = 0.5$', ha='center', fontsize=10)
ax.text(1.75, 5, '$x_2 = 0.8$', ha='center', fontsize=10)
ax.text(1.75, 4, '$x_3 = 0.2$', ha='center', fontsize=10)

# Arrow
ax.annotate('', xy=(4, 5), xytext=(3.2, 5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# ==================== LAYER 1: HIDDEN ====================
hidden_box = FancyBboxPatch((4, 2), 4, 6, boxstyle="round,pad=0.1",
                             facecolor='#FFE4B5', edgecolor=mlorange, linewidth=2)
ax.add_patch(hidden_box)
ax.text(6, 8.3, 'Layer 1: Hidden', ha='center', fontsize=10, fontweight='bold', color=mlorange)

# Computation steps
ax.text(6, 7, 'Step 1: Weighted Sum', ha='center', fontsize=9, fontweight='bold')
ax.text(6, 6.3, '$z^{(1)} = W^{(1)} \\cdot x + b^{(1)}$', ha='center', fontsize=10)
ax.text(6, 5.5, '$z_1 = 0.3(0.5) + 0.5(0.8) + 0.2(0.2) + 0.1$', ha='center', fontsize=8)
ax.text(6, 5.0, '$z_1 = 0.69$', ha='center', fontsize=9, color=mlorange)

ax.text(6, 4.2, 'Step 2: Activation', ha='center', fontsize=9, fontweight='bold')
ax.text(6, 3.5, '$h^{(1)} = \\sigma(z^{(1)})$', ha='center', fontsize=10)
ax.text(6, 2.8, '$h_1 = \\sigma(0.69) = 0.67$', ha='center', fontsize=9, color=mlorange)

# Arrow
ax.annotate('', xy=(9, 5), xytext=(8.2, 5),
            arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# ==================== LAYER 2: OUTPUT ====================
output_box = FancyBboxPatch((9, 2.5), 4, 5, boxstyle="round,pad=0.1",
                             facecolor='#E6FFE6', edgecolor=mlgreen, linewidth=2)
ax.add_patch(output_box)
ax.text(11, 7.8, 'Layer 2: Output', ha='center', fontsize=10, fontweight='bold', color=mlgreen)

ax.text(11, 6.8, 'Step 3: Weighted Sum', ha='center', fontsize=9, fontweight='bold')
ax.text(11, 6.1, '$z^{(2)} = W^{(2)} \\cdot h^{(1)} + b^{(2)}$', ha='center', fontsize=10)
ax.text(11, 5.4, '$z_{out} = 0.8(0.67) + 0.6(0.72) - 0.2$', ha='center', fontsize=8)
ax.text(11, 4.9, '$z_{out} = 0.77$', ha='center', fontsize=9, color=mlgreen)

ax.text(11, 4.1, 'Step 4: Final Activation', ha='center', fontsize=9, fontweight='bold')
ax.text(11, 3.4, '$\\hat{y} = \\sigma(z^{(2)})$', ha='center', fontsize=10)
ax.text(11, 2.8, '$\\hat{y} = \\sigma(0.77) = 0.68$', ha='center', fontsize=9, color=mlgreen, fontweight='bold')

# Bottom summary
summary_text = """Forward Pass Summary:
Input $\\rightarrow$ Linear Transform $\\rightarrow$ Activation $\\rightarrow$ Linear Transform $\\rightarrow$ Activation $\\rightarrow$ Output
Each layer: $h^{(l)} = \\sigma(W^{(l)} \\cdot h^{(l-1)} + b^{(l)})$"""

ax.text(7, 0.8, summary_text, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=mlpurple, alpha=0.9))

plt.tight_layout()
plt.savefig('layer_by_layer_computation.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('layer_by_layer_computation.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: layer_by_layer_computation.pdf")
