
# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):

    def minus(self, val):
        self.value -= val
        return self.value

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

#부모 클래스의 인스터스
# 2번 문제
c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))
print(cal.value)

cal2 = MaxLimitCalculator()
print(cal2.add(50))
print(cal2.add(60))
print(cal2.value)

#3번

#4번
li = [1,-2,3,-5,8,-3]
result=[]
print(list(filter(lambda x :x>=0, li)))

for n in li:
    if n>=0:
        result.append(n)

print(result)

def positive(a):
    a2=[]
    for i in a:
        if i >=0:
            a2.append(i)
    return a2

li = [1,-2,3,-5,8,-3]
li2 = positive(li)
print(li2)

#6번
def times(a):
    a2=[]
    for i in a:
        a2.append(i*3)
    return a2

li = [1,2,3,4]
li2 = times(li)
print(li2)
print(list(map(lambda x : x*3,li)))









