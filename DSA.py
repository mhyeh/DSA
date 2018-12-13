import hashlib
import random
import prime
import util

def KeyGenerator(bit = 1024):
    p = prime.PrimeGenerator(bit)
    q = prime.PrimeGenerator(160)
    while((p - 1) % q == 0):
        q = prime.PrimeGenerator(160)
    alpha = util.ModInv(q, p)
    d     = random.randrange(1, p)
    beta  = util.SQandMU(alpha, d, p)
    return (p, q, alpha, beta), d

def Sign(m, p, q):
    pass

def Verify(r, s, p, q):
    pass