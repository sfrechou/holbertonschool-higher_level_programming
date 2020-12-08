#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number
if number2 < 0 :
    number2 = number2 * -1
if number2 % 10 > 5 :
    print("Last digit of {} is {} and is greater than 5".format(number, number2 % 10))
elif number2 % 10 < 6 and number % 10 != 0 :
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, number2 % 10))
else :
    print("Last digit of {} is {} and is 0".format(number, number2 % 10))
