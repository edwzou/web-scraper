import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://www.kijiji.ca/b-cars-trucks/calgary/toyota-corolla/0__2008/k0c174l1700199a68"

# Send a request to the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all listings
listings = soup.find_all('div', class_='search-item')

# Extract price and year information
for listing in listings:
    price = listing.find('div', class_='price').text.strip()
    details = listing.find('div', class_='details').text.strip()
    year = None
    for detail in details.split('\n'):
        if detail.strip().isdigit() and len(detail.strip()) == 4:
            year = detail.strip()
            break
    print(f"Price: {price}, Year: {year}")
