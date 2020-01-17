import requests
from bs4 import BeautifulSoup
def get_urls(url, vendor):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    product_title = soup.find_all('a', class_='product-title')
    product_price = soup.find_all('meta', itemprop='price')
    hrefs = []
    for a in range(len(product_title)):
        hrefs.append([product_title[a].contents, f'https://{vendor}/{product_title[a]["href"]}', product_price[a]["content"]])
    return hrefs
