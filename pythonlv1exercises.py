# -*- coding: utf-8 -*-
"""
EDIT PYTHON LEVEL 1 EXERCISES

"""

# EXERCISE 1
# Create a program that:a.asks a user the radius of a cylinder;
# b.asks a user the height ofa cylinder;
# c.Prints the volume of that cylinder;
# d.Prints the surface area of that cylinder;

import math

radius = int(input('Choose a radius for a cylinder:   '))
height = int(input('Choose a height for a cylinder:  '))

print('Volume of the cylinder: ', height * math.pi * radius ** 2)
print('Surface area of the cylinder: ', 2 * math.pi * radius * (radius + height))

#EXERCISE 2:
# a.Receives a string
# b.print only the characters present at an even index number.(Eg.: ‘My string’ -> ‘M’, ‘’, ‘t’,’i’,’g’
#EXERCISE 2:
def even_string(some_string):
    
    for index,letter in enumerate(some_string):
        if index % 2 == 0:
            print(letter)
        else:
            continue
        
#EXERCISE 3:
# Create a function that:
# a.Receives an integer number
# b.Returns  true  if  thegiven  number  is  palindromic  (eg.:  7,  77,  121,3443, 5341435)

def palindromic():
    
    x = int(input('Enter a number : '))
    
    x_reversed = int(str(x)[::-1])
    
    return x == x_reversed       

#EXERCISE 4:
#Using print(), format a decimal number to be displayed:
# a.With 2 decimal places (eg.: 123.456 ->123.46);

from random import randint

random_number = randint(10,100) / 5.62
print('My random number formated with 2 decimal places is {r:1.2f}'.format(r = random_number))

#EXERCISE 5:
# Create a list of floatnumbers:
# a.ask the user for thelist size;
# b.ask the user for each of the elements, individually;
# c.return the list.

def float_list():
    
    x = ''
    float_list = []
    
    
    while not (type(x) == int):
        
        try:
            x = int(input('Please provide a list size of your choise:  '))
        except:
            print('Please provide an integer!')
        else:
            print('Thank you!')

    for element in range(x+1):
        float_list.append(float(input(f'For element {element} provide a floating point to the list:  ')))
    
    return float_list
        
float_list()







