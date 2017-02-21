from math import factorial


def inverse(n):
    '''Returns the inverse of the number n given'''
    return 1 / n
    
    
def e(n):
    '''Approximates the mathematical value e using
    a Taylor expansion, which can be expressed as
    the sum 1 + 1/1! + 1/2! + 1/3! + ...'''
    return 1 + sum([1/factorial(i) for i in range(1, n+1)])
    

if __name__ == '__main__':

    for n in range(1, 11):
        print('e({}) = {:.8f}'.format(n, e(n)))