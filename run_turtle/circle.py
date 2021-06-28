# 여러개의 원 만들기
import turtle as t

t.shape("turtle")
t.color("blue")
t.speed(0)
t.bgcolor("black")
n = 50
for x in range(n):
    t.circle(80)
    t.left(360/n)


t.mainloop()