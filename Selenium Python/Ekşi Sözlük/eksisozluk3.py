#Entryleri Dosyaya Yazmak
from selenium import webdriver
import random
import time

browser=webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount=1
entries=[]
entryCount=1

while pageCount<=10:
	randomPage=random.randint(1,1721)
	newUrl=url+str(randomPage)
	browser.get(newUrl)

	elements=browser.find_elements_by_css_selector(".content")
	for element in elements:
		entries.append(element.text)
	time.sleep(2)
	pageCount+=1

	i=1
with open("entries.txt","w",encoding="UTF-8") as file:
	for entry in entries:
		file.write(str(i)+".\n"+entry+"\n")
		file.write("*********************\n")
		i+=1


browser.close()
