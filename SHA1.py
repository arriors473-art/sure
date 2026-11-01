import hashlib

# Function to generate SHA-1 digest
def generate_sha1(text):
    encoded_text = text.encode("utf-8")
    sha1_digest = hashlib.sha1(encoded_text).hexdigest()
    return sha1_digest


# Function to display message and digest
def display_result(message, digest):
    print("Text:", message)
    print("SHA-1 Digest:", digest)


# Function to verify message integrity
def verify_integrity(original_digest, modified_digest):
    if original_digest == modified_digest:
        print("\nBoth digests are same.")
    else:
        print("\nDigests are different.")
        print("Message integrity verification detects the change.")


# Main program
print("===== SHA-1 MESSAGE DIGEST =====")

# Accept input from the user
text = input("Enter the original text: ")

# Generate SHA-1 digest of original text
sha1_original = generate_sha1(text)

# Make a small change to the original text
modified_text = text + "!"

# Generate SHA-1 digest of modified text
sha1_modified = generate_sha1(modified_text)

# Display original text and digest
print("\nOriginal Message:")
display_result(text, sha1_original)

# Display modified text and digest
print("\nModified Message:")
display_result(modified_text, sha1_modified)

# Compare both digests
verify_integrity(sha1_original, sha1_modified)
