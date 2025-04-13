from collections import Counter
import matplotlib.pyplot as plt
import os
from typing import Union

def save_histogram(text: Union[str, bytes], filename: str):
    if isinstance(text, bytes):
        text = text.hex()

    frequencies = Counter(text)
    sorted_frequencies = dict(sorted(frequencies.items()))

    os.makedirs("out", exist_ok=True)
    output_path = os.path.join("out", filename)

    plt.figure(figsize=(12, 6))
    plt.bar(sorted_frequencies.keys(), sorted_frequencies.values(), color='skyblue')
    plt.title(f"Character Histogram - {filename.split('.')[0]}")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
    print(f"Histogram saved to: {output_path}")
