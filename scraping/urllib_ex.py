# 웹 스크래이핑(크롤링)
from urllib import request

#url = "http://www.daum.com"
content = request.urlopen("http://www.daum.net")
print(content.read())