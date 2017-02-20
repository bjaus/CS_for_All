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
        
    
def primeSieve(numberList):
    if not numberList:
        return []
    else:
        prime = numberList[0]
        return [prime] + primeSieve(sift(prime, numberList[1:]))
        

if __name__ == '__main__':

    print(listPrimes(100, 100))
