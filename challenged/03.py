import re

txt = open("03.txt", 'r')
data = txt.read()

list = []

answer = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", data)

for i in answer:
    if i[4].islower():
        list.append(i[4])

for e in list:
    print(e, end='')
