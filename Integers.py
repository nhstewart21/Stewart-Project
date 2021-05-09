import random
a = -50
b = 50
x = random.randint(a, b) 	# returns an integer a <= x <= b
y = random.randint(a, b) 	# returns an integer a <= y <= b
z = random.randint(a, b) 	# returns an integer a <= z <= b
w = random.randint(a, b) 	# returns an integer a <= w <= b
print('The 4 random integers are:', x, ' ', y, ' ', z, ' ', w)
maximum = max(x, y, z, w)
minimum = min(x, y, z, w)
print("maximum = ", maximum)
print("minimum = ", minimum)
amount_even = 0
if x % 2 == 0:
    amount_even = amount_even + 1
if y % 2 == 0:
    amount_even = amount_even + 1
if z % 2 == 0:
    amount_even = amount_even + 1
if w % 2 == 0:
    amount_even = amount_even + 1
print("The number of even integers is", amount_even)

amount_odd = 0
if x % 2 != 0:
    amount_odd = amount_odd + 1
if y % 2 != 0:
    amount_odd = amount_odd + 1
if z % 2 != 0:
    amount_odd = amount_odd + 1
if w % 2 != 0:
    amount_odd = amount_odd + 1
print("The number of odd integers is", amount_odd)

amount_greater = 0
if -25 < x < 25:
    amount_greater = amount_greater + 1
if -25 < y < 25:
    amount_greater = amount_greater + 1
if -25 < z < 25:
    amount_greater = amount_greater + 1
if -25 < w < 25:
    amount_greater = amount_greater + 1
print("The number of integers greater than -25 but less than 25 is", amount_greater)

positive = 0
if x >= 0:
    positive = positive + 1
if y >= 0:
    positive = positive + 1
if z >= 0:
    positive = positive + 1
if w >= 0:
    positive = positive + 1
print("The number of positive integers is", positive)

negative = 0
if x < 0:
    negative = negative + 1
if y < 0:
    negative = negative + 1
if z < 0:
    negative = negative + 1
if w < 0:
    negative = negative + 1
print("The number of negative integers is", negative)

avg_min_max = (maximum + minimum) / 2
print("The average of the smallest and largest integers is", avg_min_max)
average = (x + y + z + w) / 4
print("The average of all four integers is", average)



