
def rotate(n, b):
    return ((n << b) | (n >> (32-b))) & 0xffffffff

def sha1(text):
    msg = bytearray(text.encode())
    length = len(msg) * 8
    msg.append(0x80)

    while len(msg) % 64 != 56:
        msg.append(0)

    msg += length.to_bytes(8, 'big')
    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE,
         0x10325476, 0xC3D2E1F0]

    for pos in range(0, len(msg), 64):
        block = msg[pos:pos+64]
        w = [int.from_bytes(block[i:i+4], 'big')
             for i in range(0, 64, 4)]

        for i in range(16, 80):
            w.append(rotate(w[i-3] ^ w[i-8] ^
                            w[i-14] ^ w[i-16], 1))

        a, b, c, d, e = h

        for i in range(80):
            if i < 20:
                f, k = (b & c) | (~b & d), 0x5A827999
            elif i < 40:
                f, k = b ^ c ^ d, 0x6ED9EBA1
            elif i < 60:
                f, k = (b & c) | (b & d) | (c & d), 0x8F1BBCDC
            else:
                f, k = b ^ c ^ d, 0xCA62C1D6

            t = (rotate(a, 5) + f + e + k + w[i]) & 0xffffffff
            a, b, c, d, e = t, a, rotate(b, 30), c, d

        h = [(x+y) & 0xffffffff for x, y in zip(h, [a,b,c,d,e])]

    return ''.join(f'{x:08x}' for x in h)


# Main program
text = input("Enter original text: ")
original_hash = sha1(text)

modified_text = text + "!"
modified_hash = sha1(modified_text)

print("\nOriginal Text:", text)
print("SHA-1 Digest:", original_hash)
print("\nModified Text:", modified_text)
print("SHA-1 Digest:", modified_hash)

if original_hash == modified_hash:
    print("\nBoth digests are same.")
else:
    print("\nDigests are different.")
    print("Message modification detected!")
