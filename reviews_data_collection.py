import requests
from bs4 import BeautifulSoup
import csv

# The base URL for the shop's reviews
base_url = "https://www.etsy.com/shop/Blackcatsandbroomsti/reviews?ref=pagination&page={}"

# This will hold the reviews data
reviews = []

# Loop over the pages until we have 75 5-star reviews with text
page_num = 1
while len(reviews) < 75:
    print("found list item")
    # Get the page content
    response = requests.get(base_url.format(page_num))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all review elements
    review_elements = soup.find_all('li', attrs={"data-region": "review"})

    # Extract the data from each review
    for review_element in review_elements:
        print("searching list item")
        # Get the star rating
        star_rating_element = review_element.find('span', attrs={"data-rating": "5", "class": "rating lit"})

        # Get the review text
        review_text_element = review_element.find('p', class_='prose wt-break-word wt-m-xs-0')
        review_text = review_text_element.text.strip() if review_text_element else None

        # If the review is 5 stars and has text, add it to our list
        if star_rating_element and review_text:
            reviews.append(review_text)
            print(len(reviews))

            # Stop if we have enough reviews
            if len(reviews) == 75:
                break

    # Go to the next page
    print("moving next page")
    page_num += 1

# Write the reviews to a TSV file
with open('reviews.tsv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['Review Text'])
    for review in reviews:
        writer.writerow([review])

