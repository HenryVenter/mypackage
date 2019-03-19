def sum_array(array):
    '''Return sum of all items in array'''
    return sum(array)


#add memoization by importing lru_cache decorator from the functools module
from functools import lru_cache
#to use this form of memoization write the following
@lru_cache(maxsize = 1000)

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    # First check that input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    #Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def reverse(word):
    return(word[::-1])
    '''Return word in reverse'''
