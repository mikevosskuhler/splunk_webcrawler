from selenium import webdriver
browser = webdriver.Chrome('/Users/mikevosskuhler/Downloads/chromedriver')

browser.get("<producturl>")
browser.find_element_by_xpath('//*[@id="9200000095000966"]/span[3]').click()
browser.get('<basketurl>')
browser.find_element_by_xpath('//*[@id="tst_quantity_dropdown"]').click()
browser.find_element_by_xpath('//*[@id="tst_quantity_dropdown"]/option[11]').click()
browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[1]/div/div[3]/div/div/div[1]/div/form/fieldset/div[2]/div[2]/input').send_keys('500')
browser.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[1]/div/div[3]/div/div/div[1]/div/form/fieldset/div[2]/div[2]/div[2]/a').click()
