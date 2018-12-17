import math
import random
import util

def PrimeGenerator(n):
    step = math.floor(math.log2(n) / 2) # 要檢查 n bits 的數是否為質數，要做 Miller Rabin Test log2(n) / 2 次
    while True:
        # 產生 n bits 質數的方法:
        # step1: 第 n 個 bit 跟第 1 個 bit 是 1
        # step2: 其他 bit random 產生
        # step3: Miller Rabin Test 檢查是否為質數
        x = random.getrandbits(n - 2) << 1
        x += 1 + (1 << (n - 2))
        if MillerRabinTest(x, step):
            return x

def MillerRabinTest(p, k=5):
    # 偶數只有 2 是質數
    if p == 2:
        return True
    if not(p & 1):
        return False
    
    u = p - 1
    t = 0

    while u & 1 == 0:
        u >>= 1
        t += 1

    def test(a):
        x = util.SQandMU(a, u, p)
        if x == 1 or x == p - 1:
            return False
        for i in range(t - 1):
            x = util.SQandMU(a, (1 << i) * u, p)
            if x == p - 1:
                return False
        return True
    while k:
        a = random.randrange(2, p - 2)
        if test(a):
            return False
        k -= 1
        
    return True