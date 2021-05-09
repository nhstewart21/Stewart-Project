import random
def fill( nx, x, y):
    lx = []
    j = 0
    while (j < nx):
      randNum = random.randint(x, y)
      lx.append(randNum)
      j = j + 1
    return lx

def display(lx):
    i = 0
    for x in lx:
        if (i % 5 == 0):
            print(' ')
        print(x, end=' ')
        i += 1
    print('\n')
    return lx

def maxValue(lx):
    mx = lx[1]
    for x in lx:
        if (x > mx):
            mx = x
    return mx

def minValue(lx):
    smalley = lx[1]
    for x in lx:
        if (x < smalley):
            smalley = x
    return smalley

def ave(lx):
    average = sum(lx) / len(lx)
    return average


def sum(lx):
    s = 0
    for i in range(len(lx)):
        s += lx[i]
    return s

def div3(lx):
    t = 0
    for i in range(len(lx)):
        if lx[i] % 3 == 0:
            t += 1
    return t

def evens(lx):
    e = 0
    for i in range(len(lx)):
        if lx[i] % 2 == 0:
            e += 1
    return e

def odds(lx):
    o = 0
    for i in range(len(lx)):
        if lx[i] % 2 == 1:
            o += 1
    return o

def digit1x(lx):
    temp = 0
    for i in range(len(lx)):
        valval = str(lx[i])
        if valval.startswith("1"):
            temp += 1
    return temp

def digitx1(lx):
    temp = 0
    for i in range(len(lx)):
        val = str(lx[i])
        if val.endswith("1"):
            temp += 1
    return temp

def median(lx):
    lx.sort()
    x = 0
    if len(lx) % 2 == 0:
        mediantime1 = lx[len(lx) // 2]
        mediantime2 = lx[len(lx) // 2 - 1]
        x = (mediantime1 + mediantime2) / 2
    else:
        x = lx[len(lx) // 2]
    return x

def sortDescending(lx):
    lx = sorted(lx, reverse=True)
    return lx

def mlxMinAverage(lx):
    t = (minValue(lx)+maxValue(lx))/2
    return t

def FirstLast(mx, mnx):
    data1 = str(mnx)
    data2 = str(mx)
    z = data2[0] + '' + data1[len(data1) - 1]
    return z

def randomCount(lx,zx):
    x = 'NOT in list'
    for y in lx:
        if(y == zx):
            x = 'YES'
            break
    return x
