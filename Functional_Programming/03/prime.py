def divisors(n, low, high):
    '''Returns True if n has a divisor in the range from low to high.
    Otherwise returns False'''
    if low > high:
        return False
    elif n % low == 0:
        return True
    else:
        return divisors(n, low+1, high)
        
        
def isPrime(n):
    '''For any n greater than or equal to 2,
    returns True if n is prime else returns False'''
    return not divisors(n, 2, n-1)
    
    
def listPrimes(n, limit):
    '''Returns a list of prime numbers between n and limit.'''
    
    if int(n) < 2:
        n = 2
    
    if n >= limit:
        return []
    elif isPrime(n):
        return [n] + listPrimes(n+1, limit)
    else:
        return listPrimes(n+1, limit)
        
        
def sift(toRemove, numList):
    '''Takes a number (toRemove) and a list of numbers (numList).
    Returns the list of those numbers in numList that are not multiples of toRemove.'''
    return [num for num in numList if num % toRemove != 0]
    
    
def primeSieve(numberList):
    '''Returns the list of all primes in numberList using a prime sieve algorithm.'''
    
    import sys
    sys.setrecursionlimit(20000) # Allows 20,000 levels of recursion
    
    if not numberList:
        return []
    else:
        prime = numberList[0]
        return [prime] + primeSieve(sift(prime, numberList[1:]))
        

if __name__ == '__main__':

    pass
