"""
Add pedagogical improvements to Neural Networks presentation:
1. Discussion prompts after each section
2. Visual roadmap on section dividers
3. Guided interpretation prompts on chart slides
"""

import shutil
from datetime import datetime
from pathlib import Path

# Configuration
SOURCE_FILE = "20251124_1135_neural_networks_polished.tex"
PREVIOUS_DIR = Path("previous")
PREVIOUS_DIR.mkdir(exist_ok=True)

# Generate new filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
NEW_FILE = f"{timestamp}_neural_networks_pedagogical.tex"

# Read source file
with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
shutil.copy(SOURCE_FILE, PREVIOUS_DIR / SOURCE_FILE)
print(f"Backed up: {SOURCE_FILE} -> {PREVIOUS_DIR / SOURCE_FILE}")

# Roadmap function
def create_roadmap(current_part):
    circles = []
    for i in range(1, 6):
        if i == current_part:
            circles.append(f"\\textcolor{{mlpurple}}{{\\textbf{{[{i}]}}}}")
        elif i < current_part:
            circles.append(f"\\textcolor{{mlgray}}{{[{i}]}}")
        else:
            circles.append(f"\\textcolor{{mllavender2}}{{[{i}]}}")
    return " -- ".join(circles)

# Section divider with roadmap
def create_section_divider(part_num, title, subtitle):
    roadmap = create_roadmap(part_num)
    return f"""
\\begin{{frame}}[t]
\\vfill
\\centering
\\begin{{beamercolorbox}}[sep=8pt,center]{{title}}
\\usebeamerfont{{title}}\\Large Part {part_num}: {title}\\par
\\end{{beamercolorbox}}
\\vspace{{0.3cm}}
{{\\normalsize {subtitle}}}
\\vspace{{0.5cm}}

{{\\small {roadmap}}}
\\vfill
\\end{{frame}}
"""

# Discussion prompt slide
def create_discussion_slide(part_num, prompt):
    return f"""
\\begin{{frame}}[t]{{Discussion: Part {part_num} Reflection}}
\\vfill
\\begin{{center}}
\\begin{{beamercolorbox}}[sep=12pt,center,rounded=true]{{block body}}
\\Large \\textbf{{Think -- Pair -- Share}}
\\end{{beamercolorbox}}
\\end{{center}}

\\vspace{{0.5cm}}
\\begin{{center}}
\\large
\\textit{{{prompt}}}
\\end{{center}}

\\vspace{{0.5cm}}
\\begin{{columns}}[T]
\\column{{0.32\\textwidth}}
\\begin{{block}}{{\\small 1. Think (1 min)}}
\\small
Reflect individually on the question
\\end{{block}}

\\column{{0.32\\textwidth}}
\\begin{{block}}{{\\small 2. Pair (2 min)}}
\\small
Discuss with a neighbor
\\end{{block}}

\\column{{0.32\\textwidth}}
\\begin{{block}}{{\\small 3. Share (2 min)}}
\\small
Share insights with class
\\end{{block}}
\\end{{columns}}
\\vfill
\\end{{frame}}
"""

# Old section dividers to replace
OLD_SECTIONS = [
    ("""\\begin{frame}[t]
\\vfill
\\centering
\\begin{beamercolorbox}[sep=8pt,center]{title}
\\usebeamerfont{title}\\Large Part 1: Foundations\\par
\\end{beamercolorbox}
\\vspace{0.5cm}
{\\normalsize From biological neurons to artificial intelligence}
\\vfill
\\end{frame}""",
     create_section_divider(1, "Foundations", "From biological neurons to artificial intelligence")),

    ("""\\begin{frame}[t]
\\vfill
\\centering
\\begin{beamercolorbox}[sep=8pt,center]{title}
\\usebeamerfont{title}\\Large Part 2: Building Blocks\\par
\\end{beamercolorbox}
\\vspace{0.5cm}
{\\normalsize Activation functions and their role in learning}
\\vfill
\\end{frame}""",
     create_section_divider(2, "Building Blocks", "Activation functions and their role in learning")),

    ("""\\begin{frame}[t]
\\vfill
\\centering
\\begin{beamercolorbox}[sep=8pt,center]{title}
\\usebeamerfont{title}\\Large Part 3: Network Architecture\\par
\\end{beamercolorbox}
\\vspace{0.5cm}
{\\normalsize Building layers of intelligence}
\\vfill
\\end{frame}""",
     create_section_divider(3, "Network Architecture", "Building layers of intelligence")),

    ("""\\begin{frame}[t]
\\vfill
\\centering
\\begin{beamercolorbox}[sep=8pt,center]{title}
\\usebeamerfont{title}\\Large Part 4: Learning Process\\par
\\end{beamercolorbox}
\\vspace{0.5cm}
{\\normalsize How networks learn from mistakes}
\\vfill
\\end{frame}""",
     create_section_divider(4, "Learning Process", "How networks learn from mistakes")),

    ("""\\begin{frame}[t]
\\vfill
\\centering
\\begin{beamercolorbox}[sep=8pt,center]{title}
\\usebeamerfont{title}\\Large Part 5: Application\\par
\\end{beamercolorbox}
\\vspace{0.5cm}
{\\normalsize Putting it all together with market prediction}
\\vfill
\\end{frame}""",
     create_section_divider(5, "Application", "Putting it all together with market prediction")),
]

# Apply section divider replacements
for old, new in OLD_SECTIONS:
    content = content.replace(old, new)

# Chart bottomnote replacements
CHART_BOTTOMNOTES = [
    ("\\bottomnote{The artificial neuron mathematically mimics biological signal integration and activation}",
     "\\bottomnote{Observe: Which biological components map directly to mathematical operations?}"),

    ("\\bottomnote{With market inputs (price=100, volume=85, sentiment=120), the neuron predicts 100\\% probability of price increase}",
     "\\bottomnote{Observe: How would changing the weights affect the final output probability?}"),

    ("\\bottomnote{Each activation function has different properties: Sigmoid for probabilities, ReLU for speed, Tanh for zero-centered outputs}",
     "\\bottomnote{Observe: Where does each function's output change most rapidly? Why does this matter?}"),

    ("\\bottomnote{Left: Linearly separable (one neuron works). Right: XOR pattern (one neuron fails, need hidden layers)}",
     "\\bottomnote{Observe: Why is it impossible to draw a single straight line separating orange from blue?}"),

    ("\\bottomnote{5 inputs, 6 hidden neurons, 1 output. Total: 36 weights to learn from data}",
     "\\bottomnote{Observe: Count the connections. Why are there 36 weights total?}"),

    ("\\bottomnote{Data flows left to right: inputs, hidden activations, output (0.742) = 74\\% buy confidence}",
     "\\bottomnote{Observe: How do the hidden layer values combine to produce the final 0.742 output?}"),

    ("\\bottomnote{Goal: Find weights (red star) that minimize loss. Gradient descent navigates this surface}",
     "\\bottomnote{Observe: What happens if we start from different random initial weights?}"),

    ("\\bottomnote{Left: 1D visualization showing steps toward minimum. Right: Loss decreasing over 100 training iterations}",
     "\\bottomnote{Observe: How does the step size (learning rate) affect how quickly we reach the minimum?}"),

    ("\\bottomnote{60 days of market data: price trend, volume bars, sentiment score, volatility index}",
     "\\bottomnote{Observe: Which features seem most correlated with the price direction markers?}"),

    ("\\bottomnote{Top: Actual prices. Middle: Before (random). Bottom: After (learned patterns, 70\\% accuracy)}",
     "\\bottomnote{Observe: Where does the trained model still make errors? What might explain these?}"),
]

# Apply bottomnote replacements
for old, new in CHART_BOTTOMNOTES:
    content = content.replace(old, new)

# Discussion prompts
DISCUSSIONS = {
    1: "What other business processes might benefit from 'learning from data' instead of following explicit rules?",
    2: "Can you think of a business metric that shows diminishing returns or threshold effects?",
    3: "For your industry, what would be the 'inputs' and 'outputs' of a useful neural network?",
    4: "How is gradient descent similar to how businesses optimize through trial and error?",
    5: "What data would you need to predict customer behavior in your domain?"
}

# Insert discussion slides after specific chart slides
# After Part 1: after "Single Neuron Computation" frame
discussion1 = create_discussion_slide(1, DISCUSSIONS[1])
content = content.replace(
    "\\bottomnote{Observe: How would changing the weights affect the final output probability?}\n\\end{frame}",
    "\\bottomnote{Observe: How would changing the weights affect the final output probability?}\n\\end{frame}" + discussion1
)

# After Part 2: after "Visual Proof: The XOR Problem" frame
discussion2 = create_discussion_slide(2, DISCUSSIONS[2])
content = content.replace(
    "\\bottomnote{Observe: Why is it impossible to draw a single straight line separating orange from blue?}\n\\end{frame}",
    "\\bottomnote{Observe: Why is it impossible to draw a single straight line separating orange from blue?}\n\\end{frame}" + discussion2
)

# After Part 3: after "Forward Propagation: Detailed Example" frame
discussion3 = create_discussion_slide(3, DISCUSSIONS[3])
content = content.replace(
    "\\bottomnote{Observe: How do the hidden layer values combine to produce the final 0.742 output?}\n\\end{frame}",
    "\\bottomnote{Observe: How do the hidden layer values combine to produce the final 0.742 output?}\n\\end{frame}" + discussion3
)

# After Part 4: after "Gradient Descent: Optimization in Action" frame
discussion4 = create_discussion_slide(4, DISCUSSIONS[4])
content = content.replace(
    "\\bottomnote{Observe: How does the step size (learning rate) affect how quickly we reach the minimum?}\n\\end{frame}",
    "\\bottomnote{Observe: How does the step size (learning rate) affect how quickly we reach the minimum?}\n\\end{frame}" + discussion4
)

# After Part 5: after "Prediction Results" frame
discussion5 = create_discussion_slide(5, DISCUSSIONS[5])
content = content.replace(
    "\\bottomnote{Observe: Where does the trained model still make errors? What might explain these?}\n\\end{frame}",
    "\\bottomnote{Observe: Where does the trained model still make errors? What might explain these?}\n\\end{frame}" + discussion5
)

# Write new file
with open(NEW_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nCreated: {NEW_FILE}")
print("Pedagogical improvements applied:")
print("  - Added visual roadmap to 5 section dividers")
print("  - Added observation prompts to 10 chart slides")
print("  - Added 5 Think-Pair-Share discussion slides")
