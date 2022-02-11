import requests 
from bs4 import BeautifulSoup

url ="https://search.daum.net/search?w=tot&DA=BFT&nil_profile=fix_similar&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res=requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
#print(soup)

# with open ("quiz.html","w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("ul",attrs={"class":"list_place"}).find_all("li")
print(data_rows)
for index,row in enumerate(data_rows):
    columns = row.find_all()
