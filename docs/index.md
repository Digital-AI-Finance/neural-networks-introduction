# Neural Networks for Finance - Student Wiki

Welcome to the comprehensive study guide for the **Neural Networks for Finance** course. This BSc-level lecture series introduces feedforward neural networks with practical applications in finance and stock prediction.

---

## Course Overview

This course covers the fundamentals of neural networks from their biological inspiration to modern applications in finance. You will learn:

- How artificial neurons model biological decision-making
- The mathematics behind perceptrons and multi-layer networks
- Training algorithms including backpropagation
- Practical considerations for financial applications

**Total Duration**: 8 lectures (~45 minutes each)

**Prerequisites**: Basic calculus (derivatives), linear algebra (vectors, matrices), introductory statistics

---

## Lecture Navigation

| # | Lecture | Topics | Slides |
|---|---------|--------|--------|
| 1 | [History and Biological Inspiration](Lecture-1-History-and-Biological-Inspiration) | McCulloch-Pitts, Hebb, biological neurons | 18 |
| 2 | [Perceptron Fundamentals](Lecture-2-Perceptron-Fundamentals) | Architecture, weights, decision boundaries | 32 |
| 3 | [MLP Architecture](Lecture-3-MLP-Architecture) | Hidden layers, forward propagation | 32 |
| 4 | [Activation and Loss Functions](Lecture-4-Activation-and-Loss-Functions) | Sigmoid, ReLU, MSE, cross-entropy | 23 |
| 5 | [Gradient Descent and Backpropagation](Lecture-5-Gradient-Descent-and-Backpropagation) | Optimization, chain rule, error propagation | 38 |
| 6 | [Training Dynamics and Regularization](Lecture-6-Training-Dynamics-and-Regularization) | Overfitting, dropout, early stopping | 37 |
| 7 | [Financial Applications](Lecture-7-Financial-Applications) | Walk-forward validation, case study | 27 |
| 8 | [Modern Networks and Future](Lecture-8-Modern-Networks-and-Future) | CNNs, RNNs, Transformers, ethics | 17 |

**Additional Resources**: [Glossary](Glossary) | [Reading List](#reading-list)

---

## How to Use This Wiki

### For Each Lecture

Each lecture page contains:

1. **Learning Objectives** - What you should understand after completing the lecture
2. **Prerequisites** - Which lectures to complete first
3. **Key Concepts** - Detailed explanations with examples
4. **Key Formulas** - Mathematical formulations with intuitive explanations
5. **Charts and Visualizations** - Key figures from the slides
6. **Practice Questions** - Self-assessment with answers
7. **Reading List** - Papers and resources for deeper study

### Recommended Study Path

**Week 1-2**: Lectures 1-2 (Foundations)
- Understand biological inspiration
- Master the single perceptron

**Week 3-4**: Lectures 3-4 (Architecture)
- Learn multi-layer networks
- Understand activation and loss functions

**Week 5-6**: Lectures 5-6 (Training)
- Master gradient descent and backpropagation
- Learn regularization techniques

**Week 7-8**: Lectures 7-8 (Applications)
- Apply knowledge to finance
- Understand modern developments

---

## Key Formulas Quick Reference

### The Perceptron
```
y = f(sum(w_i * x_i) + b)
```
Where:
- `x_i` = input features
- `w_i` = learned weights
- `b` = bias term
- `f` = activation function

### Gradient Descent Update Rule
```
w_new = w_old - learning_rate * gradient
```

### Backpropagation (Chain Rule)
```
dL/dw = dL/dy * dy/dz * dz/dw
```

### Common Activation Functions
| Function | Formula | Derivative |
|----------|---------|------------|
| Sigmoid | 1/(1+e^(-x)) | sigmoid(x)*(1-sigmoid(x)) |
| tanh | (e^x - e^(-x))/(e^x + e^(-x)) | 1 - tanh^2(x) |
| ReLU | max(0, x) | 1 if x > 0, else 0 |

---

## Reading List

### Foundational Papers
- McCulloch & Pitts (1943) - "A Logical Calculus of Ideas Immanent in Nervous Activity"
- Rosenblatt (1958) - "The Perceptron: A Probabilistic Model"
- Rumelhart, Hinton & Williams (1986) - "Learning Representations by Back-propagating Errors"

### Textbooks
- **Goodfellow, Bengio & Courville** - *Deep Learning* ([deeplearningbook.org](https://www.deeplearningbook.org/))
- **Nielsen** - *Neural Networks and Deep Learning* ([neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com/))
- **Bishop** - *Pattern Recognition and Machine Learning*

### Finance-Specific
- **Lopez de Prado** - *Advances in Financial Machine Learning*
- Heaton et al. - "Deep Learning for Finance: Deep Portfolios"

### Video Resources
- 3Blue1Brown - Neural Networks series
- Stanford CS231n - Convolutional Neural Networks for Visual Recognition

---

## Course Materials

### Slide PDFs
Download the compiled lecture PDFs from the [repository](https://github.com/Digital-AI-Finance/neural-networks-introduction).

### Chart Code
All visualizations are available as Python scripts with full source code. Each chart folder contains:
- Python script (`.py`)
- Generated PDF and PNG
- QR code linking to the code

---

## Contact and Support

This course is part of the Digital Finance curriculum at FHGR.

**Repository**: [Digital-AI-Finance/neural-networks-introduction](https://github.com/Digital-AI-Finance/neural-networks-introduction)

**QuantLet Mirror**: [QuantLet/neural-networks-introduction](https://github.com/QuantLet/neural-networks-introduction)

---

*Last updated: December 2025*
