
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





# import random

# # DSA parameters
# p = 23
# q = 11
# g = 4

# # Generate private and public keys
# private_key = random.randint(1, q-1)
# public_key = pow(g, private_key, p)

# print("Private Key:", private_key)
# print("Public Key:", public_key)

# # Sign message using private key
# def sign(message_hash):
#     k = random.randint(1, q-1)

#     r = pow(g, k, p) % q
#     k_inv = pow(k, -1, q)

#     s = (k_inv * (message_hash + private_key * r)) % q

#     return r, s

# # Verify signature using public key
# def verify(message_hash, signature):
#     r, s = signature

#     if not (0 < r < q and 0 < s < q):
#         return False

#     w = pow(s, -1, q)
#     u1 = (message_hash * w) % q
#     u2 = (r * w) % q

#     v = (pow(g, u1, p) * pow(public_key, u2, p) % p) % q

#     return v == r


# # Main program
# h = int(input("\nEnter message hash value: ")) % q

# signature = sign(h)

# print("\nDigital Signature:")
# print("r =", signature[0])
# print("s =", signature[1])

# print("\nSignature Verification:")

# if verify(h, signature):
#     print("Signature is VALID.")
# else:
#     print("Signature is INVALID.")

# # Verify with modified hash
# modified_hash = (h + 1) % q

# print("\nModified Message Verification:")

# if verify(modified_hash, signature):
#     print("Signature is VALID.")
# else:
#     print("Signature is INVALID.")
#     print("Message has been modified!")



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

