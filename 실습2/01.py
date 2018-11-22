x = int(input())
y = int(input())


a = x&y
b = int(a//8+(a%8)//4+(a%4)//2+(a%2))
print(b)

c = x|y
d = int(c//8+(c%8)//4+(c%4)//2+(c%2))
print(d)
