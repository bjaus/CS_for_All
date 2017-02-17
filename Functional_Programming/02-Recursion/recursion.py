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
        return subset(capacity, items[1:])
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
    elif first[0] == second[0]:
        return distance(first[1:], second[1:])
    else:
        substitution = 1 + distance(first[1:], second[1:])
        deletion = 1 + distance(first[1:], second)
        insertion = 1 + distance(first, second[1:])
        return min(substitution, deletion, insertion)
        
        
if __name__ == '__main__':

    from time import sleep

    me = 'Brandon'
    results = []
    
    with open('first_names.txt', 'r') as fin:
        for name in fin:
            name = name.strip()
            results.append((distance(me, name), name))
            
    results.sort()
    with open('first_name_distance.csv', 'w') as fout:
        for dist, name in results:
            fout.write('{},{}\n'.format(name, dist))
