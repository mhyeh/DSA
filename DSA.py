import random
import time
import prime
import util

def KeyGenerator(bit = 1024):
    flag = False
    while not flag:
        c = 0
        q = prime.PrimeGenerator(160)
        while 1:
            k = random.getrandbits(bit - 160)
            p = k * q + 1
            if (p.bit_length() == bit and prime.MillerRabinTest(p)):
                flag = True
                break
            c += 1
            if (c >= 100):
                break
            
    h = 2
    while util.SQandMU(h, (p - 1) // q, p) == 1:
        h  = random.randrange(2, p - 1)
    g      = util.SQandMU(h, (p - 1) // q, p)
    priKey = random.randrange(1, q)
    pubKey = util.SQandMU(g, priKey, p)
    return (p, q, g), pubKey, priKey

def Sign(m, p, q, g, priKey):
    r, s = 0, 0
    while 1:
        k = random.randrange(1, q)
        r = util.SQandMU(g, k, p) % q
        if (r == 0):
            continue
        dk = util.ModInv(k, q)
        s = (dk * (util.H(m) + priKey * r)) % q
        if (s != 0):
            break
    return r, s

def Verify(m, p, q, g, pubKey, r, s):
    assert r >= 0 and r < q and s >= 0 and s < q
    w  = util.ModInv(s, q)
    u1 = (util.H(m) * w) % q
    u2 = (r * w) % q
    v  = ((util.SQandMU(g, u1, p) * util.SQandMU(pubKey, u2, p)) % p) % q
    return v % q == r % q