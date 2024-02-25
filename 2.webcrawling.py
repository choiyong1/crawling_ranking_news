from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


# headers = "Your User Agent is:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
driver = webdriver.Chrome()
#
# #url = "https://news.naver.com/main/ranking/popularDay.naver?date=20240223"
# for day in range(17,24):
#     print(f'2024/02/{day}')
#     url = f"https://news.naver.com/main/ranking/popularDay.naver?date=202402{day}"
#     driver.get(url)
#     # time.sleep(2)
#     for name in range(1,4):
#         elem = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div[2]/div/div[{name}]/a/strong").text
#         print(elem)
#         for titles in range(1,4):
#             title = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div[2]/div/div[1]/ul/li[{titles}]/div/a").text
#             print(f'{titles}번 : {title}')
#         print('\n')
#     print('-'*100)
print("SBS")
for day in range(16,23):
    print(f'2024/02/{day}')
    Surl = f"https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=055&listType=summary&date=202402{day}"
    driver.get(Surl)
    for titles in range(1, 4):
        title = driver.find_element(By.XPATH,f"/html/body/div[1]/table/tbody/tr/td[2]/div/div[2]/ul[1]/li[{titles}]/dl/dt/a").accessibl
        dict_data = {day : title}