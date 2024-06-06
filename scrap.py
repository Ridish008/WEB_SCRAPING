import requests
import csv
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://webscraper.io/test-sites/e-commerce/allinone'

# Fetch the data from the URL
response = requests.get(url)

# Check if the response status is OK
if response.status_code == 200:
    print("Data fetched successfully!")
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements with the class "pull-right price"
    price_elements = soup.find_all('h4', class_='pull-right')
    
    # Open a CSV file to write the prices
    with open('prices.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Price'])  # Write the header row
        
        # Write each price to the CSV file
        for price in price_elements:
            csvwriter.writerow([price.text])
    
    print("Prices have been saved to prices.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
