import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests

company_name = ['YTN', 'KBS', 'SBS']

# browser = webdriver.Chrome()
df = pd.DataFrame(columns=company_name,  index=range(217,224))

for day in range(217, 224):
    url = f"https://news.naver.com/main/ranking/popularDay.naver?date=20240{day}"
    # browser.get(url)

    res = requests.get(url)

    # page_source = browser.page_source
    soup = BeautifulSoup(res.text,'lxml')
    boxs = soup.find_all("div",attrs={'class':'rankingnews_box'})

    for box in boxs:
        news = []
        name = soup.find("strong", attrs={'class': 'rankingnews_name'}).get_text()
        if name in company_name:
            titles = soup.find_all("a", attrs={'class': "list_title nclicks('RBP.rnknws')"})
            for title in titles:
                news.append(title.get_text())
            print(news)
            df.loc[day, name] = news

    # print(names)
    # for name in names:
    #     # print(name)
    #     if name.get_text() == 'YTN':
    #         print(name)
    #         ytitles = soup.find_all("a", attrs={"class": "list_title nclicks('RBP.rnknws')"})
    #         for i,ytitle in enumerate(ytitles):
    #             df.loc[day, "YTN"] = (i,'번',ytitle.text)
    #
    #     elif name.get_text() == 'KBS':
    #         print(name)
    #         ktitles = soup.find_all("a", attrs={"class": "list_title nclicks('RBP.rnknws')"})
    #         for i,ktitle in enumerate(ktitles):
    #             df.loc[day, "KBS"] = (i,'번',ktitle.text)
    #
    #     elif name.get_text() == 'SBS':
    #         print(name)
    #         stitles = soup.find_all("a", attrs={"class": "list_title nclicks('RBP.rnknws')"})
    #         for i,stitle in enumerate(stitles):
    #             df.loc[day, "SBS"] = (i,'번',stitle.text)

df.to_csv('news.csv',encoding='utf-8-sig')

