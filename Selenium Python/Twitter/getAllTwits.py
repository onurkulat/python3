from selenium import webdriver
import time
import logininfo
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
url="https://twitter.com/"
browser.get(url)

time.sleep(3)

giris_yap=browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")

giris_yap.click()


time.sleep(5)

username=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(logininfo.username)
password.send_keys(logininfo.password)

giris_yap2=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
giris_yap2.click()
time.sleep(10)

searchArea=browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.click()
searchArea.send_keys("#malatyaspor")
searchArea.send_keys(Keys.RETURN)
time.sleep(5)

#sayfadan geri gitmek için
#browser.back()


browser.close()

