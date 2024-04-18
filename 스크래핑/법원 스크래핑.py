import requests
import csv
import requests
from bs4 import BeautifulSoup

#https://curlconverter.com/ 참조

import requests

cookies = {
    'WMONID': 'QxhiKu445nz',
    'JSESSIONID': 'LQpVtfvcdqHpCqF2uPXze0pVKrKlNXocgW9M22RjjiECVyyFzh3YLAly4ibXWnMQ.amV1c19kb21haW4vYWlzMg==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'WMONID=QxhiKu445nz; JSESSIONID=LQpVtfvcdqHpCqF2uPXze0pVKrKlNXocgW9M22RjjiECVyyFzh3YLAly4ibXWnMQ.amV1c19kb21haW4vYWlzMg==',
    'Origin': 'https://www.courtauction.go.kr',
    'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'bubwLocGubun=1&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&notifyLoc=on&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2024&saSer=&ipchalGbncd=000331&termStartDt=2024.04.12&termEndDt=2024.04.26&lclsUtilCd=&mclsUtilCd=&sclsUtilCd=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'

response = requests.post(
    'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf',
    cookies=cookies,
    headers=headers,
    data=data,
)

# 엑셀 파일로 저장하기
filename = "법원경매.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["순서", "가격"] # 컬럼 속성명 만들기

writer.writerow(columns_name)

# soup 객체 만들기
soup = BeautifulSoup(response.text, "lxml")
costbox = soup.find('table', attrs={"class": "Ltbl_list"}) 
costs = costbox.find_all('td', attrs={"class": "txtright"}) 

i = 1

for cost in costs: 
    price = cost.text 
    print(f"{str(i)}위: {price}")
    data = [str(i), price]
    writer.writerow(data)
    i += 1