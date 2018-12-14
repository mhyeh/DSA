import hashlib

def H(m):
    hashF = hashlib.sha1()
    hashF.update(str(m).encode('utf-8'))
    hashMessage = hashF.hexdigest()
    return int(hashMessage, 16)

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

def EEA(l, r):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while r:
        l, (q, r) = r, divmod(l, r)
        x0, x1 = x1 - q * x0, x0
        y0, y1 = y1 - q * y0, y0
    return l, x1, y1

def ModInv(a, b):
    g, x, y = EEA(a, b)
    assert g == a * x + b * y
    return x % b

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Ord(a, n):
    assert GCD(a, n) == 1
    result, k = 1, 1
    while k < n:
        # result = (result * a) % n
        # if result == 1:
        #     return k
        if SQandMU(a, k, n) == 1:
            return k
        k += 1

def largest_factor_relatively_prime(a, b):
    while 1:
        d = GCD(a, b)
        if d <= 1:
            break
        b = d
        while 1:
            q, r = divmod(a, d)
            if r > 0:
                break
        a = q
    return a
    
def LargeOrd(a, n):
    return Ord(a, largest_factor_relatively_prime(n, a))