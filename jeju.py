# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import sys  # 한글깨짐방지
# import re #정규표현식

# #한글깨짐방지
# sys.stdout.reconfigure(encoding = 'utf-8')

# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://www.naver.com/')

# driver.find_element(By.NAME, 'query').send_keys("12월 제주 가볼만한곳", Keys.RETURN)

# #블로그 버튼 클릭
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a'))).click()
# #EC -> 원하는 조건 설정 #element_to_be_clickable -> 클릭할 수 있는 상태인지 확인

# #스크롤 다운
# SCROLL_PAUSE_SEC = 1

# #스크롤 높이 가져옴.
# last_height = driver.execute_script('return document.body.scrollHeight')

# while True:
#     #끝까지 스크롤 다운
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

#     #1초 대기
#     time.sleep(SCROLL_PAUSE_SEC)

#     #스크롤 다운 후 스크롤 높이 다시 가져옴
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == last_height:
#         break
#     last_height = new_height

# #블로그 제목 가져오기
# titles = []
# links = driver.find_elements(By.CSS_SELECTOR,'.title_area > a')
# for link in links:
#     titles.append(link.text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys  # 한글깨짐방지
import re #정규표현식
import pandas as pd  # 데이터 저장을 위해 pandas 사용

#한글깨짐방지
sys.stdout.reconfigure(encoding='utf-8')

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.naver.com/')

driver.find_element(By.NAME, 'query').send_keys("12월 제주 가볼만한곳", Keys.RETURN)

#블로그 버튼 클릭
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a'))
).click()

#스크롤 다운
SCROLL_PAUSE_SEC = 1

#스크롤 높이 가져옴.
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # 끝까지 스크롤 다운
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

titles = []
links = driver.find_elements(By.CSS_SELECTOR, '.title_area > a')
for link in links:
    titles.append(link.text)

blog_data = pd.DataFrame({'Title': titles})

blog_data.to_csv('jeju_blog_titles.csv', index=False, encoding='utf-8-sig')

print("블로그 제목을 CSV 파일로 저장했습니다: jeju_blog_titles.csv")