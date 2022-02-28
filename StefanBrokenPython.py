#!/bin/python3

#changed con_ to conversion to account for the correct variable name AND added additional ) on final line to account for equation

#program to convert kilometers to miles
kilometers = float(input("Enter amount of kilometers: "))
conversion = 0.621371
miles = kilometers * conversion
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

