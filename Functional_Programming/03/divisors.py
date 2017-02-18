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
    
print(isPrime(13))
