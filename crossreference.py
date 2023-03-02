#!python3

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, string

##This will make damned sure the driver is installed correctly - why yes, there is a story there. No, I won't tell you.
driver = webdriver.Chrome(ChromeDriverManager().install())

#open our source
driver.get('https://runic.is/')
#Let it load, it is chrome, c'mon
time.sleep(5)

# Loop through each input string
with open('oldnorse_nopunc.txt') as input_file:
    oldnorse_array = input_file.readlines()

for runa_string_in in oldnorse_array:

    # Find the input field on the page and enter the text from the input string
    input_field = driver.find_element_by_id('inntak')
    input_field.send_keys(runa_string_in)
    time.sleep(.5)

    # Find the button on the page that submits the text and click it
    submit_button = driver.find_element_by_id('fa_runir_takki')
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
    with open('futhark_raw.txt', 'a') as output_file:
        output_file.write(runo_string + '\n')
            
#KILL IT WITH FIRE
driver.close()
driver.quit()

print('Second Passs - cross-referencing reputable sources: Complete!')
