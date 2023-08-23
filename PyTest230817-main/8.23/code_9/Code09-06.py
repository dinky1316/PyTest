import bs4

webPage = open('C:/CookAnalysis/HTML/Sample03.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 각 태그의 속성까지 포함해서 선택
tag = bsObject.find('div', {'id': 'myId1'})
print(tag)

tag = bsObject.find('div', {'class': 'myClass1'})
print(tag)

# 복수로 찾을 시 리스트화 해서 출력
tag = bsObject.findAll('div', {'class': 'myClass1'})
print(tag)
