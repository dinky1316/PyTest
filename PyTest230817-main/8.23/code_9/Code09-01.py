
# 정적 크롤링 : 특정 사이트의 내용(요소)를 가져오기
# 법적으로 : 판례
# 동적 크롤링 : 셀레니움 (많이 사용, 크롬),
#  외부 API(네이버)를 이용해서 수집
import urllib.request

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
html = htmlObject.read()

print(html)
