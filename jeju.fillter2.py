import pandas as pd
import re
from collections import Counter

import sys
sys.stdout.reconfigure(encoding='utf-8')

# 데이터 읽기
data = pd.read_csv('C:/Users/r2com/Documents/jeju_blog_titles.csv', encoding='utf-8')

# 제거할 패턴 리스트
remove_words = ['제주', r'\d{1,2}월', '가볼만한곳', '겨울', r'\d{4}년']

# 제목 열 추출 (결측값 처리)
titles = data['Title'].fillna('')  # NaN 값 제거 또는 빈 문자열로 대체

# 제목 정리 함수
def clean_title(title):
    cleaned_title = title
    for word in remove_words:
        cleaned_title = re.sub(word, '', cleaned_title)
    cleaned_title = re.sub(r'[^\w\s]', '', cleaned_title)  # 특수문자 제거
    cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()  # 다중 공백 제거
    return cleaned_title

# 정리된 제목 리스트 생성
cleaned_titles = [clean_title(title) for title in titles]

# 모든 단어 리스트 생성
words = []
for title in cleaned_titles:
    words.extend(title.split())  # 제목을 단어로 분리 후 리스트에 추가

# 단어 빈도 계산
word_counts = Counter(words)

# 상위 5개 단어 추출
top_30_words = word_counts.most_common(30)

# 결과 출력
# print("중복된 상위 5개의 단어:")
# for i, (word, count) in enumerate(top_30_words, start=1):
#     print(f"{i}. {word} - {count}번")

# 결과를 데이터프레임으로 변환
df_top_words = pd.DataFrame(top_30_words, columns=['단어', '빈도수'])

# CSV 파일로 저장
output_path = 'C:/Users/r2com/Documents/top_30_words.csv'
df_top_words.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"상위 30개의 단어를 '{output_path}'에 저장했습니다.")