import random

#주사위 10번 던지기


for i in range(10):
    dice = random.randint(1,6)
    print(dice)

print('='*40)

word = ['sky' , 'moon', 'space', 'earth']
w = random.choice(word)
print(w)

