import sys
from math import sqrt

def is_prime(n):
    '''Check if n is prime'''
    for x in xrange(2,int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def prime_fac(n):
    '''Print prime factorization of n'''
    if is_prime(n):
        print n
    elif n % 2 == 0:
        print 2
        if is_prime(n/2):
            print n/2
        else:
            prime_fac(n/2)
    else:
        for x in xrange(3,int(sqrt(n))+1,2):
            if is_prime(x) and n % x == 0:
                print x
                prime_fac(n/x)

arg = int(sys.argv[1])

prime_fac(arg)
