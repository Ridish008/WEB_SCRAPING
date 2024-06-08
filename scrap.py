import requests
import csv
from bs4 import BeautifulSoup


url = 'https://webscraper.io/test-sites/e-commerce/allinone'
response = requests.get(url)


if response.status_code == 200:
    print("Data fetched successfully!")
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_elements = soup.find_all('h4', class_='pull-right')
    
    with open('prices.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Price']) 
        
        for price in price_elements:
            csvwriter.writerow([price.text])
    
    print("Prices have been saved to prices.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
