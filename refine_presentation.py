"""
Final pedagogical refinements for the Neural Networks presentation.
Adds: worked calculation, simplified summary, bridging text, quick quiz.
"""

import shutil
from datetime import datetime
from pathlib import Path

# File paths
input_file = Path("20251124_1257_neural_networks_pedagogical.tex")
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = Path(f"{timestamp}_neural_networks_refined.tex")
previous_dir = Path("previous")

# Ensure previous directory exists
previous_dir.mkdir(exist_ok=True)

# Read the input file
content = input_file.read_text(encoding='utf-8')

# ============================================================================
# 1. ADD WORKED CALCULATION EXERCISE
# ============================================================================
# Insert after "The Artificial Neuron: Mathematical Model" slide, before chart

worked_calculation_slide = r"""
\begin{frame}[t]{Practice: Calculate a Neuron's Output}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Given Values}

\begin{itemize}
\item Inputs: $x_1 = 1.2$, $x_2 = 0.8$
\item Weights: $w_1 = 0.3$, $w_2 = 0.5$
\item Bias: $b = -0.2$
\end{itemize}

\vspace{0.5em}
\textbf{Step 1: Weighted Sum}

$z = w_1 x_1 + w_2 x_2 + b$

$z = (0.3)(1.2) + (0.5)(0.8) + (-0.2)$

$z = 0.36 + 0.40 - 0.20 = \textbf{0.56}$

\column{0.48\textwidth}
\textbf{Step 2: Apply Sigmoid}

$$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-0.56}}$$

$\sigma(0.56) = \frac{1}{1 + 0.571} = \frac{1}{1.571} = \textbf{0.636}$

\vspace{0.5em}
\textbf{Interpretation}

63.6\% confidence: price will rise

\vspace{0.5em}
\textcolor{mlblue}{\textbf{Your Turn:}} What if $w_1 = 0.6$?
\end{columns}

\bottomnote{Work through this calculation -- it's the foundation of all neural network predictions}
\end{frame}

"""

# Find insertion point: after mathematical model slide, before chart
old_chart_intro = r"""\begin{frame}[t]{Single Neuron Computation: Step-by-Step Example}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{02_single_neuron_function/single_neuron_computation.pdf}"""

new_chart_intro = worked_calculation_slide + old_chart_intro

content = content.replace(old_chart_intro, new_chart_intro)

# ============================================================================
# 2. SIMPLIFY SUMMARY SLIDE TO 3 KEY POINTS
# ============================================================================

old_summary = r"""\begin{frame}[t]{Summary: From Neurons to Predictions}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Our Journey}

\begin{enumerate}
\item Biological inspiration
\item Mathematical model
\item Activation functions
\item Network architecture
\item Forward propagation
\end{enumerate}

\column{0.48\textwidth}
\textbf{Learning Process}

\begin{enumerate}
\setcounter{enumi}{5}
\item Loss functions
\item Gradient descent
\item Training iterations
\item Pattern discovery
\item Improved predictions
\end{enumerate}
\end{columns}

\vspace{0.5cm}
\begin{block}{Key Takeaway}
Neural networks \textbf{learn patterns from data} rather than following explicit rules. This enables them to discover complex relationships that would be impossible to program manually.
\end{block}

\bottomnote{Each concept was paired with a visualization to reinforce understanding}
\end{frame}"""

new_summary = r"""\begin{frame}[t]{Summary: Three Key Insights}
\vspace{0.5cm}

\begin{block}{\Large 1. Neurons Compute Weighted Sums}
\large
Each artificial neuron multiplies inputs by learned weights, adds a bias, and applies a non-linear activation function. This simple operation, repeated across layers, enables complex pattern recognition.
\end{block}

\vspace{0.3cm}
\begin{block}{\Large 2. Networks Learn from Errors}
\large
Training uses gradient descent to minimize prediction errors. The network adjusts weights in the direction that reduces loss -- like a trader learning from past mistakes.
\end{block}

\vspace{0.3cm}
\begin{block}{\Large 3. Patterns Emerge from Data}
\large
Neural networks discover relationships we never explicitly programmed. They find what matters in the data, enabling predictions for complex, non-linear business problems.
\end{block}

\bottomnote{These three principles underpin all deep learning -- master them and you understand neural networks}
\end{frame}"""

content = content.replace(old_summary, new_summary)

# ============================================================================
# 3. ADD BRIDGING TEXT TO SECTION DIVIDERS
# ============================================================================

# Part 1 divider
old_part1 = r"""{\normalsize From biological neurons to artificial intelligence}
\vspace{0.5cm}

{\small \textcolor{mlpurple}{\textbf{[1]}} -- \textcolor{mllavender2}{[2]} -- \textcolor{mllavender2}{[3]} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

new_part1 = r"""{\normalsize From biological neurons to artificial intelligence}
\vspace{0.3cm}

\textit{Let's begin with the inspiration from nature}
\vspace{0.3cm}

{\small \textcolor{mlpurple}{\textbf{[1]}} -- \textcolor{mllavender2}{[2]} -- \textcolor{mllavender2}{[3]} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

content = content.replace(old_part1, new_part1)

# Part 2 divider
old_part2 = r"""{\normalsize Activation functions and their role in learning}
\vspace{0.5cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlpurple}{\textbf{[2]}} -- \textcolor{mllavender2}{[3]} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

new_part2 = r"""{\normalsize Activation functions and their role in learning}
\vspace{0.3cm}

\textit{Now that we understand neurons, let's explore what makes them powerful}
\vspace{0.3cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlpurple}{\textbf{[2]}} -- \textcolor{mllavender2}{[3]} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

content = content.replace(old_part2, new_part2)

# Part 3 divider
old_part3 = r"""{\normalsize Building layers of intelligence}
\vspace{0.5cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlpurple}{\textbf{[3]}} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

new_part3 = r"""{\normalsize Building layers of intelligence}
\vspace{0.3cm}

\textit{With building blocks ready, let's construct full networks}
\vspace{0.3cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlpurple}{\textbf{[3]}} -- \textcolor{mllavender2}{[4]} -- \textcolor{mllavender2}{[5]}}"""

content = content.replace(old_part3, new_part3)

# Part 4 divider
old_part4 = r"""{\normalsize How networks learn from mistakes}
\vspace{0.5cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlgray}{[3]} -- \textcolor{mlpurple}{\textbf{[4]}} -- \textcolor{mllavender2}{[5]}}"""

new_part4 = r"""{\normalsize How networks learn from mistakes}
\vspace{0.3cm}

\textit{We can make predictions -- now let's learn how to improve them}
\vspace{0.3cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlgray}{[3]} -- \textcolor{mlpurple}{\textbf{[4]}} -- \textcolor{mllavender2}{[5]}}"""

content = content.replace(old_part4, new_part4)

# Part 5 divider
old_part5 = r"""{\normalsize Putting it all together with market prediction}
\vspace{0.5cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlgray}{[3]} -- \textcolor{mlgray}{[4]} -- \textcolor{mlpurple}{\textbf{[5]}}}"""

new_part5 = r"""{\normalsize Putting it all together with market prediction}
\vspace{0.3cm}

\textit{Theory complete -- let's apply everything to a real case}
\vspace{0.3cm}

{\small \textcolor{mlgray}{[1]} -- \textcolor{mlgray}{[2]} -- \textcolor{mlgray}{[3]} -- \textcolor{mlgray}{[4]} -- \textcolor{mlpurple}{\textbf{[5]}}}"""

content = content.replace(old_part5, new_part5)

# ============================================================================
# 4. ADD QUICK QUIZ SLIDE WITH ANSWERS
# ============================================================================

quiz_slide = r"""
\begin{frame}[t]{Quick Check: Test Your Understanding}
\begin{columns}[T]
\column{0.55\textwidth}
\textbf{Q1: What does the activation function do?}
\begin{enumerate}[(a)]
\item Stores the input data
\item \textcolor{mlgreen}{\textbf{Adds non-linearity to enable complex patterns}}
\item Calculates the learning rate
\end{enumerate}

\vspace{0.3em}
\textbf{Q2: Why do we need multiple layers?}
\begin{enumerate}[(a)]
\item To make training faster
\item To use more data
\item \textcolor{mlgreen}{\textbf{To learn hierarchical, complex patterns}}
\end{enumerate}

\vspace{0.3em}
\textbf{Q3: What does gradient descent minimize?}
\begin{enumerate}[(a)]
\item The number of neurons
\item \textcolor{mlgreen}{\textbf{The prediction error (loss function)}}
\item The training time
\end{enumerate}

\column{0.42\textwidth}
\textbf{Check Your Answers}

\vspace{0.5em}
\begin{block}{Answer Key}
\begin{itemize}
\item Q1: (b) Non-linearity
\item Q2: (c) Hierarchical patterns
\item Q3: (b) Loss/error
\end{itemize}
\end{block}

\vspace{0.3em}
\textbf{Scoring}
\begin{itemize}
\item 3/3: Excellent grasp!
\item 2/3: Review that topic
\item 1/3: Revisit core concepts
\end{itemize}
\end{columns}

\bottomnote{If any answer surprised you, go back and review that section}
\end{frame}

"""

# Insert quiz after summary, before "When to Use"
old_when_to_use = r"""\begin{frame}[t]{When to Use Neural Networks}"""
new_when_to_use = quiz_slide + old_when_to_use

content = content.replace(old_when_to_use, new_when_to_use)

# ============================================================================
# SAVE OUTPUT
# ============================================================================

# Move previous version to previous folder
if input_file.exists():
    shutil.copy(input_file, previous_dir / input_file.name)
    print(f"Backed up: {input_file} -> previous/{input_file.name}")

# Write the refined content
output_file.write_text(content, encoding='utf-8')
print(f"Created: {output_file}")

# Count changes
changes = [
    "1. Added worked calculation exercise slide (after mathematical model)",
    "2. Simplified summary to 3 memorable key insights",
    "3. Added bridging text to all 5 section dividers",
    "4. Added quick quiz slide with 3 questions and answers"
]

print("\nRefinements applied:")
for change in changes:
    print(f"  {change}")

# Estimate page count
slide_count = content.count(r'\begin{frame}')
print(f"\nTotal slides: {slide_count} (was 39, added 2 new slides)")
print(f"Output file: {output_file}")
