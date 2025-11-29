CHART_METADATA = {
    'title': 'Case Study Architecture',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/case_study_architecture'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(6, 8.5, 'Case Study: Stock Return Prediction Architecture', fontsize=14, fontweight='bold', ha='center', color=mlpurple)

# Input layer
rect1 = mpatches.FancyBboxPatch((0.5, 4), 2, 3, boxstyle="round,pad=0.05",
                                facecolor=mlblue, alpha=0.3, edgecolor=mlblue, lw=2)
ax.add_patch(rect1)
ax.text(1.5, 6.5, 'Input Layer', fontsize=10, fontweight='bold', ha='center', color=mlblue)
ax.text(1.5, 5.5, '50 features', fontsize=9, ha='center')
ax.text(1.5, 5, '(technical +', fontsize=8, ha='center')
ax.text(1.5, 4.5, 'fundamental)', fontsize=8, ha='center')

# Hidden layers
for i, (x, neurons) in enumerate([(3.5, 128), (5.5, 64), (7.5, 32)]):
    rect = mpatches.FancyBboxPatch((x, 4), 1.5, 3, boxstyle="round,pad=0.05",
                                    facecolor=mlpurple, alpha=0.3, edgecolor=mlpurple, lw=2)
    ax.add_patch(rect)
    ax.text(x+0.75, 6.5, f'Hidden {i+1}', fontsize=9, fontweight='bold', ha='center', color=mlpurple)
    ax.text(x+0.75, 5.5, f'{neurons} neurons', fontsize=8, ha='center')
    ax.text(x+0.75, 5, 'ReLU', fontsize=8, ha='center')
    ax.text(x+0.75, 4.5, f'Dropout 0.{3-i}', fontsize=8, ha='center')

# Output layer
rect_out = mpatches.FancyBboxPatch((9.5, 4.5), 2, 2, boxstyle="round,pad=0.05",
                                    facecolor=mlgreen, alpha=0.3, edgecolor=mlgreen, lw=2)
ax.add_patch(rect_out)
ax.text(10.5, 6, 'Output', fontsize=10, fontweight='bold', ha='center', color=mlgreen)
ax.text(10.5, 5.2, '1 neuron', fontsize=9, ha='center')
ax.text(10.5, 4.8, '(return pred)', fontsize=8, ha='center')

# Arrows
arrow_x = [2.5, 5, 7, 9]
for x in arrow_x:
    ax.annotate('', xy=(x+0.4, 5.5), xytext=(x, 5.5), arrowprops=dict(arrowstyle='->', color=mlgray, lw=1.5))

# Architecture details
details = [
    'Total Parameters: ~15,000',
    'Loss Function: MSE',
    'Optimizer: Adam (lr=0.001)',
    'Batch Size: 64',
    'Early Stopping: patience=10',
]
for i, d in enumerate(details):
    ax.text(6, 2.5 - i*0.5, d, ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('case_study_architecture.pdf', bbox_inches='tight', dpi=300)
plt.savefig('case_study_architecture.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: case_study_architecture.pdf")
