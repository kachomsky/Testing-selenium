import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.get('http://www.newtours.demoaut.com/')
time.sleep(5)
driver.find_element_by_link_text("REGISTER").click()
time.sleep(2)
countryDropDown = Select(driver.find_element_by_name("country"))
countryDropDown.select_by_index(5)
countryDropDown.select_by_value("11")
countryDropDown.select_by_visible_text("CONGO")
time.sleep(2)
driver.quit()