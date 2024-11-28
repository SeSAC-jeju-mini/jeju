import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.font_manager as fm

# 한글 폰트 설정 (경로 수정)
font_path = r"C:\Users\R2COM\AppData\Local\Microsoft\Windows\Fonts\NanumSquareB.otf"
font_name = fm.FontProperties(fname=font_path).get_name()

import sys
sys.stdout.reconfigure(encoding='utf-8')

# 데이터 읽기
data = pd.read_csv('C:/Users/r2com/Documents/top_30_words.csv', encoding='utf-8')

# '단어'와 '빈도수' 열을 가져옵니다.
words = data['단어']
frequencies = data['빈도수']

# 단어 빈도 분석
word_counts = Counter(dict(zip(words, frequencies)))

# 빈도수 상위 5개 단어
top_words = word_counts.most_common(5)
print("상위 5개 단어:", top_words)

# 네트워크 분석 (단어 간 관계를 보여주기 위한 그래프)
G = nx.Graph()

# 단어를 노드로 추가하고 빈도수를 엣지로 추가
for word, freq in top_words:
    G.add_node(word, size=freq)

# 단어 간 관계를 간단하게 임의로 추가 (여기서는 연결 예시로 직접 추가)
G.add_edge('도', '여행', weight=5)
G.add_edge('여행', '추천', weight=3)

# # 그래프 그리기
# pos = nx.spring_layout(G, k=0.5, iterations=20)  # 레이아웃 설정
# plt.figure(figsize=(10, 8))
# nx.draw(G, pos, with_labels=True, node_size=[v['size']*200 for v in G.nodes.values()],
#         node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')
# plt.title("단어 관계 네트워크")


# 워드클라우드 생성 (빈도수를 기준으로 시각화)
wordcloud = WordCloud(width=800, height=600, background_color='white', 
                      font_path=font_path).generate_from_frequencies(word_counts)

# 워드클라우드 출력
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 축 제거
plt.rc('font', family=font_name)
plt.show()