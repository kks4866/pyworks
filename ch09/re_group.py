import re

p=re.compile("(\w+)\s+(\d+[-]\d{4}[-]\d{4})")
s =p.search("jang 010-8354-5088")
print(s.group(1))
print(s.group(2))