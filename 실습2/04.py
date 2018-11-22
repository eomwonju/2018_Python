for i in range (9, 0, -1) :
    if 4<i<9 :
        for j in range (1, 6) :
            print("%2d0%d"%(i,j),end ='')
        print()
    else :
        for j in range (1,8) :
            print("%2d0%d"%(i,j),end ='')
        print()
