def derivative(f, h):
    '''Returns a new function that is the approximation of
    the derivative of f with respect to h.'''
    
    return lambda x: (f(x+h) - f(x)) / h
    
    
def kthDeriviative(f, h, k):
    '''Returns a new function that is the approximation of
    the kth derivative of f with respect to h.'''
    if k == 1:
        return derivative(f, h)
    else:
        return derivative(kthDeriviative(f, h, k-1), h)
        
        
def square(x):
    return x ** 2
    
    
def quartic(x):
    return x ** 4
    
    
    
if __name__ == '__main__':
    g = kthDeriviative(quartic, 0.0001, 3)
    print(g(11))