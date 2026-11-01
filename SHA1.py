import hashlib

# Accept input from the user
text = input("Enter the original text: ")

# Generate SHA-1 digest of original text
sha1_original = hashlib.sha1(text.encode()).hexdigest()

# Make a small change to the original text
modified_text = text + "!"

# Generate SHA-1 digest of modified text
sha1_modified = hashlib.sha1(modified_text.encode()).hexdigest()

# Display results
print("\n===== SHA-1 MESSAGE DIGEST =====")

print("Original Text:", text)
print("SHA-1 Digest:", sha1_original)

print("\nModified Text:", modified_text)
print("SHA-1 Digest:", sha1_modified)

# Compare both digests
if sha1_original == sha1_modified:
    print("\nBoth digests are same.")
else:
    print("\nDigests are different.")
    print("Message integrity verification detects the change.")