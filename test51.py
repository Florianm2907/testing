import requests

url = "http://hack.arrrg.de/chal/chal301"  # Replace with the actual URL you want to delete.

try:
    response = requests.delete(url)
    if response.status_code == 204:  # HTTP 204 No Content is a common response for successful DELETE requests.
        print("Delete request successful.")
    else:
        print(f"Failed to delete. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
