
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless =True 
options.add_argument("window-size=1920*1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatsmyua.info/"
browser.get(url)
id = browser.find_element_by_id("custom-ua-string")
print(id.text)
browser.quit()