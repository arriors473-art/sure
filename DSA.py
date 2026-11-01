
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# STEP 1: Generate DSA Private and Public Keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

print("===== DIGITAL SIGNATURE USING DSA =====")

# STEP 2: Sender enters the message
message = input("\nEnter original message: ").encode()

print("\n--- SENDER ---")
print("Original Message:", message.decode())

# STEP 3: Generate Digital Signature using Private Key
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")
print("Signature:", signature.hex())

# STEP 4: Receiver verifies using Public Key
print("\n--- RECEIVER ---")

try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )

    print("Original Message Verification: SUCCESS")
    print("Authentication: Valid")
    print("Message Integrity: Verified")

except InvalidSignature:
    print("Original Message Verification: FAILED")

# STEP 5: Modify the message
modified_message = input(
    "\nEnter modified message: "
).encode()

print("\nModified Message:", modified_message.decode())

# STEP 6: Verify Modified Message
try:
    public_key.verify(
        signature,
        modified_message,
        hashes.SHA256()
    )

    print("Modified Message Verification: SUCCESS")

except InvalidSignature:
    print("Modified Message Verification: FAILED")
    print("Message modification detected!")

print("\n===== PROGRAM COMPLETED =====")






import hashlib
import secrets

# STEP 1: DSA PARAMETERS
p = 23
q = 11

g = 4

# STEP 2: PRIVATE AND PUBLIC KEY
x = 3                       # Private key
y = pow(g, x, p)            # Public key

# Modular inverse using Extended Euclidean Algorithm
def inverse(a, m):
    return pow(a, -1, m)

# SHA-256 HASH
def hash_message(message):
    digest = hashlib.sha256(message).digest()
    value = int.from_bytes(digest, 'big')

    # Take leftmost q.bit_length() bits
    shift = len(digest) * 8 - q.bit_length()
    return value >> shift

# STEP 3: DIGITAL SIGNATURE GENERATION
def sign(message):
    z = hash_message(message)

    while True:
        k = secrets.randbelow(q - 1) + 1

        r = pow(g, k, p) % q
        if r == 0:
            continue

        k_inv = inverse(k, q)
        s = (k_inv * (z + x * r)) % q

        if s != 0:
            return r, s

# STEP 4: SIGNATURE VERIFICATION
def verify(message, signature):
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    z = hash_message(message)

    w = inverse(s, q)
    u1 = (z * w) % q
    u2 = (r * w) % q

    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

    return v == r

# MAIN PROGRAM
print("===== DSA DIGITAL SIGNATURE =====")

message = input("Enter original message: ").encode()

print("\n--- SENDER ---")
print("Original Message:", message.decode())

signature = sign(message)

print("Digital Signature:", signature)
print("Signature Generated Successfully!")

# Verify original message
print("\n--- RECEIVER ---")

if verify(message, signature):
    print("Original Message Verification: SUCCESS")
    print("Authentication: Valid")
    print("Message Integrity: Verified")
else:
    print("Original Message Verification: FAILED")

# Modify message
modified = input("\nEnter modified message: ").encode()

print("\nModified Message:", modified.decode())

if verify(modified, signature):
    print("Modified Message Verification: SUCCESS")
else:
    print("Modified Message Verification: FAILED")
    print("Message Modification Detected!")

print("\n===== PROGRAM COMPLETED =====")




# from cryptography.hazmat.primitives.asymmetric import dsa
# from cryptography.hazmat.primitives import hashes
# from cryptography.exceptions import InvalidSignature

# # Generate private and public keys
# private_key = dsa.generate_private_key(key_size=2048)
# public_key = private_key.public_key()

# # Accept message
# message = input("Enter message: ").encode()

# # Sign using private key
# signature = private_key.sign(message, hashes.SHA256())

# print("\nDigital Signature Generated Successfully!")
# print("Signature:", signature.hex())

# # Verify using public key
# try:
#     public_key.verify(signature, message, hashes.SHA256())
#     print("\nSignature is VALID.")
# except InvalidSignature:
#     print("\nSignature is INVALID.")

# # Modify message
# modified_message = message + b" Modified"

# print("\nModified Message Verification:")

# try:
#     public_key.verify(signature, modified_message, hashes.SHA256())
#     print("Signature is VALID.")
# except InvalidSignature:
#     print("Signature is INVALID.")
#     print("Message has been modified!")

# DSA NUMERICAL EXAMPLE
# =====================

# This is a small illustrative example to understand DSA signature generation
# and verification. The numbers are deliberately small for easy calculation.
# Real DSA uses much larger parameters.

# 1. KEY GENERATION
# -----------------
# Choose:
#     p = 23
#     q = 11
#     g = 4

# Choose private key:
#     x = 3

# Calculate public key:
#     y = g^x mod p
#       = 4^3 mod 23
#       = 64 mod 23
#       = 18

# Therefore:
#     Private key x = 3
#     Public key y = 18
#     Public parameters: p = 23, q = 11, g = 4


# 2. SIGNATURE GENERATION
# ----------------------
# Message:
#     HELLO

# Calculate message hash:
#     H = SHA-256(HELLO)

# For this simplified numerical example, assume:
#     H(m) = 8

# Note: 8 is an assumed small hash value for demonstration. It is NOT the
# actual SHA-256 digest of HELLO.

# Choose a per-signature secret random number:
#     k = 3

# Calculate r:
#     r = (g^k mod p) mod q
#       = (4^3 mod 23) mod 11
#       = (64 mod 23) mod 11
#       = 18 mod 11
#       = 7

# Calculate the modular inverse of k:
#     k^(-1) mod q = 3^(-1) mod 11 = 4

# Check:
#     3 * 4 mod 11 = 1

# Calculate s:
#     s = k^(-1) * (H(m) + x*r) mod q
#       = 4 * (8 + 3*7) mod 11
#       = 4 * (8 + 21) mod 11
#       = 4 * 29 mod 11
#       = 116 mod 11
#       = 6

# Digital signature:
#     (r, s) = (7, 6)


# 3. SIGNATURE VERIFICATION
# -------------------------
# The receiver has:
#     p = 23, q = 11, g = 4
#     Public key y = 18
#     Signature (r, s) = (7, 6)
#     Assumed message hash H(m) = 8

# Calculate w:
#     w = s^(-1) mod q
#       = 6^(-1) mod 11
#       = 2

# Check:
#     6 * 2 mod 11 = 1

# Calculate u1:
#     u1 = H(m) * w mod q
#        = 8 * 2 mod 11
#        = 16 mod 11
#        = 5

# Calculate u2:
#     u2 = r * w mod q
#        = 7 * 2 mod 11
#        = 14 mod 11
#        = 3

# Calculate v:
#     v = ((g^u1 * y^u2) mod p) mod q
#       = ((4^5 * 18^3) mod 23) mod 11

# Calculate powers modulo 23:
#     4^5 mod 23 = 12
#     18^3 mod 23 = 13

# Then:
#     v = ((12 * 13) mod 23) mod 11
#       = (156 mod 23) mod 11
#       = 18 mod 11
#       = 7

# Compare:
#     r = 7
#     v = 7

# Since r = v, the signature is VALID for this message and public key.


# 4. IF THE MESSAGE IS MODIFIED
# -----------------------------
# If HELLO changes to HELLO123, its hash changes:
#     H(HELLO) != H(HELLO123)

# The receiver uses the new hash to calculate u1 and v. The verification
# value will no longer equal the original r (except with negligible
# probability in a properly sized real system).

# Therefore:
#     r != v
#     Signature verification FAILS.


# 5. SUMMARY
# ----------
# Key generation:
#     Public key y = g^x mod p

# Signature generation:
#     r = (g^k mod p) mod q
#     s = k^(-1) * (H(m) + x*r) mod q

# Verification:
#     w  = s^(-1) mod q
#     u1 = H(m) * w mod q
#     u2 = r * w mod q
#     v  = ((g^u1 * y^u2) mod p) mod q

# Decision:
#     If v = r, the signature is valid.
#     If v != r, verification fails.

# IMPORTANT NOTES
# ---------------
# 1. DSA is a digital signature algorithm, not an encryption algorithm.
# 2. The private key is used for signing; the public key is used for verification.
# 3. k must be secret, unpredictable, and never reused. Reusing or exposing k
#    can reveal the private key.
# 4. This tiny example is for learning only. It is not secure for real use.
# 5. In the Python cryptography library, SHA-256 hashing and all DSA
#    calculations are handled internally by sign() and verify().
