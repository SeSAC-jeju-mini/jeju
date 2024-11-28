import pandas as pd
import re

import sys  # 한글깨짐방지
sys.stdout.reconfigure(encoding = 'utf-8')

# 데이터 읽기
data = pd.read_csv('C:/Users/r2com/Documents/jeju_blog_titles.csv', encoding='utf-8')

# 제거할 패턴 리스트
remove_words = ['제주', r'\d{1,2}월', '가볼만한곳', '겨울', r'\d{4}년']

# 제목 열 추출 (대소문자 구분 확인)
titles = data['Title'].fillna('')  # NaN 값 제거 또는 빈 문자열로 대체


# 제목 정리 및 출력
for title in titles:
    cleaned_title = title  # 원래 제목 복사
    
    # 불필요한 단어 제거
    for word in remove_words:
        cleaned_title = re.sub(word, '', cleaned_title)
    
    # 특수 문자, 괄호, 불필요한 기호 제거
    cleaned_title = re.sub(r'[^\w\s]', '', cleaned_title)
    
    # 다중 공백을 하나로 줄임
    cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()
    
    # 결과 출력
    if cleaned_title:  # 제목이 비어있지 않으면 출력
        print(cleaned_title)