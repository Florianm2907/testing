import requests
import time

def fetch_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch content. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Failed to fetch content. Error: {e}"

def main():
    website_url = "https://hack.arrrg.de/chal/orakel"  # Replace this with the URL of the website you want to connect to

    while True:
        content = fetch_website_content(website_url)
        print(content)
        if "Antwort" in content: print(f"{content}\n"*100)
        print("Wartet 14 Minuten")
        time.sleep(60*14)  # Sleep for 120 seconds (2 minutes) before fetching the content again

if __name__ == "__main__":
    main()
