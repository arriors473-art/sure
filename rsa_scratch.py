
import time
import math

# Step 1: Define two prime numbers
p = 23
q = 5

# Step 2: Calculate n
n = p * q

# Step 3: Calculate Euler's Totient
phi = (p - 1) * (q - 1)

# Step 4: Select public exponent
e = 3

# Step 5: Calculate private exponent
d = pow(e, -1, phi)

print("===== RSA ENCRYPTION AND DECRYPTION =====")

print("\nPrime Number p:", p)
print("Prime Number q:", q)
print("Value of n:", n)
print("Euler's Totient:", phi)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))

# Step 6: Accept message
message = input("\nEnter message: ")

# Convert message into ASCII values
plain_values = [ord(ch) for ch in message]

# Step 7: Encryption
start = time.perf_counter()

ciphertext = []

for m in plain_values:
    c = pow(m, e, n)
    ciphertext.append(c)

encryption_time = time.perf_counter() - start

print("\nOriginal Message:", message)
print("ASCII Values:", plain_values)
print("Encrypted Message:", ciphertext)

# Step 8: Decryption
start = time.perf_counter()

decrypted_values = []

for c in ciphertext:
    m = pow(c, d, n)
    decrypted_values.append(m)

decryption_time = time.perf_counter() - start

# Convert ASCII values back into characters
decrypted_message = ''.join(chr(m) for m in decrypted_values)

print("\nDecrypted ASCII Values:", decrypted_values)
print("Decrypted Message:", decrypted_message)

# Step 9: Display performance
print("\nEncryption Time:", round(encryption_time, 8), "seconds")
print("Decryption Time:", round(decryption_time, 8), "seconds")

# Step 10: Verification
print("\nDecryption Correct:", message == decrypted_message)

print("\nRSA Experiment Completed Successfully!")
