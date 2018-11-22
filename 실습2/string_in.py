str1 = input()

strTemp =''

for ch1 in str1:
    if ch1 in 'aeiouy':
        strTemp += ('k'+ ch1)
    else:
        strTemp += (ch1 + 'i' )

print(strTemp)