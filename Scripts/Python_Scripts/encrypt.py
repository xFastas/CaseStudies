import base64
import json
import pickle

#USE this file to encrypt a list of usernames and passwords with base 64

def simple_xor_encrypt(data, key):
    encrypted_data = [byte ^ key for byte in data]
    return bytes(encrypted_data)

def list_to_bytes(my_list):
    # Convert the list to bytes using JSON serialization
    serialized_data = json.dumps(my_list).encode()
    return serialized_data

# Replace 'your_list' with the list you want to encrypt and write


# Convert the list to bytes
with open("fruits.pkl", "rb") as f:
    fruits = pickle.load(f)
    f.close()

newFruits = []
for entry in fruits:
    entry[1] = "qR#"+entry[1][3:]
    newFruits.append(entry)

print(newFruits)


newFruits = [["Apple", "Banana"], ["Pen", "Pineapple"]]
serialized_data = list_to_bytes(fruits)

# Choose a key for XOR encryption
encryption_key = 42

# Encrypt the data
encrypted_data = simple_xor_encrypt(serialized_data, encryption_key)

# Write the encrypted data to a file
with open('encrypted_data.txt', 'wb') as file:
    file.write(base64.b64encode(encrypted_data))

print(f"Encryption completed. File saved as 'encrypted_data.txt'.")
