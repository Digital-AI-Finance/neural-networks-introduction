---
title: "Multi-Layer Perceptron Architecture"
lecture_num: 3
pdf_file: mlp_architecture.pdf
short_title: "MLP Architecture"
---

# Lecture 3: Multi-Layer Perceptron Architecture

**Duration**: ~45 minutes | **Slides**: 32 | **Prerequisites**: [Lecture 2](Lecture-2-Perceptron-Fundamentals)

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Explain why hidden layers are necessary
2. Describe the architecture of a multi-layer perceptron (MLP)
3. Perform forward propagation calculations
4. Understand matrix notation for neural networks
5. Explain how MLPs solve the XOR problem
6. Design network architectures for different problems

---

## Key Concepts

### 1. From Perceptron to Multi-Layer Networks

Recall from Lecture 2: A single perceptron cannot solve XOR because it's not linearly separable.

**The Solution**: Stack multiple perceptrons into layers!

By combining simple linear classifiers, we can create complex non-linear decision boundaries.

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/mlp_architecture_2_3_1">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/mlp_architecture_2_3_1/mlp_architecture_2_3_1.png" alt="MLP Architecture">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 2. MLP Architecture

An MLP consists of:

| Layer Type | Description |
|------------|-------------|
| **Input Layer** | Receives raw features (not neurons, just data) |
| **Hidden Layer(s)** | Intermediate processing layers |
| **Output Layer** | Produces final prediction |

**Notation**: A network with 2 inputs, 3 hidden neurons, and 1 output is written as 2-3-1.

**Key Properties:**
- Each neuron in layer L connects to ALL neurons in layer L+1 (fully connected)
- Information flows forward only (feedforward network)
- No connections within a layer or backward

---

### 3. Why "Hidden" Layers?

Hidden layers are "hidden" because:
- We don't directly observe their values during training
- They automatically learn useful intermediate representations
- They enable non-linear transformations

**Intuition**: Hidden layers transform the input space into a new representation where the problem becomes linearly separable.

---

### 4. Forward Propagation

Forward propagation computes the network output given an input.

**Layer-by-layer computation:**

```
Layer 0 (Input): x
Layer 1 (Hidden): h = f(W_1 * x + b_1)
Layer 2 (Output): y = f(W_2 * h + b_2)
```

Where:
- W_1, W_2 = weight matrices
- b_1, b_2 = bias vectors
- f = activation function (applied element-wise)

---

### 5. Matrix Notation

For efficient computation, we use matrix operations.

**Single layer forward pass:**
```
z = W * x + b
a = f(z)
```

Where:
- **W** is a (neurons_out x neurons_in) matrix
- **x** is a (neurons_in x 1) vector
- **b** is a (neurons_out x 1) vector
- **z** is a (neurons_out x 1) vector (pre-activation)
- **a** is a (neurons_out x 1) vector (post-activation)

**Example: 2-3-1 Network**

Input: x = [x_1, x_2]^T (2x1)

Layer 1:
- W_1 is 3x2 (3 hidden neurons, 2 inputs)
- b_1 is 3x1
- z_1 = W_1 * x + b_1 (3x1)
- h = f(z_1) (3x1)

Layer 2:
- W_2 is 1x3 (1 output, 3 hidden neurons)
- b_2 is 1x1
- z_2 = W_2 * h + b_2 (1x1)
- y = f(z_2) (1x1)

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/matrix_multiplication_visual">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/matrix_multiplication_visual/matrix_multiplication_visual.png" alt="Matrix Multiplication">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 6. Solving XOR with an MLP

Let's see how a 2-2-1 network solves XOR.

**The key insight**: The hidden layer transforms the input space!

**Architecture:**
- 2 inputs (x_1, x_2)
- 2 hidden neurons (h_1, h_2)
- 1 output (y)

**What the hidden neurons learn:**
- h_1 computes something like OR(x_1, x_2)
- h_2 computes something like AND(x_1, x_2)

**The output neuron then computes:**
- y = h_1 AND (NOT h_2)
- Which equals XOR!

| x_1 | x_2 | h_1 (OR-like) | h_2 (AND-like) | y (XOR) |
|-----|-----|---------------|----------------|---------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/xor_solution_mlp">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/xor_solution_mlp/xor_solution_mlp.png" alt="XOR Solution">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 7. Hidden Layer Representations

The hidden layer creates a new feature space where the problem becomes easier.

**Original space (inputs):**
- XOR points: (0,0), (0,1), (1,0), (1,1)
- Not linearly separable

**Transformed space (hidden layer):**
- Same points mapped to new coordinates
- NOW linearly separable!

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/hidden_layer_representations">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/hidden_layer_representations/hidden_layer_representations.png" alt="Hidden Layer Representations">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

**Key insight**: Deep networks learn hierarchical representations - each layer transforms data into more useful forms.

---

### 8. Why Activation Functions Matter

**The Linear Collapse Problem:**

If all neurons used linear activations (f(z) = z), then:
```
y = W_2 * (W_1 * x + b_1) + b_2
  = W_2 * W_1 * x + W_2 * b_1 + b_2
  = W' * x + b'
```

Where W' = W_2 * W_1 and b' = W_2 * b_1 + b_2

**The result**: No matter how many layers, the entire network collapses to a single linear transformation!

**Solution**: Non-linear activation functions break this collapse and enable learning complex patterns.

---

### 9. Designing Network Architecture

**How many hidden layers?**
- 1 hidden layer: Can approximate any continuous function (universal approximation theorem)
- More layers: Can learn hierarchical features more efficiently
- Modern "deep" networks: Often 10-100+ layers

**How many neurons per layer?**
- Too few: Underfitting (can't capture complexity)
- Too many: Overfitting (memorizes training data)
- Rule of thumb: Start with neurons between input and output size

**Guidelines:**
| Problem | Suggested Architecture |
|---------|----------------------|
| Simple classification | 1 hidden layer, ~10-50 neurons |
| Image recognition | Multiple layers, decreasing size |
| Tabular data | 2-3 hidden layers |
| Complex patterns | Deeper networks |

---

### 10. Historical Context: 1969-1986

After the AI winter (1969), neural network research continued slowly:

**Key developments:**
- 1974: Werbos develops backpropagation (PhD thesis, largely ignored)
- 1982: Hopfield networks revive interest
- 1986: Rumelhart, Hinton & Williams publish backpropagation

**The 1986 breakthrough**: "Learning Representations by Back-propagating Errors" showed that MLPs could be trained effectively, ending the AI winter.

---

## Key Formulas

### Forward Propagation (General)
```
For layer l = 1 to L:
    z^[l] = W^[l] * a^[l-1] + b^[l]
    a^[l] = f(z^[l])
```

Where a^[0] = x (the input).

### Weight Matrix Dimensions
```
W^[l] has shape (n^[l], n^[l-1])
```
Where n^[l] is the number of neurons in layer l.

### Total Parameters
```
For layer l: n^[l] * n^[l-1] + n^[l] (weights + biases)
```

**Example (2-3-1 network):**
- Layer 1: 3*2 + 3 = 9 parameters
- Layer 2: 1*3 + 1 = 4 parameters
- Total: 13 parameters

---

## Finance Application: Multi-Factor Model

A multi-layer network can capture complex relationships between factors:

**Traditional linear factor model:**
```
Return = beta_1*Factor_1 + beta_2*Factor_2 + ... + epsilon
```

**MLP factor model:**
- Can capture non-linear factor relationships
- Can model interactions between factors
- Can learn regime-dependent factor exposures

**Architecture for stock prediction:**
```
Input layer: 10-20 financial features
Hidden layer 1: 64 neurons (learn feature interactions)
Hidden layer 2: 32 neurons (learn higher-order patterns)
Output: 1 neuron (predicted return or probability)
```

---

## Practice Questions

### Mathematical Understanding

**Q1**: A 3-4-2 network has how many total parameters (weights + biases)?

<details>
<summary>Answer</summary>
Layer 1: 4*3 + 4 = 16 parameters (12 weights, 4 biases)
Layer 2: 2*4 + 2 = 10 parameters (8 weights, 2 biases)
Total: 26 parameters
</details>

**Q2**: Given a 2-3-1 network with:
- W_1 = [[1, 1], [1, 1], [1, 1]] (3x2)
- b_1 = [-0.5, -1.5, -0.5] (3x1)
- Activation: step function

Compute the hidden layer output for input x = [1, 0].

<details>
<summary>Answer</summary>
z_1 = W_1 * x + b_1
z_1 = [[1, 1], [1, 1], [1, 1]] * [1, 0]^T + [-0.5, -1.5, -0.5]^T
z_1 = [1, 1, 1]^T + [-0.5, -1.5, -0.5]^T
z_1 = [0.5, -0.5, 0.5]^T

Applying step function (>= 0 -> 1):
h = [1, 0, 1]^T
</details>

**Q3**: Why is a 2-100-1 network more powerful than a 2-1 network for solving complex problems?

<details>
<summary>Answer</summary>
The 2-100-1 network has a hidden layer with 100 neurons, enabling it to:
1. Transform the input space through 100 different linear transformations
2. Create complex non-linear decision boundaries
3. Approximate any continuous function (universal approximation)

The 2-1 network (single perceptron) can only create linear decision boundaries.
</details>

### Conceptual Understanding

**Q4**: In your own words, explain why stacking linear layers still results in a linear transformation.

<details>
<summary>Answer</summary>
When we compose linear functions, the result is still linear. If f(x) = Ax + b and g(x) = Cx + d, then g(f(x)) = C(Ax + b) + d = CAx + Cb + d = Wx + v, which is another linear function.

Mathematically, the composition of linear transformations is still a linear transformation. This is why non-linear activation functions are essential - they break this linearity and allow the network to learn complex patterns.
</details>

**Q5**: How does the hidden layer enable solving XOR?

<details>
<summary>Answer</summary>
The hidden layer transforms the 2D input space into a new representation. In this new space, points that were not linearly separable (the XOR pattern) become linearly separable. Each hidden neuron learns a different linear boundary, and the output neuron combines these to create a non-linear decision boundary in the original space.
</details>

**Q6**: What's the trade-off between network width (neurons per layer) and depth (number of layers)?

<details>
<summary>Answer</summary>
Width:
- More neurons = more capacity to model complex functions
- But: More parameters, risk of overfitting, slower training

Depth:
- More layers = ability to learn hierarchical features
- Each layer can build on representations from previous layers
- But: Harder to train (vanishing gradients), more parameters

Modern practice often favors deeper networks with moderate width, using techniques like batch normalization and skip connections to enable training.
</details>

### Application

**Q7**: You're designing an MLP for fraud detection with 50 input features. The output is binary (fraud/not fraud). Suggest an architecture and explain your choices.

<details>
<summary>Answer</summary>
Suggested architecture: 50-32-16-1

Reasoning:
- Input: 50 features
- Hidden 1 (32 neurons): Compress features, learn initial patterns
- Hidden 2 (16 neurons): Learn higher-order feature combinations
- Output (1 neuron): Binary classification with sigmoid

The "funnel" shape (decreasing neurons) is common for classification - it progressively compresses information toward the decision. Starting with fewer neurons than inputs forces the network to learn efficient representations.

Alternative: 50-64-32-1 if you believe the features need expansion before compression.
</details>

---

## Reading List

### Essential Reading
- **Rumelhart, Hinton & Williams (1986)** - "Learning Representations by Back-propagating Errors" - The breakthrough paper
- **Nielsen, Chapter 1-2** - Neural Networks and Deep Learning ([online](http://neuralnetworksanddeeplearning.com/))

### Theoretical Foundation
- **Cybenko (1989)** - "Approximation by Superpositions of a Sigmoidal Function" - Universal approximation theorem
- **Hornik (1991)** - "Approximation Capabilities of Multilayer Feedforward Networks"

### Modern Perspectives
- **Goodfellow et al., Chapter 6** - Deep Learning textbook - Feedforward networks

### Video Resources
- **3Blue1Brown** - "But what is a neural network?" ([YouTube](https://www.youtube.com/watch?v=aircAruvnKk))
- **Stanford CS231n** - Lecture 4: Neural Networks

---

## Summary

This lecture covered:

1. **Why hidden layers** - Overcome linear limitations of single perceptrons
2. **MLP architecture** - Input, hidden, and output layers
3. **Forward propagation** - Computing output from input layer by layer
4. **Matrix notation** - Efficient representation for computation
5. **Solving XOR** - Hidden layers transform space to enable linear separation
6. **Architecture design** - Guidelines for choosing layers and neurons

**Key Takeaway**: Multi-layer networks can learn complex, non-linear patterns by transforming data through successive layers.

**Next Lecture**: [Activation and Loss Functions](Lecture-4-Activation-and-Loss-Functions) - We'll explore the activation functions that enable non-linearity and the loss functions that guide learning.

<div class="lecture-nav">
<a href="Lecture-2-Perceptron-Fundamentals">Previous: Perceptron</a>
<a href="index">Home</a>
<a href="Lecture-4-Activation-and-Loss-Functions">Next: Activations</a>
</div>
