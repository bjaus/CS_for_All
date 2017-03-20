'''
Harvey Mudd College - CS for All
Problem Name: Recursion Muscles 
Topic: Introduction to recursion
Lectures: Module 1, Lecture 1
URL: https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/RecursionMuscles!
'''

def dot(L, K):
    '''
    dot(L, K) should output the dot product of the lists L and K. 
    Recall that the dot product of two vectors or lists is the sum of the products of the elements in the same position in the two vectors. You may assume that the two lists are of equal length. If they are of different lengths, it's up to you what result is returned. If these two lists are both empty, dot should output 0.0. Assume that the input lists contain only numeric values.
    '''
    if not (len(L) and len(K)):
        return 0
    else:
        prod = L[0] * K[0]
        return prod + dot(L[1:], K[1:])


def explode(S):
    '''
    explode(S) should take a string S as input and should return a list of the characters (each of which is a string of length 1) in that string. For example:
    '''
    s = []
    if len(S) == 0:
        return s
    else:
        s += S[0]
        return s + explode(S[1:])


def ind(e, L):
    '''
    ind(e, L) takes in an element e and a sequence L where by "sequence" we mean either a list or a string; fortunately indexing and slicing works the same for both lists and strings, so your ind function should be able to handle both types of input!. Then, ind should return the index at which e is first found in L. Counting begins at 0, as is usual with lists. If e is NOT an element of L, then ind(e, L) should return an integer that is at least the length of L. Remember, don't use the len function explicitly though! Your recursive implementation can do this by itself.
    '''
    if L[0] == e: 
        return 0
    else:
        try: 
            return 1 + ind(e, L[1:])
        except IndexError: 
            return 1


def removeAll(e, L):
    '''
    removeAll(e, L) takes in an element e and a list L. Then, removeAll should return another list that is identical to L except that all elements identical to e have been removed. Notice that e has to be a top-level element to be removed.
    '''
    r = []
    if not L:
        return []
    elif L[0] == e:
        pass
    else:
        r.append(L[0])
    return r + removeAll(e, L[1:])


def myFilter(f, L):
    '''
    In this example, the predicate even returns True if and only if its input is an even integer. When we invoke filter with predicate even and the list [0, 1, 2, 3, 4, 5, 6] we get back a list of the even numbers in that list. Of course, the beauty of filter is that you can use it with all different kinds of predicates and all different kinds of lists. It's a very general and powerful function! Your job is to write your own version of filter called myFilter. Remember, your implementation may use recursion, indexing and slicing, and concatenation but no built-in python functions
    '''
    r = []
    if not L:
        return r
    elif f(L[0]):
        r.append(L[0])
    return r + myFilter(f, L[1:])


def deepReverse(L):
    '''
    deepReverse(L) takes as input a list of elements where some of those elements may be lists themselves. deepReverse returns the reversal of the list where, additionally, any element that is a list is also deepReversed.
    '''
    i = 0
    res = []
    res = res + L
    if not isinstance(L, list):
        return []
    while i < len(L):
        if not isinstance(L[i], list):
            if i == 0:
                res[len(res)-1] = L[i]
            else:
                res[len(res)-i-1] = L[i]
        else:
            res[len(res)-i-1] = deepReverse(L[i])
        i += 1
    return res


def wordScore(S, scoreDict):
    '''
    wordScore(S, scoredict) should take as input a string S and a scoredict in the format described, which will have only lowercase letters, and should return as output the scrabble score of that string
    '''
    if not S:
        return 0
    else:
        return scoreDict[S[0]] + wordScore(S[1:], scoreDict)



if __name__ == '__main__':

    # Test dot(L, K)
    # print(dot([5, 3], [6, 4])) # --> 42

    # Test explode(S)
    # print(explode('spam')) # --> ['s', 'p', 'a', 'm']

    # Test ind(e, L)
    # print(ind(42, [55, 77, 42, 12, 42, 100])) # --> 2
    # print(ind(42, range(0, 100))) # --> 42
    # print(ind('hi', ['hello', 42, True])) # --> 3
    # print(ind('hi', ['well', 'hi', 'there'])) # --> 1
    # print(ind('i', 'team')) # --> 4
    # print(ind(' ', 'outer exploration')) # --> 5

    # Test removeAll(e, L)
    # print(removeAll(42, [55, 77, 42, 11, 42, 88])) # --> [55, 77, 11, 88]
    # print(removeAll(42, [55, [77, 42], [11, 42], 88])) # --> [55, [77, 42], [11, 42], 88]
    # print(removeAll([77, 42], [55, [77, 42], [11, 42], 88])) # --> [55, [11, 42], 88]

    # Test myFilter(f, L)
    # print(myFilter(lambda x: x % 2 == 0, range(0, 12))) # --> [0, 2, 4, 6, 8, 10]
    # print(myFilter(lambda x: x % 2 == 1, range(0, 12))) # --> [1, 3, 5, 7, 9, 11]

    # Test deepReverse
    print(deepReverse([1, [2, 3], 4])) # --> [4, [3, 2], 1]

    # Test wordScore(S, scoreDict)
    # SCRABBLE_SCORE = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,
    #                   "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
    #                   "k": 5, "l": 1, "m": 3, "n": 1, "o": 1,
    #                   "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
    #                   "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

    # print(wordScore('brandon', SCRABBLE_SCORE)) # --> 10
    # print(wordScore('kayla', SCRABBLE_SCORE)) # --> 12
    # print(wordScore('zachary', SCRABBLE_SCORE)) # --> 24
    # print(wordScore('jesus', SCRABBLE_SCORE)) # --> 12
