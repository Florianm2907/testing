from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Define the base URL and the range of numbers you want to cycle through
base_url = "https://hack.arrrg.de/challenge/"
start_number = 420
end_number = 1000  # Change this to the desired range

# Create a WebDriver (you'll need to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Change to the appropriate driver for your browser

# Iterate through the range of numbers
number = 0
url = f"{base_url}{number}"

    # Open the URL in the browser
driver.get(url)

input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputName'))  # Replace with the ID of your text field
            )
input_field.send_keys("flolol")
input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputPw'))  # Replace with the ID of your text field
            )
input_field.send_keys("1234!")
input_field.send_keys(Keys.ENTER)  # Pressing Enter after inputting the number

# Extract the tab title
tab_title = driver.title
titel = []
# Print the URL and tab title
print(f"URL: {url}\nTab Title: {tab_title}\n")
t.sleep(2)
for number in range(start_number, end_number + 1):
    # Construct the URL
    url = f"{base_url}{number}"

    # Open the URL in the browser
    driver.get(url)

    # Extract the tab title
    tab_title = driver.title

    # Print the URL and tab title
    # print(f"URL: {url}\nTab Title: {tab_title}\n")
    if len(tab_title): titel.append(f"Nummer {number}: {tab_title}")
    print(titel)
    # t.sleep(1)
# Close the browser
driver.quit()
