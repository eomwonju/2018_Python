# '''
class tv:
    def __init__(self):
        self.volume = 0
        self.channel = 0

    def setChannel(self, x):
        self.channel = x

    def setVolume(self, y):
        self.volume = y

    def turnOn():
        return

    def turnOff():
        return


sam = int(input())
lg = int(input())
SS = []
LG = []

for i in range(sam):
    SS.append(tv())
for j in range(lg):
    LG.append(tv())

while 1:
    str = input()
    a = str.split()
    if a[0] == 'END':
        break
    elif a[0] == 'LG':
        if a[2] == 'volume':
            LG[int(a[1]) - 1].setVolume(int(a[3]))
        elif a[2] == 'channel':
            LG[int(a[1]) - 1].setChannel(int(a[3]))
    elif a[0] == 'SS':
        if a[2] == 'volume':
            SS[int(a[1]) - 1].setVolume(int(a[3]))
        elif a[2] == 'channel':
            SS[int(a[1]) - 1].setChannel(int(a[3]))
    elif a[0] == 'PP':
        if a[1] == 'SS':
            if a[3] == 'volume':
                data = SS[int(a[2]) - 1].volume
            elif a[3] == 'channel':
                data = SS[int(a[2]) - 1].channel
        elif a[1] == 'LG':
            if a[3] == 'volume':
                data = LG[int(a[2]) - 1].volume
            elif a[3] == 'channel':
                data = LG[int(a[2]) - 1].channel
        print(data)

# '''