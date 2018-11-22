x1 = int(input())
x2 = int(input())

for i in range(x1, 0, -1):
    for j in range(1,x2+1):
        if i <= j :
            print("%4d"%(i*100+(j-i+1)), end='')
        else:
            print("    ", end='')
    print()