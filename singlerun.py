#!python3
#first Pass

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  as ChromeService
import time, string, subprocess, json

print('First Pass, removing punctuation.')
# Scrub oldnorse_input.txt for punctuation
def remove_punctuation(punc_input):
  # define punctuation to remove, using a known constant from the string library
  punct = string.punctuation
  # return the input string with all punctuation marks removed
  return ''.join([char for char in punc_input if char not in punct])
# Open the input file in read mode, assign it
with open('oldnorse_input.txt', 'r') as input_file:
  # read the entire contents of the file as a string
  punc_input = input_file.read()
# Call the remove_punctuation function
punc_output = remove_punctuation(punc_input)
# open the output file in write mode
with open('1-oldnorse_nopunc.txt', 'w') as output_file:
  # write the output string to the file
  output_file.write(punc_output)
print('First pass: Complete!')

print('Second pass, cross referencing runic.is')
driver_path = 'chromedriver/chromedriver'
brave_path = '/usr/bin/brave-browser'
####HACK - Updating to Selenium 4.

# Set the path to the ChromeDriver executable
service = ChromeService(driver_path)
# Configure Chrome options
options = webdriver.ChromeOptions()
options.binary_location = brave_path
# options.add_argument("--headless")
# Create the Chrome WebDriver using the Service and Options
driver = webdriver.Chrome(service=service, options=options)

####HACK
#open our source
driver.get('https://runic.is/')
#Let it load
time.sleep(3)
# Loop through each input string
with open('1-oldnorse_nopunc.txt') as input_file:
    oldnorse_array = input_file.readlines()
for runa_string_in in oldnorse_array:
    # Find the input field on the page and enter the text from the input string
    input_field = driver.find_element('id', 'inntak')
    input_field.send_keys(runa_string_in)
    time.sleep(.5)
    # Find the button on the page that submits the text and click it
    submit_button = driver.find_element('id', 'fa_runir_takki')
    submit_button.click()
    time.sleep(.5)
    # Use BeautifulSoup to parse the HTML on the page and find the resulting output text
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # Screen for Stanza numbers
    if len(runa_string_in) <= 4:
        runo_string = runa_string_in
    else:
        runo_string = soup.find('div', {'id': 'runirstadur'}).text
    # Housecleaning the input box
    input_field.clear()
    time.sleep(1)
    # Write the output text to the output.txt file
    with open('2-futhark_raw.txt', 'a') as output_file:
        output_file.write(runo_string + '\n')
#KILL IT WITH FIRE
driver.close()
driver.quit()
print('Second Passs: Complete!')

print('Third pass: Fixing the letter-typos')
## Import the dictionaries from the file
with open('dictionaries/letterswap.json') as f:
    ls_dict = json.load(f)
# Open the input file
with open('2-futhark_raw.txt', 'r') as g:
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
with open('3-futhark_allrunes.txt', 'w') as f:
    # Write the modified string to the output file
    f.write(modified_s)
print('Third pass: Complete!')

print('Fourth Pass, spell-check')
with open('dictionaries/spellcheck.json') as f:
    sc_dict = json.load(f)
# Open the input file
with open('3-futhark_allrunes.txt', 'r') as f:
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
    modified_line = '᛫'.join(modified_words) # I like the dot-space better. Looks somehow too thin. Needs meat.
    # Add the modified line to the list of modified lines
    modified_lines.append(modified_line)
# Open the output file
with open('4-spchked_futhark.txt', 'w') as f:
    # Write the modified lines to the output file
    f.writelines(modified_lines)
print('Fourth pass: Complete!')

print('Fifth Pass, remove empty lines.')
# Open the input file in read mode
with open('4-spchked_futhark.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
# Open the output file in write mode
with open('FINAL.txt', 'w') as file:
    # Loop through each line
    for line in lines:
        # Check if the line is empty (contains only whitespace)
        if line.strip():
            # Write non-empty lines to the output file
            file.write(line)
print('Final Pass Complete.')