import random
import prime
import util

def KeyGenerator(bit = 1024):
    # b, n = divmod(bit - 1, 160)
    # p, q = 0, 0
    # while (1):
    #     while (1):
    #         g = 160 + random.randrange(1, 100)
    #         seed = random.getrandbits(g)
    #         U = util.H(seed) ^ util.H((seed + 1) % (1 << g))
    #         q = U | (1 << 159) | 1
    #         if prime.MillerRabinTest(q):
    #             break
    #     flag = True
    #     while (1):
    #         counter, offset = 0, 2
    #         w = 0
    #         for k in range(0, n):
    #             v  = util.H((seed + offset + k) % (1 << g))
    #             w += v * (1 << (k * 160))
    #         v  = util.H((seed + offset + n) % (1 << g))
    #         w += (v % (1 << b)) * (1 << (n * 160))
    #         x  = w + 1 << (bit - 1)
    #         c  = x % (2 * q)
    #         p  = x - (c - 1)
    #         if (p >= 1 << (bit - 1) and prime.MillerRabinTest(p)):
    #             break
    #         else:
    #             counter += 1
    #             offset  += n + 1
    #             if (counter >= 4096):
    #                 flag = False
    #                 break
    #     if flag:
    #         break

    q = prime.PrimeGenerator(160)
    while 1:
        k = random.getrandbits(bit - 160)
        p = k * q + 1
        if (p.bit_length() == bit and prime.MillerRabinTest(p)):
            break


    # p = prime.PrimeGenerator(bit)
    # q = prime.PrimeGenerator(160)
    # while((p - 1) % q != 0):
    #     q = prime.PrimeGenerator(160)
    g = util.LargeOrd(q, p)
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