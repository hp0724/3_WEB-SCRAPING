import requests 
from bs4 import BeautifulSoup

def create_soup(url):
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
    res= requests.get(url,headers=headers)
    res.raise_for_status()
    soup =BeautifulSoup(res.text,"lxml")
    return soup

def print_news(index,title,link):
    print("{}. {}".format(index+1 , title))
    print("  (링크 :{}".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%E3%85%86%EB%81%BC&tqi=hlhUYsprvToss552%2F1Cssssss4V-430320"
    soup=create_soup(url)

    # 어제보다 3° 높아요  맑음
    cast=soup.find("p",attrs ={"class":"summary"}).get_text()
    print(cast)

    curr_temp=soup.find("div",attrs={"class":"temperature_text"}).get_text().replace("현재 온도","")
    curr_temp=curr_temp.replace("°","")
    min_temp=soup.find("span",attrs={"class":"lowest"}).get_text() 
    max_temp=soup.find("span",attrs={"class":"highest"}).get_text()
    morning_rain_rate =soup.find("li",attrs={"class":"week_item today"}).get_text()
    morning_rain_rate =soup.find("span",attrs={"class":"rainfall"}).get_text()
    afternoon_rain_rate =soup.find("strong",attrs={"class":"time"},text="오후")
 
    print(morning_rain_rate)
    print(afternoon_rain_rate)
    # print(curr_temp)
    # print(min_temp)
    # print(max_temp)
    # 현재 00'C ()

def scrape_it_news():
    print("[it 뉴스 ]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup=create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    for index ,news in enumerate(news_list):
        a_idx= 0 
        img = news.find("img")
        if img: 
            a_idx = 1 # img 태그가 있으면 1번쨰 a 태그의 정보를 사용 

        a_tag = news.find_all("a")[a_idx] 
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index,title,link)
    print()

def scrape_engilsh():
    print("[오늘의 영어 회화 ")

    print()

if __name__ == "__main__":
    #scrape_weather() #오늘의 날씨 정보 가져오기 
    scrape_it_news() # it 뉴스 정보 가져오기 
    #scrape_english() # 오늘의 영어 회화 가져오기 