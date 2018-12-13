import DSA

if __name__ == '__main__':
    (p, q, a, b), d = DSA.KeyGenerator()
    print("%X" % p)
    print("%X" % q)
    print("%X" % a)
    print("%X" % b)
    print("%X" % d)