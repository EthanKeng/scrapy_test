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
for i in range(1.9):
	driver.get('https://www.zillow.com/seattle-wa/apartments/2_p/?searchQueryState={%22pagination%22:{%22currentPage%22:{0}},%22mapBounds%22:{%22west%22:-122.42537498474121,%22east%22:-122.33439445495605,%22south%22:47.64133548441369,%22north%22:47.700789515009895},%22mapZoom%22:13,%22regionSelection%22:[{%22regionId%22:16037,%22regionType%22:6}],%22isMapVisible%22:true,%22filterState%22:{%22isForSaleByAgent%22:{%22value%22:false},%22isForSaleByOwner%22:{%22value%22:false},%22isNewConstruction%22:{%22value%22:false},%22isForSaleForeclosure%22:{%22value%22:false},%22isComingSoon%22:{%22value%22:false},%22isAuction%22:{%22value%22:false},%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false},%22isForRent%22:{%22value%22:true},%22isSingleFamily%22:{%22value%22:false},%22isManufactured%22:{%22value%22:false},%22isLotLand%22:{%22value%22:false},%22isTownhouse%22:{%22value%22:false}},%22isListVisible%22:true}'.format(i))
	sleep(3)

	driver.find_element_by_xpath('//a[@class="area-box-close"]').click()
	sleep(3)