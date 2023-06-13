#!python3
#Pass #2

from bs4 import BeautifulSoup
from selenium import webdriver
import time, string, subprocess

driver_path = "chromedriver/chromedriver"
brave_path = "/usr/bin/brave-browser"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--headless=new")
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

#open our source
driver.get('https://runic.is/')
#Let it load
time.sleep(3)

# Loop through each input string
with open('texts/oldnorse_nopunc.txt') as input_file:
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
    with open('texts/futhark_raw.txt', 'a') as output_file:
        output_file.write(runo_string + '\n')
            
#KILL IT WITH FIRE
driver.close()
driver.quit()

print('Second Passs - cross-referencing reputable sources: Complete!')
