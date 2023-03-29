#!python3

import json

with open('dictionaries/spellcheck.json') as f:
    sc_dict = json.load(f)

# Open the input file
with open('texts/futhark_allrunes.txt', 'r') as f:
    # Read the file line by line
    lines = f.readlines()

# Initialize an empty list to store the modified lines
modified_lines = []

# Iterate over the lines
for line in lines:
    # Split the line into words
    words = line.split('᛫')

    # Initialize an empty list to store the modified words
    modified_words = []

    # Iterate over the words
    for word in words:
        # If the word is a key in the dictionary, replace it with the corresponding value
        if word in sc_dict:
            word = sc_dict[word]
        # Otherwise, keep the word as it is
        modified_words.append(word)

    # Join the modified words into a modified line
    modified_line = ' '.join(modified_words)
    # Add the modified line to the list of modified lines
    modified_lines.append(modified_line)

# Open the output file
with open('texts/CLEAN_futhark.txt', 'w') as f:
    # Write the modified lines to the output file
    f.writelines(modified_lines)

print("Fourth pass - spell check versus a world renowned expert's opinion: Complete!")
