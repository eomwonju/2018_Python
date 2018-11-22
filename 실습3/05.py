import random
gawibawibo={1:'scisssor',2:'rock',3:'paper'}
b=0
while b<2:
    computer=random.randint(1,3)
    me=int(input())
    print('com:',gawibawibo[computer],'me:',gawibawibo[me])
    if me==1:
        if computer ==1:
            a='Draw'
        elif computer ==2:
            a='lose'
        else :
            a='Win'
            b=b+1
        print(a)
    elif me==2:
        if computer ==1:
            a='Win'
            b=b+1
        elif computer ==2:
            a='Draw'
        else:
            a='Lose'
        print(a)
    else:
        if computer ==1:
            a='Lose'
        elif computer ==2:
            a='Win'
            b=b+1
        else:
            a='Draw'
        print(a)
print('Won twice')
