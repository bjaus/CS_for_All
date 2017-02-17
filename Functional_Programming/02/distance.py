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

    import os

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'name_distances'))

    me = input('\nCheck what name? ').strip()
    results = []
    
    with open('first_names.txt', 'r') as fin:
        for name in fin:
            name = name.strip()
            if not name == '':
                if ' ' in name:
                    name = name.split(' ')[0]
                results.append((distance(me, name), name))
            
    results.sort()
    with open('{}_name_distance.csv'.format(me), 'w') as fout:
        fout.write('Name,Distance\n')
        for dist, name in results:
            fout.write('{},{}\n'.format(name, dist))