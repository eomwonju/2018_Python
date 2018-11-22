f1 = open('test.txt','w+')

for i in range(1,10) :
    data = '%d lines\n'%i
    f1.write(data)

text = f1.seek((int(input())-1)*8, 0)
print(f1.readline(text))

f1.close()