def reverse(string):
    '''Takes a string as an argument
    and return its reversal.'''

    if string == '':
        return ''
    else:
        first_letter = string[0]
        return reverse(string[1:]) + first_letter
        
        
def subset(capacity, items):
    '''Given a suitcase capacity and a list of items
        consiting of positive numbers, returns a numbers
        indicating the largest sum that can be made from a 
        subset of the items without exceeding the capacity.'''
        
    if capacity <= 0 or items == []:
        return 0
    elif items[0] > capacity:
        return subset(capacity, [items[1:])
    else:
        lose_it = subset(capacity, items[1:])
        use_it = items[0] + subset(capacity - items[0], items[1:])
        return max(lose_it, use_it)
        
        
def distance(first, second):
    '''Returns the edit distance between first and second.'''
    
    if first == '':
        return len(second)
    elif second == '':
        return len(first)