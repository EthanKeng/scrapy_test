import csv
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


writer = csv.writer(open("result_file.csv", 'w'))
writer.writerow(['type', 'area', 'floor', 'price', 'url'])

driver = webdriver.Chrome('/Users\jojo7\Desktop\Scrapy\Chromedriver')
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
            writer.writerow([type, area, floor, price, url])
            
        driver.find_element_by_xpath('//*[@class= "pageNext"]').click()
        sleep(3)

    except NoSuchElementException:
        # logger.info('No more pages to load.')
        driver.quit()
        break


# sleep(0.5)


# profiles = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
# profiles = [profile.get_attribute('href') for profile in profiles]
# for profile in profiles:
#     driver.get(profile)
#     sleep(5)

#     sel = Selector(text=driver.page_source)

#     name = sel.xpath('//title/text()').extract_first().split(' | ')[0]
#     job_title = sel.xpath('//h2/text()').extract_first().strip()
#     schools = ', '.join(sel.xpath('//*[contains(@class, "pv-entity__school-name")]/text()').extract())
#     location = sel.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first().strip()
#     ln_url = driver.current_url

#     print('\n')
#     print(name)
#     print(job_title)
#     print(schools)
#     print(location)
#     print(ln_url)
#     print('\n')

#     try:
#         driver.find_element_by_xpath('//*[text()="More…"]').click()
#         sleep(1)

#         driver.find_element_by_xpath('//*[text()="Connect"]').click()
#         sleep(1)

#         driver.find_element_by_xpath('//*[text()="Send now"]').click()
#         sleep(1)
#     except:
#         pass

#     writer.writerow([name, job_title, schools, location, ln_url])

# driver.quit()
