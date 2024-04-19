from requests import get

def riot_crowl(name):
    
    api_key = "RGAPI-0c58aaca-2526-49e4-bde8-9294a2e4e69b"
    
    base_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }
    
    res = get(url=base_url,headers=headers)
    
    if res.status_code != 200:
        print("잘못 받아옴")
    else:
        enc_id = res.json()['id']
        
        riot_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{enc_id}"
        
        riot_res = get(url=riot_url,headers=headers)
        riot_lists = riot_res.json()
        
        def get_riot_list(riot_list):
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
            results.append(get_riot_list(riot_list))
        length = len(results)
        
        return results,length