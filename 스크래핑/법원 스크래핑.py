import requests
import csv
import requests
from bs4 import BeautifulSoup

cookies = {
    'WMONID': 'm3CoZqmuOK4',
    'JSESSIONID': 'yFcwz7VmBAkn1T3oEkwGzrUHCk3zuq7toPTyQQ6aUAugs1T9nYevBZa7FbxZGycO.amV1c19kb21haW4vYWlzMQ==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'WMONID=m3CoZqmuOK4; JSESSIONID=yFcwz7VmBAkn1T3oEkwGzrUHCk3zuq7toPTyQQ6aUAugs1T9nYevBZa7FbxZGycO.amV1c19kb21haW4vYWlzMQ==',
    'Origin': 'https://www.courtauction.go.kr',
    'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.21 Safari/537.36',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'bubwLocGubun=1&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&notifyLoc=on&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2024&saSer=&ipchalGbncd=000331&termStartDt=2024.03.12&termEndDt=2024.03.26&lclsUtilCd=&mclsUtilCd=&sclsUtilCd=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'

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

columns_name = ["순위", "가격"] # 컬럼 속성명 만들기

writer.writerow(columns_name)

# 웹 서버에 요청하기
response.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(response.text, "lxml")
cartoonsBox = soup.find('table', attrs={"class": "Ltbl_list"}) # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
cartoons = cartoonsBox.find_all('td', attrs={"class": "txtright"}) # 인기 급상승 영역에서 'a'태그 모두 찾아 변수 cartoons에 할당
# print(cartoons)
i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for cartoon in cartoons: 
    title = cartoon.text 
    print(f"{str(i)}위: {title}")
    data = [str(i), title]
    writer.writerow(data)
    i += 1