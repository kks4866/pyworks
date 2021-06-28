#1번문제
import math

A=[70,60,55,75,95,90,80,80,85,100]
total =0
for score in A:
    total += score
average = total /len(A)
print(average)

#2번문제
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n%2 ==1:
        result.append(n*2)

result2=[]
result2=[n*2 for n in numbers if n%2==1]
print(result)

#3번문제
class Calculator:
    def __init__(self):
        self.value=0

    def add(self,val):
        self.value+=val

class UpgradeCalculator(Calculator):
    def minus(self, val):
       self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#4번문제
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value +=val
        if self.value >100:
            self.value =100
            return self.value

cal2 =MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)

def abs_square(a):
    b=a*a
    return math.sqrt(b)

print