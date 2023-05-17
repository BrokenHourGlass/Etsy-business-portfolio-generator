import requests
from bs4 import BeautifulSoup
import os
import json

base_url = "https://www.etsy.com/shop/Blackcatsandbroomsti?ref=items-pagination&page={}&sort_order=date_desc"

# This will hold all the item data
items = []

# Ensure the catalog directory exists
os.makedirs('catalog', exist_ok=True)

# Loop over the first 4 pages
# change 2 to 5
for page_num in range(1, 5):
    # Get the page content
    response = requests.get(base_url.format(page_num))

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all item link elements
    item_links = soup.find_all('a', class_='listing-link')

    # Visit each item's page and extract the data
    for link in item_links:
        item_url = link['href']
        item_response = requests.get(item_url)
        item_soup = BeautifulSoup(item_response.text, 'html.parser')

        # Get the item name, price, description, and image URLs
        name = item_soup.find('h1', class_='wt-text-body-01 wt-line-height-tight wt-break-word wt-mt-xs-1').text.strip()
        price = item_soup.find('p', class_='wt-text-title-03 wt-mr-xs-1').text.strip()
        description_div = item_soup.find('div', attrs={"data-id": "description-text"})
        description = description_div.text if description_div else "No description"
        images = [img['src'] for img in item_soup.find_all('img', class_='wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded') if 'src' in img.attrs]

        # Add the item data to our list
        item_data = {
            'name': name,
            'price': price,
            'description': description,
            'images': images,
        }

        # Save the item data to a file
        with open(f'catalog/{name}.json', 'w') as f:
            json.dump(item_data, f)