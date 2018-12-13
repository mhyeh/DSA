def SQandMU(x, h, n):
    b = bin(h).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r *= x
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
