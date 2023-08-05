import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from bs4 import BeautifulSoup
import requests
 


driver = webdriver.Chrome()
driver.get('https://www.uta-net.com/')

#歌ネットでアーティスト検索
element = driver.find_element(By.XPATH, 
"/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div/input")
artist = "YOASOBI"
element.send_keys(artist)

#検索ボタンをクリック
element = driver.find_element(By.XPATH, 
"/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div/button")
element.click()


#driver = webdriver.Chrome()
#driver.get('https://www.uta-net.com/search/?target=art&type=in&keyword=' + artist)

#element = driver.find_element(By.XPATH, 
"/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/a"
#element.click()

#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5)  # Let the user actually see something!
driver.quit()


#アーティストの検索結果から番号を取得
load_url = 'https://www.uta-net.com/search/?target=art&type=in&keyword=' + artist
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
#print(soup)

elems = soup.select('tr')

for elem in elems:
    print(elem.get('href'))