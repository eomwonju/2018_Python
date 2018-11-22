x = int(input())

bigBox =0
smallBox = 0

bigBox = x //10 # 큰 박스의 갯수
r = x%10
if (0 <r<= 5):
    smallBox+=1
elif ( r > 5):
    bigBox+=1

print("%d %d %d"%(bigBox, smallBox, bigBox*8+smallBox*5+x))