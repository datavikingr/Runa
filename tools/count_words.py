#!python3

import re
from collections import Counter
import sys

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove non-alphanumeric characters and split into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count word frequency
    word_count = Counter(words)

    return word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_words.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_count = count_words(input_file)

    # Print word count in the format "[word] - [# of occurrences]"
    for word, count in word_count.most_common():
        print(f"{word} - {count}")