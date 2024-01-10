#   a212_rsa_decrypt.py
import rsa as rsa


def get_int_input(prompt):
    result = input(prompt)
    while not (result.isdigit()):
        result = input(prompt)
    return int(result)

key = get_int_input("Enter the Decryption Key: " )
mod_value = get_int_input("Enter the Modulus: " )
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
