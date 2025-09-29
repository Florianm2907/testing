import requests
from bs4 import BeautifulSoup

url = 'https://hack.arrrg.de/challenge/100'
headers = {
    'User-Agent': 'NintendoBrowser/4.3.1.11264.US',
    'Authorization': 'Bearer YourAccessToken',
    # Add any other headers you want to modify
}
session = requests.Session()
login_url = url
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

response = requests.get(url, headers=headers)
login_form = soup.find('form')
username_field = login_form.find('input', {'name': 'username'})
password_field = login_form.find('input', {'name': 'password'})
payload = {
    'username': 'flolol',
    'password': '1234!'
}

# Submit the login form
session.post(login_url, data=payload)

print(response.text)
