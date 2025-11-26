"""
Transform Neural Networks presentation to new layout structure.
- Concept slides: Definition-Example format (Layout 9)
- Chart slides: Full-Size Chart format (Layout 21)
"""

import re
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
SOURCE_FILE = "20251123_1616_neural_networks_template.tex"
PREVIOUS_DIR = Path("previous")
PREVIOUS_DIR.mkdir(exist_ok=True)

# Generate new filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
NEW_FILE = f"{timestamp}_neural_networks_layouts.tex"

# Read source file
with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Move previous version to previous/ folder
shutil.copy(SOURCE_FILE, PREVIOUS_DIR / SOURCE_FILE)
print(f"Backed up: {SOURCE_FILE} -> {PREVIOUS_DIR / SOURCE_FILE}")

# Define the new layouts

CHART_SLIDE_TEMPLATE = r"""\begin{{frame}}[t]{{{title}}}
\begin{{center}}
\vspace{{0.3em}}
\includegraphics[width=0.95\textwidth,height=0.80\textheight,keepaspectratio]{{{chart_path}}}
\end{{center}}

\bottomnote{{{bottomnote}}}
\end{{frame}}"""

# Chart slides mapping: frame title -> (chart_path, bottomnote)
CHART_SLIDES = {
    "From Biology to Artificial Intelligence": (
        "01_biological_neuron/biological_vs_artificial.pdf",
        "The artificial neuron mathematically mimics biological signal integration and activation"
    ),
    "Single Neuron Computation: Step-by-Step Example": (
        "02_single_neuron_function/single_neuron_computation.pdf",
        "With market inputs (price=100, volume=85, sentiment=120), the neuron predicts 100\\% probability of price increase"
    ),
    "Activation Functions: Visual Comparison": (
        "03_activation_functions/activation_functions.pdf",
        "Each activation function has different properties: Sigmoid for probabilities, ReLU for speed, Tanh for zero-centered outputs"
    ),
    "Visual Proof: The XOR Problem": (
        "04_linear_limitation/linear_limitation.pdf",
        "Left: Linearly separable (one neuron works). Right: XOR pattern (one neuron fails, need hidden layers)"
    ),
    "Neural Network Architecture Diagram": (
        "05_network_architecture/network_architecture.pdf",
        "5 inputs $\\rightarrow$ 6 hidden neurons $\\rightarrow$ 1 output. Total: 36 weights to learn from data"
    ),
    "Forward Propagation: Detailed Example": (
        "06_forward_propagation/forward_propagation.pdf",
        "Data flows left to right: inputs (105.2, 0.75, 0.62) $\\rightarrow$ hidden activations $\\rightarrow$ output (0.742) = 74\\% buy confidence"
    ),
    "Loss Landscape: The Error Surface": (
        "07_loss_landscape/loss_landscape.pdf",
        "Goal: Find weights (red star) that minimize loss. Different starting points converge to same optimum through gradient descent"
    ),
    "Gradient Descent: Optimization in Action": (
        "08_gradient_descent/gradient_descent.pdf",
        "Left: 1D visualization showing steps toward minimum. Right: Loss decreasing over 100 training iterations"
    ),
    "Market Data: Input Features for Neural Network": (
        "09_market_prediction_data/market_prediction_data.pdf",
        "60 days of market data: price trend (up/down markers), volume bars, sentiment score, volatility index"
    ),
    "Prediction Results: Before vs After Training": (
        "10_prediction_results/prediction_results.pdf",
        "Top: Actual prices. Middle: Before training (random, 50\\% accuracy). After training (learned patterns, 70\\% accuracy)"
    ),
}

# Concept slides to transform to Definition-Example format
CONCEPT_SLIDES = {
    "Nature's Computer: How Your Brain Makes Predictions": {
        "definition": r"""\textbf{Biological Neuron Structure}

\begin{itemize}
\item \textbf{Dendrites:} Receive signals from other neurons
\item \textbf{Soma:} Integrates incoming signals with weights
\item \textbf{Axon:} Transmits output to next neurons
\item \textbf{Synapses:} Connection points with varying strengths
\end{itemize}

\vspace{0.3em}
\textbf{Key Principle}

Neurons process multiple weighted inputs and fire when threshold is exceeded.""",
        "example": r"""\textbf{Business AI Insights}

\begin{enumerate}
\item \textcolor{mlblue}{Multiple inputs combined}\\
$\rightarrow$ Consider many market factors
\item \textcolor{mlblue}{Weighted connections}\\
$\rightarrow$ Some factors matter more
\item \textcolor{mlblue}{Non-linear activation}\\
$\rightarrow$ Threshold effects (tipping points)
\item \textcolor{mlblue}{Layered processing}\\
$\rightarrow$ Abstract reasoning emerges
\end{enumerate}

\vspace{0.3em}
\textit{We can create mathematical models that learn the same way!}""",
        "bottomnote": "Next: See the visual comparison of biological vs artificial neurons"
    },
    "The Artificial Neuron: Mathematical Model": {
        "definition": r"""\textbf{Step 1: Weighted Sum}

Mimics soma integration:
$$z = \sum_{i=1}^{n} w_i x_i + b$$

\begin{itemize}
\item $x_i$: Input features (market data)
\item $w_i$: Weights (\textcolor{mlred}{learned from data})
\item $b$: Bias term (baseline adjustment)
\end{itemize}

\vspace{0.3em}
\textit{Like dendrites weighting signals differently}""",
        "example": r"""\textbf{Step 2: Activation Function}

Mimics axon firing:
$$y = f(z) = \frac{1}{1+e^{-z}}$$

\begin{itemize}
\item $f$: Activation function (non-linearity)
\item Output: probability between 0 and 1
\item Mimics neuron ``firing'' at threshold
\end{itemize}

\vspace{0.3em}
\textbf{Complete Formula:}
$$y = \sigma\left(\sum_{i=1}^{n} w_i x_i + b\right)$$""",
        "bottomnote": "Next: See a concrete example with real market numbers"
    },
    "Activation Functions: Why Non-Linearity Matters": {
        "definition": r"""\textbf{The Problem}

Without activation functions:
\begin{itemize}
\item Neural networks = fancy linear regression
\item Real business relationships are \textcolor{mlred}{non-linear}!
\end{itemize}

\vspace{0.3em}
\textbf{Three Common Functions}

\begin{itemize}
\item \textbf{Sigmoid:} Smooth (0,1) range\\
Perfect for probabilities
\item \textbf{ReLU:} Fast, efficient\\
Most popular in modern networks
\item \textbf{Tanh:} Zero-centered (-1,1)\\
Alternative to sigmoid
\end{itemize}""",
        "example": r"""\textbf{Business Non-Linearity Examples}

\begin{enumerate}
\item \textbf{Diminishing returns}\\
Doubling marketing spend doesn't double sales
\item \textbf{Threshold effects}\\
Sentiment must reach tipping point
\item \textbf{Saturation}\\
Engagement plateaus beyond certain point
\item \textbf{Network effects}\\
Value increases non-linearly with users
\end{enumerate}

\vspace{0.3em}
\textit{Activation functions let networks capture these patterns!}""",
        "bottomnote": "Next: Visual comparison of these three activation functions"
    },
    "The Limitation: Why One Neuron Is Not Enough": {
        "definition": r"""\textbf{What One Neuron Can Do}

\begin{itemize}
\item Draw a single straight line (hyperplane)
\item Separate \textcolor{mlgreen}{linearly separable} patterns
\item Example: ``Buy if price $>$ 100 AND volume $>$ 50''
\end{itemize}

\vspace{0.3em}
\textbf{Business Analogy}

One simple rule for decision-making

\vspace{0.3em}
\textbf{Limitation}

Only linear decision boundaries possible""",
        "example": r"""\textbf{What One Neuron Cannot Do}

\begin{itemize}
\item Complex, curved decision boundaries
\item XOR-like patterns: ``Buy when high price XOR high volume''
\item \textcolor{mlred}{Real-world market patterns!}
\end{itemize}

\vspace{0.3em}
\textbf{Business Reality}

Multiple interacting factors, non-linear relationships, conditional dependencies

\vspace{0.5em}
\begin{center}
\Large \textcolor{mlgreen}{\textbf{Solution: Multiple Layers!}}
\end{center}""",
        "bottomnote": "Next: See the XOR problem that proves one neuron's limitation"
    },
    "Building the Network: Layers of Intelligence": {
        "definition": r"""\textbf{Multi-Layer Architecture}

\begin{itemize}
\item \textbf{Input Layer:} Raw market features\\
No computation, like sensory neurons
\item \textbf{Hidden Layer(s):} Pattern detection\\
Feature combinations, like association cortex\\
Learns ``high volume + rising price = momentum''
\item \textbf{Output Layer:} Final prediction\\
Probability output, like motor neurons
\end{itemize}

\vspace{0.3em}
\textbf{Result:} Buy/Sell decision""",
        "example": r"""\textbf{Hierarchical Learning Principle}

\begin{itemize}
\item \textcolor{mlblue}{Layer 1:} Detects simple patterns\\
``price rising'', ``volume high''
\item \textcolor{mlblue}{Layer 2:} Combines into complex patterns\\
``strong momentum'', ``weak support''
\item \textcolor{mlblue}{Layer 3:} Makes strategic decisions\\
``high probability buy signal''
\end{itemize}

\vspace{0.3em}
\textbf{Key Insight}

Each layer builds on previous layer's abstractions""",
        "bottomnote": "Next: See the full network architecture with all connections"
    },
    "Forward Propagation: How Networks Make Predictions": {
        "definition": r"""\textbf{The Forward Pass Process}

\begin{enumerate}
\item \textbf{Input:} Feed market features
\item \textbf{Hidden Layer:}
$$a^{(1)} = \sigma(W^{(1)}x + b^{(1)})$$
Detects patterns like ``rising trend''
\item \textbf{Output Layer:}
$$y = \sigma(W^{(2)}a^{(1)} + b^{(2)})$$
\end{enumerate}

\vspace{0.3em}
\textbf{Efficiency}

All neurons in layer compute in parallel!""",
        "example": r"""\textbf{Concrete Example}

\textbf{Input:} price=105.2, volume=0.75, sentiment=0.62

\textbf{Hidden Layer:} Detects patterns

\textbf{Output:} $y = 0.742$

\vspace{0.3em}
\textbf{Interpretation:}
\begin{itemize}
\item 74.2\% confidence price will rise
\item If $y > 0.5$ $\rightarrow$ \textcolor{mlgreen}{\textbf{BUY}}
\item If $y < 0.5$ $\rightarrow$ \textcolor{mlred}{\textbf{SELL}}
\end{itemize}""",
        "bottomnote": "Next: See forward propagation with actual numbers and calculations"
    },
    "Learning from Mistakes: The Training Process": {
        "definition": r"""\textbf{Learning Process Steps}

\begin{enumerate}
\item \textbf{Predict} with random weights
\item \textbf{Measure error} (Loss Function):
$$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
\item \textbf{Adjust weights} (Gradient Descent):
$$w_{new} = w_{old} - \eta \frac{\partial L}{\partial w}$$
\item \textbf{Repeat} thousands of times
\end{enumerate}

\vspace{0.2em}
$\eta$ = learning rate (how fast we learn)""",
        "example": r"""\textbf{Concrete Example}

\textbf{Initial:} Network predicts 55\% price rise

\textbf{Actual:} Price fell ($y=0$)

\textbf{Error:} $(0-0.55)^2 = 0.30$

\vspace{0.3em}
\textbf{Learning Step:}
\begin{itemize}
\item Calculate gradient (direction of error)
\item Move weights opposite direction
\item Error decreases each iteration
\end{itemize}

\vspace{0.2em}
\textit{Like a trader learning from past mistakes}""",
        "bottomnote": "Next: Visualize the loss landscape that we're trying to navigate"
    },
    "Gradient Descent: Learning by Stepping Downhill": {
        "definition": r"""\textbf{Algorithm Steps}

\begin{enumerate}
\item \textbf{Calculate gradient:}
$$\frac{\partial L}{\partial w} = \text{slope of loss}$$
\item \textbf{Step opposite direction:}
$$w_{new} = w_{old} - \eta \times \text{gradient}$$
\item \textbf{Repeat until convergence}
\end{enumerate}

\vspace{0.3em}
\textbf{Learning Rate Trade-offs}
\begin{itemize}
\item \textcolor{mlgreen}{Too small:} Slow learning
\item \textcolor{mlred}{Too large:} Unstable, overshoots
\item \textcolor{mlblue}{Just right:} Steady progress
\end{itemize}""",
        "example": r"""\textbf{Business Analogy}

Like a trader learning from mistakes:

\begin{itemize}
\item \textbf{Fast learning phase}\\
Rapid improvement from obvious patterns
\item \textbf{Steady progress}\\
Fine-tuning strategy
\item \textbf{Convergence}\\
Optimal trading rules learned
\end{itemize}

\vspace{0.3em}
\textbf{Key Insight}

Gradient tells us which direction reduces error fastest""",
        "bottomnote": "Next: See how loss decreases over training iterations"
    },
    "Putting It Together: Market Prediction Case Study": {
        "definition": r"""\textbf{Business Application}

\begin{itemize}
\item \textbf{Goal:} Predict if stock price rises/falls
\item \textbf{Data:} 60 days historical market data
\item \textbf{Features:} 4 input variables per day
\end{itemize}

\vspace{0.3em}
\textbf{Input Features}
\begin{enumerate}
\item Historical Stock Price
\item Trading Volume (normalized)
\item Market Sentiment (0-1)
\item Volatility Index (0-1)
\end{enumerate}""",
        "example": r"""\textbf{Target Variable}

Binary output:
\begin{itemize}
\item 1 = price increased
\item 0 = price decreased
\end{itemize}

Network outputs: $p(\text{price rise})$

\vspace{0.3em}
\textbf{Training Setup}
\begin{itemize}
\item Training: First 45 days (learn)
\item Test: Last 15 days (evaluate)
\item Network: 4 $\rightarrow$ 6 $\rightarrow$ 1
\end{itemize}""",
        "bottomnote": "Next: See the actual market data used for training"
    },
    "Training Results: Before vs After": {
        "definition": r"""\textbf{The Experiment}

\begin{itemize}
\item \textbf{Before training:}\\
Random weights $\rightarrow$ coin flip predictions
\item \textbf{After training:}\\
Learned weights $\rightarrow$ intelligent predictions
\item \textbf{Test set:} 30 days unseen data
\end{itemize}

\vspace{0.3em}
\textbf{Key Results}
\begin{itemize}
\item \textcolor{mlred}{Before:} $\approx$50\% accuracy
\item \textcolor{mlgreen}{After:} $\approx$70\% accuracy
\item \textbf{Improvement:} +20 percentage points
\end{itemize}""",
        "example": r"""\textbf{What the Network Learned}

\begin{itemize}
\item High volume + rising price + positive sentiment = likely rise
\item Low volume + high volatility = uncertain
\item Sentiment lags price but confirms trends
\end{itemize}

\textit{Discovered from data alone!}

\vspace{0.3em}
\textbf{Reality Check}
\begin{itemize}
\item 70\% is \textcolor{mlgreen}{good} for markets
\item 100\% is \textcolor{mlred}{impossible}
\item 70\% over many trades = profit
\end{itemize}""",
        "bottomnote": "Next: See detailed before/after comparison with prediction accuracy"
    },
}


def create_definition_example_slide(title, definition, example, bottomnote):
    """Create a Definition-Example format slide (Layout 9)."""
    return rf"""\begin{{frame}}[t]{{{title}}}
\begin{{columns}}[T]
\column{{0.48\textwidth}}
{definition}

\column{{0.48\textwidth}}
{example}
\end{{columns}}

\bottomnote{{{bottomnote}}}
\end{{frame}}"""


def transform_content(content):
    """Transform the LaTeX content with new layouts."""

    # Split into preamble and document body
    doc_start = content.find(r'\begin{document}')
    preamble = content[:doc_start + len(r'\begin{document}')]
    body = content[doc_start + len(r'\begin{document}'):]

    # Find all frames
    frame_pattern = r'\\begin\{frame\}.*?\\end\{frame\}'
    frames = re.findall(frame_pattern, body, re.DOTALL)

    new_frames = []

    for frame in frames:
        # Extract frame title
        title_match = re.search(r'\\begin\{frame\}(?:\[.*?\])?\{([^}]+)\}', frame)
        if not title_match:
            # Plain frame or frame without title in braces
            new_frames.append(frame)
            continue

        title = title_match.group(1)

        # Check if this is a chart slide
        if title in CHART_SLIDES:
            chart_path, bottomnote = CHART_SLIDES[title]
            new_frame = CHART_SLIDE_TEMPLATE.format(
                title=title,
                chart_path=chart_path,
                bottomnote=bottomnote
            )
            new_frames.append(new_frame)
            print(f"  Transformed chart slide: {title}")

        # Check if this is a concept slide to transform
        elif title in CONCEPT_SLIDES:
            slide_data = CONCEPT_SLIDES[title]
            new_frame = create_definition_example_slide(
                title=title,
                definition=slide_data["definition"],
                example=slide_data["example"],
                bottomnote=slide_data["bottomnote"]
            )
            new_frames.append(new_frame)
            print(f"  Transformed concept slide: {title}")

        else:
            # Keep original frame
            new_frames.append(frame)

    # Reconstruct document
    new_body = '\n\n'.join(new_frames) + '\n\n\\end{document}'

    return preamble + '\n\n' + new_body


# Transform the content
print("\nTransforming slides...")
new_content = transform_content(content)

# Write new file
with open(NEW_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nCreated: {NEW_FILE}")
print(f"Total slides transformed: {len(CHART_SLIDES) + len(CONCEPT_SLIDES)}")
