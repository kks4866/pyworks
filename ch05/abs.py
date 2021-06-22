# abs(x) 직접 정의
#절대값 알고리즘1
def abs_sign(x): #math 모듈호출
    return x
n1 = -11

if 0<n1:
    print(n1)
else:
    print(n1*-1)
    
#절대값 2
def abs_sign(x):
    if x<0:
        return -x
    else:
        return x

#절대값 3
def abs_square(x):
    y= x*x
    return math.sqrt(y)

n2 = abs_sign(-3)
n3 = abs_square(-3)
print(n2)
print(n3)
