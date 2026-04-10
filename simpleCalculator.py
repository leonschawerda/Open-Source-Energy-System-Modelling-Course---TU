# author: Leon Schawerda

""" adds up all numbers of a list """
def add(values): 
    result = 0
    for val in values:
        result += val
    return result

"""substract a list of values from the first value"""
def subtract (start, values):
    result = start # set start value
    for val in values:
        result -= val
    return result

""" multiplies all numbers of a list"""
def multiply (values):
    result = values[0] # initialise with first value
    for i in range(1,len(values)):
        result *= values[i]
    return result

"""divide the first number by the second"""
def divide (x,y) :
     return x / y
