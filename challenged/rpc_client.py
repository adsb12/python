

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.system.listMethods())  # 사용 가능한 함수 출력

result = s.wikidocs(2)
print(result)  # http://wikidocs.net/2의 컨텐츠 출력