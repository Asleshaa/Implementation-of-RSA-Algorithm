import random
print ('Implementation of RSA algorithm')
def prime_number_verification(number):
    for m in range(3, int(number**0.5)+2, 2):
        if number % m == 0:
            raise ValueError('not prime')
    return True   
    if number %  2 == 0 or number < 2:
        raise ValueError ('not prime')
    if number == 2:
        return True
def greateest_common_denominator(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def generating_Key_values(P, Q):
    if not (prime_number_verification(P) and prime_number_verification(Q)):
        return ValueError ('The numbers chosen should be prime')
    if P == Q:
        return ValueError ('The values chosen  p , q shouldnot be equal')
    N = P * Q
    print ('value of N = P * Q')
    print (N)
    bigN = (P-1) * (Q-1)
    print ('value of bigN=(P-1) * (Q-1)')
    print (bigN)
    e = random.randrange(1, bigN)
    gcd = greateest_common_denominator(e, bigN)
    while gcd > 1:
        gcd = greateest_common_denominator(e, bigN)
        e = random.randrange(1, bigN)
    d = mod_inverse(e, bigN)
    print ('value generated for e is:')
    print (e)
    print ('value generated for d is:')
    print (d)
    return ((e, N), (d, N))
def mod_inverse(e, bigN):
    a1 = 0
    a2 = 1
    b1 = 1
    d = 0
    s_bigN = bigN
    while e > 0:
        s1 = s_bigN//e
        s2 = s_bigN - s1 * e
        s_bigN = e
        e = s2
        a = a2- s1 * a1
        b = d - s1 * b1
        a2 = a1
        a1 = a
        d = b1
        b1 = b
    if s_bigN == 1:
        return d + bigN
def encrypt(PU, plaintext):
    key, N = PU
    encryption_text = [pow(ord(char), key, N) for char in plaintext]
    return encryption_text
def decrypt(PR, ciphertext):
    key, N = PR
    decryption_text = [chr(pow(char, key, N)) for char in ciphertext]
    return ''.join(decryption_text)
if __name__ == '__main__':
    P = int(input("P =  "))
    Q = int(input("Q =  "))
    while not(Q > P):
        P = int(input("P = "))
        Q = int(input("chose Q greater than P "))
    print(not(Q > P))	
    public, private =  generating_Key_values(P, Q)
    print ("PU = (e,N) ", public ," PR = (d,N) ", private)
    plain_text = input("Enter plain text: ")
    encrypted_text = encrypt(public, plain_text)
    print ("cipher text = ")
    print (''.join(map(lambda x: str(x), encrypted_text)))
    print ("Decrypted text =  ")
    print (decrypt(private, encrypted_text))
