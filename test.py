import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date,timedelta

now = date.today()
# now_week = date.today() - timedelta(6)
# start = now_week.strftime("%y%m%d")
# stop = now.strftime("%y%m%d")
start = now - timedelta(7)
day = start

# start_stop = range(int(start),int(stop)-1)
company_name = ['YTN', 'KBS', 'SBS']
df = pd.DataFrame(columns=company_name)

# for day in range(int(start), int(stop)):
for x in range(8):
    day_string = day.strftime("%y%m%d")
    url = f"https://news.naver.com/main/ranking/popularDay.naver?date=20{day_string}"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    boxs = soup.find_all("div", attrs={"class": "rankingnews_box"})
    for box in boxs:
        news = []
        name = box.find("strong", attrs={"class": "rankingnews_name"}).get_text()
        if name in company_name:
            titles = box.find_all("a", attrs={'class': "list_title nclicks('RBP.rnknws')"})
            for i, title in enumerate(titles):
                if i <= 2:
                    news.append(f'{i + 1}번 :' + title.get_text())
                else:
                    pass
            news = '\n'.join(news)
            news.split('\n', )

            df.loc[day_string, name] = news
    day = day + timedelta(1)

df.to_csv('news.csv', encoding='utf-8-sig')



