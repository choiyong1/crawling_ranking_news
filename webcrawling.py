import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime

company_name = ['YTN', 'KBS', 'SBS']

df = pd.DataFrame(columns=company_name,  index=range(17,24))

for day in range(17, 24):
    url = f"https://news.naver.com/main/ranking/popularDay.naver?date=202402{day}"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    boxs = soup.find_all("div",attrs={"class": "rankingnews_box"})
    for box in boxs:
        news = []
        name = box.find("strong",attrs={"class": "rankingnews_name"}).get_text()
        if name in company_name:
            titles = box.find_all("a", attrs={'class': "list_title nclicks('RBP.rnknws')"})
            for i,title in enumerate(titles):
                if i <= 2:
                    news.append(f'{i+1}번 :' + title.get_text())
                else:
                    pass
            news = '\n'.join(news)
            news.split('\n',)
            df.loc[day, name] = news


df.to_csv('news.csv',encoding='utf-8-sig')

