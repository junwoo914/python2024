import requests
serviceKey='4Q7d86tT2k4lJzXLCtQVkfaGJvPVn3WuBk/HZHzYE0cm1QhKAm34Cpum+AmGBuDe0vhEGpkTRPnv5pZxspiwwQ=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' :serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
air=response.text
print(air)