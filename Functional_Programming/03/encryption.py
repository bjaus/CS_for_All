import random
from prime import primeSieve


def inverse(e, m):
    '''Returns the inverse of e mod m'''
    return list(filter(lambda d: e * d % m == 1, list(range(1, m))))[0]


def makeEncoderDecoder():
    '''Returns two functions: An RSA encryption function
    and an RSA decryption function.'''
    
    # Choose 2 primes:
    
    p, q = random.sample(primeSieve(list(range(2, 10))), 2)
    n = p * q # compute n
    m = (p - 1) * (q - 1) # compute m
    print('Maximum number that can be encrypted is', n - 1)
    
    # Choose a random prime for e
    
    e = random.choice(primeSieve(list(range(2, m))))
    if m % e == 0: # If e divides m, it won't work!
        print('Please try again')
        return
    else:
        d = inverse(e, m) # compute d
        encoder = lambda x: (x ** e) % n # encryption function
        decoder = lambda y: (y ** d) % n # decryption function
        return [encoder, decoder]


if __name__ == '__main__':
    # print(primeSieve(list(range(1001))))
    print(makeEncoderDecoder())