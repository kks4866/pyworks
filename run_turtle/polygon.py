# 다른 곳에 도형 그리기
import turtle as t

t.shape("turtle")


def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)
def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)
        

polygon(3)
polygon(5)

t.up() # 선 올리기
t.forward(200) #100px 뒤로 이동
t.down() #선 내리기

polygon(4)
polygon2(4,80)

t.up() # 선 올리기
t.back(400) #100px 뒤로 이동
t.down() #선 내리기

polygon2(5,50)
