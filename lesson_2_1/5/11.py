import rsa as rsa

key = input("Enter the Encryption Key: " )
while not (key.isdigit()):
    key = input("Enter the Encryption Key: " )
key = int(key)

mod_value = input("Enter the Modulus: " )
while not (mod_value.isdigit()):
    mod_value = input("Enter the Modulus: " )
mod_value = int(mod_value)
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
