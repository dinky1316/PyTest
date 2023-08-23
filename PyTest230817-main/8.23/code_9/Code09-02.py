import urllib.request
import bs4

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
# 위 코드가 정리가 덜 된 태그 집합
# 아래 코드는 bs4 -> BeautifulSoup 클래스를 이용
bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')

print(bsObject)
