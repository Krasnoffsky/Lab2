import lab2
import random


if __name__ == '__main__':

    A = lab2.User()
    B = lab2.User()

    print("---Shamir---")

    Shamir = lab2.ShamirCypher()

    m = random.randint(1, Shamir.p - 1)

    A.c, A.d = Shamir.keyGenerator()
    B.c, B.d = Shamir.keyGenerator()

    print("Message before encoding: ", m)

    x1 = Shamir.encode(m, A.c)
    x2 = Shamir.encode(x1, B.c)
    x3 = Shamir.encode(x2, A.d)
    x4 = Shamir.encode(x3, B.d)
    print(x1, " ", x2, " ", x3)

    print("Message after decoding: ", x4)

    print("---Elgamal---")

    Elgamal = lab2.ElgamalCypher()

    B.c, B.d = Elgamal.keyGenerator()

    k = random.randint(1, Elgamal.p - 2)
    m = random.randint(1, Elgamal.p - 1)

    print("Message before encoding: ", m)

    r, e = Elgamal.encode(k, B.d, m)
    m = Elgamal.decode(e, r, B.c)
    print(e)

    print("Message after decoding: ", m)

    print("---Vernam---")

    Vernam = lab2.VernamCypher()

    m = 123456789

    print("Message before encoding: ", m)

    e = Vernam.encode(m)
    m = Vernam.decode(e)
    print(e)

    print("Message after decoding: ", m)

    print("---RSA---")

    RSA = lab2.RSACypher()

    B.c, B.d, B.n = RSA.keyGenerator()

    m = random.randint(1, B.n)
    print("Message before encoding: ", m)

    e = RSA.encode(m, B.d, B.n)
    m = RSA.decode(e, B.c, B.n)
    print(e)

    print("Message after decoding: ", m)
