# Importing required libraries
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.bbc.com/news"

# Send a GET request to fetch the website's HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the news article titles
    titles = soup.find_all('h3', class_='gs-c-promo-heading__title')
    
    # Print the titles
    print("Top News Articles:")
    for i, title in enumerate(titles[:10], start=1):  # Displaying the top 10 articles
        print(f"{i}. {title.text}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

