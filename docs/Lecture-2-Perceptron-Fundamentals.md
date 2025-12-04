---
title: "Perceptron Fundamentals"
lecture_num: 2
pdf_file: perceptron_fundamentals.pdf
short_title: "Perceptron"
description: "Master the perceptron - the simplest neural network. Learn about weights, bias, activation functions, decision boundaries, and the perceptron learning algorithm. Understand the XOR limitation."
keywords: ['perceptron', 'decision boundary', 'activation function', 'XOR problem', 'linear separability', 'perceptron learning algorithm', 'weights and bias']
---

# Lecture 2: Perceptron Fundamentals

**Duration**: ~45 minutes | **Slides**: 32 | **Prerequisites**: [Lecture 1](Lecture-1-History-and-Biological-Inspiration)

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Define the mathematical structure of a perceptron
2. Explain the role of weights, bias, and activation functions
3. Visualize decision boundaries in 2D
4. Implement the perceptron learning algorithm
5. Identify the XOR problem and understand why it matters
6. Apply perceptrons to simple classification tasks

---

## Key Concepts

### 1. The Perceptron Architecture

A perceptron is the simplest possible neural network: a single artificial neuron.

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module1_perceptron/charts/perceptron_architecture">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module1_perceptron/charts/perceptron_architecture/perceptron_architecture.png" alt="Perceptron Architecture" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

**Components:**

| Component | Symbol | Description |
|-----------|--------|-------------|
| Inputs | x_1, x_2, ..., x_n | Feature values |
| Weights | w_1, w_2, ..., w_n | Learned parameters |
| Bias | b | Threshold adjustment |
| Net Input | z | Weighted sum + bias |
| Activation | f(z) | Decision function |
| Output | y | Final prediction |

---

### 2. Mathematical Formulation

#### Step 1: Compute the Net Input (z)

The perceptron first computes a weighted sum of inputs:

```
z = w_1*x_1 + w_2*x_2 + ... + w_n*x_n + b
```

In vector notation:
```
z = w^T * x + b
```

Where:
- **w** = weight vector [w_1, w_2, ..., w_n]
- **x** = input vector [x_1, x_2, ..., x_n]
- **b** = bias (scalar)

#### Step 2: Apply the Activation Function

The step function converts z to a binary output:

```
y = f(z) = { 1 if z >= 0
           { 0 if z < 0
```

**Alternative threshold notation:**
```
y = { 1 if z >= threshold
    { 0 if z < threshold
```

The bias `b` effectively shifts the threshold: `z >= 0` is equivalent to `w^T*x >= -b`.

---

### 3. Weights: The Importance of Features

Weights determine how much each input influences the output.

| Weight Value | Interpretation |
|--------------|----------------|
| Large positive | Feature strongly supports class 1 |
| Large negative | Feature strongly supports class 0 |
| Near zero | Feature has little influence |

**Finance Example: Stock Screener**

| Feature | Weight | Interpretation |
|---------|--------|----------------|
| P/E Ratio | -0.5 | Higher P/E slightly decreases buy signal |
| Momentum | +2.0 | Strong positive momentum strongly increases buy signal |
| Volume | +0.3 | Higher volume slightly supports buying |
| Debt/Equity | -1.5 | High debt moderately decreases buy signal |

The perceptron learns these weights from training data!

---

### 4. The Bias Term

The bias `b` controls the decision threshold independently of input values.

**Intuition**: The bias determines how "easily" the neuron fires.
- **Positive bias**: Lower bar to fire (more likely to output 1)
- **Negative bias**: Higher bar to fire (more likely to output 0)

**Geometric interpretation**: The bias shifts the decision boundary away from the origin.

---

### 5. Decision Boundaries

A perceptron creates a **linear decision boundary** - a hyperplane that separates two classes.

In 2D (two features), the decision boundary is a line defined by:
```
w_1*x_1 + w_2*x_2 + b = 0
```

Solving for x_2:
```
x_2 = -(w_1/w_2)*x_1 - (b/w_2)
```

This is a line with:
- Slope = -w_1/w_2
- Intercept = -b/w_2

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module1_perceptron/charts/decision_boundary_2d">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module1_perceptron/charts/decision_boundary_2d/decision_boundary_2d.png" alt="Decision Boundary" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

**Key Insight**: Everything on one side of the line is classified as 1, everything on the other side as 0.

---

### 6. The Perceptron Learning Algorithm

The perceptron learns by adjusting weights when it makes mistakes.

**Algorithm:**

```
1. Initialize weights w and bias b (often to zeros or small random values)
2. For each training example (x, y_true):
   a. Compute prediction: y_pred = f(w^T * x + b)
   b. Compute error: error = y_true - y_pred
   c. Update weights: w = w + learning_rate * error * x
   d. Update bias: b = b + learning_rate * error
3. Repeat until convergence or max iterations
```

**Update Rule Explained:**

| y_true | y_pred | error | Action |
|--------|--------|-------|--------|
| 1 | 1 | 0 | No update (correct) |
| 0 | 0 | 0 | No update (correct) |
| 1 | 0 | +1 | Increase weights toward x |
| 0 | 1 | -1 | Decrease weights away from x |

**Learning Rate (eta)**: Controls the step size of updates
- Too large: Overshoots, unstable learning
- Too small: Very slow convergence
- Typical values: 0.01 to 0.1

---

### 7. Perceptron Convergence Theorem

**Theorem**: If the training data is linearly separable, the perceptron learning algorithm will converge to a solution in a finite number of steps.

**Implications:**
- Guaranteed to find a separating hyperplane (if one exists)
- No guarantee on number of iterations
- No guarantee of finding the "best" hyperplane

**Limitation**: If data is NOT linearly separable, the algorithm will never converge.

---

### 8. The XOR Problem

The XOR (exclusive or) function demonstrates the fundamental limitation of single perceptrons.

**XOR Truth Table:**

| x_1 | x_2 | XOR(x_1, x_2) |
|-----|-----|---------------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module1_perceptron/charts/xor_problem">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module1_perceptron/charts/xor_problem/xor_problem.png" alt="XOR Problem" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

**Why can't a perceptron solve XOR?**

Plot the points:
- (0,0) -> 0 (class 0)
- (0,1) -> 1 (class 1)
- (1,0) -> 1 (class 1)
- (1,1) -> 0 (class 0)

No single straight line can separate the 0s from the 1s!

**Solution preview**: Multi-layer perceptrons (MLPs) can solve XOR by combining multiple perceptrons. This is covered in Lecture 3.

---

### 9. Linear Separability

**Definition**: A dataset is linearly separable if there exists a hyperplane that perfectly separates the two classes.

**Examples of linearly separable problems:**
- AND gate
- OR gate
- Simple threshold decisions

**Examples of non-linearly separable problems:**
- XOR gate
- Circular class boundaries
- Many real-world classification problems

**Finance Connection**: Many financial classification problems (e.g., "will this stock outperform?") are NOT linearly separable, which is why we need more powerful models.

---

## Key Formulas

### Perceptron Output
```
y = f(sum_{i=1}^{n} w_i * x_i + b)
```

### Step Activation Function
```
f(z) = { 1 if z >= 0
       { 0 otherwise
```

### Weight Update Rule
```
w_i(new) = w_i(old) + eta * (y_true - y_pred) * x_i
```

### Bias Update Rule
```
b(new) = b(old) + eta * (y_true - y_pred)
```

### Decision Boundary (2D)
```
w_1*x_1 + w_2*x_2 + b = 0
```

---

## Finance Application: Binary Stock Classifier

**Problem**: Given financial metrics, classify stocks as "Buy" or "Pass"

**Features (inputs):**
- x_1 = Normalized P/E ratio
- x_2 = 6-month momentum (%)
- x_3 = Normalized trading volume
- x_4 = Debt-to-equity ratio
- x_5 = Earnings surprise (%)

**Output:**
- y = 1: Buy
- y = 0: Pass

**Training data**: Historical stocks with known outcomes (did they outperform the benchmark?)

**Learned interpretation**: After training, examine the weights:
- Large positive w_2 (momentum): Momentum is a strong buy signal
- Negative w_1 (P/E): High P/E stocks are less attractive
- etc.

---

## Practice Questions

### Mathematical Understanding

**Q1**: Given weights w = [2, -1] and bias b = -1, what is the output for input x = [1, 0]?

<details>
<summary>Answer</summary>
z = w^T * x + b = (2)(1) + (-1)(0) + (-1) = 2 + 0 - 1 = 1

Since z = 1 >= 0, the output y = 1.
</details>

**Q2**: For the same perceptron (w = [2, -1], b = -1), what is the equation of the decision boundary?

<details>
<summary>Answer</summary>
The decision boundary is where z = 0:
2*x_1 + (-1)*x_2 + (-1) = 0
2*x_1 - x_2 - 1 = 0
x_2 = 2*x_1 - 1

This is a line with slope 2 and y-intercept -1.
</details>

**Q3**: A perceptron makes an error: y_true = 1 but y_pred = 0. The input is x = [3, 2] and learning rate is 0.1. If the current weights are w = [0.5, 0.5] and b = 0, what are the new weights and bias?

<details>
<summary>Answer</summary>
error = y_true - y_pred = 1 - 0 = 1

w_new = w_old + eta * error * x
w_new = [0.5, 0.5] + 0.1 * 1 * [3, 2]
w_new = [0.5 + 0.3, 0.5 + 0.2]
w_new = [0.8, 0.7]

b_new = b_old + eta * error
b_new = 0 + 0.1 * 1 = 0.1
</details>

### Conceptual Understanding

**Q4**: Why is the bias term necessary? What happens if we remove it?

<details>
<summary>Answer</summary>
Without bias, the decision boundary must pass through the origin (0, 0). This severely limits which problems can be solved. With bias, we can shift the decision boundary anywhere in the feature space, making the perceptron much more flexible.
</details>

**Q5**: Can a perceptron learn the AND function? What about the OR function?

<details>
<summary>Answer</summary>
Yes to both! AND and OR are linearly separable.

For AND (both inputs must be 1):
- Weights w = [1, 1], bias b = -1.5
- z = x_1 + x_2 - 1.5
- Only (1,1) gives z = 0.5 > 0

For OR (at least one input is 1):
- Weights w = [1, 1], bias b = -0.5
- z = x_1 + x_2 - 0.5
- (1,0), (0,1), and (1,1) all give z > 0
</details>

**Q6**: Why is XOR important in the history of neural networks?

<details>
<summary>Answer</summary>
XOR demonstrated a fundamental limitation of single-layer perceptrons. Minsky and Papert proved mathematically that no single perceptron can solve XOR. This contributed to the first AI winter by showing that perceptrons couldn't solve many interesting problems. However, this limitation was later overcome with multi-layer networks.
</details>

### Application

**Q7**: You're building a perceptron for credit approval with features: income (x_1), credit score (x_2), existing loans (x_3). After training, the weights are w = [0.8, 1.2, -0.5]. Interpret these weights.

<details>
<summary>Answer</summary>
- w_1 = 0.8 (income): Higher income moderately increases approval probability
- w_2 = 1.2 (credit score): Higher credit score strongly increases approval probability (most important feature)
- w_3 = -0.5 (existing loans): More existing loans moderately decreases approval probability

Credit score has the largest absolute weight, making it the most influential feature in the decision.
</details>

---

## Reading List

### Essential Reading
- **Rosenblatt (1958)** - "The Perceptron: A Probabilistic Model" - The original paper
- **Nielsen, Chapter 1** - Neural Networks and Deep Learning ([online](http://neuralnetworksanddeeplearning.com/chap1.html))

### Mathematical Deep Dive
- **Novikoff (1962)** - "On Convergence Proofs on Perceptrons" - The convergence theorem proof
- **Goodfellow et al., Chapter 6** - Deep Learning textbook

### Historical Context
- **Minsky & Papert (1969)** - "Perceptrons" - The famous critique

### Video Resources
- **3Blue1Brown** - "Gradient descent, how neural networks learn" ([YouTube](https://www.youtube.com/watch?v=IHZwWFHWa-w))

---

## Summary

This lecture covered:

1. **Perceptron architecture** - Inputs, weights, bias, activation, output
2. **Mathematical formulation** - z = w^T * x + b, y = f(z)
3. **Decision boundaries** - Linear hyperplanes separating classes
4. **Learning algorithm** - Adjust weights based on errors
5. **Convergence theorem** - Guaranteed convergence for linearly separable data
6. **XOR problem** - The fundamental limitation that led to multi-layer networks

**Key Takeaway**: A single perceptron is a powerful but limited classifier. It can only solve linearly separable problems.

**Next Lecture**: [MLP Architecture](Lecture-3-MLP-Architecture) - We'll see how stacking perceptrons into layers overcomes the XOR limitation.

<div class="lecture-nav">
<a href="Lecture-1-History-and-Biological-Inspiration">Previous: History</a>
<a href="index">Home</a>
<a href="Lecture-3-MLP-Architecture">Next: MLP</a>
</div>
