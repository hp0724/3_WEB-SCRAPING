import time
from selenium import webdriver

browser =webdriver.Chrome("./chromedriver.exe")

#1. 네이버 이동 
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭 
elem=browser.find_element_by_class_name("link_login")
elem.click()

# 3. id pw 입력 
browser.find_element_by_id("id").send_keys("hp0724")
browser.find_element_by_id("pw").send_keys("password")


# 4 login 버튼 클릭 
browser.find_element_by_id("log.login").click()
time .sleep(1.5)

# 5 id를 새로 입력 
#browser.find_element_by_id("id").send_keys("hp0124")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("hp0124")

#6 html 정보 출력 
print(browser.page_source)

#7 브라우저 종료 
browser.quit()


