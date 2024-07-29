#!python3

import string

# Scrub oldnorse_input.txt for punctuation
def remove_punctuation(punc_input):
  # define punctuation to remove, using a known constant from the string library
  punct = string.punctuation
  # return the input string with all punctuation marks removed
  return ''.join([char for char in punc_input if char not in punct])

# Open the input file in read mode, assign it
with open('texts/oldnorse_input.txt', 'r') as input_file:
  # read the entire contents of the file as a string
  punc_input = input_file.read()

# Call the remove_punctuation function
punc_output = remove_punctuation(punc_input)

# open the output file in write mode
with open('texts/oldnorse_nopunc.txt', 'w') as output_file:
  # write the output string to the file
  output_file.write(punc_output)

print('First pass - remove punctuation: Complete!')
