import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
data = urllib.request.urlopen(url)

pfile = pickle.load(data)

opf = open("05.txt", "w")

data = ""

for i in range(0, len(pfile)):
    for j in range(0, len(pfile[i])):
            data += pfile[i][j][0]*pfile[i][j][1]
    data += "\n"
    
opf.write(data)