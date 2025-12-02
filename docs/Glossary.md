---
title: "Glossary"
short_title: "Glossary"
---

# Glossary of Neural Network Terms

This glossary provides definitions for key terms used throughout the Neural Networks for Finance course.

---

## A

**Activation Function**
A non-linear function applied to a neuron's output. Common examples include sigmoid, tanh, and ReLU. Essential for enabling neural networks to learn non-linear patterns.

**Attention Mechanism**
A technique that allows neural networks to focus on relevant parts of the input when producing output. Forms the basis of Transformer architectures.

**Autoencoder**
A neural network trained to reconstruct its input, learning compressed representations in the process. Used for dimensionality reduction and anomaly detection.

---

## B

**Backpropagation**
The algorithm for computing gradients of the loss function with respect to network weights. Works by propagating error backward from output to input layers using the chain rule.

**Batch Gradient Descent**
A training method that computes gradients using the entire training dataset before each weight update. Accurate but slow for large datasets.

**Batch Size**
The number of training examples used in one iteration of gradient descent. Typical values range from 16 to 256.

**Bias (Network)**
A learnable parameter added to the weighted sum in a neuron, allowing the activation function to shift left or right. Analogous to the intercept in linear regression.

**Bias (Statistical)**
Systematic error in model predictions. Can arise from training data, model architecture, or feature selection.

---

## C

**Chain Rule**
The calculus rule for computing derivatives of composite functions: d/dx[f(g(x))] = f'(g(x)) * g'(x). Foundation of backpropagation.

**Classification**
The task of assigning inputs to discrete categories (e.g., buy/sell, fraud/not fraud).

**Convolutional Neural Network (CNN)**
A neural network architecture using convolutional layers, designed for grid-like data such as images. Uses local connectivity and weight sharing.

**Convergence**
When training loss stops decreasing significantly, indicating the optimization has found a (local) minimum.

**Cross-Entropy Loss**
A loss function for classification problems that measures the difference between predicted probabilities and true labels. Also called log loss.

---

## D

**Dead ReLU**
A ReLU neuron that only outputs zero because its inputs are consistently negative. The neuron stops learning because its gradient is zero.

**Decision Boundary**
The surface that separates different classes in a classifier. For a perceptron, this is a hyperplane.

**Deep Learning**
Machine learning using neural networks with many layers (deep networks). Enables learning hierarchical representations.

**Derivative**
The rate of change of a function. In neural networks, derivatives of the loss with respect to weights guide learning.

**Dropout**
A regularization technique that randomly sets neuron outputs to zero during training. Prevents overfitting by encouraging redundant representations.

---

## E

**Early Stopping**
Stopping training when validation performance stops improving. Prevents overfitting by avoiding excessive training.

**Efficient Market Hypothesis (EMH)**
The theory that asset prices reflect all available information, making consistent outperformance difficult.

**Epoch**
One complete pass through the entire training dataset.

**Error**
The difference between predicted and actual values. Also called residual.

---

## F

**Feature**
An input variable used by the model. In finance: P/E ratio, momentum, volume, etc.

**Feature Engineering**
The process of creating informative input features from raw data. Critical for financial applications.

**Feedforward Network**
A neural network where information flows only from input to output, with no cycles. Includes MLPs.

**Forward Propagation**
Computing the network output from input by passing data through successive layers.

---

## G

**Gradient**
A vector of partial derivatives indicating the direction of steepest increase of a function. Used to update weights in gradient descent.

**Gradient Descent**
An optimization algorithm that iteratively adjusts parameters in the direction opposite to the gradient to minimize a function.

**Gradient Vanishing/Exploding**
Problems where gradients become extremely small or large during backpropagation, hindering learning in deep networks.

---

## H

**Hebbian Learning**
The principle that connections between neurons that fire together should strengthen. "Neurons that fire together wire together."

**Hidden Layer**
A layer between input and output layers. Learns intermediate representations not directly observed.

**Hyperparameter**
A parameter set before training (not learned), such as learning rate, number of layers, or regularization strength.

---

## I

**Initialization**
Setting initial values for network weights before training. Proper initialization is critical for successful learning.

---

## L

**L1 Regularization**
Adding the sum of absolute weights to the loss function. Encourages sparse weights (many zeros).

**L2 Regularization**
Adding the sum of squared weights to the loss function. Encourages small weights. Also called weight decay.

**Learning Rate**
A hyperparameter controlling the step size in gradient descent. Too large causes divergence; too small causes slow learning.

**Linear Separability**
When two classes can be separated by a linear boundary (hyperplane). Perceptrons can only solve linearly separable problems.

**Local Minimum**
A point where the loss is lower than all nearby points, but not necessarily the global minimum.

**Long Short-Term Memory (LSTM)**
A type of recurrent neural network designed to handle long sequences by using gating mechanisms.

**Look-Ahead Bias**
Using information that wouldn't have been available at prediction time. A critical error in financial ML.

**Loss Function**
A function measuring how wrong the model's predictions are. Training minimizes this function.

---

## M

**McCulloch-Pitts Neuron**
The first mathematical model of a neuron (1943). Binary inputs/outputs with fixed weights.

**Mean Squared Error (MSE)**
A loss function for regression that computes the average squared difference between predictions and targets.

**Mini-Batch**
A subset of training data used for one gradient update. Balances accuracy and computational efficiency.

**Multi-Layer Perceptron (MLP)**
A feedforward neural network with one or more hidden layers. Can approximate any continuous function.

---

## N

**Neural Network**
A computational model inspired by biological neurons, consisting of interconnected nodes organized in layers.

**Neuron (Artificial)**
A computational unit that computes a weighted sum of inputs, adds a bias, and applies an activation function.

**Non-Stationarity**
When statistical properties (mean, variance) change over time. Common in financial data.

---

## O

**Optimization**
The process of finding parameters that minimize (or maximize) an objective function.

**Output Layer**
The final layer of a network that produces predictions.

**Overfitting**
When a model performs well on training data but poorly on new data. The model has memorized rather than generalized.

---

## P

**Parameter**
A learnable value in the network (weights and biases). Distinguished from hyperparameters.

**Perceptron**
The simplest neural network: a single neuron with adjustable weights. Can solve linearly separable problems.

**Perceptron Convergence Theorem**
Guarantees that the perceptron learning algorithm will find a solution in finite time if the data is linearly separable.

---

## R

**Recurrent Neural Network (RNN)**
A neural network with connections forming cycles, allowing it to process sequential data.

**Regime Change**
A shift in market behavior or statistical properties. Models trained in one regime may fail in another.

**Regularization**
Techniques to prevent overfitting by constraining model complexity. Examples: L1, L2, dropout.

**ReLU (Rectified Linear Unit)**
An activation function: f(x) = max(0, x). Popular for hidden layers due to computational efficiency.

**Regression**
Predicting a continuous value (e.g., stock return) rather than a category.

---

## S

**Sigmoid Function**
An activation function that squashes input to range (0, 1). Formula: 1/(1 + e^(-x)).

**Softmax Function**
An activation function that converts a vector to a probability distribution (outputs sum to 1). Used for multi-class classification.

**Stochastic Gradient Descent (SGD)**
Gradient descent using one training example per update. Fast but noisy.

**Supervised Learning**
Learning from labeled data where each input has a known correct output.

---

## T

**Tanh Function**
An activation function that squashes input to range (-1, 1). Zero-centered, often preferred over sigmoid.

**Test Set**
Data held out completely from training and validation, used only for final performance evaluation.

**Training**
The process of adjusting network weights to minimize the loss function.

**Training Curve**
A plot of loss (or accuracy) over training epochs, used to diagnose learning progress.

**Transaction Costs**
Costs incurred when trading, including commissions, bid-ask spread, and market impact.

**Transformer**
A neural network architecture based entirely on attention mechanisms, without recurrence or convolution.

---

## U

**Underfitting**
When a model is too simple to capture patterns in the data, performing poorly even on training data.

**Universal Approximation Theorem**
States that a neural network with one hidden layer can approximate any continuous function, given enough neurons.

---

## V

**Validation Set**
Data used during training to tune hyperparameters and monitor for overfitting. Separate from training and test sets.

**Vanishing Gradient**
When gradients become extremely small in early layers, preventing those layers from learning.

---

## W

**Walk-Forward Validation**
A validation method for time series that trains on past data and tests on future data, rolling forward through time.

**Weight**
A learnable parameter that scales an input to a neuron. Determines the importance of each input.

**Weight Decay**
Another term for L2 regularization, referring to the shrinkage of weights toward zero.

---

## X

**XOR Problem**
A classification problem that cannot be solved by a single perceptron because it is not linearly separable. Motivated the development of multi-layer networks.

---

## Notation Reference

| Symbol | Meaning |
|--------|---------|
| x | Input |
| y | Target/output |
| w | Weight |
| b | Bias |
| z | Pre-activation (weighted sum) |
| a | Post-activation |
| L | Loss |
| eta | Learning rate |
| lambda | Regularization strength |
| f | Activation function |
| W | Weight matrix |

---

[Home](index) | [Lecture 1](Lecture-1-History-and-Biological-Inspiration)
