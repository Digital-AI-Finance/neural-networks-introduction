---
title: "Activation and Loss Functions"
lecture_num: 4
pdf_file: activation_loss_functions.pdf
short_title: "Activations & Loss"
description: "Compare activation functions (sigmoid, tanh, ReLU) and loss functions (MSE, cross-entropy). Learn when to use each for regression and classification problems in neural networks."
keywords: ['activation function', 'sigmoid', 'tanh', 'ReLU', 'loss function', 'MSE', 'cross-entropy', 'vanishing gradient']
---

# Lecture 4: Activation and Loss Functions

**Duration**: ~45 minutes | **Slides**: 23 | **Prerequisites**: [Lecture 3](Lecture-3-MLP-Architecture)

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Explain why activation functions are necessary
2. Compare sigmoid, tanh, and ReLU activation functions
3. Choose appropriate activation functions for different layers
4. Understand the purpose of loss functions
5. Apply MSE and cross-entropy loss to appropriate problems
6. Connect loss functions to the optimization process

---

## Key Concepts

### 1. Why Activation Functions?

Recall from Lecture 3: Without non-linear activation functions, any multi-layer network collapses to a single linear transformation.

**Activation functions provide:**
- Non-linearity (essential for learning complex patterns)
- Bounded output (for some functions)
- Differentiability (needed for gradient-based learning)

---

### 2. The Sigmoid Function

The sigmoid (logistic) function was historically the most popular activation.

**Formula:**
```
sigmoid(z) = 1 / (1 + e^(-z))
```

**Properties:**
- Output range: (0, 1)
- Smooth, differentiable everywhere
- Centered at 0.5

**Derivative:**
```
sigmoid'(z) = sigmoid(z) * (1 - sigmoid(z))
```

**Advantages:**
- Outputs interpretable as probabilities
- Smooth gradient

**Disadvantages:**
- Vanishing gradient for large |z|
- Not zero-centered
- Computationally expensive (exponentials)

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/sigmoid_function">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/sigmoid_function/sigmoid_function.png" alt="Sigmoid Function" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 3. The Tanh Function

Tanh is a scaled and shifted sigmoid.

**Formula:**
```
tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))
```

Or equivalently:
```
tanh(z) = 2 * sigmoid(2z) - 1
```

**Properties:**
- Output range: (-1, 1)
- Zero-centered
- Smooth, differentiable everywhere

**Derivative:**
```
tanh'(z) = 1 - tanh^2(z)
```

**Advantages:**
- Zero-centered (better gradient flow)
- Stronger gradients than sigmoid

**Disadvantages:**
- Still suffers from vanishing gradients
- Computationally expensive

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/tanh_function">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/tanh_function/tanh_function.png" alt="Tanh Function" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 4. The ReLU Function

ReLU (Rectified Linear Unit) is the most popular modern activation.

**Formula:**
```
ReLU(z) = max(0, z)
```

**Properties:**
- Output range: [0, infinity)
- Not bounded above
- Not differentiable at z = 0 (use subgradient)

**Derivative:**
```
ReLU'(z) = { 1 if z > 0
           { 0 if z < 0
           { undefined at z = 0 (typically use 0 or 1)
```

**Advantages:**
- No vanishing gradient for positive values
- Computationally efficient (no exponentials)
- Sparse activation (many zeros)

**Disadvantages:**
- "Dead ReLU" problem: neurons can get stuck at 0
- Not zero-centered
- Unbounded (can cause exploding values)

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/relu_function">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/relu_function/relu_function.png" alt="ReLU Function" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 5. Activation Function Comparison

| Function | Formula | Range | Pros | Cons |
|----------|---------|-------|------|------|
| Sigmoid | 1/(1+e^(-z)) | (0,1) | Probabilistic interpretation | Vanishing gradient |
| Tanh | (e^z-e^(-z))/(e^z+e^(-z)) | (-1,1) | Zero-centered | Vanishing gradient |
| ReLU | max(0,z) | [0,inf) | Fast, no vanishing gradient | Dead neurons |

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/activation_comparison">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/activation_comparison/activation_comparison.png" alt="Activation Comparison" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

**Modern best practice:**
- Hidden layers: ReLU (or variants like Leaky ReLU, ELU)
- Output layer: Depends on task (see below)

---

### 6. Choosing Output Activation

The output layer activation depends on the problem type:

| Problem Type | Output Activation | Output Range |
|--------------|-------------------|--------------|
| Binary classification | Sigmoid | (0, 1) - probability |
| Multi-class classification | Softmax | (0, 1) per class, sum to 1 |
| Regression | None (linear) | (-inf, inf) |
| Bounded regression | Sigmoid or tanh | Scaled to target range |

---

### 7. The Universal Approximation Theorem

**Theorem** (Cybenko, 1989; Hornik, 1991): A feedforward network with a single hidden layer containing a finite number of neurons can approximate any continuous function on compact subsets of R^n, given appropriate activation functions and sufficient neurons.

**Implications:**
- Neural networks are theoretically capable of learning any pattern
- BUT: The theorem doesn't tell us how many neurons are needed
- AND: It doesn't tell us how to find the right weights

**Practical reality:**
- Deeper networks often work better than very wide shallow ones
- Finding good weights requires proper training algorithms

---

### 8. Loss Functions: Measuring Mistakes

A loss function quantifies how wrong the network's predictions are.

**Purpose:**
- Provides a single number to minimize
- Guides the optimization process
- Different losses for different problems

**Notation:**
- y_true (or y): The correct answer
- y_pred (or y-hat): The network's prediction
- L: The loss value

---

### 9. Mean Squared Error (MSE)

MSE is the standard loss for regression problems.

**Formula:**
```
MSE = (1/n) * sum((y_true - y_pred)^2)
```

For a single example:
```
L = (y_true - y_pred)^2
```

**Properties:**
- Always non-negative
- Zero only when predictions are perfect
- Heavily penalizes large errors (quadratic)

**Derivative:**
```
dL/dy_pred = -2 * (y_true - y_pred)
```

**Use for:**
- Stock price prediction
- Portfolio return forecasting
- Any continuous target variable

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/mse_visualization">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/mse_visualization/mse_visualization.png" alt="MSE Visualization" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 10. Binary Cross-Entropy Loss

Cross-entropy is the standard loss for classification problems.

**Formula (for binary classification):**
```
BCE = -[y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred)]
```

**Intuition:**
- When y_true = 1: Loss = -log(y_pred) -> want y_pred close to 1
- When y_true = 0: Loss = -log(1 - y_pred) -> want y_pred close to 0

**Properties:**
- Always non-negative
- Penalizes confident wrong predictions heavily
- Works well with sigmoid output

**Derivative:**
```
dL/dy_pred = -y_true/y_pred + (1-y_true)/(1-y_pred)
```

**Use for:**
- Buy/sell classification
- Fraud detection
- Any binary outcome

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module2_mlp/charts/cross_entropy_visualization">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module2_mlp/charts/cross_entropy_visualization/cross_entropy_visualization.png" alt="Cross-Entropy Visualization" loading="lazy">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 11. Choosing the Right Loss Function

| Problem | Loss Function | Output Activation |
|---------|---------------|-------------------|
| Regression | MSE | Linear |
| Binary classification | Binary cross-entropy | Sigmoid |
| Multi-class (one-hot) | Categorical cross-entropy | Softmax |
| Multi-label | Binary cross-entropy per label | Sigmoid per output |

**Finance examples:**
- Predicting next-day return: MSE + Linear output
- Predicting up/down: Cross-entropy + Sigmoid output
- Predicting sector (11 classes): Categorical cross-entropy + Softmax output

---

## Key Formulas

### Activation Functions

| Function | Formula | Derivative |
|----------|---------|------------|
| Sigmoid | sigma(z) = 1/(1+e^(-z)) | sigma(z)(1-sigma(z)) |
| Tanh | tanh(z) = (e^z-e^(-z))/(e^z+e^(-z)) | 1-tanh^2(z) |
| ReLU | max(0, z) | 1 if z>0, 0 otherwise |

### Loss Functions

**Mean Squared Error:**
```
L_MSE = (1/n) * sum_{i=1}^{n} (y_i - y_hat_i)^2
```

**Binary Cross-Entropy:**
```
L_BCE = -(1/n) * sum_{i=1}^{n} [y_i*log(y_hat_i) + (1-y_i)*log(1-y_hat_i)]
```

---

## Finance Application: Output Design

When building financial prediction models, output design matters:

**Stock Direction Prediction:**
- Output: Sigmoid (probability of going up)
- Loss: Binary cross-entropy
- Interpretation: P(up) = 0.7 means 70% confidence in upward movement

**Return Prediction:**
- Output: Linear (unbounded)
- Loss: MSE
- Interpretation: Predicted return of 0.02 means expected 2% return

**Risk Level Classification (Low/Medium/High):**
- Output: Softmax (3 neurons)
- Loss: Categorical cross-entropy
- Interpretation: [0.1, 0.3, 0.6] means 60% probability of high risk

---

## Practice Questions

### Mathematical Understanding

**Q1**: Calculate sigmoid(0), sigmoid(2), and sigmoid(-2).

<details>
<summary>Answer</summary>
sigmoid(0) = 1/(1+e^0) = 1/(1+1) = 0.5
sigmoid(2) = 1/(1+e^(-2)) = 1/(1+0.135) = 0.88
sigmoid(-2) = 1/(1+e^2) = 1/(1+7.39) = 0.12
</details>

**Q2**: Given y_true = 1 and y_pred = 0.9, calculate the binary cross-entropy loss.

<details>
<summary>Answer</summary>
BCE = -[y_true * log(y_pred) + (1-y_true) * log(1-y_pred)]
BCE = -[1 * log(0.9) + 0 * log(0.1)]
BCE = -log(0.9)
BCE = -(-0.105) = 0.105

This is a small loss because the prediction (0.9) is close to the true value (1).
</details>

**Q3**: For the same prediction (y_pred = 0.9), what would the BCE loss be if y_true = 0?

<details>
<summary>Answer</summary>
BCE = -[0 * log(0.9) + 1 * log(0.1)]
BCE = -log(0.1)
BCE = -(-2.303) = 2.303

This is a much higher loss! The model confidently predicted 1 (0.9 probability) but the true answer was 0 - a confident wrong prediction is heavily penalized.
</details>

### Conceptual Understanding

**Q4**: Why does ReLU help with the vanishing gradient problem?

<details>
<summary>Answer</summary>
For positive inputs, ReLU has a derivative of exactly 1. This means gradients pass through unchanged, avoiding the "shrinking" that happens with sigmoid/tanh where derivatives are always < 1.

With sigmoid: If derivative is 0.25 and you have 4 layers, the gradient becomes 0.25^4 = 0.004 (tiny!)
With ReLU: If derivative is 1 for positive inputs, gradient stays at 1^4 = 1 (preserved!)
</details>

**Q5**: What is the "dead ReLU" problem and how might it be addressed?

<details>
<summary>Answer</summary>
Dead ReLU: If a neuron's weighted input becomes consistently negative, its output is always 0, and its gradient is always 0. The neuron never learns and is effectively "dead."

Solutions:
1. Leaky ReLU: f(z) = max(0.01z, z) - small gradient for negative values
2. ELU: f(z) = z if z>0, else alpha*(e^z - 1) - smooth transition
3. Proper weight initialization (He initialization)
4. Lower learning rates
</details>

**Q6**: Why is cross-entropy preferred over MSE for classification?

<details>
<summary>Answer</summary>
1. Cross-entropy penalizes confident wrong predictions more heavily
2. The gradient of cross-entropy with sigmoid is simpler: (y_pred - y_true)
3. MSE + sigmoid has very small gradients when predictions are wrong but confident
4. Cross-entropy is derived from maximum likelihood estimation for Bernoulli distributions, making it theoretically appropriate for classification
</details>

### Application

**Q7**: You're building a model to predict stock volatility (always positive). What output activation and loss would you use?

<details>
<summary>Answer</summary>
Since volatility is always positive and continuous:

Option 1 (Simple):
- Output activation: ReLU or Softplus (ensures positive output)
- Loss: MSE

Option 2 (If predicting log-volatility):
- Output activation: Linear
- Loss: MSE
- Then exponentiate to get actual volatility

Option 3 (If volatility is bounded, e.g., 0-100%):
- Output activation: Sigmoid scaled to range
- Loss: MSE
</details>

---

## Reading List

### Essential Reading
- **Nielsen, Chapter 3** - "Improving the way neural networks learn" ([online](http://neuralnetworksanddeeplearning.com/chap3.html))
- **Goodfellow et al., Chapter 6** - Deep Learning - "Deep Feedforward Networks"

### Activation Functions
- **Nair & Hinton (2010)** - "Rectified Linear Units Improve Restricted Boltzmann Machines"
- **Glorot et al. (2011)** - "Deep Sparse Rectifier Neural Networks"

### Theoretical Foundation
- **Cybenko (1989)** - "Approximation by Superpositions of a Sigmoidal Function"
- **Hornik (1991)** - "Approximation Capabilities of Multilayer Feedforward Networks"

### Finance Applications
- **Heaton et al. (2016)** - "Deep Learning for Finance" - Discusses output design for financial problems

---

## Summary

This lecture covered:

1. **Why activation functions** - Enable non-linearity in neural networks
2. **Sigmoid** - Smooth, bounded (0,1), but vanishing gradients
3. **Tanh** - Zero-centered, but still vanishing gradients
4. **ReLU** - Fast, no vanishing gradient, but dead neurons possible
5. **Loss functions** - MSE for regression, cross-entropy for classification
6. **Output design** - Match activation and loss to the problem type

**Key Takeaway**: The combination of activation function and loss function determines how well your network can learn and what problems it can solve.

**Next Lecture**: [Gradient Descent and Backpropagation](Lecture-5-Gradient-Descent-and-Backpropagation) - We'll learn how neural networks actually find good weights.

<div class="lecture-nav">
<a href="Lecture-3-MLP-Architecture">Previous: MLP</a>
<a href="index">Home</a>
<a href="Lecture-5-Gradient-Descent-and-Backpropagation">Next: Backprop</a>
</div>
