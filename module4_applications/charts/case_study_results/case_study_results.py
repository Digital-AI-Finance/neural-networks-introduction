CHART_METADATA = {
    'title': 'Case Study Results',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/case_study_results'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

np.random.seed(42)

# Left: Cumulative returns comparison
ax1 = axes[0]
days = np.arange(252)
benchmark = 100 * np.exp(np.cumsum(np.random.randn(252) * 0.01))
nn_strategy = 100 * np.exp(np.cumsum(np.random.randn(252) * 0.008 + 0.0002))

ax1.plot(days, benchmark, color=mlgray, lw=2, label='Benchmark (Buy & Hold)')
ax1.plot(days, nn_strategy, color=mlgreen, lw=2, label='NN Strategy')
ax1.fill_between(days, benchmark, nn_strategy, where=nn_strategy > benchmark, alpha=0.3, color=mlgreen)
ax1.fill_between(days, benchmark, nn_strategy, where=nn_strategy < benchmark, alpha=0.3, color=mlred)

ax1.set_xlabel('Trading Days', fontsize=11)
ax1.set_ylabel('Portfolio Value', fontsize=11)
ax1.set_title('Backtest Performance', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# Right: Performance metrics
ax2 = axes[1]
ax2.axis('off')

metrics = [
    ('Metric', 'NN Model', 'Benchmark'),
    ('Annual Return', '12.5%', '8.2%'),
    ('Volatility', '14.2%', '18.5%'),
    ('Sharpe Ratio', '0.88', '0.44'),
    ('Max Drawdown', '-12.3%', '-22.1%'),
    ('Hit Rate', '53.2%', '-'),
    ('Avg Win/Loss', '1.15', '-'),
]

y_pos = 0.9
for row in metrics:
    for i, (text, color) in enumerate(zip(row, [mlgray, mlgreen, mlblue])):
        weight = 'bold' if y_pos > 0.85 else 'normal'
        ax2.text(0.1 + i*0.35, y_pos, text, fontsize=11, color=color, fontweight=weight, ha='left')
    y_pos -= 0.11

ax2.text(0.5, 0.15, 'Note: Results are hypothetical backtest', transform=ax2.transAxes,
         ha='center', fontsize=9, color=mlred, style='italic')
ax2.set_title('Performance Metrics', fontsize=12, fontweight='bold')

plt.suptitle('Case Study: Results Summary', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('case_study_results.pdf', bbox_inches='tight', dpi=300)
plt.savefig('case_study_results.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: case_study_results.pdf")
