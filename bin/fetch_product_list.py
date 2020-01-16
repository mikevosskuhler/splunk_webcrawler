import requests
from bs4 import BeautifulSoup
def get_urls(url, vendor):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_found=soup.find_all('a', class_='product-title')
    hrefs = []
    for a in range(len(all_found)):
        hrefs.append([all_found[a].contents, f'https://{vendor}/{all_found[a]["href"]}'])
    return hrefs
