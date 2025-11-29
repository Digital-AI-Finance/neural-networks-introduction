"""
Model Comparison for Financial Prediction
Module 4: Applications & Modern Perspectives
"""

import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Finance Model Comparison',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/finance_model_comparison'
}

# Colors
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ==================== LEFT: Model Performance Bar Chart ====================
ax = axes[0]

models = ['Linear\nRegression', 'Decision\nTree', 'Random\nForest', 'SVM', 'MLP\n(Shallow)', 'MLP\n(Deep)']
accuracy = [51.2, 52.8, 54.1, 53.3, 54.8, 55.2]
colors = [mlgray, mlgray, mlorange, mlgray, mlblue, mlpurple]

bars = ax.bar(models, accuracy, color=colors, edgecolor='white', linewidth=2)

# Random benchmark line
ax.axhline(y=50, color=mlred, linestyle='--', linewidth=2, label='Random (50%)')

ax.set_ylabel('Directional Accuracy (%)', fontsize=11)
ax.set_title('Model Comparison: Predicting Stock Direction', fontsize=11, fontweight='bold', color=mlpurple)
ax.set_ylim(48, 58)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar, val in zip(bars, accuracy):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{val}%', ha='center', fontsize=9)

# Key insight
ax.text(2.5, 49, 'Even small improvements (>50%) can be profitable at scale',
        fontsize=9, ha='center', color=mlpurple, style='italic')

# ==================== RIGHT: Complexity vs Performance ====================
ax = axes[1]

# Model complexity (arbitrary scale)
complexity = [1, 2, 4, 3, 6, 10]
training_perf = [52, 58, 68, 62, 78, 92]  # Training accuracy
test_perf = [51.2, 52.8, 54.1, 53.3, 54.8, 55.2]  # Test accuracy

ax.scatter(complexity, training_perf, c=mlblue, s=150, marker='^', label='Training', zorder=5)
ax.scatter(complexity, test_perf, c=mlorange, s=150, marker='o', label='Test (Out-of-sample)', zorder=5)

# Connect with lines
ax.plot(complexity, training_perf, color=mlblue, linewidth=1, linestyle='--', alpha=0.5)
ax.plot(complexity, test_perf, color=mlorange, linewidth=1, linestyle='--', alpha=0.5)

# Model labels
for i, model in enumerate(['LR', 'DT', 'RF', 'SVM', 'MLP-S', 'MLP-D']):
    ax.annotate(model, (complexity[i], test_perf[i]), xytext=(5, -10),
                textcoords='offset points', fontsize=8, color=mlgray)

# Gap annotation
ax.annotate('', xy=(10, 92), xytext=(10, 55.2),
            arrowprops=dict(arrowstyle='<->', color=mlred, lw=2))
ax.text(10.5, 75, 'Overfitting\nGap', fontsize=9, color=mlred, va='center')

ax.set_xlabel('Model Complexity', fontsize=11)
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_title('Complexity vs Performance', fontsize=11, fontweight='bold', color=mlpurple)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 12)
ax.set_ylim(45, 100)

# Warning box
ax.text(6, 48, 'More complexity = More overfitting risk in finance!',
        fontsize=9, ha='center', color=mlred,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor=mlred))

fig.suptitle('Model Selection in Finance: Balancing Complexity and Generalization',
             fontsize=14, fontweight='bold', color=mlpurple, y=1.02)

plt.tight_layout()
plt.savefig('finance_model_comparison.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.savefig('finance_model_comparison.png', format='png', bbox_inches='tight', dpi=300)
plt.close()

print("Generated: finance_model_comparison.pdf")
