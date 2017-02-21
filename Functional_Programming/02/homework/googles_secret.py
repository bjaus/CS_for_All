# Hyperlink: https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/GooglesSecret!

import math
from functools import reduce

def e(n):
    '''Approximates the mathematical value e using
    a Taylor expansion, which can be expressed as
    the sum 1 + 1/1! + 1/2! + 1/3! + ...'''
    return 1 + sum([1/math.factorial(i) for i in range(1, n+1)])
    
    
def error(n):
    '''Returns the absolute value of the difference between
    the "actual" value of e and the approximation in the e(n)
    function assuming that n terms (beyond the leading 1) as used.'''
    return abs(e(n) - math.e)
 

def factorial(n):
    '''Returns the factorial of a given number n.'''
    return reduce(lambda x, y: x * y, list(range(1, n+1)))
    
    
def mean(L):
    '''Takes a list as input and returns the mean (average)
    value in that list using the functools.reduce function.'''
    return reduce(lambda x, y: x + y, L) / len(L)
    
    
def divides(n):
    def div(k):
        return n % k == 0
    return div
    

def prime(n):
    '''Takes a positive intger n as input and returns True or False
    depending on whether n is prime or composite number.'''
    return None
    

if __name__ == '__main__':

    # for n in range(1, 11):
        # print('\ne({}) = {}\nerror: {}'.format(n, e(n), error(n)))
        # print(factorial(n))

    # print(mean(list(range(1, 11))))
    x = divides(200)
    print(x(2))