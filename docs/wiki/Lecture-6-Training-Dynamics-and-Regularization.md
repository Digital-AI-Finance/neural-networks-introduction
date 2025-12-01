# Lecture 6: Training Dynamics and Regularization

**Duration**: ~45 minutes | **Slides**: 37 | **Prerequisites**: [Lecture 5](Lecture-5-Gradient-Descent-and-Backpropagation)

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Distinguish between batch, mini-batch, and stochastic gradient descent
2. Explain overfitting and why it's problematic
3. Apply L1 and L2 regularization
4. Understand and implement dropout
5. Use early stopping to prevent overfitting
6. Design train/validation/test splits

---

## Key Concepts

### 1. Batch vs. Stochastic Gradient Descent

**Batch Gradient Descent:**
- Compute gradient using ALL training examples
- Update weights once per epoch
- Accurate gradient estimate
- Slow for large datasets
- Memory intensive

**Stochastic Gradient Descent (SGD):**
- Compute gradient using ONE training example
- Update weights after each example
- Noisy gradient estimate
- Fast updates
- Can escape local minima

**Mini-Batch Gradient Descent (Best of Both):**
- Compute gradient using a small batch (32-256 examples)
- Balance between accuracy and speed
- Efficient hardware utilization
- Most commonly used in practice

| Method | Batch Size | Updates/Epoch | Gradient Quality |
|--------|------------|---------------|------------------|
| Batch | All (n) | 1 | Accurate |
| Mini-Batch | 32-256 | n/batch_size | Good |
| Stochastic | 1 | n | Noisy |

---

### 2. Training Curves

Monitoring training progress is essential for understanding model behavior.

**What to plot:**
- Training loss over epochs
- Validation loss over epochs
- Gap between training and validation

**Healthy training:**
- Both losses decrease
- Small gap between train/val loss
- Smooth convergence

**Unhealthy signs:**
- Training loss increases: Learning rate too high
- Large train/val gap: Overfitting
- Flat training loss: Vanishing gradients or learning rate too low

---

### 3. Overfitting: The Enemy of Generalization

**Definition:** Overfitting occurs when a model performs well on training data but poorly on new, unseen data.

**Why it happens:**
- Model is too complex relative to data
- Training data isn't representative
- Training too long

**The problem for finance:**
- Model memorizes historical patterns
- Patterns may not repeat in the future
- Leads to poor live trading performance

![Overfitting Curves](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/overfitting_curves/overfitting_curves.png)

**Signs of overfitting:**
- Training loss continues to decrease
- Validation loss starts increasing
- Perfect training accuracy but poor test accuracy

---

### 4. Train/Validation/Test Split

**Three-way split:**

| Split | Purpose | Typical Size |
|-------|---------|--------------|
| Training | Learn weights | 60-80% |
| Validation | Tune hyperparameters | 10-20% |
| Test | Final evaluation | 10-20% |

**Critical rules:**
- NEVER use test data during training or tuning
- Test set provides unbiased final estimate
- Validation set is for model selection

**Finance consideration:** Use time-based splits (more in Lecture 7):
- Train: Jan 2010 - Dec 2018
- Validation: Jan 2019 - Dec 2020
- Test: Jan 2021 - Dec 2022

---

### 5. L2 Regularization (Weight Decay)

L2 regularization penalizes large weights by adding a term to the loss.

**Modified loss:**
```
L_total = L_original + lambda * sum(w_i^2)
```

Where lambda controls regularization strength.

**Effect on update rule:**
```
w = w - eta * (dL/dw + 2*lambda*w)
w = (1 - 2*eta*lambda)*w - eta*dL/dw
```

The term `(1 - 2*eta*lambda)` shrinks weights toward zero ("weight decay").

**Why it helps:**
- Prevents weights from becoming too large
- Encourages simpler models
- Reduces overfitting

**Typical values:** lambda = 0.0001 to 0.1

---

### 6. L1 Regularization (Lasso)

L1 regularization penalizes the absolute value of weights.

**Modified loss:**
```
L_total = L_original + lambda * sum(|w_i|)
```

**Key difference from L2:**
- L1 pushes weights to exactly zero (sparsity)
- L2 pushes weights to be small but rarely zero

**When to use L1:**
- Feature selection is important
- Want a sparse model
- Interpretability matters

![L1 vs L2](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/l1_l2_comparison/l1_l2_comparison.png)

---

### 7. Dropout

Dropout randomly "drops" neurons during training by setting their output to zero.

**How it works:**
1. For each training batch:
   - Randomly select neurons to drop (probability p, typically 0.2-0.5)
   - Set dropped neurons' outputs to 0
   - Scale remaining outputs by 1/(1-p)
2. At test time:
   - Use all neurons
   - No dropout

**Why it helps:**
- Prevents co-adaptation of neurons
- Acts like training many networks and averaging
- Encourages redundant representations

![Dropout Visualization](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/dropout_visualization/dropout_visualization.png)

**Implementation:**
```
During training:
    mask = random(0,1) < (1-p)  # Keep with probability 1-p
    a = a * mask / (1-p)         # Scale to maintain expected value

During testing:
    a = a  # Use all neurons, no scaling needed
```

---

### 8. Early Stopping

Early stopping stops training when validation performance stops improving.

**Algorithm:**
```
1. Train and monitor validation loss each epoch
2. Track best validation loss seen so far
3. If validation loss doesn't improve for 'patience' epochs, stop
4. Return weights from best validation epoch
```

**Parameters:**
- **Patience:** How many epochs to wait (typically 5-20)
- **Min delta:** Minimum improvement to count (e.g., 0.0001)

![Early Stopping](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/early_stopping_demo/early_stopping_demo.png)

**Advantages:**
- Simple to implement
- Provides automatic stopping criterion
- Often as effective as other regularization

---

### 9. Combining Regularization Techniques

In practice, multiple techniques are often used together:

**Common combination:**
- L2 regularization (always helps)
- Dropout (for larger networks)
- Early stopping (as final safeguard)

**Example configuration:**
```
L2 lambda = 0.001
Dropout rate = 0.3 (hidden layers only)
Early stopping patience = 10 epochs
```

**Important:** Regularization hyperparameters should be tuned on validation set!

---

### 10. Hyperparameter Tuning

**Key hyperparameters to tune:**

| Hyperparameter | Typical Range | Tuning Method |
|----------------|---------------|---------------|
| Learning rate | 0.0001 - 0.1 | Log-scale search |
| Batch size | 16 - 256 | Powers of 2 |
| Hidden layers | 1 - 5 | Start small |
| Neurons/layer | 32 - 512 | Powers of 2 |
| L2 lambda | 0.00001 - 0.1 | Log-scale search |
| Dropout rate | 0 - 0.5 | Linear search |

**Tuning strategies:**
1. **Grid search:** Try all combinations (expensive)
2. **Random search:** Sample random combinations (often better)
3. **Bayesian optimization:** Smart sampling based on results

---

### 11. Weight Initialization

Proper initialization is crucial for training deep networks.

**Bad initialization:**
- All zeros: All neurons compute the same thing (symmetry problem)
- Too large: Exploding activations/gradients
- Too small: Vanishing activations/gradients

**Good initialization methods:**

**Xavier (Glorot) for sigmoid/tanh:**
```
W ~ Normal(0, sqrt(2/(n_in + n_out)))
```

**He initialization for ReLU:**
```
W ~ Normal(0, sqrt(2/n_in))
```

**Why it matters:** Proper initialization keeps activations and gradients in a reasonable range throughout the network.

---

## Key Formulas

### L2 Regularization
```
L_total = L_original + (lambda/2) * sum(w^2)
dL/dw = dL_original/dw + lambda * w
```

### L1 Regularization
```
L_total = L_original + lambda * sum(|w|)
dL/dw = dL_original/dw + lambda * sign(w)
```

### Dropout (Training)
```
a_dropped = a * mask / (1-p)
where mask[i] = 1 with probability (1-p), 0 otherwise
```

### Mini-Batch Gradient
```
gradient = (1/m) * sum_{i=1}^{m} gradient_i
where m = batch size
```

---

## Finance Application: The Backtest Trap

**The problem:** Overfitting in backtesting can create strategies that look profitable historically but fail in live trading.

**Warning signs:**
- Strategy works perfectly on training period
- Dramatic performance drop on new data
- Strategy relies on many parameters

**Prevention:**
1. Use walk-forward validation (Lecture 7)
2. Apply strong regularization
3. Use simple models when possible
4. Test on truly out-of-sample data

![Backtest Trap](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module3_training/charts/backtest_trap/backtest_trap.png)

---

## Practice Questions

### Mathematical Understanding

**Q1**: With L2 regularization (lambda=0.01) and learning rate (eta=0.1), if a weight is currently w=2.0 and dL_original/dw=0.5, what is the new weight?

<details>
<summary>Answer</summary>
Total gradient = dL_original/dw + lambda * w = 0.5 + 0.01 * 2.0 = 0.52
w_new = w - eta * gradient = 2.0 - 0.1 * 0.52 = 1.948

Note how the regularization term (0.01 * 2.0 = 0.02) adds to the gradient, pushing the weight more toward zero.
</details>

**Q2**: A network uses dropout with p=0.4 (40% of neurons dropped). During training, if a neuron's activation is 1.5, what values might it take after dropout?

<details>
<summary>Answer</summary>
Either:
- 0 (with probability 0.4) - neuron is dropped
- 1.5 / (1-0.4) = 1.5 / 0.6 = 2.5 (with probability 0.6) - scaled up

The scaling ensures the expected value remains 1.5:
E[output] = 0.4 * 0 + 0.6 * 2.5 = 1.5
</details>

**Q3**: You have 10,000 training examples and use batch size 100. How many weight updates occur per epoch?

<details>
<summary>Answer</summary>
Updates per epoch = total examples / batch size = 10,000 / 100 = 100 updates per epoch
</details>

### Conceptual Understanding

**Q4**: Why does L1 regularization lead to sparse weights while L2 doesn't?

<details>
<summary>Answer</summary>
L1 gradient is constant (lambda or -lambda) regardless of weight magnitude. This constant "push" toward zero affects small and large weights equally.

L2 gradient is proportional to weight (lambda * w). As weights get smaller, the regularization pressure decreases. Weights never quite reach zero.

Geometrically: L1 constraint region has corners at axes, while L2 is a smooth sphere. Solutions tend to occur at corners (sparse) for L1.
</details>

**Q5**: Why is dropout only applied during training, not testing?

<details>
<summary>Answer</summary>
During training, dropout forces the network to learn redundant representations and prevents overfitting.

During testing, we want the best possible prediction, which means using all neurons. We trained the network to work with dropout, so the scaled outputs during training ensure that test-time outputs (using all neurons) have the same expected magnitude.
</details>

**Q6**: Why might stochastic gradient descent actually work better than batch gradient descent for some problems?

<details>
<summary>Answer</summary>
The noise in SGD can be beneficial:
1. Helps escape local minima by adding randomness
2. Acts as implicit regularization
3. Can find flatter minima (which generalize better)

Also practical benefits:
4. Faster updates (don't wait for full dataset scan)
5. Works with streaming data
6. Lower memory requirements
</details>

### Application

**Q7**: You're training a stock prediction model. Training loss is 0.001 but validation loss is 0.05. What's happening and how would you address it?

<details>
<summary>Answer</summary>
This is severe overfitting - the model has memorized training data but doesn't generalize.

Potential fixes:
1. Add L2 regularization (start with lambda=0.01)
2. Add dropout (start with 0.3-0.5)
3. Reduce model complexity (fewer layers/neurons)
4. Get more training data
5. Use early stopping based on validation loss
6. Apply data augmentation if applicable

Start with the simplest fixes (regularization, early stopping) before reducing model capacity.
</details>

**Q8**: How would you decide between using L1 vs L2 regularization for a financial model?

<details>
<summary>Answer</summary>
Use L1 if:
- You want automatic feature selection
- Interpretability is important
- You suspect many features are irrelevant
- You want a sparse model

Use L2 if:
- All features are likely relevant
- You want stable small weights
- Correlated features should share weight (L2 spreads weight across correlated features)

In practice, you can try both or use Elastic Net (combination) and pick based on validation performance.
</details>

---

## Reading List

### Essential Reading
- **Nielsen, Chapter 3** - "Improving the way neural networks learn" ([online](http://neuralnetworksanddeeplearning.com/chap3.html))
- **Goodfellow et al., Chapter 7** - "Regularization for Deep Learning"

### Dropout
- **Srivastava et al. (2014)** - "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
- **Hinton et al. (2012)** - "Improving neural networks by preventing co-adaptation of feature detectors"

### Weight Initialization
- **Glorot & Bengio (2010)** - "Understanding the difficulty of training deep feedforward neural networks"
- **He et al. (2015)** - "Delving Deep into Rectifiers" (He initialization)

### Optimization
- **Ruder (2016)** - "An overview of gradient descent optimization algorithms" ([blog](https://ruder.io/optimizing-gradient-descent/))

### Finance-Specific
- **Lopez de Prado (2018)** - "Advances in Financial Machine Learning" - Chapter on backtesting

---

## Summary

This lecture covered:

1. **Batch vs SGD** - Trade-offs between gradient accuracy and speed
2. **Overfitting** - When models memorize rather than learn
3. **Train/val/test split** - Proper data separation for evaluation
4. **L2 regularization** - Penalize large weights, encourage simplicity
5. **L1 regularization** - Encourage sparsity and feature selection
6. **Dropout** - Random neuron dropping for robustness
7. **Early stopping** - Stop when validation stops improving

**Key Takeaway**: Regularization is essential for building models that generalize. Multiple techniques can and should be combined.

**Next Lecture**: [Financial Applications](Lecture-7-Financial-Applications) - We'll apply everything learned to real financial problems.

---

[Previous: Lecture 5](Lecture-5-Gradient-Descent-and-Backpropagation) | [Home](Home) | [Next: Lecture 7](Lecture-7-Financial-Applications)
