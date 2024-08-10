import random

with open("username.txt", "r") as f:
    users = f.readlines()

cleanUsers = []
for user in users:
    cleanUser = user[:-1]
    cleanUsers.append(cleanUser)

with open("passwords.txt", "r") as f:
    passwords = f.readlines()

correctPasswords = []
for password in passwords:
    correctPassword = password[:-1]
    correctPasswords.append(correctPassword)


with open("newpasswords.txt", "w") as f:
    for user in cleanUsers:
        randomEntry = random.choice(correctPasswords)
        correctPasswords.remove(randomEntry)
        f.write(randomEntry+"\n")

#newPasswords = []
#for user in splitUsers:
