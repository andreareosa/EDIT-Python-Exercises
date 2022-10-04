# Python Exercises
This repository is about breaking the ice with python. It contains several exercises solved and some of the exercises were collected from my Data Science and Business Analytics course at EDIT.
The exercises template always include the questions and the solutions.

## Python - Level 1 Exercises

- To access the exercises questions: [Click Here!](https://github.com/andreareosa/EDIT-Python-Exercises/blob/main/Data%20Mining%20Exercises%20L1.pdf)
- For my solutions: [Click Here!](https://github.com/andreareosa/EDIT-Python-Exercises/blob/main/Python%20-%20Level%201%20Exercises.ipynb)

## Python - Functions

Create a .py file with two functions:
- One that receives a list with numbers and returns the biggest.
- Other that receives a list of numbers and returns the same list without the smallest.

```python
def biggest():

#This function asks the user for his inputs to create a list and then returns the biggest number of that list
  
    i = ''

    while not(type(i) == int):
        try:
            i = int(input('Please provide the total number of elements for your list: '))
        
        except:
            print('Please provide a valid number!')
             

    received_list = []  

    
    for x in range(i):
        while True:
            try:           
                x = int(input('Please enter the value of the %d element: ' % x))
                received_list.append(x)
                break
            
            except:
                print('Please provide a valid element!')
    
    
    print('List created:',received_list)
    print(f'Biggest number in the list: {max(received_list)}')
    return max(received_list)


def smallest():

#This function asks the user for his inputs to create a list and then returns the same list without the smallest number of that list
  
    i = ''

    while not(type(i) == int):
        try:
            i = int(input('Please provide the total number of elements for your list: '))
        
        except:
            print('Please provide a valid number!')
             

    received_list = []  

    
    for x in range(i):
        while True:
            try:           
                x = int(input('Please enter the value of the %d element: ' % x))
                received_list.append(x)
                break
        
            except:
                print('Please provide a valid element!')
       
    print('List created:',received_list)
    print(f'Smallest number that has been removed from the list: {min(received_list)}')
    
    received_list.remove(min(received_list)) 
    return received_list


biggest()
smallest()
```
