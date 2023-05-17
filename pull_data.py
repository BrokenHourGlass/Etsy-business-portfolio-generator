import requests
import json, sys, os

from dotenv import load_dotenv

load_dotenv()

# your Etsy API key
api_key = os.getenv("API_KEY")

# the shop_id or shop_name
shop_id = 'Blackcatsandbroomsti'

# make the API request
response = requests.get(f'https://openapi.etsy.com/v2/shops/{shop_id}/listings/active?api_key={api_key}')

# parse the JSON response
data = json.loads(response.text)

# print each listing
for listing in data['results']:
    print(listing['title'], listing['price'], listing['url'])
