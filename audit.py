
#Use this file to audit users on a linux system
#It compares users to usernames in a .txt file (usernames.txt)

def read_passwd_file(file_path):
    with open(file_path, 'r') as passwd_file:
        lines = passwd_file.readlines()
    return lines

def extract_usernames(lines):
    usernames = [line.split(':')[0] for line in lines]
    return usernames

def check_usernames(usernames, allowed_users):
    for username in usernames:
        if username not in allowed_users:
            print(f"User not in the list: {username}")

if __name__ == "__main__":
    # Replace 'allowed_users_list' with your list of allowed usernames
    with open("usernames.txt", "r") as f:
        users = f.readlines()
        f.close()
    
    newUsers = []
    for user in users:
        newUsers.append(user[:-1])


    passwd_file_path = '/etc/passwd'

    try:
        passwd_lines = read_passwd_file(passwd_file_path)
        passwd_usernames = extract_usernames(passwd_lines)
        check_usernames(passwd_usernames, newUsers)
    except FileNotFoundError:
        print(f"Error: {passwd_file_path} not found. Make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")