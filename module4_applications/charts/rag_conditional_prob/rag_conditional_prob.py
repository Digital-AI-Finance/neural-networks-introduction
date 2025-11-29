CHART_METADATA = {
    'title': 'RAG Conditional Probability Venn Diagram',
    'url': 'https://github.com/QuantLet/neural-networks-introduction/tree/main/rag_conditional_prob'
}

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

mlpurple = '#3333B2'
mlblue = '#0066CC'
mlorange = '#FF7F0E'
mlgreen = '#2CA02C'
mlred = '#D62728'
mlgray = '#7F7F7F'

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: Classic Venn diagram for P(Answer | Query, Documents)
ax1 = axes[0]
ax1.set_xlim(-2, 2.5)
ax1.set_ylim(-1.8, 2)
ax1.set_aspect('equal')
ax1.axis('off')

# Draw three overlapping circles
# Circle 1: Query space (Q)
circle_q = plt.Circle((-0.4, 0.3), 1.0, fill=True, facecolor=mlblue, alpha=0.3,
                       edgecolor=mlblue, linewidth=2.5, label='Query (x)')
ax1.add_patch(circle_q)

# Circle 2: Document space (D)
circle_d = plt.Circle((0.6, 0.3), 1.0, fill=True, facecolor=mlorange, alpha=0.3,
                       edgecolor=mlorange, linewidth=2.5, label='Documents (z)')
ax1.add_patch(circle_d)

# Circle 3: Answer space (A)
circle_a = plt.Circle((0.1, -0.5), 0.9, fill=True, facecolor=mlgreen, alpha=0.3,
                       edgecolor=mlgreen, linewidth=2.5, label='Answer (y)')
ax1.add_patch(circle_a)

# Highlight the triple intersection (the RAG sweet spot)
from matplotlib.patches import Wedge, PathPatch
from matplotlib.path import Path

# Mark the center intersection region
ax1.plot(0.1, 0.0, 'o', markersize=15, color=mlpurple, zorder=5)
ax1.annotate('P(y|x,z)', (0.1, 0.0), (0.1, 0.4), fontsize=12, fontweight='bold',
             color=mlpurple, ha='center',
             arrowprops=dict(arrowstyle='->', color=mlpurple, lw=2))

# Labels for each circle
ax1.text(-1.1, 0.8, 'Query\n(x)', fontsize=11, ha='center', color=mlblue, fontweight='bold')
ax1.text(1.3, 0.8, 'Retrieved\nDocs (z)', fontsize=11, ha='center', color=mlorange, fontweight='bold')
ax1.text(0.1, -1.2, 'Answer (y)', fontsize=11, ha='center', color=mlgreen, fontweight='bold')

# Annotations for regions
ax1.text(-0.9, -0.1, 'P(x)', fontsize=9, ha='center', color=mlblue, alpha=0.8)
ax1.text(1.1, -0.1, 'P(z|x)', fontsize=9, ha='center', color=mlorange, alpha=0.8)

ax1.set_title('RAG: Conditional Probability Spaces', fontsize=13, fontweight='bold', pad=15)

# Right: Concrete example with numerical values
ax2 = axes[1]
ax2.set_xlim(-2, 2.5)
ax2.set_ylim(-1.8, 2)
ax2.set_aspect('equal')
ax2.axis('off')

# Same three circles but with concrete example
# Query: "What is the capital of France?"
# Documents: Retrieved relevant docs
# Answer: "Paris"

circle_q2 = plt.Circle((-0.4, 0.3), 1.0, fill=True, facecolor=mlblue, alpha=0.25,
                        edgecolor=mlblue, linewidth=2)
ax2.add_patch(circle_q2)

circle_d2 = plt.Circle((0.6, 0.3), 1.0, fill=True, facecolor=mlorange, alpha=0.25,
                        edgecolor=mlorange, linewidth=2)
ax2.add_patch(circle_d2)

circle_a2 = plt.Circle((0.1, -0.5), 0.9, fill=True, facecolor=mlgreen, alpha=0.25,
                        edgecolor=mlgreen, linewidth=2)
ax2.add_patch(circle_a2)

# Concrete probability values in regions
ax2.text(-1.0, 0.6, 'Query:\n"Capital of\nFrance?"', fontsize=9, ha='center',
         color=mlblue, fontweight='bold', style='italic')

ax2.text(1.2, 0.6, 'Retrieved:\n"France...Paris\nis the capital"', fontsize=8, ha='center',
         color=mlorange, fontweight='bold', style='italic')

ax2.text(0.1, -1.3, 'Answer: "Paris"', fontsize=10, ha='center',
         color=mlgreen, fontweight='bold', style='italic')

# Central intersection with probability
ax2.plot(0.1, 0.0, 'o', markersize=20, color=mlpurple, alpha=0.7, zorder=5)
ax2.text(0.1, 0.0, '95%', fontsize=10, ha='center', va='center',
         color='white', fontweight='bold', zorder=6)

# Show the marginalization formula below
ax2.text(0.1, -1.65, r'$P(y|x) = \sum_z P(y|x,z) \cdot P(z|x)$', fontsize=11,
         ha='center', color=mlpurple, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor=mlpurple, alpha=0.9))

ax2.set_title('Concrete Example: Question Answering', fontsize=13, fontweight='bold', pad=15)

# Add legend at bottom
handles = [
    patches.Patch(facecolor=mlblue, alpha=0.3, edgecolor=mlblue, linewidth=2, label='Query Space (x)'),
    patches.Patch(facecolor=mlorange, alpha=0.3, edgecolor=mlorange, linewidth=2, label='Document Space (z)'),
    patches.Patch(facecolor=mlgreen, alpha=0.3, edgecolor=mlgreen, linewidth=2, label='Answer Space (y)'),
]
fig.legend(handles=handles, loc='lower center', ncol=3, fontsize=10, frameon=True,
           bbox_to_anchor=(0.5, 0.02))

plt.suptitle('RAG Formula: A Concrete Example', fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.08, 1, 0.95])
plt.savefig('rag_conditional_prob.pdf', bbox_inches='tight', dpi=300)
plt.savefig('rag_conditional_prob.png', bbox_inches='tight', dpi=300)
plt.close()
print("Generated: rag_conditional_prob.pdf")
