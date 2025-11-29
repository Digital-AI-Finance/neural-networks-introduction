CHART_METADATA = {
    'title': 'Course Summary',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/course_summary'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

ax.text(7, 9.5, 'Neural Networks: Course Summary', fontsize=16, fontweight='bold', ha='center', color=mlpurple)

# Four modules
modules = [
    (2, 7, 'Module 1:\nPerceptron', ['Single neuron', 'Binary classification', 'Linear separability', 'XOR limitation'], mlblue),
    (5.5, 7, 'Module 2:\nMLP', ['Hidden layers', 'Activation functions', 'Universal approximation', 'Loss functions'], mlpurple),
    (9, 7, 'Module 3:\nTraining', ['Backpropagation', 'Gradient descent', 'Regularization', 'Hyperparameters'], mlgreen),
    (12.5, 7, 'Module 4:\nApplications', ['Finance use cases', 'Pitfalls', 'Best practices', 'Modern architectures'], mlorange),
]

for x, y, title, items, color in modules:
    rect = mpatches.FancyBboxPatch((x-1.5, y-2.5), 3, 4.5, boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.15, edgecolor=color, lw=2)
    ax.add_patch(rect)
    ax.text(x, y+1.5, title, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
    for i, item in enumerate(items):
        ax.text(x, y - 0.3 - i*0.55, f'- {item}', ha='center', va='center', fontsize=9)

# Connecting arrows
for i in range(3):
    x_start = 2 + i * 3.5 + 1.5
    x_end = 2 + (i+1) * 3.5 - 1.5
    ax.annotate('', xy=(x_end, 7), xytext=(x_start, 7),
                arrowprops=dict(arrowstyle='->', color=mlgray, lw=2))

# Key takeaways
ax.text(7, 2.5, 'Key Takeaways', fontsize=12, fontweight='bold', ha='center', color=mlred)
takeaways = [
    'Neural networks are universal function approximators',
    'Training requires careful attention to overfitting',
    'Financial applications face unique challenges (noise, non-stationarity)',
    'Success depends on proper validation and realistic expectations',
]
for i, t in enumerate(takeaways):
    ax.text(7, 1.8 - i*0.5, f'{i+1}. {t}', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('course_summary.pdf', bbox_inches='tight', dpi=300)
plt.savefig('course_summary.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: course_summary.pdf")
