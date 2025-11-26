"""
Integration script for 10 new charts into the Neural Networks presentation.
Adds charts at gap-filling positions with concept slides.
"""

import shutil
from datetime import datetime
from pathlib import Path

# File paths
input_file = Path("20251124_1308_neural_networks_refined.tex")
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = Path(f"{timestamp}_neural_networks_20charts.tex")
previous_dir = Path("previous")

# Ensure previous directory exists
previous_dir.mkdir(exist_ok=True)

# Read the input file
content = input_file.read_text(encoding='utf-8')

# ============================================================================
# CHART 11: Problem Visualization - After "The Prediction Challenge" slide
# ============================================================================
chart11_slide = r"""
\begin{frame}[t]{Why Simple Rules Fail: Market Data Complexity}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{11_problem_visualization/problem_visualization.pdf}
\end{center}

\bottomnote{Observe: Can you draw a single line that separates green (up) from red (down) in any panel?}
\end{frame}

"""

# Insert after "The Prediction Challenge" slide
old_after_challenge = r"""\bottomnote{Our journey begins with understanding how nature solved similar prediction problems}
\end{frame}

\begin{frame}[t]{What We Need: A Learning System}"""

new_after_challenge = r"""\bottomnote{Our journey begins with understanding how nature solved similar prediction problems}
\end{frame}
""" + chart11_slide + r"""
\begin{frame}[t]{What We Need: A Learning System}"""

content = content.replace(old_after_challenge, new_after_challenge)

# ============================================================================
# CHART 12: Decision Boundary Concept - After "What We Need" slide
# ============================================================================
chart12_slide = r"""
\begin{frame}[t]{The Goal: Learn Complex Decision Boundaries}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{12_decision_boundary_concept/decision_boundary_concept.pdf}
\end{center}

\bottomnote{Observe: The rightmost panel shows what neural networks can learn - curved boundaries that adapt to data}
\end{frame}

"""

# Insert after "What We Need" slide, before Part 1 divider
old_before_part1 = r"""\bottomnote{Next: Understanding biological neurons as the foundation}
\end{frame}


\begin{frame}[t]
\vfill
\centering
\begin{beamercolorbox}[sep=8pt,center]{title}
\usebeamerfont{title}\Large Part 1: Foundations\par"""

new_before_part1 = r"""\bottomnote{Next: Understanding biological neurons as the foundation}
\end{frame}
""" + chart12_slide + r"""
\begin{frame}[t]
\vfill
\centering
\begin{beamercolorbox}[sep=8pt,center]{title}
\usebeamerfont{title}\Large Part 1: Foundations\par"""

content = content.replace(old_before_part1, new_before_part1)

# ============================================================================
# CHART 13: Neuron as Decision Maker - After biological neuron concept slide
# ============================================================================
chart13_slide = r"""
\begin{frame}[t]{From Concept to Computation: Neuron as Decision Maker}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{13_neuron_decision_maker/neuron_decision_maker.pdf}
\end{center}

\bottomnote{Observe: The decision boundary (purple line) divides the space into BUY and SELL zones based on weighted inputs}
\end{frame}

"""

# Insert after biological neuron concept, before the biological vs artificial chart
old_before_bio_chart = r"""\bottomnote{Next: See the visual comparison of biological vs artificial neurons}
\end{frame}

\begin{frame}[t]{From Biology to Artificial Intelligence}"""

new_before_bio_chart = r"""\bottomnote{Next: See the visual comparison of biological vs artificial neurons}
\end{frame}
""" + chart13_slide + r"""
\begin{frame}[t]{From Biology to Artificial Intelligence}"""

content = content.replace(old_before_bio_chart, new_before_bio_chart)

# ============================================================================
# CHART 14: Sigmoid Saturation - After activation functions chart
# ============================================================================
chart14_slide = r"""
\begin{frame}[t]{Advanced: The Vanishing Gradient Problem}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{14_sigmoid_saturation/sigmoid_saturation.pdf}
\end{center}

\bottomnote{Advanced insight: Sigmoid's tiny gradients in saturation zones slow learning -- ReLU solves this in deep networks}
\end{frame}

"""

# Insert after activation functions chart, before "The Limitation" slide
old_after_activation = r"""\bottomnote{Observe: Where does each function's output change most rapidly? Why does this matter?}
\end{frame}

\begin{frame}[t]{The Limitation: Why One Neuron Is Not Enough}"""

new_after_activation = r"""\bottomnote{Observe: Where does each function's output change most rapidly? Why does this matter?}
\end{frame}
""" + chart14_slide + r"""
\begin{frame}[t]{The Limitation: Why One Neuron Is Not Enough}"""

content = content.replace(old_after_activation, new_after_activation)

# ============================================================================
# CHART 15: Boundary Evolution - After XOR problem chart
# ============================================================================
chart15_slide = r"""
\begin{frame}[t]{Solution: How Adding Neurons Creates Curved Boundaries}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{15_boundary_evolution/boundary_evolution.pdf}
\end{center}

\bottomnote{Key insight: More neurons = more flexibility. Each neuron adds a decision line; combined, they form complex shapes}
\end{frame}

"""

# Insert after XOR chart, before Part 2 discussion
old_after_xor = r"""\bottomnote{Observe: Why is it impossible to draw a single straight line separating orange from blue?}
\end{frame}
\begin{frame}[t]{Discussion: Part 2 Reflection}"""

new_after_xor = r"""\bottomnote{Observe: Why is it impossible to draw a single straight line separating orange from blue?}
\end{frame}
""" + chart15_slide + r"""
\begin{frame}[t]{Discussion: Part 2 Reflection}"""

content = content.replace(old_after_xor, new_after_xor)

# ============================================================================
# CHART 16: Feature Hierarchy - After network architecture chart
# ============================================================================
chart16_slide = r"""
\begin{frame}[t]{What Each Layer ``Sees'': Feature Hierarchy}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{16_feature_hierarchy/feature_hierarchy.pdf}
\end{center}

\bottomnote{Observe: Raw data transforms through layers into increasingly abstract representations until a decision emerges}
\end{frame}

"""

# Insert after network architecture chart, before forward propagation concept
old_after_arch = r"""\bottomnote{Observe: Count the connections. Why are there 36 weights total?}
\end{frame}

\begin{frame}[t]{Forward Propagation: How Networks Make Predictions}"""

new_after_arch = r"""\bottomnote{Observe: Count the connections. Why are there 36 weights total?}
\end{frame}
""" + chart16_slide + r"""
\begin{frame}[t]{Forward Propagation: How Networks Make Predictions}"""

content = content.replace(old_after_arch, new_after_arch)

# ============================================================================
# CHART 17: Overfitting vs Underfitting - After gradient descent chart
# ============================================================================
chart17_slide = r"""
\begin{frame}[t]{Critical Concept: Overfitting vs Underfitting}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{17_overfitting_underfitting/overfitting_underfitting.pdf}
\end{center}

\bottomnote{Key practical skill: Watch for diverging training/validation loss -- that's when to stop training!}
\end{frame}

"""

# Insert after gradient descent chart, before Part 4 discussion
old_after_gd = r"""\bottomnote{Observe: How does the step size (learning rate) affect how quickly we reach the minimum?}
\end{frame}
\begin{frame}[t]{Discussion: Part 4 Reflection}"""

new_after_gd = r"""\bottomnote{Observe: How does the step size (learning rate) affect how quickly we reach the minimum?}
\end{frame}
""" + chart17_slide + r"""
\begin{frame}[t]{Discussion: Part 4 Reflection}"""

content = content.replace(old_after_gd, new_after_gd)

# ============================================================================
# CHART 18: Learning Rate Comparison - After overfitting chart (just added)
# ============================================================================
chart18_slide = r"""
\begin{frame}[t]{Learning Rate in Practice: Finding the Sweet Spot}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{18_learning_rate_comparison/learning_rate_comparison.pdf}
\end{center}

\bottomnote{Practical tip: Start with lr=0.01, then tune based on loss curves. Too high = oscillation, too low = slow}
\end{frame}

"""

# Insert after overfitting chart (just added), before Part 4 discussion
# Update the replacement to include both chart 17 and 18
old_after_chart17 = r"""\bottomnote{Key practical skill: Watch for diverging training/validation loss -- that's when to stop training!}
\end{frame}

\begin{frame}[t]{Discussion: Part 4 Reflection}"""

new_after_chart17 = r"""\bottomnote{Key practical skill: Watch for diverging training/validation loss -- that's when to stop training!}
\end{frame}
""" + chart18_slide + r"""
\begin{frame}[t]{Discussion: Part 4 Reflection}"""

content = content.replace(old_after_chart17, new_after_chart17)

# ============================================================================
# CHART 19: Confusion Matrix - After prediction results chart
# ============================================================================
chart19_slide = r"""
\begin{frame}[t]{Understanding Model Performance: Confusion Matrix}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{19_confusion_matrix/confusion_matrix.pdf}
\end{center}

\bottomnote{Business insight: 70\% accuracy means different things for trading -- precision determines false BUY rate}
\end{frame}

"""

# Insert after prediction results chart, before Part 5 discussion
old_after_results = r"""\bottomnote{Observe: Where does the trained model still make errors? What might explain these?}
\end{frame}
\begin{frame}[t]{Discussion: Part 5 Reflection}"""

new_after_results = r"""\bottomnote{Observe: Where does the trained model still make errors? What might explain these?}
\end{frame}
""" + chart19_slide + r"""
\begin{frame}[t]{Discussion: Part 5 Reflection}"""

content = content.replace(old_after_results, new_after_results)

# ============================================================================
# CHART 20: Trading Backtest - After Part 5 discussion, before summary
# ============================================================================
chart20_slide = r"""
\begin{frame}[t]{The Business Case: Strategy Backtest Results}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{20_trading_backtest/trading_backtest.pdf}
\end{center}

\bottomnote{Bottom line: 70\% accuracy translates to meaningful outperformance -- this is why neural networks matter for business}
\end{frame}

"""

# Insert after Part 5 discussion, before summary
old_before_summary = r"""\end{columns}
\vfill
\end{frame}


\begin{frame}[t]{Summary: Three Key Insights}"""

new_before_summary = r"""\end{columns}
\vfill
\end{frame}
""" + chart20_slide + r"""
\begin{frame}[t]{Summary: Three Key Insights}"""

content = content.replace(old_before_summary, new_before_summary)

# ============================================================================
# SAVE OUTPUT
# ============================================================================

# Move previous version to previous folder
if input_file.exists():
    shutil.copy(input_file, previous_dir / input_file.name)
    print(f"Backed up: {input_file} -> previous/{input_file.name}")

# Write the new content
output_file.write_text(content, encoding='utf-8')
print(f"Created: {output_file}")

# Count slides
slide_count = content.count(r'\begin{frame}')
print(f"\nTotal slides: {slide_count} (was 41, added 10 new chart slides)")

# List new charts added
new_charts = [
    "11. Problem Visualization (after Prediction Challenge)",
    "12. Decision Boundary Concept (before Part 1)",
    "13. Neuron Decision Maker (after bio neuron concept)",
    "14. Sigmoid Saturation (after activation functions)",
    "15. Boundary Evolution (after XOR problem)",
    "16. Feature Hierarchy (after network architecture)",
    "17. Overfitting/Underfitting (after gradient descent)",
    "18. Learning Rate Comparison (after overfitting)",
    "19. Confusion Matrix (after prediction results)",
    "20. Trading Backtest (before summary)"
]

print("\nNew chart slides integrated:")
for chart in new_charts:
    print(f"  {chart}")

print(f"\nOutput file: {output_file}")
