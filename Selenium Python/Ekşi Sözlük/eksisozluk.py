from selenium import webdriver

import time

browser=webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

browser.get(url)
time.sleep(5)

elements= browser.find_elements_by_css_selector(".content")

for element in elements:
	print("***********************")
	print(element.text)

browser.close()

#//*[@id="entry-item-list"]/li[1]/div[1] 1.  chrome incele copy xpath
#//*[@id="entry-item-list"]/li[1]/div[1] 2.


