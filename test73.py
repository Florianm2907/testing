from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Set up the Chrome webdriver
field_width = int(input("Enter the width of the field: "))

driver = webdriver.Chrome()
# URL of the webpage
url = 'https://hack.arrrg.de/mortal-coil/'  # Update with the actual URL
# Navigate to the webpage
driver.get(url)
t.sleep(2)

input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputName'))  # Replace with the ID of your text field
            )
input_field.send_keys("flolol")
input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputPw'))  # Replace with the ID of your text field
            )
input_field.send_keys("1234!")
input_field.send_keys(Keys.ENTER)

driver.get(url)
t.sleep(1)
# Find all cell elements
cells = driver.find_elements(By.CSS_SELECTOR, '#coilgame_inner .cell')

# Store cell data in an array
cell_data = []
for cell in cells:
    cell_data.append(cell.get_attribute('class'))

cell_data = []
row_data = []
for i, cell in enumerate(cells):
    row_data.append(cell.get_attribute('class'))
    # If the current cell index is divisible by the width or it's the last cell
    if (i + 1) % field_width == 0 or i == len(cells) - 1:
        cell_data.append(row_data)
        row_data = []

for row in cell_data:
    print(row)

posx = 0
posy = 0

def move_up(posx, posy, cell_data):
    for i in range(len(cell_data)):
        if cell_data[posy-1]:
            if not 'cell blocked' in cell_data[posy-1][posx]:
                cell_data[posy][posx] = 'cell blocked'
                posy -= 1
        else: return False
    return posx, posy, cell_data

def move_down(posx, posy, cell_data):
    for i in range(len(cell_data)):
        if cell_data[posy+1]:
            if not 'cell blocked' in cell_data[posy+1][posx]:
                cell_data[posy][posx] = 'cell blocked'
                posy += 1
        else: return False
    return posx, posy, cell_data

def move_right(posx, posy, cell_data):
    for i in range(len(cell_data[0])):
        if cell_data[posx+1]:
            if not 'cell blocked' in cell_data[posy][posx+1]:
                cell_data[posy][posx] = 'cell blocked'
                posx += 1
        else: return False
    return posx, posy, cell_data

def move_left(posx, posy, cell_data):
    for i in range(len(cell_data[0])):
        if cell_data[posx-1]:
            if not 'cell blocked' in cell_data[posy][posx-1]:
                cell_data[posy][posx] = 'cell blocked'
                posx -= 1
        else: return False
    return posx, posy, cell_data

def start(x, y):
    if not 'cell blocked' in cell_data[y][x]: 
        posx = x
        posy = y
        cell_data[y][x] = 'cell blocked'
    return posx, posy

def solved(cell_data):
    for row in cell_data:
        if 'cell empty' in row: return False
    return True

for row in range(len(cell_data)):
    for column in range(len(row)):
        start(column, row)
        while not solved(cell_data):
            



driver.quit()