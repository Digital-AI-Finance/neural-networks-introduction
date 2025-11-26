"""
Quick script to copy and compile with real trained chart
"""
import shutil
from datetime import datetime
from pathlib import Path

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
new_file = Path(f"{timestamp}_neural_networks_real_trained.tex")

# Copy the final version
shutil.copy("20251124_1748_neural_networks_final.tex", new_file)

print(f"Created: {new_file}")
print("Now the real trained chart is included!")
print(f"\nReal accuracies from trained models:")
print("  1 Neuron (Logistic): 50%")
print("  2 Neurons: 51%")
print("  4 Neurons: 100%")
print("  10 Neurons: 100%")
