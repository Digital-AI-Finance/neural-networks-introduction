CHART_METADATA = {
    'title': 'Backtest Trap',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/backtest_trap'
}

import matplotlib.pyplot as plt
import numpy as np

# Color palette
mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

np.random.seed(42)

# Left: Overfitted backtest vs reality
ax1 = axes[0]
days = np.arange(0, 500)

# Backtest performance (looks great)
backtest = 100 * np.exp(0.0008 * days + 0.01 * np.random.randn(len(days)).cumsum() * 0.1)

# Live performance (reality)
live_start = 300
live_days = days[live_start:]
live = backtest[live_start] * np.exp(-0.0003 * (live_days - live_start) + 0.015 * np.random.randn(len(live_days)).cumsum() * 0.1)

ax1.plot(days[:live_start], backtest[:live_start], color=mlgreen, lw=2, label='Backtest (In-sample)')
ax1.plot(days[live_start:], backtest[live_start:], '--', color=mlgreen, lw=2, alpha=0.5, label='Backtest (Extrapolated)')
ax1.plot(live_days, live, color=mlred, lw=2, label='Live Trading (Out-of-sample)')
ax1.axvline(x=live_start, color=mlgray, linestyle='--', lw=1.5)
ax1.text(live_start + 5, 180, 'Go Live', fontsize=10, color=mlgray)

ax1.set_xlabel('Trading Days', fontsize=11)
ax1.set_ylabel('Portfolio Value', fontsize=11)
ax1.set_title('The Backtest Trap: Overfitting to History', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# Right: Why it happens
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

causes = [
    (5, 8.5, 'Common Causes of Backtest Overfitting', mlpurple, 13),
    (1, 7, '1. Look-ahead bias', mlred, 10),
    (1, 6, '   Using future data in decisions', mlgray, 9),
    (1, 5, '2. Survivorship bias', mlred, 10),
    (1, 4, '   Only testing on surviving stocks', mlgray, 9),
    (1, 3, '3. Data snooping', mlred, 10),
    (1, 2, '   Testing many strategies, reporting best', mlgray, 9),
    (1, 1, '4. Transaction costs ignored', mlred, 10),
]

for x, y, text, color, size in causes:
    weight = 'bold' if size > 9 else 'normal'
    ax2.text(x, y, text, fontsize=size, color=color, fontweight=weight, ha='left' if x == 1 else 'center')

# Warning box
rect = plt.Rectangle((5.5, 0.5), 4, 3, fill=True, color=mlorange, alpha=0.2, ec=mlorange, lw=2)
ax2.add_patch(rect)
ax2.text(7.5, 3, 'Solution:', fontsize=11, fontweight='bold', ha='center', color=mlorange)
ax2.text(7.5, 2.2, 'Walk-forward\nvalidation', fontsize=10, ha='center', color=mlorange)
ax2.text(7.5, 1.2, 'Out-of-sample\ntesting', fontsize=10, ha='center', color=mlorange)

plt.tight_layout()
plt.savefig('backtest_trap.pdf', bbox_inches='tight', dpi=300)
plt.savefig('backtest_trap.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: backtest_trap.pdf")
