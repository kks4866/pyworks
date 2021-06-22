# 1번문제

국어 = 80
영어 = 75
수학 = 55
sum = 국어+영어+수학
Average = sum/3

print("평균 점수 : ", Average)

#2번문제
num = 13

print(13%2)

n=13
if n%2==0:
    print("짝수")
else:
    print("홀수")
    
#3번문제
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#4번문제

pin ="881120-2068234"
gender = pin[7]
print(gender)

if gender == "1":
    print("남자입니다")
else:
    print("여자입니다")

#5번 문제
a = "a:b:c:d"
b = a.replace(':','#')
print(b)


#6번 문제
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7번 문제
a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#split() 예제
msg='Life is too short'
msg = msg.split() #구분기호 : 공백
print(msg)

s ="a:b:c"
s = s.split(':')
print(s)
#8번 문제

a = (1,2,3)
a = a +(4,)
print(a)

#9번 문제
a= dict()
print(a)
a['name']='python'
print(a)
a[('a')]='python'
#print(a)
#a[[1]]='python'
print(a)
a[250]='python'
print(a)

#10번 문제

a={'A':90,'B':80,'C':70}
result=a.pop('B') #추출
print(a)
print(result)

#11번 문제
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet= set(a)
b= list(aSet)
print(b)

#12번 문제
a=b=[1,2,3]
a[1]=4
print(b)













