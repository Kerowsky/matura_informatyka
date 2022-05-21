from math import *
def isPrime(n):
    if n < 2:
        return False
    if n==2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


for i in range(2, 26):
    print(i, isPrime(i))