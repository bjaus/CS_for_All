def reverse(string):
    '''Takes a string as an argument
    and return its reversal.'''

    if string == '':
        return ''
    else:
        first_letter = string[0]
        return reverse(string[1:]) + first_letter