from NumbersRandom import *

n = 25
a = 10
b = 60
print("1 populating my list ")
myList = fill(n, a, b)
print(" 2 the list (5 lines) == ", myList)
display(myList)

myList = sortDescending(myList)
print("3 the sorted array largest to smallest is   ", myList)

m = maxValue(myList)
mn = minValue(myList)
s = sum(myList)
average = ave(myList)
e = evens(myList)
o = odds(myList)

print("4  Sum ==  ", s)
print("5  Minimum ", mn)
print("6  Maximum == ", m)
print("7  Average == ", average)
print("8  the number of even integers == ", e)
print("9  the number of odd integers ==  ", o)

x = digit1x(myList)
print("10 the number of integers start with the digit 1 == ", x)
y = digitx1(myList)
print("11 the number of integers end with the digit 1 == ", y)

z = div3(myList)
print("12 the number of integers divisible by 3 with no remainder == ", z)

m = median(myList)
print("13 the median of the list is  ", m)

mave = mlxMinAverage(myList)
print("14 the average of the maximum and minimum  ", mave)

z = FirstLast(m, mn)
print('15 the integer formed by first digit + lastdigit == ', z)
c = randomCount(myList, z)
print("16 the number ", z, 'in the list ?? ', c)

