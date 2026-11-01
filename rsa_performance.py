
import rsa
import time


key_sizes = [512, 1024, 2048]


messages = [
    b"12345678",
    b"1234567890123456",
    b"12345678901234567890123456789012"
]

print("\nRSA PERFORMANCE ANALYSIS")
print("=" * 65)

for key_size in key_sizes:

    print("\nRSA Key Size:", key_size, "bits")
    print("-" * 65)

    start = time.perf_counter()

    public_key, private_key = rsa.newkeys(key_size)

    end = time.perf_counter()

    key_time = end - start

    print("Key Generation Time:", round(key_time, 6), "seconds")

  
    for message in messages:

        message_size = len(message)

  
        start = time.perf_counter()

        ciphertext = rsa.encrypt(message, public_key)

        end = time.perf_counter()

        encryption_time = end - start

      
        start = time.perf_counter()

        decrypted = rsa.decrypt(ciphertext, private_key)

        end = time.perf_counter()

        decryption_time = end - start

      
        print("\nMessage Size:", message_size, "bytes")
        print("Encryption Time:", round(encryption_time, 6), "seconds")
        print("Decryption Time:", round(decryption_time, 6), "seconds")
        print("Decryption Correct:", message == decrypted)

print("\nRSA Experiment Completed Successfully!")
