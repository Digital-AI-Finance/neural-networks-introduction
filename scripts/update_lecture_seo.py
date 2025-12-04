"""
Update lecture markdown files with:
1. Enhanced SEO front matter (description, keywords)
2. Lazy loading on all images
"""
import re
from pathlib import Path

# Lecture metadata for SEO
LECTURE_SEO = {
    'Lecture-1-History-and-Biological-Inspiration.md': {
        'description': 'Learn about the origins of neural networks from 1943-1969, including McCulloch-Pitts neurons, Hebbian learning, and the perceptron. Understand how biological neurons inspired artificial neural networks.',
        'keywords': ['neural network history', 'McCulloch-Pitts', 'Hebbian learning', 'perceptron', 'biological neurons', 'AI winter', 'Rosenblatt']
    },
    'Lecture-2-Perceptron-Fundamentals.md': {
        'description': 'Master the perceptron - the simplest neural network. Learn about weights, bias, activation functions, decision boundaries, and the perceptron learning algorithm. Understand the XOR limitation.',
        'keywords': ['perceptron', 'decision boundary', 'activation function', 'XOR problem', 'linear separability', 'perceptron learning algorithm', 'weights and bias']
    },
    'Lecture-3-MLP-Architecture.md': {
        'description': 'Understand multi-layer perceptron (MLP) architecture. Learn forward propagation, matrix notation, hidden layer representations, and how MLPs solve the XOR problem.',
        'keywords': ['MLP', 'multi-layer perceptron', 'hidden layers', 'forward propagation', 'matrix notation', 'XOR solution', 'universal approximation']
    },
    'Lecture-4-Activation-and-Loss-Functions.md': {
        'description': 'Compare activation functions (sigmoid, tanh, ReLU) and loss functions (MSE, cross-entropy). Learn when to use each for regression and classification problems in neural networks.',
        'keywords': ['activation function', 'sigmoid', 'tanh', 'ReLU', 'loss function', 'MSE', 'cross-entropy', 'vanishing gradient']
    },
    'Lecture-5-Gradient-Descent-and-Backpropagation.md': {
        'description': 'Learn gradient descent optimization and the backpropagation algorithm. Understand loss landscapes, learning rate, chain rule, and credit assignment in neural networks.',
        'keywords': ['gradient descent', 'backpropagation', 'chain rule', 'learning rate', 'loss landscape', 'optimization', 'credit assignment']
    },
    'Lecture-6-Training-Dynamics-and-Regularization.md': {
        'description': 'Master neural network training with batch vs stochastic gradient descent, overfitting prevention, L1/L2 regularization, dropout, and early stopping techniques.',
        'keywords': ['overfitting', 'regularization', 'L1', 'L2', 'dropout', 'early stopping', 'batch gradient descent', 'SGD', 'weight decay']
    },
    'Lecture-7-Financial-Applications.md': {
        'description': 'Apply neural networks to finance: walk-forward validation, avoiding look-ahead bias, regime changes, feature engineering for stock prediction, and transaction cost analysis.',
        'keywords': ['financial ML', 'walk-forward validation', 'look-ahead bias', 'stock prediction', 'regime changes', 'feature engineering', 'transaction costs', 'Sharpe ratio']
    },
    'Lecture-8-Modern-Networks-and-Future.md': {
        'description': 'Explore modern neural network architectures: CNNs, RNNs, LSTMs, and Transformers. Learn about attention mechanisms, ethical AI considerations, and future directions in financial ML.',
        'keywords': ['CNN', 'RNN', 'LSTM', 'Transformer', 'attention mechanism', 'deep learning', 'ethical AI', 'financial ML future']
    }
}

def update_front_matter(content, filename):
    """Add description and keywords to front matter"""
    if filename not in LECTURE_SEO:
        return content

    seo = LECTURE_SEO[filename]

    # Find the front matter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return content

    front_matter = match.group(1)

    # Check if description already exists
    if 'description:' in front_matter:
        return content

    # Add description and keywords before the closing ---
    new_fields = f"description: \"{seo['description']}\"\n"
    new_fields += f"keywords: {seo['keywords']}\n"

    # Insert before the closing ---
    new_content = content.replace(
        f"---\n{front_matter}\n---",
        f"---\n{front_matter}\n{new_fields}---"
    )

    return new_content

def add_lazy_loading(content):
    """Add loading='lazy' to all img tags"""
    # Pattern to match img tags without loading attribute
    pattern = r'<img\s+src="([^"]+)"\s+alt="([^"]+)">'
    replacement = r'<img src="\1" alt="\2" loading="lazy">'

    return re.sub(pattern, replacement, content)

def process_file(filepath):
    """Process a single lecture file"""
    content = filepath.read_text(encoding='utf-8')
    filename = filepath.name

    # Update front matter
    content = update_front_matter(content, filename)

    # Add lazy loading
    content = add_lazy_loading(content)

    # Write back
    filepath.write_text(content, encoding='utf-8')
    print(f"Updated: {filename}")

def main():
    docs_dir = Path(__file__).parent.parent / 'docs'

    # Process all lecture files
    for lecture_file in sorted(docs_dir.glob('Lecture-*.md')):
        process_file(lecture_file)

    print("\nAll lecture files updated with SEO metadata and lazy loading!")

if __name__ == '__main__':
    main()
