news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    # for index ,news in enumerate(news_list):
    #     a_idx= 0 
    #     img = news.find("img")
    #     if img: 
    #         a_idx = 1 # img 태그가 있으면 1번쨰 a 태그의 정보를 사용 

    #     a_tag = news.find_all("a"[a_idx])
    #     title = a_tag.get_text().strip()
    #     link = news.find("a")[a_idx]["href"]
    #     print_news(index,title,link)
    # print()