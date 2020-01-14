from fetch_product_list import get_urls
import csv
url = input('what is the search url?')
vendor = input('who is the vendor?')

urls = get_urls(url, vendor)
with open("products_list.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(urls)
