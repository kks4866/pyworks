import sys

args = sys.argv[1:] #리스트형 자료

sum = 0
for i in args:
    sum = sum +  int(i)

print(sum)




