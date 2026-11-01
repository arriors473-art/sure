
print("==================================")
print("  CUSTOM ENCRYPTION AND DECRYPTION")
print("==================================")


text = input("Enter plaintext: ")
key = int(input("Enter secret key (number): "))

encrypted = ""
decrypted = ""

#Encryption
for i in range(len(text)):

    ch=text[i]

    value=ord(ch)^key

    value=value+(i*i)

    encrypted += chr(value)

#Decryption
for i in range(len(encrypted)):
    value=ord(encrypted[i])

    value=value-(i*i)

    ch=chr(value^key)

    decrypted+=ch

print("\nEncrypted text (ASCII codes):")


for ch in encrypted:
    print(ord(ch),end=" ")

# DISPLAY DECRYPTED TEXT
print("\n\nDecrypted text:", decrypted)

# VERIFICATION
if text == decrypted:
    print("Status: Encryption and Decryption Successful!")
else:
    print("Status: Decryption Failed!")
