#!python3
import string

def process_line(line):
    # Swap „ and “ for "
    modified_line = line.replace("„", "\"").replace("“", "\"")
    # Check if the line contains "Bellows" or "Íslenzk fornrit"
    if "Bellows" not in modified_line and "Íslenzk fornrit" not in modified_line:
        # Remove lines that only contain punctuation
        if not all(char in string.punctuation or char.isspace() for char in modified_line):
            # Remove blank lines
            if modified_line.strip():  # Check if the line is not empty after stripping whitespace
                return modified_line
    
    return ''

def main():
    files = ['english_input.txt', 'oldnorse_input.txt']
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Process each line
        modified_lines = [process_line(line) for line in lines]
        with open(file_path, 'w', encoding='utf-8') as file: # Write modified content back to the file
            file.writelines(modified_lines)

main()