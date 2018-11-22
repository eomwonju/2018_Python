import math
probability={'a':7,'b':9,'c':11,'d':13,'e':3,'f':20,'g':5,'h':30,'i':2,'j':5}
moonja=input()
value=0
for i in moonja:
    value+=probability[i]
print(math.ceil(value/len(moonja)))
