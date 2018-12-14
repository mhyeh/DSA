import DSA

if __name__ == '__main__':
    (p, q, g), pubKey, priKey = DSA.KeyGenerator()
    print("p      %X" % p)
    print("q      %X" % q)
    print("g      %X" % g)
    print("pubKey %X" % pubKey)
    print("priKey %X" % priKey)
    print()

    m = "123456789"
    r, s = DSA.Sign(m, p, q, g, priKey)
    print("r      %X" % r)
    print("s      %X" % s)
    print()

    print("v", DSA.Verify(m, p, q, g, pubKey, r, s))