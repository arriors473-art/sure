
import hashlib
import os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


KEY = b"0123456789abcdef0123456789abcdef"


# SHA-256 function
def sha256(data):
    return hashlib.sha256(data).hexdigest()


# SENDER
def sender():

    path = input("Enter image path: ").strip('"')

    image = Path(path).read_bytes()
    filename = Path(path).name

    # Generate nonce and encrypt image
    nonce = os.urandom(12)
    aes = AESGCM(KEY)
    encrypted = aes.encrypt(nonce, image, None)

    print("\n--- SENDER ---")
    print("Image:", filename)
    print("Original SHA-256:", sha256(image))
    print("Encryption: AES-256-GCM")
    print("Image encrypted successfully!")

    # Return encrypted data for receiver
    return filename, nonce, encrypted, sha256(image)


# RECEIVER
def receiver(filename, nonce, encrypted, original_hash):

    try:
        # Decrypt image
        aes = AESGCM(KEY)
        image = aes.decrypt(nonce, encrypted, None)

        # Save recovered image
        output = "received_" + filename
        Path(output).write_bytes(image)

        received_hash = sha256(image)+"!"

        print("\n--- RECEIVER ---")
        print("Decryption: Successful")
        print("Authentication: Valid")
        print("Saved Image:", output)
        print("Received SHA-256:", received_hash)

        # Compare hashes
        if original_hash == received_hash:
            print("\nImage Integrity: Verified")
        else:
            print("\nImage Integrity: Failed")

    except Exception:
        print("\nAuthentication Failed! Image rejected.")


# MAIN PROGRAM
print("===== SECURE IMAGE TRANSMISSION =====")

data = sender()
receiver(*data)
