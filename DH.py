
# Diffie-Hellman Key Exchange with MITM Attack

# Take input from user
p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

alice_private = int(input("Enter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\n===== NORMAL DIFFIE-HELLMAN =====")

print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

# Generate shared secret key
alice_key = pow(bob_public, alice_private, p)
bob_key = pow(alice_public, bob_private, p)

print("Alice's Shared Key:", alice_key)
print("Bob's Shared Key:", bob_key)

if alice_key == bob_key:
    print("Shared Key Generated Successfully!")

# =====================================

print("\n===== MAN-IN-THE-MIDDLE ATTACK =====")

# Eve's private keys (demonstration values)
eve_alice_private = 7
eve_bob_private = 9

# Eve generates public keys
eve_to_alice = pow(g, eve_alice_private, p)
eve_to_bob = pow(g, eve_bob_private, p)

# Eve intercepts and replaces public keys
print("\nAlice sends:", alice_public)
print("Eve replaces with:", eve_to_bob)

print("\nBob sends:", bob_public)
print("Eve replaces with:", eve_to_alice)

# Alice and Bob generate separate keys with Eve
alice_mitm_key = pow(eve_to_alice, alice_private, p)
bob_mitm_key = pow(eve_to_bob, bob_private, p)

# Eve calculates both shared keys
eve_alice_key = pow(alice_public, eve_alice_private, p)
eve_bob_key = pow(bob_public, eve_bob_private, p)

print("\nAlice's Key with Eve:", alice_mitm_key)
print("Eve's Key with Alice:", eve_alice_key)

print("\nBob's Key with Eve:", bob_mitm_key)
print("Eve's Key with Bob:", eve_bob_key)

# Verify attack
if (alice_mitm_key == eve_alice_key and
    bob_mitm_key == eve_bob_key):

    print("\nMITM ATTACK SUCCESSFUL!")
    print("Eve can intercept communication.")

