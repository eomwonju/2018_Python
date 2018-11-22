x = int(input())
y = int(input())

for i in range (x,0, -1) :
    for j in range(1, y+1) :
        if i<=j :
            print("%4d"%(i*100+j-i+1), end = '')
        else :
            print("    ", end = '')

    print()
