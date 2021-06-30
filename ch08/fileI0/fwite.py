
# 파일 열기(open()) -> 파일 쓰기(write()) -> 파일 닫기(close())

f = open('C:/pyfile/hello.txt', 'w')
f.write('Hello ~ python\n')
#f.write(1000) #숫자는 입력불가 - 포맷 방식으로 입력 가능
f.write('\n%.1f' % 7.3)
num ="\n%d" %100000
f.write(num)
f.write('\n안녕 ~ 파이썬\n')
f.close()