import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.google.com/')
time.sleep(2)
search_box = driver.find_element_by_id('lst-ib')
search_box.send_keys("Draculinio")
search_button = driver.find_element_by_name("btnK")
search_button.click()
time.sleep(2)
driver.quit()
