# 라이브러리 준비하기
import csv
import requests
from bs4 import BeautifulSoup

url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%88%9C%EC%9C%84"

# 엑셀 파일로 저장하기
filename = "네이버 음원순위.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["순위", "제목"] # 컬럼 속성명 만들기

writer.writerow(columns_name)

# 웹 서버에 요청하기
res = requests.get(url)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
songBox = soup.find('div', attrs={"class": "chart_list_wrap"}) # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
songs = songBox.find_all('span', attrs={"class": "txt"}) # 인기 급상승 영역에서 'a'태그 모두 찾아 변수 cartoons에 할당

i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for song in songs: 
    title = song.text 
    print(f"{str(i)}위: {title}")
    data = [str(i), title]
    writer.writerow(data)
    i += 1