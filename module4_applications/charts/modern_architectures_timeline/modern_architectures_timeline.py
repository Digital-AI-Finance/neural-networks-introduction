CHART_METADATA = {
    'title': 'Modern Architectures Timeline',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/modern_architectures_timeline'
}

import matplotlib.pyplot as plt
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, ax = plt.subplots(1, 1, figsize=(14, 6))
ax.set_xlim(2011, 2025)
ax.set_ylim(0, 10)
ax.axis('off')

ax.axhline(y=5, color=mlgray, lw=3, alpha=0.5)

events = [
    (2012, 'AlexNet', 'CNN revolution', mlgreen, 7),
    (2014, 'VGG/GoogLeNet', 'Deeper nets', mlgreen, 3),
    (2015, 'ResNet', 'Skip connections', mlgreen, 7),
    (2017, 'Transformer', 'Attention is all you need', mlred, 3),
    (2018, 'BERT', 'Bidirectional LM', mlred, 7),
    (2019, 'GPT-2', 'Large language model', mlred, 3),
    (2020, 'GPT-3', '175B parameters', mlred, 7),
    (2022, 'ChatGPT', 'RLHF breakthrough', mlpurple, 3),
    (2023, 'GPT-4', 'Multimodal', mlpurple, 7),
    (2024, 'Claude/Gemini', 'Competition', mlpurple, 3),
]

for year, name, desc, color, y_pos in events:
    ax.plot(year, 5, 'o', color=color, markersize=12, zorder=5)
    ax.plot([year, year], [5, y_pos], '-', color=color, lw=2)
    ax.text(year, y_pos + (0.4 if y_pos > 5 else -0.4), f'{name}\n({desc})',
            ha='center', va='bottom' if y_pos > 5 else 'top', fontsize=8, color=color, fontweight='bold')

# Year labels
for year in range(2012, 2025, 2):
    ax.text(year, 4.3, str(year), ha='center', fontsize=8, color=mlgray)

# Era labels
ax.axvspan(2011, 2016.5, alpha=0.1, color=mlgreen)
ax.axvspan(2016.5, 2021.5, alpha=0.1, color=mlred)
ax.axvspan(2021.5, 2025, alpha=0.1, color=mlpurple)

ax.text(2014, 9.5, 'CNN Era', ha='center', fontsize=11, color=mlgreen, fontweight='bold')
ax.text(2019, 9.5, 'Transformer Era', ha='center', fontsize=11, color=mlred, fontweight='bold')
ax.text(2023, 9.5, 'LLM Era', ha='center', fontsize=11, color=mlpurple, fontweight='bold')

ax.set_title('Modern Deep Learning Architectures: 2012-2024', fontsize=14, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('modern_architectures_timeline.pdf', bbox_inches='tight', dpi=300)
plt.savefig('modern_architectures_timeline.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: modern_architectures_timeline.pdf")
