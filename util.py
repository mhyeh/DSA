import hashlib
import time

# sha1 --> hex string --> int
def H(m):
    hashF = hashlib.sha1()
    hashF.update(str(m).encode('utf-8'))
    hashMessage = hashF.hexdigest()
    return int(hashMessage, 16)

# Fast algorithm to calculate x ^ h % n
def SQandMU(x, h, n=0):
    b = bin(h).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r *= x
        if (n != 0):
            r %= n
    return r

# Extended Euclidean algorithm
# Find gcd, x, y, such that GCD(a, b) == gcd == x * a + y * b
def EEA(l, r):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while r:
        l, (q, r) = r, divmod(l, r)
        x0, x1 = x1 - q * x0, x0
        y0, y1 = y1 - q * y0, y0
    return l, x1, y1

# Find modular multiplicative inverse of a which respect to the modulus m
def ModInv(a, b):
    g, x, y = EEA(a, b)
    assert g == a * x + b * y
    return x % b

# Find greatest common divisor of a and b
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a
