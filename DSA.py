import random
import time
import prime
import util

def KeyGenerator(bit = 1024):
    # Generate 2 large prime p, q, (p - 1) % q == 0
    flag = False
    while not flag:
        c = 0
        q = prime.PrimeGenerator(160) # q is 160 bits

        # (p - 1) % q == 0 --> p = q * k + 1
        # p is 1024 bits (default) --> k is (1024 - 160) bits
        while 1:
            k = random.getrandbits(bit - 160)
            p = k * q + 1
            if (p.bit_length() == bit and prime.MillerRabinTest(p)):
                flag = True
                break
            c += 1

            # 可能因為 q 的關係導致很難找到 p ，所以如果一段時間找不到 p ，就換一個 q 試試看
            if (c >= 100):
                break
            
    # Generate g, such that multiplicative order modulo p of g is q
    h = 2
    while util.SQandMU(h, (p - 1) // q, p) == 1:
        h  = random.randrange(2, p - 1)
    g      = util.SQandMU(h, (p - 1) // q, p)

    priKey = random.randrange(1, q)     # Grnerate private key
    pubKey = util.SQandMU(g, priKey, p) # Generate public key = g ^ priKey % q
    return (p, q, g), pubKey, priKey

def Sign(m, p, q, g, priKey):
    # 簽章
    r, s = 0, 0
    while 1:
        k = random.randrange(1, q)
        r = util.SQandMU(g, k, p) % q
        if (r == 0):
            continue
            # 發生R=0的情況，試另一組k
        dk = util.ModInv(k, q)
        s = (dk * (util.H(m) + priKey * r)) % q
        if (s != 0):
            break
    return r, s

def Verify(m, p, q, g, pubKey, r, s):
    # 驗證簽章
    assert r >= 0 and r < q and s >= 0 and s < q
    w  = util.ModInv(s, q)
    u1 = (util.H(m) * w) % q
    u2 = (r * w) % q
    v  = ((util.SQandMU(g, u1, p) * util.SQandMU(pubKey, u2, p)) % p) % q
    return v % q == r % q