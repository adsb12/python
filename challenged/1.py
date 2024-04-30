ex = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
#문제에서 준거

sen = []
#배열에 담고

for x in ex:                                            #준거만큼 돌린다
    x = ord(x)                                         #아스키 코드변환
    if x!=32 and chr(x).isalpha():             #띄워쓰기  제외 알파벳인지 확인
        if x>120:                                      #121은 y라 
            sen.append(chr(x-24))               #a로 돌아감
        else:
            sen.append(chr(x+2))                #아니면 문제내용대로 +2
    else:
        sen.append(chr(x))                        #알파벳 아니면 그대로 출력
for x in sen:
    print(x, end=' ')                                 #개행(\n) 안되게
    

ex2 = 'map'
before = 'abcdefghijklmnopqrstuvwxyz'
after = 'cdefghijklmnopqrstuvwxyzab'

sen2 = ex2.maketrans(before, after)
print(ex2.translate(sen2))