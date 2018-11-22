x = int(input())

if (x%10)>5 :
    a = x//10 + 1
    b = 0
    c = 18*(x//10) + 8 + (x%10)

else :
    a = x//10
    b = 1
    c = 18*(x//10) + 5 + (x%10)

print(a)
print(b)
print(c)
