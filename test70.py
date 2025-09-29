import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
# Replace 'path_to_webdriver' with the path to your web driver executable
driver = webdriver.Chrome()  # Or specify your browser driver

# Open the website and authenticate if required
driver.get('https://hack.arrrg.de/challenge/83')  # Replace with your target website

input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputName'))  # Replace with the ID of your text field
            )
input_field.send_keys("flolol")
input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputPw'))  # Replace with the ID of your text field
            )
input_field.send_keys("1234!")
input_field.send_keys(Keys.ENTER)  # Pressing Enter after inputting the number
driver.get('https://hack.arrrg.de/challenge/83')  # Replace with your target website


# Wait for 10 seconds to manually authenticate if necessary
time.sleep(1)
# Function to input numbers every 5 seconds
def input_numbers():
    a = 1
    try:
        for i in range(274, 274):
            input_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'challenge_answer'))  # Replace with the ID of your text field
                )
            input_field.send_keys(i)
            input_field.send_keys(Keys.ENTER)  # Pressing Enter after inputting the number
            time.sleep(1)
            number = i
            a += 1
            if a == 21: 
                time.sleep(31)
                i-=1
                a = 0
                driver.get('https://hack.arrrg.de/challenge/83')  # Replace with your target website
    except:
        print(number)
# Reload the page and start entering numbers
while True:
    driver.refresh()
    input_numbers()

