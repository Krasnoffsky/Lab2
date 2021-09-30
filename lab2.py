import random


class User:

    c = 0
    d = 0
    n = 0

    def __init__(self):
        self.c = 0
        self.d = 0
        self.n - 0


class ShamirCypher:

    p = 0

    def __init__(self):
        self.p = SimpleGenerator()

    def keyGenerator(self):
        c = random.randrange(1, 1000000000, 2)
        d = 0

        while GCD(c, self.p - 1) != 1:
            c = random.randrange(1, 100000000, 2)

        U = []
        U = EuclideAl(c, self.p - 1)
        d = U[1]

        if d < 0:
            d = self.p - 1 + d

        return (c, d)

    def encode(self, a, e):
        return FastAsFakPow(a, e, self.p)


class ElgamalCypher:

    p = 0
    g = 0

    def __init__(self):
        self.p = SimpleGenerator()
        self.g = int((self.p - 1) / 2)

    def keyGenerator(self):
        c = random.randint(1, self.p - 1)
        d = FastAsFakPow(self.g, c, self.p)

        return (c, d)

    def encode(self, k, d, m):
        r = FastAsFakPow(self.g, k, self.p)
        e = (m * FastAsFakPow(d, k, self.p)) % self. p

        return (r, e)

    def decode(self, e, r, c):
        m = (e * FastAsFakPow(r, self.p - 1 - c, self.p)) % self.p

        return m


class VernamCypher:

    k = 0

    def __init__(self):
        self.k = 0

    def encode(self, m):
        min = (2 ** (len(bin(m)) - 3))
        lim = (2 ** (len(bin(m)) - 2)) - 1

        self.k = random.randint(min, lim)

        e = m ^ self.k

        return e

    def decode(self, e):
        return e ^ self.k


class RSACypher:

    def keyGenerator(self):
        p = SimpleGenerator()
        q = SimpleGenerator()
        N = p * q
        fi = (p - 1) * (q - 1)
        d = random.randint(1, fi - 1)

        while(GCD(fi, d) != 1):
            d = random.randint(1, fi - 1)

        U = EuclideAl(d, fi)
        c = U[1]

        if (c < 0):
            c = c + fi

        return (c, d, N)

    def encode(self, m, d, N):
        return FastAsFakPow(m, d, N)

    def decode(self, e, c, N):
        return FastAsFakPow(e, c, N)


def FastAsFakPow(a, e, m):

    result = 1
    bin_e = DecToBin(e)
    last_num = a % m

    if (bin_e % 10 == 1):
        result = (result * last_num) % m

    bin_e = bin_e // 10

    while (bin_e != 0):

        last_num = (last_num * last_num) % m
        if (bin_e % 2 == 1):
            result = (result * last_num) % m

        bin_e = bin_e // 10

    return result


def DecToBin(dec):

    bin = 0
    last_bit = 0
    k = 1

    while (dec != 0):
        last_bit = dec & 1
        bin = bin + last_bit * k
        dec = dec >> 1
        k = k * 10

    return bin


def isPrime(p):
    if p <= 1:
        return False

    b = int(p ** 0.5)

    for i in range(2, b + 1):
        if p % i == 0:
            return False

    return True


def SimpleGenerator():

    lim = 1000000000
    res = random.randint(1, lim)

    while not (isPrime(res) and isPrime(int((res - 1) / 2))):
        res = random.randint(1, lim)

    return res


def GCD(a, b):

    r = 0
    while(b != 0):
        r = a % b
        a = b
        b = r

    return a


def EuclideAl(a, b):
    U = [a, 1, 0]
    V = [b, 0, 1]
    T = [0, 0, 0]
    q = 0

    while V[0] != 0:
        q = U[0] // V[0]
        T[0] = U[0] % V[0]
        T[1] = U[1] - q * V[1]
        T[2] = U[2] - q * V[2]
        U[0] = V[0]
        U[1] = V[1]
        U[2] = V[2]
        V[0] = T[0]
        V[1] = T[1]
        V[2] = T[2]

    return U
