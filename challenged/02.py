txt = open('02.txt','r')
data = txt.read()

answer = ''

for i in data:
    if i.isalpha():
        answer += i
        
print(answer)

import re

answer2 = re.findall("[A-Za-z]", data)
print(answer2)