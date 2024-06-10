# 라이브러리 준비하기
import csv
import requests
from bs4 import BeautifulSoup
from collections import Counter

a = []

def max_num():
    url = "https://dhlottery.co.kr/common.do?method=main"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    max_count = soup.find('strong', attrs={"id":"lottoDrwNo"}).text
    return int(max_count)

def lottoNumber(draw_no):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        a.append(data['drwtNo1'])
        return a
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")
        
for i in range(1,max_num()):
    lottoNumber(i)
print(Counter(a))