'''
Harvey Mudd College - CS for All
Problem Name: Making Change
Topic: Finding the optimal way to make change using the use-it-or-lose-it recusion paradigm
Lectures: Module 1, Lecture 2
URL: https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/CS5BlackMasterHWPage
'''

def change(amount, coins):
    '''
    Given an amount of money and a list of coin types, returns the
    least number of coins that makes up the amount of money.
    '''
    if amount <= 0 or not coins:
        return 0
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        loseIt = 1 + change(amount, coins[1:])
        useIt = coins[0] + change(amount - coins[0], coins[1:])
        return max(loseIt, useIt)


if __name__ == '__main__':
    amount = 48
    coins = [1, 5, 10, 25]
    print(change(amount, coins))

"""
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

# Change the code below to try it out
print distance('spam', 'poems')
"""