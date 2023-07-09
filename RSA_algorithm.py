import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    # The number to be encrypted and decrypted
    # author: @Tanish Banthia
    msg = int(input("Enter a message msg: "))

    # Input prime numbers p and q
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))

    n = p * q
    z = (p - 1) * (q - 1)

    print("The value of z =", z)

    e = 2
    while e < z:
        # e is for public key exponent
        if gcd(e, z) == 1:
            break
        e += 1

    print("The value of e =", e)

    d = 0
    for i in range(10):
        x = 1 + (i * z)
        # d is for private key exponent
        if x % e == 0:
            d = x // e
            break

    print("The value of d =", d)

    c = (msg ** e) % n
    print("Encrypted message is:", c)

    # Decrypting the message
    msg_back = (c ** d) % n
    print("Decrypted message is:", msg_back)
