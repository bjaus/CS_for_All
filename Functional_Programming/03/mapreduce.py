def add(x, y):
    '''Returns the sum of two arguments.'''
    return x + y
    
    
def trip(x):
    '''Takes a number x as an argument.'''
    return x * 3
    
    
def mapReduce(mapFunction, reduceFunction, myList):
    '''Applies mapFunction to myList to construct a new list
    and then applies reduceFunction to the new list
    and returns that value.'''
    return reduce(reduceFunction, map(mapFunction, myList))
    
    
    
if __name__ == '__main__':
    