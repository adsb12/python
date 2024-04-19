from requests import get

def riot_crowl(name):
    
    api_key = "RGAPI-0c58aaca-2526-49e4-bde8-9294a2e4e69b"
    #api 키
    
    base_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
    #api센터에 있던 url에서 마지막 값은 입력 할 값이니 변수를 넣어준다
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }
    #header값을 들고 오는데 토큰값만 자기껄로 변경 해주자
    
    res = get(url=base_url,headers=headers)
    #riot_api에 주소를 던지고 헤더값도 던진다
    
    if res.status_code != 200:              #실패하면 밑에 출력
        print("잘못 받아옴")
    else:
        enc_id = res.json()['id']
        #받아온 값 중에 필요한건 암호화된 id이니까 그것만 가져온다
        
        riot_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{enc_id}"
        #그리고 league-v4에 위와 똑같이 값을 던진다
        
        riot_res = get(url=riot_url,headers=headers) #똑같이 가져와주고
        riot_lists = riot_res.json()                             #json형식으로 담는다
        
        def get_riot_list(riot_list):                             #배열에 담기 위한 함수 선언
            r_res = [
                riot_list.get('queueType'),
                riot_list.get('tier'),
                riot_list.get('rank'),
                riot_list.get('wins'),
                riot_list.get('losses'),
                riot_list.get('leagueName'),
                riot_list.get('leaguePoints')
            ]
            return r_res
        
        results = []
        for riot_list in riot_lists:
            results.append(get_riot_list(riot_list))        #results에 결과값 저장
        length = len(results)                                     #나중에 값이 없을때를 대비한 것
        
        return results,length