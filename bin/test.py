import csv 
import sys
file_name = '/opt/splunk/etc/apps/splunk_webcrawler/lookups/test_list.csv'
with open(file_name, 'rU') as f:  #opens PW file
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=','))



from selenium import webdriver
from bs4 import BeautifulSoup
from check_stock import check_inventory
webdriver_location = '/home/mike/Downloads/chromedriver'
product_url = 'https://www.bol.com/nl/p/philips-sonicare-protectiveclean-4500-hx6837-28-elektrische-tandenborstel/9200000093063161/'
basket_url = 'https://www.bol.com/nl/order/basket.html'
html = check_inventory(product_url, basket_url, webdriver_location)
soup = BeautifulSoup(html, 'html.parser')
soup.find_all('select', class_="js_quantity_dropdown tst_item_count_selection")[0].contents[21].contents