import sys
import os
import hashlib
from itertools import product

# This program is to crack md5 hashed value.
# Using: md5_cracker filename
# For example: md5_cracker 1MillionPassword_hashed.txt

# Get path of file and open it.
path = os.getcwd()
file_name = sys.argv[1]
full_path = os.path.join(path, file_name)
f = open(full_path, 'r')

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*'
# Define list s to put all hashed password in input file.
s = []
# Define variable cracked_num to check how many passwords have been cracked.
cracked_num = 0

# Append all hashed password in input file to list s.
while True:
    # Used strip() in the end to delete leading and trailing characters.
    # In this case, to remove newline at the end of each password.
    line = f.readline().strip()
    if not line:
        break
    s.append(line)

# Start cracking
for length in range(6, 0, -1):
    # Itertools product list of chars with length
    plaintext_list = product(chars, repeat=length)

    for plaintext in plaintext_list:
        text = ''.join(plaintext)
        # Hash text with md5
        # Used encode() to convert the string into bytes to be acceptable by hash function.
        hashed_text = hashlib.md5(text.encode('utf-8'))
        hashed_text = hashed_text.hexdigest()

        # Check if hashed_text is in s
        if hashed_text in s:
            print("Success! %d/%d, %s : %s"%(s.index(hashed_text)+1, len(s), text, hashed_text))
            cracked_num += 1

print("Cracking is over! %d has been cracked!"%(cracked_num))

# Close file
f.close()