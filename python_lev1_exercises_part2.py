# -*- coding: utf-8 -*-
"""
EDIT PYTHON LEVEL 1 EXERCISES - Part II
@author: andre.areosa
"""

"""
# EXERCISE 6:
 Create a program that:
     a. reads a file(txt file)containing more than 10 rows;
     b. creates a new file which excludes the 10th row of the original one.
"""
def file_reader(file):
    
    myfile = open(file,'r')
    content = myfile.read()
    rows = len(content.split("\n"))
    
    if rows <= 10:
        print('This file has less than 10 rows. No actions will be taken')
        
    else:
        print('A new file will be created without the 10th row of the origianl one')
        
        newfile = open('newfile.txt','w+')
        with open(file) as f:
            for index,line in enumerate(f):
                if index != 9:                
                    newfile.write(line)   
                    
"""
# EXERCISE 7:
  Given an integer number, use a loop to find its factorial.
"""
def factorial():
    
    x = ''
    
    while not (type(x) == int):
        try:
            x = int(input('Please provide an integer number: '))
        
        except ValueError:
            print('Please provide an integer number!')
    
    factorial = 1

    for n in range(1,x+1):
        factorial = factorial * n 
    
    return f'The factorial of {x} is {factorial}!'

"""
# EXERCISE 8:
  Using numpy library, create an array with values from 100 to 1000 with step=50, 
  having 6 rows and 3 columns.
"""
import numpy as np 

x = np.arange(100,1000,50).reshape(6,3)

"""
# EXERCISE 9:
  Sum arrays [[1, 2, 3], [10 , 10, 10]] and [[4, 2, 3], [1 ,1, 10]] and, then, create a new 
  array containing the square of each element.
"""
x = np.array([[1, 2, 3], [10 , 10, 10]])
y = np.array([[4, 2, 3], [1 ,1, 10]])

squared_elements = []

for i in np.nditer(x+y):
    i = i**2
    squared_elements.append(i)
    
np_squared_elements = np.array(squared_elements)

print(np_squared_elements)

"""
# EXERCISE 10:
  Consider array [[1,2,3],[4,5,6],[7,8,9]], delete its second column and insert 
  [[99,99,99]] on its place."""

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
x = np.delete(x,1,1)

new_col = np.array([[99,99,99]])
y = np.insert(x,1,new_col,axis=1)
print(y)

"""
# EXERCISE 11:
  Check if a string contains a ‘x’ followed by one or more ‘y’."""
import re

def string_check(somestring):
    
    pattern = '\Dxy+'
    result = re.search(pattern,somestring)
    
    if result is not None:
        print('Check!')
    else:
        print("No check! There is no 'x' followed by one or more 'y' in that string")

"""
# EXERCISE 12:
  Create a function that receives an IP address and returns a list with both: original IP, 
  original IP without its leading zeros (eg.: ['128.005.055.190', '128.5.55.190'])."""
def ip_receiver(ip_address):
    
    clean_ip = []

    for letter in ip_address:
        if letter != '0':
            clean_ip.append(letter)
        else:
            continue
        
    clean_ip = ''.join(clean_ip)
    print(f'The original IP is {ip_address}')
    print(f'The clean IP is {clean_ip}')

"""
# EXERCISE 13:
  Create a program that:
  a. Asks the user to write a sequence of words split by commas;
  b. Prints that list sorted alphabetically. (Eg.: a,c,b -> [a,b,c])"""
def words_split():
    
    x = input('Write a sequence of words split by commas:   ')
    
    words_list = [word for word in x if word != ',']
    words_list.sort()
    print(words_list)

