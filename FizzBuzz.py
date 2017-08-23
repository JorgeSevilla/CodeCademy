# -*- coding: utf-8 -*-
# Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz
# instead of the number and for the multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz.

for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print x, "FizzBuzz"  # En caso muiplo de 3 y de 5
    elif x % 3 == 0:
        print x, "Fizz"  # En caso múltipo de 3 se imprime x para saber número
    elif x % 5 == 0:
        print x, "Buzz"  # En caso múltipo de 5 se imprime x para saber número
    else:
        print x



