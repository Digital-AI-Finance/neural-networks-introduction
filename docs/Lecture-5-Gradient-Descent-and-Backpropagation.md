---
title: "Gradient Descent and Backpropagation"
lecture_num: 5
pdf_file: gradient_descent_backprop.pdf
short_title: "Backpropagation"
---

# Lecture 5: Gradient Descent and Backpropagation

**Duration**: ~45 minutes | **Slides**: 38 | **Prerequisites**: [Lecture 4](Lecture-4-Activation-and-Loss-Functions)

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Explain gradient descent as an optimization algorithm
2. Visualize loss landscapes and local minima
3. Understand the role of learning rate in training
4. Apply the chain rule to compute gradients
5. Trace backpropagation through a simple network
6. Explain how credit assignment works in neural networks

---

## Key Concepts

### 1. The Optimization Problem

Training a neural network means finding weights that minimize the loss function.

**Formal statement:**
```
Find W* = argmin_W L(W)
```

Where:
- W = all weights and biases in the network
- L = loss function
- W* = optimal weights

**The challenge**: Neural networks can have millions of parameters. We can't try all possible combinations!

---

### 2. Loss Landscapes

The loss function creates a "landscape" over the weight space.

**Visualization (2D slice):**
- x-axis, y-axis: Two weights
- z-axis (height): Loss value
- Goal: Find the lowest point

**Key features:**
- **Global minimum**: The absolute lowest point (what we want)
- **Local minima**: Low points that aren't the lowest
- **Saddle points**: Points that are minima in some directions, maxima in others
- **Plateaus**: Flat regions where gradients are tiny

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module3_training/charts/loss_landscape_3d">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/loss_landscape_3d/loss_landscape_3d.png" alt="Loss Landscape">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 3. Gradient Descent: The Core Idea

**Intuition**: Imagine standing on a hill in fog. To go down, you feel the slope under your feet and step in the direction that goes down most steeply.

**Algorithm:**
```
1. Start at a random position (initialize weights)
2. Compute the gradient (direction of steepest increase)
3. Take a step in the opposite direction (gradient descent, not ascent!)
4. Repeat until convergence
```

**Update rule:**
```
W_new = W_old - learning_rate * gradient
```

Or more precisely:
```
w_i = w_i - eta * (dL/dw_i)
```

Where:
- eta (learning rate): How big each step is
- dL/dw_i: Partial derivative of loss with respect to weight w_i

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module3_training/charts/gradient_descent_contour">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/gradient_descent_contour/gradient_descent_contour.png" alt="Gradient Descent Contour">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 4. The Learning Rate

The learning rate controls step size and is crucial for successful training.

**Too large:**
- Overshoots the minimum
- Can diverge (loss increases!)
- Unstable training

**Too small:**
- Very slow convergence
- May get stuck in local minima
- Wastes computational resources

**Just right:**
- Steady progress toward minimum
- Smooth decrease in loss

**Typical values:** 0.001 to 0.1 (often requires experimentation)

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module3_training/charts/learning_rate_comparison">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/learning_rate_comparison/learning_rate_comparison.png" alt="Learning Rate Comparison">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 5. The Chain Rule (Calculus Review)

Backpropagation relies on the chain rule for computing derivatives of composite functions.

**The rule:**
```
If y = f(g(x)), then dy/dx = (dy/dg) * (dg/dx)
```

**Example:**
```
y = (3x + 2)^2

Let u = 3x + 2, so y = u^2

dy/dx = (dy/du) * (du/dx)
      = 2u * 3
      = 6(3x + 2)
```

**For neural networks:** The loss depends on the output, which depends on hidden layers, which depend on weights. We apply the chain rule repeatedly!

---

### 6. Backpropagation: The Algorithm

Backpropagation efficiently computes all gradients by working backward through the network.

**Key insight:** Many gradients share common sub-computations. By working backward, we compute each term only once.

**The process:**

1. **Forward pass:** Compute and store all intermediate values (z, a for each layer)

2. **Compute output error:** delta_L = dL/da_L * f'(z_L)

3. **Backpropagate error:** For each layer l from L-1 to 1:
   ```
   delta_l = (W_{l+1}^T * delta_{l+1}) * f'(z_l)
   ```

4. **Compute gradients:**
   ```
   dL/dW_l = delta_l * a_{l-1}^T
   dL/db_l = delta_l
   ```

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module3_training/charts/backprop_flow_diagram">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/backprop_flow_diagram/backprop_flow_diagram.png" alt="Backprop Flow">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 7. Credit Assignment

**The problem:** When the network makes a mistake, which weights are responsible?

**The solution:** Backpropagation assigns "credit" (or blame) to each weight based on how much it contributed to the error.

**Intuition:**
- Weights on connections that carried large signals get more blame
- Weights connected to neurons with large gradients get more blame
- The further a weight is from the output, the more its credit is diluted

<div class="chart-container">
<a href="https://github.com/Digital-AI-Finance/neural-networks-introduction/tree/main/module3_training/charts/credit_assignment">
<img src="https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/credit_assignment/credit_assignment.png" alt="Credit Assignment">
</a>
<span class="chart-link">Click chart to view Python source code</span>
</div>

---

### 8. A Worked Example

Consider a simple 2-1-1 network:
- Input: x = [1, 2]
- Hidden: 1 neuron with sigmoid
- Output: 1 neuron with sigmoid
- Target: y = 1

**Weights:**
- W1 = [0.5, 0.5] (input to hidden)
- b1 = 0
- W2 = 0.5 (hidden to output)
- b2 = 0

**Forward pass:**
```
z1 = 0.5*1 + 0.5*2 + 0 = 1.5
a1 = sigmoid(1.5) = 0.82
z2 = 0.5*0.82 + 0 = 0.41
a2 = sigmoid(0.41) = 0.60
```

**Loss (MSE):**
```
L = (1 - 0.60)^2 = 0.16
```

**Backward pass:**
```
dL/da2 = -2*(1 - 0.60) = -0.80
da2/dz2 = sigmoid(0.41)*(1-sigmoid(0.41)) = 0.24
delta2 = -0.80 * 0.24 = -0.19

dL/dW2 = delta2 * a1 = -0.19 * 0.82 = -0.16
dL/db2 = delta2 = -0.19

delta1 = (W2 * delta2) * sigmoid'(z1)
       = (0.5 * -0.19) * (0.82 * 0.18)
       = -0.095 * 0.15 = -0.014

dL/dW1 = delta1 * x^T = -0.014 * [1, 2] = [-0.014, -0.028]
```

**Update (learning rate = 0.5):**
```
W2_new = 0.5 - 0.5*(-0.16) = 0.58
W1_new = [0.5, 0.5] - 0.5*[-0.014, -0.028] = [0.507, 0.514]
```

---

### 9. Historical Context: 1986-2012

**1986**: Rumelhart, Hinton & Williams publish "Learning Representations by Back-propagating Errors" - making backpropagation widely known.

**Key insight:** Backpropagation made training multi-layer networks practical.

**Challenges remained:**
- Vanishing gradients in deep networks
- Local minima concerns
- Limited computing power

**2012**: AlexNet wins ImageNet competition, sparking the deep learning revolution.

---

### 10. The Vanishing Gradient Problem

When using sigmoid/tanh activations in deep networks, gradients can become extremely small.

**Why it happens:**
- Sigmoid derivative max = 0.25 (at z=0)
- Each layer multiplies gradients by activation derivatives
- With 10 layers: 0.25^10 = 0.000001

**Result:** Early layers learn extremely slowly or not at all.

**Solutions:**
- Use ReLU activations (derivative = 1 for positive inputs)
- Better weight initialization
- Skip connections (ResNets)
- Batch normalization

---

## Key Formulas

### Gradient Descent Update
```
w = w - eta * dL/dw
```

### Chain Rule
```
dL/dw = dL/da * da/dz * dz/dw
```

### Backpropagation (Output Layer)
```
delta_L = (a_L - y) * f'(z_L)
```
For sigmoid output with MSE loss.

### Backpropagation (Hidden Layers)
```
delta_l = (W_{l+1}^T * delta_{l+1}) * f'(z_l)
```

### Weight Gradient
```
dL/dW_l = delta_l * a_{l-1}^T
```

---

## Finance Application: Optimizing Trading Strategies

Gradient descent in finance is like optimizing a trading strategy:

**Analogy:**
- Weights = Strategy parameters (entry threshold, position size, etc.)
- Loss function = Negative Sharpe ratio (we want to maximize Sharpe)
- Gradient = How to adjust parameters to improve performance
- Learning rate = How aggressively to change the strategy

**Challenges specific to finance:**
- Non-stationary data (market regimes change)
- Limited data (can't generate more historical data)
- Transaction costs not differentiable
- Look-ahead bias danger

---

## Practice Questions

### Mathematical Understanding

**Q1**: If the loss with respect to the output is dL/da = -2 and the sigmoid derivative at the output is f'(z) = 0.2, what is the output layer delta?

<details>
<summary>Answer</summary>
delta = dL/da * f'(z)
delta = -2 * 0.2 = -0.4
</details>

**Q2**: A weight is currently w = 1.5. The gradient dL/dw = 0.3. With learning rate eta = 0.1, what is the new weight?

<details>
<summary>Answer</summary>
w_new = w_old - eta * dL/dw
w_new = 1.5 - 0.1 * 0.3
w_new = 1.5 - 0.03 = 1.47
</details>

**Q3**: Why do we subtract the gradient (gradient descent) rather than add it?

<details>
<summary>Answer</summary>
The gradient points in the direction of steepest increase of the loss function. We want to decrease the loss, so we move in the opposite direction. Subtracting the gradient moves us "downhill" in the loss landscape.
</details>

### Conceptual Understanding

**Q4**: Why is backpropagation more efficient than computing each gradient separately?

<details>
<summary>Answer</summary>
Backpropagation reuses intermediate computations. When computing dL/dw for weights in early layers, we need terms like dL/da_L, dL/da_{L-1}, etc. By computing these once and propagating backward, we avoid redundant calculations.

If we computed each gradient from scratch, we'd repeat the same chain rule calculations many times. Backpropagation computes all gradients in O(n) time, where n is the number of parameters.
</details>

**Q5**: What happens if we set the learning rate to 0?

<details>
<summary>Answer</summary>
With learning rate = 0, the update rule becomes:
w_new = w_old - 0 * gradient = w_old

The weights never change! The network never learns. This is why learning rate is crucial - it must be positive for any learning to occur.
</details>

**Q6**: Explain the vanishing gradient problem in terms of the chain rule.

<details>
<summary>Answer</summary>
By the chain rule, the gradient for an early layer involves multiplying many terms:
dL/dw_1 = (dL/da_L) * (da_L/dz_L) * (dz_L/da_{L-1}) * ... * (da_2/dz_2) * (dz_2/da_1) * (da_1/dz_1) * (dz_1/dw_1)

Each (da/dz) term is the activation derivative. For sigmoid, max is 0.25. Multiplying many numbers < 1 together gives a tiny result. This is why deep networks with sigmoid had gradients that "vanished" to nearly zero for early layers.
</details>

### Application

**Q7**: You're training a network and notice the loss is oscillating wildly without decreasing. What's likely wrong and how would you fix it?

<details>
<summary>Answer</summary>
The learning rate is likely too high, causing the optimizer to overshoot the minimum and bounce around.

Fixes:
1. Reduce the learning rate (e.g., divide by 10)
2. Use learning rate scheduling (start high, decrease over time)
3. Use adaptive learning rate methods (Adam, RMSprop)
4. Check for data preprocessing issues (features not normalized)
</details>

**Q8**: Why is it important to store intermediate values (z, a) during the forward pass?

<details>
<summary>Answer</summary>
Backpropagation needs these values to compute gradients:
- Activation values (a) are needed to compute dL/dW = delta * a^T
- Pre-activation values (z) are needed to compute activation derivatives f'(z)

Without storing these, we'd need to recompute them during backpropagation, doubling the computational cost. This is a classic space-time tradeoff.
</details>

---

## Reading List

### Essential Reading
- **Rumelhart, Hinton & Williams (1986)** - "Learning Representations by Back-propagating Errors" - The seminal paper
- **Nielsen, Chapter 2** - "How the backpropagation algorithm works" ([online](http://neuralnetworksanddeeplearning.com/chap2.html))

### Mathematical Foundation
- **Goodfellow et al., Chapter 6.5** - Deep Learning - "Back-Propagation and Other Differentiation Algorithms"

### Practical Insights
- **Karpathy (2019)** - "A Recipe for Training Neural Networks" ([blog](http://karpathy.github.io/2019/04/25/recipe/))

### Video Resources
- **3Blue1Brown** - "What is backpropagation really doing?" ([YouTube](https://www.youtube.com/watch?v=Ilg3gGewQ5U))
- **Stanford CS231n** - Lecture 4: Backpropagation

### Historical Perspective
- **Schmidhuber (2015)** - "Deep Learning in Neural Networks: An Overview"

---

## Summary

This lecture covered:

1. **Optimization problem** - Finding weights that minimize loss
2. **Loss landscapes** - Visualizing the space we're searching
3. **Gradient descent** - Walking downhill by following gradients
4. **Learning rate** - Critical hyperparameter controlling step size
5. **Chain rule** - Mathematical foundation for computing gradients
6. **Backpropagation** - Efficient algorithm for gradient computation
7. **Credit assignment** - How networks attribute error to weights

**Key Takeaway**: Backpropagation + gradient descent is the engine that makes neural network learning possible. Understanding these algorithms is essential for debugging and improving networks.

**Next Lecture**: [Training Dynamics and Regularization](Lecture-6-Training-Dynamics-and-Regularization) - We'll learn about practical training considerations and how to prevent overfitting.

<div class="lecture-nav">
<a href="Lecture-4-Activation-and-Loss-Functions">Previous: Activations</a>
<a href="index">Home</a>
<a href="Lecture-6-Training-Dynamics-and-Regularization">Next: Training</a>
</div>
