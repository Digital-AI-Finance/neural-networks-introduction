import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
import numpy as np

# Professional color scheme
COLOR_BIO = '#2E7D32'  # Green for biological
COLOR_AI = '#1565C0'   # Blue for artificial
COLOR_ACCENT = '#FFA000'  # Orange for highlights

# Set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('From Biological Intelligence to Business AI', fontsize=18, fontweight='bold', color='#1a1a1a')

# LEFT: Biological Neuron
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Biological Neuron\n(How Your Brain Works)', fontsize=14, fontweight='bold', color=COLOR_BIO)

# Dendrites (inputs) - multiple signals
for i in range(3):
    y_pos = 7.5 - i * 1.8
    ax1.plot([0.5, 2.5], [y_pos, 6], COLOR_BIO, linewidth=2.5, alpha=0.8)
    ax1.plot([0, 0.5], [y_pos, y_pos], COLOR_BIO, linewidth=2.5, alpha=0.8)

    # Add signal indicators
    ax1.scatter([0.5 + j*0.5 for j in range(3)], [y_pos + (6-y_pos)/4 * j for j in range(3)],
               s=30, c=COLOR_ACCENT, alpha=0.6, zorder=5)

    ax1.text(-0.5, y_pos, f'Signal {i+1}', fontsize=10, ha='right', va='center', color=COLOR_BIO)

ax1.text(1, 2.5, 'DENDRITES\n(Inputs)', fontsize=9, ha='center', style='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.3, edgecolor=COLOR_BIO))

# Soma (cell body)
soma = Circle((3.5, 5.8), 1.3, facecolor='#A5D6A7', edgecolor=COLOR_BIO, linewidth=3)
ax1.add_patch(soma)
ax1.text(3.5, 5.8, 'SOMA\n(Cell Body)', fontsize=11, ha='center', va='center', fontweight='bold', color='#1B5E20')
ax1.text(3.5, 4, 'Integrates\nWeighted Signals', fontsize=9, ha='center', style='italic',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

# Axon with electrical activity indication
ax1.plot([4.8, 8.5], [5.8, 5.8], COLOR_BIO, linewidth=4)
# Action potential waves
for x in np.linspace(5, 8, 4):
    ax1.plot([x-0.2, x, x+0.2], [5.4, 6.2, 5.4], COLOR_ACCENT, linewidth=2, alpha=0.7)
ax1.text(6.7, 6.7, 'AXON (Electrical signal)', fontsize=10, ha='center', color=COLOR_BIO, fontweight='bold')

# Synapses (output) - showing signal transmission
for i in range(2):
    y_pos = 6.3 - i * 1.2
    ax1.plot([8.5, 9.5], [5.8, y_pos], COLOR_BIO, linewidth=2.5, alpha=0.8)
    circle = Circle((9.5, y_pos), 0.2, facecolor=COLOR_ACCENT, edgecolor=COLOR_BIO, linewidth=2)
    ax1.add_patch(circle)
    ax1.text(10.2, y_pos, f'To Neuron {i+1}', fontsize=9, ha='left', va='center', color=COLOR_BIO)

ax1.text(9.5, 4, 'SYNAPSES\n(Connections)', fontsize=9, ha='center', style='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.4, edgecolor=COLOR_ACCENT))

# Add business context
ax1.text(5, 1, 'Brain Analogy: Like a trader weighing\nmultiple market signals to make decision',
         fontsize=10, ha='center', style='italic', color='#424242',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9', alpha=0.6))

# RIGHT: Artificial Neuron
ax2.set_xlim(0, 11)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Artificial Neuron\n(Mathematical Model for Business AI)', fontsize=14, fontweight='bold', color=COLOR_AI)

# Inputs with weights - more detailed
input_labels = ['Market\nPrice', 'Trading\nVolume', 'Sentiment\nScore']
for i in range(3):
    y_pos = 7.5 - i * 1.8
    ax2.plot([0, 2.2], [y_pos, 5.8], COLOR_AI, linewidth=2.5, alpha=0.7)

    # Input value boxes
    input_box = FancyBboxPatch((-0.6, y_pos-0.25), 0.5, 0.5, boxstyle='round,pad=0.05',
                                facecolor='#BBDEFB', edgecolor=COLOR_AI, linewidth=2)
    ax2.add_patch(input_box)
    ax2.text(-0.35, y_pos, f'$x_{i+1}$', fontsize=12, ha='center', va='center', fontweight='bold')
    ax2.text(-0.35, y_pos - 0.7, input_labels[i], fontsize=8, ha='center', va='top', color=COLOR_AI)

    # Weight labels - more prominent
    mid_x, mid_y = 1.1, (y_pos + 5.8) / 2
    ax2.text(mid_x, mid_y, f'$w_{i+1}$', fontsize=10, ha='center', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF9C4', alpha=0.8, edgecolor=COLOR_ACCENT, linewidth=1.5))

ax2.text(0.5, 2.8, 'INPUTS\n(Features)', fontsize=9, ha='center', style='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#E3F2FD', alpha=0.5))

# Summation node - more prominent
sum_circle = Circle((3.8, 5.8), 0.9, facecolor='#81C784', edgecolor=COLOR_BIO, linewidth=3)
ax2.add_patch(sum_circle)
ax2.text(3.8, 5.8, r'$\mathbf{\Sigma}$', fontsize=20, ha='center', va='center', fontweight='bold')
ax2.text(3.8, 4.5, 'Weighted\nSum', fontsize=9, ha='center', fontweight='bold')

# Bias
ax2.plot([3.8, 3.8], [3.3, 4.7], 'darkred', linewidth=2.5)
bias_box = FancyBboxPatch((3.3, 2.8), 1, 0.4, boxstyle='round,pad=0.05',
                          facecolor='#FFCDD2', edgecolor='darkred', linewidth=2)
ax2.add_patch(bias_box)
ax2.text(3.8, 3, 'bias (b)', fontsize=10, ha='center', va='center', fontweight='bold', color='darkred')

# Activation function - more detailed
ax2.plot([4.8, 6.5], [5.8, 5.8], COLOR_AI, linewidth=2.5)
activation_box = FancyBboxPatch((6.5, 4.9), 2, 1.8, boxstyle='round,pad=0.15',
                                facecolor='#E1BEE7', edgecolor='#7B1FA2', linewidth=3)
ax2.add_patch(activation_box)
ax2.text(7.5, 6.2, 'ACTIVATION', fontsize=10, ha='center', fontweight='bold', color='#4A148C')
ax2.text(7.5, 5.8, r'$f(z)$', fontsize=16, ha='center', va='center', fontweight='bold')

# Sigmoid curve (small)
x_curve = np.linspace(-2, 2, 50)
y_curve = 1 / (1 + np.exp(-x_curve))
x_plot = 7.5 + x_curve * 0.35
y_plot = 5 + y_curve * 0.7
ax2.plot(x_plot, y_plot, '#7B1FA2', linewidth=2)

# Output
ax2.plot([8.5, 9.5], [5.8, 5.8], COLOR_AI, linewidth=2.5, alpha=0.7)
output_circle = Circle((10, 5.8), 0.4, facecolor=COLOR_ACCENT, edgecolor='darkorange', linewidth=3)
ax2.add_patch(output_circle)
ax2.text(10, 5.8, '$y$', fontsize=14, ha='center', va='center', fontweight='bold', color='white')
ax2.text(10, 4.7, 'Prediction\n(0 to 1)', fontsize=9, ha='center', fontweight='bold')

# Formula annotation - more prominent
formula_text = r'$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$'
ax2.text(5.5, 2, formula_text, fontsize=14, ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFDE7', alpha=0.9, edgecolor=COLOR_ACCENT, linewidth=2))

# Add business context
ax2.text(5.5, 0.7, 'Business Application: Predicts stock direction\nby combining market signals with learned weights',
         fontsize=10, ha='center', style='italic', color='#424242',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#E3F2FD', alpha=0.6))

# Add parallel labels
ax2.text(3.8, 7.5, 'Like SOMA', fontsize=8, ha='center', style='italic', color=COLOR_BIO)
ax2.text(7.5, 7.3, 'Like AXON firing', fontsize=8, ha='center', style='italic', color=COLOR_BIO)

plt.tight_layout()
plt.savefig('biological_vs_artificial.pdf', bbox_inches='tight', dpi=300)
print("Improved chart saved: biological_vs_artificial.pdf")
