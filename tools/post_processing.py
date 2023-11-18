#!python3
import re

def is_line_matching_pattern(line):
    pattern = r'^\d{1,3}\.$'  # Allows 1 to 3 digits before the dot
    return re.match(pattern, line.strip()) is not None

def process_lines(lines):
    modified_lines = []

    for i, line in enumerate(lines):
        if i > 0 and line.strip().isdigit(): # Rule 1: Add a blank line before lines that only contain a number, except for the first line
            modified_lines.append('\n')
        if is_line_matching_pattern(line):
            modified_lines.append('\n')
        if line.strip().isdigit() and not line.endswith('.'): # Rule 2: Lines that only contain numbers must end with a period
            line = line.strip() + '.\n'
        modified_lines.append(line)
    return modified_lines

def main():
    files = ['EN-Lat.txt', 'EN-ASF.txt'] #'ON-YF.txt', 'ON-Lat.txt', 
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        modified_lines = process_lines(lines) # Process lines
        # Write modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

main()