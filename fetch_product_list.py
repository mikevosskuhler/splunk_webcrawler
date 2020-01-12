import requests
from bs4 import BeautifulSoup
def get_urls(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    all_found=soup.find_all('a', class_='product-title')
    hrefs = []
    for a in range(len(all_found)):
        hrefs.append(f'https://<vendor>.com/{all_found[a]["href"]}')
    return hrefs
urls = get_urls('<searchurl>')
print(urls)
