import math
import random
import util

def PrimeGenerator(n):
    step = math.floor(math.log2(n) / 2)
    while True:
        x = random.getrandbits(n - 2) << 1
        x += 1 + (1 << (n - 2))
        if MillerRabinTest(x, step):
            return x

def MillerRabinTest(p, k):
    if p == 2:
        return True
    if not(p & 1):
        return False
    
    u = p - 1
    t = 0

    while u & 1 == 0:
        u >>= 1
        t += 1

    def test(a):
        x = util.SQandMU(a, u, p)
        if x == 1 or x == p - 1:
            return False
        for i in range(t - 1):
            x = util.SQandMU(a, 2 ** i * u, p)
            if x == p - 1:
                return False
        return True
    while k:
        a = random.randrange(2, p - 2)
        if test(a):
            return False
        k -= 1
        
    return True