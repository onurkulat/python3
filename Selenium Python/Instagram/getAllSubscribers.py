from selenium import webdriver
import time
import logininfo

browser=webdriver.Chrome()
url="https://www.instagram.com/"

browser.get(url)

time.sleep(2)

girisYap=browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")

girisYap.click()
time.sleep(5)

username=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
password=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

#username=browser.find_element_by_name("username")
#password=browser.find_element_by_name("password") bu şekildede alınabilir


username.send_keys(logininfo.username)
password.send_keys(logininfo.password)

girisYap2=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")
girisYap2.click()

time.sleep(8)

simdidegilbutonu=browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")
simdidegilbutonu.click()
time.sleep(4)

profilbutonu=browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
profilbutonu.click()

time.sleep(5)
takipcibutonu=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
#tuslar=browser.find_element_by_css_selector(".bnq48")
#takipcibutonu=tuslar.click()

takipcibutonu.click()

#scroll özelliği
#followers=document.querySelector(".PZuss")
#followers.scrollTo(0,followers.scrollHeight)

time.sleep(5)

jscommand="""
followers=document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""

lenOfPage=browser.execute_script(jscommand)
match=False
while (match==False):
	lastCount=lenOfPage
	time.sleep(1)
	lenOfPage=browser.execute_script(jscommand)
	if lastCount==lenOfPage:
		match=True


time.sleep(5)

followersList=[]

followers=browser.find_element_by_css_selector(".FPmhX.notranslate._0imsa ")

for follower in followers:
	followersList.append(follower.text)



with open("takipciler.txt","w",encoding="UTF-8") as file:
	for follower in followersList:
		file.write(follower+"\n")



browser.close()