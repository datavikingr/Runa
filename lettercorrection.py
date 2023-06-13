#! python3
#3rd Pass

import json

## Import the dictionaries from the file
with open('dictionaries/letterswap.json') as f:
    ls_dict = json.load(f)

# Open the input file
with open('texts/futhark_raw.txt', 'r') as g:
    # Read the entire file into a string
    s = g.read()

# Initialize an empty list to store the modified characters
modified_chars = []

# Iterate over the characters in the string
for c in s:
    # If the character is a key in the dictionary, replace it with the corresponding value
    if c in ls_dict:
        c = ls_dict[c]
    # Otherwise, keep the character as it is
    modified_chars.append(c)

# Join the modified characters into a modified string
modified_s = ''.join(modified_chars)

# Open the output file
with open('texts/futhark_allrunes.txt', 'w') as f:
    # Write the modified string to the output file
    f.write(modified_s)
    
print('Third pass - remove bugged output: Complete!')
