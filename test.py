import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
url = ('https://news.naver.com/main/ranking/popularDay.naver?date=20240225')
browser.get(url)