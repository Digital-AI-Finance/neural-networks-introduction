"""
Apply final fixes to the presentation:
1. Split Feature Hierarchy into 2 slides (Input+Hidden1, Hidden2+Output)
2. Redesign Summary to Definition-Example two-column layout
"""

import shutil
from datetime import datetime
from pathlib import Path

# File paths
input_file = Path("20251124_1513_neural_networks_20charts.tex")
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = Path(f"{timestamp}_neural_networks_final.tex")
previous_dir = Path("previous")

# Ensure previous directory exists
previous_dir.mkdir(exist_ok=True)

# Read the input file
content = input_file.read_text(encoding='utf-8')

# ============================================================================
# FIX 1: Split Feature Hierarchy into 2 slides
# ============================================================================

# Find and replace the single Feature Hierarchy slide with 2 slides
old_hierarchy_slide = r"""\begin{frame}[t]{What Each Layer ``Sees'': Feature Hierarchy}
\begin{center}
\vspace{0.3em}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{16_feature_hierarchy/feature_hierarchy.pdf}
\end{center}

\bottomnote{Observe: Raw data transforms through layers into increasingly abstract representations until a decision emerges}
\end{frame}"""

new_hierarchy_slides = r"""\begin{frame}[t]{Feature Hierarchy (Part 1): From Raw Data to Patterns}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Input Layer: Raw Numbers}

The network receives:
\begin{itemize}
\item Stock prices: [102.3, 103.1, ...]
\item Trading volume: [1.2M, 0.9M, ...]
\item Sentiment scores: [0.6, 0.5, ...]
\end{itemize}

\vspace{0.3em}
Just numbers -- no meaning yet!

\column{0.48\textwidth}
\textbf{Hidden Layer 1: Simple Patterns}

The first layer detects:
\begin{itemize}
\item \textcolor{mlorange}{Upward trends}
\item \textcolor{mlorange}{Downward trends}
\item \textcolor{mlorange}{Momentum shifts}
\item \textcolor{mlorange}{Volume spikes}
\end{itemize}

\vspace{0.3em}
Finds basic features in the noise
\end{columns}

\bottomnote{First transformation: Raw numbers become recognizable patterns}
\end{frame}

\begin{frame}[t]{Feature Hierarchy (Part 2): From Patterns to Decisions}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Hidden Layer 2: Complex Patterns}

Combines simple patterns:
\begin{itemize}
\item Trend + High volume = \textcolor{mlgreen}{Bullish}
\item Trend + Low volume = \textcolor{mlred}{Bearish}
\item Support/resistance levels
\item Multi-day patterns
\end{itemize}

\vspace{0.3em}
Strategic insights emerge!

\column{0.48\textwidth}
\textbf{Output Layer: Trading Decision}

Final decision:
\begin{itemize}
\item \textcolor{mlgreen}{\textbf{BUY}}: 68\% confidence
\item \textcolor{mlred}{SELL}: 32\% confidence
\end{itemize}

\vspace{0.3em}
Since 68\% $>$ 50\% threshold:

\begin{center}
\Large \textcolor{mlgreen}{\textbf{ACTION: BUY}}
\end{center}
\end{columns}

\bottomnote{Final transformation: Patterns become actionable trading signals}
\end{frame}"""

content = content.replace(old_hierarchy_slide, new_hierarchy_slides)

# ============================================================================
# FIX 2: Redesign Summary to Definition-Example two-column layout
# ============================================================================

old_summary = r"""\begin{frame}[t]{Summary: Three Key Insights}
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

new_summary = r"""\begin{frame}[t]{Summary: Three Key Insights}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Definition}

\vspace{0.3em}
\textcolor{mlpurple}{\textbf{1. Neurons Compute Weighted Sums}}

Each neuron:
$$y = \sigma\left(\sum w_i x_i + b\right)$$

\begin{itemize}
\item Weighted inputs
\item Non-linear activation
\item Parallel processing
\end{itemize}

\vspace{0.5em}
\textcolor{mlpurple}{\textbf{2. Networks Learn from Errors}}

Gradient descent:
$$w_{new} = w_{old} - \eta \nabla L$$

\begin{itemize}
\item Measure prediction error
\item Adjust weights
\item Minimize loss function
\end{itemize}

\vspace{0.5em}
\textcolor{mlpurple}{\textbf{3. Patterns Emerge from Data}}

\begin{itemize}
\item No explicit rules
\item Discovers relationships
\item Generalizes to new data
\end{itemize}

\column{0.48\textwidth}
\textbf{Business Example}

\vspace{0.3em}
\textcolor{mlgreen}{\textit{Market Prediction}}

Input: Price (0.8), Volume (0.6)

Computation:
\begin{itemize}
\item $(0.6 \times 0.8) + (0.4 \times 0.6) = 0.72$
\item $\sigma(0.72) = 0.67$
\item $0.67 > 0.5$ $\rightarrow$ \textbf{BUY}
\end{itemize}

\vspace{0.5em}
\textcolor{mlgreen}{\textit{Learning Process}}

\begin{itemize}
\item Predicted: 55\% rise, Actual: fell
\item Error: $(0 - 0.55)^2 = 0.30$
\item Adjust: Reduce weights on price
\item Next time: Better prediction
\end{itemize}

\vspace{0.5em}
\textcolor{mlgreen}{\textit{Discovered Patterns}}

\begin{itemize}
\item Volume + sentiment $\rightarrow$ direction
\item 70\% accuracy (no manual rules!)
\item Outperforms buy-and-hold
\end{itemize}
\end{columns}

\bottomnote{Master these three principles and you understand neural networks}
\end{frame}"""

content = content.replace(old_summary, new_summary)

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
print(f"\nTotal slides: {slide_count} (was 50, split hierarchy adds 1, total 51)")

print("\nFixes applied:")
print("  1. Chart 15 regenerated with proper bent lines")
print("  2. Feature Hierarchy split into 2 conceptual slides (removed chart)")
print("  3. Summary redesigned to Definition-Example two-column layout")

print(f"\nOutput file: {output_file}")
