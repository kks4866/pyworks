
with open('scorelist.txt', 'a') as f:
    while True:
            key= input("성적을 저장할까요?(y/n")
            if key == 'n' or key == 'N':
                 break
            if key == 'y' or key == 'Y':
                name = input("이름 입력 : ")
                kor = int(input("국어 점수 입력 : "))
                math = int(input("수학 점수 입력 : "))
                #avg = (kor + math) / 2
    f.write(name + ' ')
    f.write(str(kor) + ' ')
    f.write(str(math) + ' ')
       # f.write(str(avg) + '\n')








