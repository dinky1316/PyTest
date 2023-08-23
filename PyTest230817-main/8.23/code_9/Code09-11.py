import bs4
import urllib.request

# 찾을 때 웹 브라우저의 검사 (f12 개발자 도구, element 요소탭에서)
# ctrl + shift + c : 웹 하면에 마우스 커서를 올려보면 해당 요소의 태그 및
# 정보를 알 수 있음. 그러면, 그 정보를 가지고 크롤링을 함
# 크롤링을 하기 위한 준비물. -> 찾아서 정리하는 시간이 오래걸림

nateUrl = "https://news.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div 태그의 속성 : class, 값 : snbArea ->
tag = bsObject.find('div', {'class': 'snbArea'})

print('## 네이트 뉴스의 메뉴 목록 ##')

# div 태그의 속성 : class, 값 : snbArea -> li 태그를 모두 찾아서 리스트에 담기
# li_list
li_list = tag.findAll('li')
for li in li_list:
    # 하나씩 꺼내서 텍스트 속성만 출력
    print(li.text, end='  ')
    # print(f"li의 내용 : {li}")
    a_tag = li.find("a")
    a_tag_href = a_tag['href']
    print(a_tag_href, end='  ')
