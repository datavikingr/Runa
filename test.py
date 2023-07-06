from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, string, subprocess, json

driver = webdriver.Chrome()
driver.get('https://runic.is/')
driver.implicitly_wait(0.5)
input_field = driver.find_element(By.ID, 'inntak')
input_field.send_keys("um")
submit_button = driver.find_element(By.ID, 'fa_runir_takki')
submit_button.click()
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
runo_string = soup.find('h4', {'class': 'runir-nidurstada'}).contents[0]
print(runo_string)
time.sleep(2)