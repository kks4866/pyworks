# 정규 표현식 예제
import re

#p = re.compile('[a.z]+') # +은 임의의 문자 1개 메타 문자
p = re.compile('a+b') # +는 앞문자 1개 이상 이메타 문자
m = p.match('afternoon')
print(m)
print(m.group()) #group()은 문자열을 표시해주는 함수