# 딕셔너리

person={}

print(person)

person['name'] = '이순신'
person['age'] = 40

print(person)

person['address'] = "전라도"
print(person)

for value in person:
    print(person[value])

#요소 삭제 :dic.pop('address')와 같음
del person['address']
print(person)
