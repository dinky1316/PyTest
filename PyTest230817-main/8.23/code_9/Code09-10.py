import bs4
import urllib.request

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
# 가독성있네 다 변환을 한 상태
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div -> id 속성의 값 : NateBi, 네이트 로고
tag = bsObject.find('div', {'id': 'NateBi'})
print(tag, '\n')

# div의 id 속성 값 : NateBi : tag 담았고 -> 하위에 a 태그 찾기 : a_tag
a_tag = tag.find("a")
print(a_tag, '\n')

# div의 id 속성 값 : NateBi : tag 담았고 -> 하위에 a 태그 찾기 : a_tag
# 이어서 속성의 href의 값만 추출
href = a_tag['href']
print(href, '\n')

# div의 id 속성 값 : NateBi : tag 담았고 -> 하위에 a 태그 찾기 : a_tag
# text만 가져오기
text = a_tag.text
print(text)
