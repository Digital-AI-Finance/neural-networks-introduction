# ==============================================================================
# Chart: Prediction Results
# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/10_prediction_results/
# Author: Digital-AI-Finance
# License: MIT License
# Created: 2025-11-23
# ==============================================================================

"""
Prediction Results

Neural network visualization chart

Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/10_prediction_results/
"""

CHART_METADATA = {
    'name': 'Prediction Results',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/10_prediction_results',
    'author': 'Digital-AI-Finance',
    'license': 'MIT License',
    'created': '2025-11-23',
    'description': 'Neural network visualization chart'
}

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.3)

fig.suptitle('Neural Network Performance: Before vs After Training', fontsize=16, fontweight='bold')

# Generate synthetic data
np.random.seed(42)
days_test = 30
dates = np.arange(days_test)

# Actual prices
base_price = 105
trend = np.linspace(0, 8, days_test)
noise = np.random.randn(days_test) * 1.5
actual_price = base_price + trend + noise

# Actual direction (1 = up, 0 = down)
price_change = np.diff(actual_price, prepend=actual_price[0])
actual_direction = (price_change > 0).astype(int)

# BEFORE TRAINING: Random predictions (basically coin flip)
before_predictions = np.random.choice([0, 1], size=days_test)
before_accuracy = np.mean(before_predictions == actual_direction)

# AFTER TRAINING: Much better predictions (70% accuracy)
# Copy actual with some random errors
after_predictions = actual_direction.copy()
# Introduce 30% errors
error_indices = np.random.choice(days_test, size=int(days_test * 0.3), replace=False)
after_predictions[error_indices] = 1 - after_predictions[error_indices]
after_accuracy = np.mean(after_predictions == actual_direction)

# TOP ROW: Actual Prices
ax_actual = fig.add_subplot(gs[0, :])
ax_actual.plot(dates, actual_price, 'k-', linewidth=3, label='Actual Price', marker='o')
ax_actual.scatter(dates[actual_direction == 1], actual_price[actual_direction == 1],
                 color='green', s=100, marker='^', edgecolors='darkgreen', linewidth=2,
                 label='Actual: Price Up', zorder=5)
ax_actual.scatter(dates[actual_direction == 0], actual_price[actual_direction == 0],
                 color='red', s=100, marker='v', edgecolors='darkred', linewidth=2,
                 label='Actual: Price Down', zorder=5)
ax_actual.set_xlabel('Day', fontsize=11)
ax_actual.set_ylabel('Stock Price ($)', fontsize=11)
ax_actual.set_title('Ground Truth: Actual Price Movement', fontsize=12, fontweight='bold')
ax_actual.legend(loc='upper left', fontsize=9)
ax_actual.grid(True, alpha=0.3)

# MIDDLE LEFT: Before Training
ax_before = fig.add_subplot(gs[1, 0])
# Show prediction accuracy
correct_before = (before_predictions == actual_direction)
x_pos = np.arange(days_test)

colors_before = ['green' if c else 'red' for c in correct_before]
ax_before.bar(x_pos[before_predictions == 1], np.ones(np.sum(before_predictions == 1)),
             color='lightblue', alpha=0.6, label='Predicted: Up', edgecolor='blue')
ax_before.bar(x_pos[before_predictions == 0], -np.ones(np.sum(before_predictions == 0)),
             color='lightcoral', alpha=0.6, label='Predicted: Down', edgecolor='red')

# Mark correct vs incorrect
for i, (pred, actual, correct) in enumerate(zip(before_predictions, actual_direction, correct_before)):
    marker = 'o' if correct else 'x'
    color = 'green' if correct else 'red'
    y_pos = 1 if pred == 1 else -1
    ax_before.plot(i, y_pos, marker, color=color, markersize=8, markeredgewidth=2)

ax_before.axhline(y=0, color='black', linewidth=1)
ax_before.set_xlabel('Day', fontsize=10)
ax_before.set_ylabel('Prediction', fontsize=10)
ax_before.set_title(f'BEFORE Training: Random Guessing\nAccuracy: {before_accuracy:.1%}',
                   fontsize=11, fontweight='bold', color='red')
ax_before.set_ylim([-1.5, 1.5])
ax_before.set_yticks([-1, 1])
ax_before.set_yticklabels(['Down', 'Up'])
ax_before.legend(loc='upper right', fontsize=8)
ax_before.grid(True, alpha=0.3, axis='x')

# MIDDLE RIGHT: After Training
ax_after = fig.add_subplot(gs[1, 1])
correct_after = (after_predictions == actual_direction)

colors_after = ['green' if c else 'red' for c in correct_after]
ax_after.bar(x_pos[after_predictions == 1], np.ones(np.sum(after_predictions == 1)),
            color='lightblue', alpha=0.6, label='Predicted: Up', edgecolor='blue')
ax_after.bar(x_pos[after_predictions == 0], -np.ones(np.sum(after_predictions == 0)),
            color='lightcoral', alpha=0.6, label='Predicted: Down', edgecolor='red')

# Mark correct vs incorrect
for i, (pred, actual, correct) in enumerate(zip(after_predictions, actual_direction, correct_after)):
    marker = 'o' if correct else 'x'
    color = 'green' if correct else 'red'
    y_pos = 1 if pred == 1 else -1
    ax_after.plot(i, y_pos, marker, color=color, markersize=8, markeredgewidth=2)

ax_after.axhline(y=0, color='black', linewidth=1)
ax_after.set_xlabel('Day', fontsize=10)
ax_after.set_ylabel('Prediction', fontsize=10)
ax_after.set_title(f'AFTER Training: Learned Patterns\nAccuracy: {after_accuracy:.1%}',
                  fontsize=11, fontweight='bold', color='green')
ax_after.set_ylim([-1.5, 1.5])
ax_after.set_yticks([-1, 1])
ax_after.set_yticklabels(['Down', 'Up'])
ax_after.legend(loc='upper right', fontsize=8)
ax_after.grid(True, alpha=0.3, axis='x')

# BOTTOM: Comparison Metrics
ax_metrics = fig.add_subplot(gs[2, :])

# Create a bar chart comparing metrics
metrics = ['Accuracy', 'Correct\nPredictions', 'Wrong\nPredictions']
before_values = [before_accuracy * 100,
                np.sum(correct_before),
                np.sum(~correct_before)]
after_values = [after_accuracy * 100,
               np.sum(correct_after),
               np.sum(~correct_after)]

x = np.arange(len(metrics))
width = 0.35

bars1 = ax_metrics.bar(x - width/2, before_values, width, label='Before Training',
                       color='lightcoral', edgecolor='darkred', linewidth=2)
bars2 = ax_metrics.bar(x + width/2, after_values, width, label='After Training',
                       color='lightgreen', edgecolor='darkgreen', linewidth=2)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax_metrics.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.0f}' if height > 10 else f'{height:.1f}',
                       ha='center', va='bottom', fontsize=10, fontweight='bold')

ax_metrics.set_ylabel('Value', fontsize=11)
ax_metrics.set_title('Performance Comparison', fontsize=12, fontweight='bold')
ax_metrics.set_xticks(x)
ax_metrics.set_xticklabels(metrics, fontsize=10)
ax_metrics.legend(fontsize=10, loc='upper left')
ax_metrics.grid(True, alpha=0.3, axis='y')

# Add improvement annotation
improvement = after_accuracy - before_accuracy
arrow_y = max(before_values[0], after_values[0]) + 5
ax_metrics.annotate('', xy=(0 + width/2, after_values[0]), xytext=(0 - width/2, before_values[0]),
                   arrowprops=dict(arrowstyle='->', lw=3, color='darkgreen'))
ax_metrics.text(0, arrow_y + 3, f'+{improvement:.1%}\nImprovement', ha='center', fontsize=10,
               fontweight='bold', color='darkgreen',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# Add conclusion
conclusion = 'Training transforms random guessing into intelligent prediction by learning patterns from data'
fig.text(0.5, 0.01, conclusion, ha='center', fontsize=11, style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
plt.savefig('prediction_results.pdf', bbox_inches='tight', dpi=300)
print("Chart saved: prediction_results.pdf")

# Source: https://github.com/Digital-AI-Finance/neural-networks/tree/main/10_prediction_results/
