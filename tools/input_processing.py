#!python3

def process_line(line):
    # Swap „ and “ for "
    modified_line = line.replace("„", "\"").replace("“", "\"")
    # Remove blank lines
    if modified_line.strip():  # Check if the line is not empty after stripping whitespace
        return modified_line + '\n'
    else:
        return ''

def main():
    files = ['english_input.txt', 'oldnorse_input.txt']
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Process each line
        modified_lines = [process_line(line) for line in lines if "Bellows" not in line or "Íslenzk fornrit" not in line]
        with open(file_path, 'w', encoding='utf-8') as file: # Write modified content back to the file
            file.writelines(modified_lines)

main()