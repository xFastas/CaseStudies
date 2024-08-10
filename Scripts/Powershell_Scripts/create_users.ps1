# This file is used to create usernames/passwords for every user on the windows systems


# Import the Active Directory module
Import-Module ActiveDirectory

# Read the base64-encoded file
$fileContent = Get-Content -Path 'C:\Users\South\Desktop\userpass\encrypted_data.txt' -Raw

# Decode base64
$base64Decoded = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($fileContent))

# Choose the same key used for encryption in Python
$encryptionKey = #set to any number

# Simple XOR decryption
$decryptedData = $base64Decoded.ToCharArray() | ForEach-Object { [char]($_ -bxor $encryptionKey) }

# Join characters to form a string
$decryptedString = -join $decryptedData

# Deserialize JSON directly
$decryptedList = $decryptedString | ConvertFrom-Json

# Display the decrypted list
# Loop through the list and change the password for each user in Active Directory
foreach ($user in $decryptedList) {
    $username = $user[0]
    $password = $user[1]

    # Change the password in Active Directory
    Set-ADAccountPassword -Identity $username -NewPassword (ConvertTo-SecureString -String $password -AsPlainText -Force) -Reset

    Write-Host "Password changed successfully for user $username"
}
    Write-Host "----------------------"