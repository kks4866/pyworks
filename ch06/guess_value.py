import random

com= random.randint(1,30)
while True:
    guess = int(input("맞혀보세요(1~30):"))
    if com == guess:
        print("정답!")
        break    
    elif com < guess:
        print("너무 커요")
    else:
        print("너무 작아요")                  


    
