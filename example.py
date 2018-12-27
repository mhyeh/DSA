import DSA

if __name__ == '__main__':
    while True:
        cmdGenerate = "0) Generate keys\n"
        cmdSign = "1) Signature generation\n"
        cmdVerify = "2) Signature verification\n"
        cmdExit = "3) Exit\n"
        opt = input("please input your command\n" + cmdGenerate + cmdSign + cmdVerify + cmdExit + "> ")
        if opt == "0":
            (p, q, g), pubKey, priKey = DSA.KeyGenerator()
            print("\n============== result ==============\n")
            print("P      %X" % p)
            print("Q      %X" % q)
            print("G      %X" % g)
            print("pubKey %X" % pubKey)
            print("priKey %X\n" % priKey)
        elif opt == "1":
            m = input("Please enter your message: ")
            p = int(input("Please enter P(base 16): "), 16)
            q = int(input("Please enter Q(base 16): "), 16)
            g = int(input("Please enter G(base 16): "), 16)
            priKey = int(input("Please enter your key(base 16): "), 16)
            r, s = DSA.Sign(m, p, q, g, priKey)
            print("\n============== result ==============\n")
            print("R %X" % r)
            print("S %X\n" % s)

        elif opt == "2":
            m = input("Please enter your message: ")
            p = int(input("Please enter P(base 16): "), 16)
            q = int(input("Please enter Q(base 16): "), 16)
            g = int(input("Please enter G(base 16): "), 16)
            r = int(input("Please enter R(base 16): "), 16)
            s = int(input("Please enter S(base 16): "), 16)
            pubKey = int(input("Please enter your key(base 16): "), 16)
            print("\n============== result ==============\n")
            print("Result\n", DSA.Verify(m, p, q, g, pubKey, r, s))
        else:
            break