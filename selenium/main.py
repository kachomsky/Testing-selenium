import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.newtours.demoaut.com/')
time.sleep(5)
user_box = driver.find_element_by_name('userName')
pass_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_name('login')
user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(5)
driver.quit()