import base64
import json

#Use this to decrypt your list of usenames and passwords (more of a scrap script to take from)

def simple_xor_decrypt(encrypted_data, key):
    decrypted_data = [byte ^ key for byte in encrypted_data]
    return bytes(decrypted_data)

def bytes_to_list(serialized_data):
    # Convert bytes back to the list using JSON deserialization
    deserialized_data = json.loads(serialized_data.decode())
    return deserialized_data

# Read the encrypted data from the file
with open('encrypted_data.txt', 'rb') as file:
    read_encrypted_data = base64.b64decode(file.read())

# Choose a key for XOR decryption
decryption_key = 42

# Decrypt the data
decrypted_data = simple_xor_decrypt(read_encrypted_data, decryption_key)

# Convert bytes back to the list
decrypted_list = bytes_to_list(decrypted_data)

print(f"Decrypted List: {decrypted_list}")
