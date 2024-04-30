import requests
from bs4 import BeautifulSoup

nothing = "63579"

def get_data(nothing):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    data = str(soup)
    
    return get_nothing(data)

def get_nothing(data):
    txt = "and the next nothing is"
    if txt in data:
        nothing = data[data.find("is ") + 3:]
        print(nothing)
        return nothing
    else:
        return data
    
if __name__ == "__main__":
    while nothing.isnumeric() == True:
        nothing = get_data(nothing)
    print(nothing)