for i in range(9,1, -1):
    for j in range(1,9):
        if(5<=i<=8 and j>=6 ):
            break
        else:
            print("%4d"%(i*100+j), end='')
    print()