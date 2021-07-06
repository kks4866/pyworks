import re

#그룹핑된 문자열에 이름 붙이기
#?<그룹이름)
p=re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d{4}[-]\d{4})")
s =p.search("jang 010-8354-5088")
print(s.group("name"))
print(s.group("phone"))