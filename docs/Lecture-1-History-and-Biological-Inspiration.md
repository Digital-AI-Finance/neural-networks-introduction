# Lecture 1: History and Biological Inspiration

**Duration**: ~45 minutes | **Slides**: 18 | **Prerequisites**: None

---

## Learning Objectives

After completing this lecture, you should be able to:

1. Explain the historical development of neural networks from 1943-1969
2. Describe how biological neurons process information
3. Identify the key contributions of McCulloch, Pitts, Hebb, and Rosenblatt
4. Understand the analogy between neural networks and decision-making committees
5. Recognize why the brain inspired early AI researchers

---

## Key Concepts

### 1. The Investment Committee Analogy

Before diving into mathematics, consider how an investment committee makes decisions:

**The Process:**
1. Each analyst provides input based on their expertise
2. Opinions are weighted by seniority/experience
3. Weighted votes are summed
4. If the total exceeds a threshold: **Buy**

| Analyst | Opinion | Weight | Weighted Vote |
|---------|---------|--------|---------------|
| Analyst A | +1 (bullish on earnings) | 1.0 | +1.0 |
| Analyst B | -1 (concerned about debt) | 1.0 | -1.0 |
| Analyst C | +1 (good momentum) | 1.0 | +1.0 |
| Senior Partner | -1 (market risk) | 2.0 | -2.0 |
| **Total** | | | **-1.0** |

With a threshold of 0, the decision is: **Don't Buy**

**This is exactly how a perceptron works!** The artificial neuron:
- Receives inputs (analyst opinions)
- Applies weights (seniority)
- Sums the weighted inputs
- Applies a threshold decision rule

---

### 2. Historical Timeline: 1943-1969

#### 1943: McCulloch-Pitts Neuron

Warren McCulloch (neuroscientist) and Walter Pitts (mathematician) published "A Logical Calculus of Ideas Immanent in Nervous Activity."

**Key Insight**: Neurons can be modeled as logical gates that perform computation.

Their model:
- Binary inputs (0 or 1)
- Binary output (fires or doesn't fire)
- Threshold-based activation

**Limitation**: Weights were fixed, not learned.

![McCulloch-Pitts Model](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module1_perceptron/charts/mcculloch_pitts_diagram/mcculloch_pitts_diagram.png)

#### 1949: Hebbian Learning

Donald Hebb proposed how neural connections strengthen:

> "Neurons that fire together, wire together."

**Hebb's Rule**: When neuron A consistently activates neuron B, the connection between them strengthens.

Mathematically:
```
delta_w = learning_rate * x * y
```
Where:
- `delta_w` = change in weight
- `x` = input activation
- `y` = output activation

This was the first learning rule for neural networks!

#### 1958: The Perceptron

Frank Rosenblatt at Cornell built the **Mark I Perceptron**, a physical machine that could:
- Learn to classify visual patterns
- Adjust weights automatically through training

**The New York Times (1958)**: "The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence."

The hype was enormous - perhaps too enormous.

#### 1969: The AI Winter Begins

Marvin Minsky and Seymour Papert published "Perceptrons," mathematically proving that:

1. Single perceptrons cannot solve the XOR problem
2. Many interesting problems are not linearly separable

This criticism, combined with overhyped expectations, led to the first "AI Winter" - a period of reduced funding and interest in neural networks.

---

### 3. Biological Neurons

To understand artificial neurons, we must first understand their biological inspiration.

#### Structure of a Biological Neuron

| Component | Function |
|-----------|----------|
| **Dendrites** | Receive signals from other neurons |
| **Cell Body (Soma)** | Processes incoming signals |
| **Axon** | Transmits output signal |
| **Synapses** | Connections to other neurons |

#### How Neurons Communicate

1. **Input**: Dendrites receive chemical signals (neurotransmitters)
2. **Integration**: Cell body sums incoming signals
3. **Threshold**: If sum exceeds threshold, neuron "fires"
4. **Output**: Electrical signal travels down axon
5. **Transmission**: Signal converted to chemical at synapse

#### Key Numbers
- Human brain: ~86 billion neurons
- Each neuron: ~7,000 synaptic connections
- Total synapses: ~100 trillion

![Biological vs Artificial Neuron](https://raw.githubusercontent.com/Digital-AI-Finance/neural-networks-introduction/main/module1_perceptron/charts/biological_vs_artificial_neuron/biological_vs_artificial_neuron.png)

---

### 4. From Biology to Mathematics

The artificial neuron is a simplified mathematical model:

| Biological | Artificial |
|------------|------------|
| Dendrites | Inputs (x) |
| Synaptic strength | Weights (w) |
| Cell body | Summation function |
| Threshold | Activation function |
| Axon output | Output (y) |

**Important**: Artificial neurons are inspired by biology but do NOT accurately model real neurons. The brain is far more complex than our models suggest.

---

## Key Formulas

### McCulloch-Pitts Neuron
```
y = 1 if sum(x_i) >= threshold
y = 0 otherwise
```

### Hebbian Learning Update
```
w_new = w_old + eta * x * y
```
Where `eta` is the learning rate.

---

## Finance Application: Stock Screening

A perceptron can act as a simple stock screener:

**Inputs (features)**:
- P/E Ratio
- 6-month momentum
- Trading volume
- Debt-to-equity ratio
- Earnings surprise

**Output**:
- 1 = Add to portfolio (Buy)
- 0 = Pass

**The key insight**: Instead of manually setting decision rules, the perceptron learns appropriate weights from historical winners and losers.

---

## Practice Questions

### Conceptual Understanding

**Q1**: Why did McCulloch and Pitts model neurons as binary threshold units?

<details>
<summary>Answer</summary>
They focused on the neuron's all-or-nothing firing behavior. A neuron either fires (sends a signal) or doesn't - there's no "partial" firing. This maps naturally to binary logic (0 or 1, True or False).
</details>

**Q2**: What is Hebb's learning rule in simple terms?

<details>
<summary>Answer</summary>
"Neurons that fire together, wire together." If an input neuron consistently causes an output neuron to fire, the connection between them strengthens. This is the biological basis for learning and memory.
</details>

**Q3**: Why was the XOR problem significant for perceptrons?

<details>
<summary>Answer</summary>
XOR (exclusive or) cannot be solved by a single perceptron because it's not linearly separable - you cannot draw a single straight line to separate the two classes. This demonstrated fundamental limitations of single-layer networks.
</details>

**Q4**: True or False: Artificial neurons accurately simulate biological neurons.

<details>
<summary>Answer</summary>
False. Artificial neurons are highly simplified mathematical models. Real neurons have complex temporal dynamics, thousands of connections, and use chemical signaling. The artificial model captures only the basic input-weight-threshold concept.
</details>

**Q5**: In the investment committee analogy, what corresponds to the "weights" in a perceptron?

<details>
<summary>Answer</summary>
The seniority or expertise level of each analyst. Just as a senior partner's opinion carries more weight than a junior analyst's, learned weights in a perceptron determine how much each input feature influences the final decision.
</details>

### Application

**Q6**: A loan approval perceptron has these inputs: income, credit score, employment years. What might negative weights indicate for certain features?

<details>
<summary>Answer</summary>
Negative weights would indicate features that reduce the likelihood of approval. For example, a negative weight on "number of existing loans" would mean more loans decrease approval probability. However, income and credit score would typically have positive weights.
</details>

**Q7**: Why did the AI winter occur after Minsky and Papert's book?

<details>
<summary>Answer</summary>
Several factors: (1) The mathematical proof that perceptrons couldn't solve important problems like XOR, (2) The overhyped expectations from media coverage in the 1950s-60s that neural networks would quickly achieve human-level intelligence, (3) The resulting loss of confidence from funding agencies and researchers.
</details>

---

## Reading List

### Essential Reading
- **McCulloch & Pitts (1943)** - "A Logical Calculus of Ideas Immanent in Nervous Activity" - The foundational paper
- **Rosenblatt (1958)** - "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain"

### Historical Context
- **Minsky & Papert (1969)** - "Perceptrons" - The book that started the AI winter
- **Olazaran (1996)** - "A Sociological Study of the Official History of the Perceptrons Controversy"

### Accessible Introductions
- **Nielsen, Chapter 1** - "Using neural nets to recognize handwritten digits" ([online](http://neuralnetworksanddeeplearning.com/chap1.html))
- **3Blue1Brown** - "But what is a neural network?" ([YouTube](https://www.youtube.com/watch?v=aircAruvnKk))

### Finance Connection
- **Dixon, Halperin & Bilokon (2020)** - "Machine Learning in Finance" - Chapter on neural network history

---

## Summary

This lecture covered:

1. **The investment committee analogy** - Neural networks are like weighted voting systems
2. **Historical development** (1943-1969) - From McCulloch-Pitts to the AI winter
3. **Biological inspiration** - How real neurons inspired artificial ones
4. **Key limitations** - Why single perceptrons faced fundamental constraints

**Next Lecture**: [Perceptron Fundamentals](Lecture-2-Perceptron-Fundamentals) - We dive deep into the mathematics and learning algorithm of the perceptron.

---

[Home](index) | Next: [Lecture 2: Perceptron Fundamentals](Lecture-2-Perceptron-Fundamentals)
