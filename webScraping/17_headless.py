
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless =True 
options.add_argument("window-size=1920*1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()


url = "https://play.google.com/store/movies"
browser.get(url)

import time 
interval =2 # 2초에 한번씩 스크롤 내림 

# 현재 문서 높이를 가져와서 저장 
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행 
while True:
    #스크롤 가장 아래로 내림 
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    #페이지 로딩 대기 
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장 
    curr_height = browser.execute_script("return document.body.scrollHeight")

    #이전이랑 현재랑 높이가 같으면 새로운 로딩이 없다는것 
    if curr_height == prev_height :
        break

    prev_height=curr_height

print("스크롤 완료 ")

browser.get_screenshot_as_file("goolge_move.png")


import requests 
from bs4 import BeautifulSoup

soup =BeautifulSoup(browser.page_source,"lxml")

movies =soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
print(len(movies))


for movie in movies : 
    title = movie.find("div",attrs={"class":"Epkrse"}).get_text()
    #print(title)

    #할인전 가격
    original_price =movie.find("span",attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price=original_price.get_text()
    else:
        #print(title,"할인되지 않은 영화제외 ")
        continue
    #할인된가격

    price = movie.find("span",attrs={"class":"VfPpfd VixbEe"}).get_text()
    
    # 링크
    link = movie.find("a",attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # 올바른 링크 https://play.google.com/store/movies +link

    print(f"제목:{title}")
    print(f"할인 전 금액 {original_price}")
    print(f"할인 후 금액 {price}")
    print("링크:","https://play.google.com"+link)
    print("-"*60)
browser.quit()
