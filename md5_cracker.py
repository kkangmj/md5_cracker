import sys
import os
from itertools import product
import hashlib

# Using: ./md5_cracker filename
# For example: ./md5_cracker 1MillionPassword_hashed.txt

path = os.getcwd()
file_name = sys.argv[1]
full_path = os.path.join(path, file_name)
f = open(full_path, 'r')

chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*'

while True:
    line = f.readline().strip()
    if not line:
        break

    flag = True

    for length in range(1, 8):
        plaintext_list = product(chars, repeat=length)
        for plaintext in plaintext_list:
            text = ''.join(plaintext)
            # encode() : converts the string into bytes to be acceptable by hash function.
            hashed_text = hashlib.md5(text.encode('utf-8'))
            hashed_text = hashed_text.hexdigest()

            if hashed_text == line:
                print("Success! %s is %s" %(text, line))
                flag = False

    if flag:
        print("Fail!", line)


f.close()


'''
Reference:
https://gist.github.com/miodeqqq/8e064f14d446348914f0e45818234a2e
https://itmining.tistory.com/122
https://www.geeksforgeeks.org/sha-in-python/
'''