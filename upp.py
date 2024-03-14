import pickle
import subprocess
import os
import base64
import json

###This Script is Used To Create Usernames/Passwords/SSH Directories for every user on the system
###Make sure the ssh key (sshkey.txt) and  encrypted data (encrypted_data.txt, use encrypt.py to encrypt the data) is in the same directory


def create_user(username, password, sshKey):
    try:
        # Create the user
        subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', username])

        # Set the password for the user
        passwd_process = subprocess.Popen(['passwd', username], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        password_bytes = password.encode('utf-8')
        passwd_process.stdin.write(password_bytes + b'\n')
        passwd_process.stdin.write(password_bytes)
        passwd_process.stdin.flush()
    
        stdout,stderr = passwd_process.communicate()


        # Create and Set public Key
        sshDirectoryPath = "/home/"+username+"/.ssh"
        authorizedKeyPath = "/home/"+username+"/.ssh/authorized_keys"

        os.makedirs(sshDirectoryPath, exist_ok=True)
        os.system("sudo chown -R "+username+": /home/"+username+"/.ssh")
        os.system("sudo chmod 700 "+sshDirectoryPath)


        with open(authorizedKeyPath, "a") as f:
            f.write("\n" + sshKey + "\n")
            f.close()


        print("User "+username+" created successfully.")
    except Exception as e:
        print("Error creating user "+username+": "+str(e))

def simple_xor_decrypt(encrypted_data, key):
    decrypted_data = [byte ^ key for byte in encrypted_data]
    return bytes(decrypted_data)

def bytes_to_list(serialized_data):
    # Convert bytes back to the list using JSON deserialization
    deserialized_data = json.loads(serialized_data.decode())
    return deserialized_data

def get_decrypted_list():

    # Read the encrypted data from the file
    with open('encrypted_data.txt', 'rb') as file:
        read_encrypted_data = base64.b64decode(file.read())

    # Choose a key for XOR decryption
    decryption_key = 42

    # Decrypt the data
    decrypted_data = simple_xor_decrypt(read_encrypted_data, decryption_key)

    # Convert bytes back to the list
    decrypted_list = bytes_to_list(decrypted_data)
    return decrypted_list

def main():
        
        with open("sshkey.txt", "r") as f:
            sshKey = f.readline()

        
        decrypted_list = get_decrypted_list()

        for ucred in get_decrypted_list:
            create_user(ucred[0], ucred[1], sshKey)
             

if __name__ == "__main__":
    main()