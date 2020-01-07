import csv
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# writer = csv.writer(open("result_file.csv", 'w'))
# writer.writerow(['type', 'area', 'floor', 'price', 'address', 'url'])

driver = webdriver.Chrome('/Users\ken\github\scrapy_test\Chromedriver')
# driver.maximize_window()
sleep(0.5)
driver.get('https://www.nna.jp/')
sleep(3)
driver.find_element_by_id('user_code').send_keys('s-ookawa@hoosiers.co.jp')
driver.find_element_by_id('password').send_keys('')
driver.find_element_by_id('loginbutton').click()
