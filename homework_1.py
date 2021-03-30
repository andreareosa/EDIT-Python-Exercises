# -*- coding: utf-8 -*-
"""
01. DATA SCIENCE FUNDAMENTAL
FUNCTIONS HOMEWORK - ANDRÉ AREOSA
"""
# EXERCISE 1

def biggest():
    
    """This function asks the user for his inputs to create a list
       and then returns the biggest number of that list"""
 
    list_range = ''
    list_created = []
    
    while not (type(list_range) == int):
        try:
            list_range = int(input('Please enter the total number of elements for your list:  '))
            
        except ValueError:
            print('Please provide a number!')
            
    for num in range(1, list_range + 1):
        while True:
            list_element = input('Please enter the value of the %d element: ' % num)
            
            try:
                list_element = int(list_element)
                list_created.append(list_element)
                break
            
            except ValueError:
                print('Please provide a number!')
    
    print('List created:',list_created)
    print(f'{max(list_created)} is the biggest number in the list!')
    return max(list_created)


# EXERCISE 2

def smallest():
    
    """This function asks the user for his inputs to create a list
    and returns the same list without the smallest number(s)"""
    
    list_range = ''
    list_created = []
    
    while not (type(list_range) == int):
        try:
            list_range = int(input('Please enter the total number of elements for your list:  '))
            
        except:
            print('Please provide a number!')
            
    for num in range(1, list_range + 1):
        while True:
            list_element = input('Please enter the value of the %d element: ' % num)
            
            try:
                list_element = int(list_element)
                list_created.append(list_element)
                break
            
            except ValueError:
                print('Please provide a number!')
                
    smallest = min(list_created)
    result = []
    
    for num in list_created:
        if num != smallest:
            result.append(num)
    
    print('List created:',list_created)
    print(f'{smallest} is the smallest number and has been removed from the list!')
    return result


biggest()
smallest()
