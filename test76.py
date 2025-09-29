import requests
from bs4 import BeautifulSoup

def extract_cells(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the div with id "coilgame"
        coilgame_div = soup.find('div', id='coilgame')
        
        # Find all divs with class "cell"
        cells = coilgame_div.find_all('div', class_='cell')
        
        # Extract the class of each cell and store them in an array
        cell_classes = [cell['class'][1] for cell in cells]
        
        return cell_classes
    else:
        print("Failed to fetch the webpage.")
        return None

# Example usage
url = "https://hack.arrrg.de/mortal-coil/"
cells = extract_cells(url)
if cells:
    print(cells)
