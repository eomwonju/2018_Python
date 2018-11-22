#Don't use For/While
#Must use basic operator

x1 = int(input())
x2 = int(input())

result1 = x1 & x2 #둘 다 불이 켜진 집
result2 = x1 | x2 #한집이라도 불이 켜진 집

sum1 = 0 #둘 불이 켜진 호 라인의 수 측정
sum2 = 0 #한 집이라도 불이 켜진 호 라인의 수 측정

# 풀이 1
sum1 += ( result1>>3) & 1
sum1 += ( result1>>2) & 1
sum1 += ( result1>>1) & 1
sum1 += result1 & 1

sum2 += ( result2>>3) & 1
sum2 += ( result2>>2) & 1
sum2 += ( result2>>1) & 1
sum2 += result2 & 1

print("method 1 : %d %d"%(sum1, sum2))

# 풀이 2
sum1 = 0 #풀이 1과의 구별
sum2 = 0 #풀이 2과의 구별
sum1 += result1 // 8
result1 %=8
sum1 += result1 //4
result1 %=4
sum1 += result1 //2
result1 %=2
sum1 += result1

sum2 += result2 //8
result2 %=8
sum2 += result2 //4
result2 %=4
sum2 += result2 //2
result2 %=2
sum2 += result2

print("method 2 : %d %d"%(sum1, sum2))