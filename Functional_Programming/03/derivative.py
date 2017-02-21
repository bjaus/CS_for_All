def derivative(f, h):
    '''Returns a new function that is the approximation of
    the derivative of f with respect to h.'''
    
    return lambda x: (f(x+h) - f(x)) / h