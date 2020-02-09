from selenium import webdriver
import time
def check_inventory(producturl, basketurl, webdriver_location):
    browser = webdriver.Chrome(webdriver_location)
    browser.get(producturl)
    browser.find_element_by_class_name('js_preventable_buy_action').click()
    time.sleep(5)
    browser.get(basketurl)
    browser.find_element_by_id('tst_quantity_dropdown').click()
    browser.find_element_by_xpath('//*[@id="tst_quantity_dropdown"]/option[11]').click()
    browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[1]/div/div[3]/div/div/div[1]/div/form/fieldset/div[2]/div[2]/input').send_keys('500')
    browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[1]/div/div[3]/div/div/div[1]/div/form/fieldset/div[2]/div[2]/div[2]/a').click()
    return browser.page_source