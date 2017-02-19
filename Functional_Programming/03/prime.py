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
    

if __name__ == '__main__':

    import sys
    
    try:
        low = int(input('Input lower value (integer): '))
    except:
        sys.exit(1)
        
    try:
        high = int(input('Input upper value (integer): '))
    except:
        sys.exit(2)
    
    for num in range(low, high):
        if isPrime(num):
            print(num)
