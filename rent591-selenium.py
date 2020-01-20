import csv
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



writer = csv.writer(open("result_file.csv", 'w'))
writer.writerow(['type', 'area', 'floor', 'price', 'address', 'url'])

driver = webdriver.Chrome('/Users\jojo7\Documents\GitHub\scrapy_test\chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://rent.591.com.tw/?kind=0&region=1&area=0,10&shape=2&other=balcony_1')
sleep(3)

driver.find_element_by_xpath('//a[@class="area-box-close"]').click()
sleep(3)

while True:
    try:
        sel = Selector(text=driver.page_source)
        box = sel.xpath('//*[@class="listInfo clearfix "]')
        for contents in box:            
            type = contents.xpath(".//p[1]/text()[1]").get().strip()
            area = contents.xpath(".//p[1]/text()[2]").get().strip()
            floor = contents.xpath(".//p[1]/text()[3]").get().strip()
            price = contents.xpath('.//*[@class="price"]/i/text()').get() 
            url = contents.xpath('.//h3/a/@href').get()
            address = contents.xpath('.//li[2]/p[2]/em/text()').get().strip()
            writer.writerow([type, area, floor, price, address, url])
        driver.find_element_by_xpath('//*[@class= "pageNext"]').click()
        sleep(3)

    except NoSuchElementException:
        # logger.info('No more pages to load.')
        driver.quit()
        break


