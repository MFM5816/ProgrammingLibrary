#!/usr/bin/env python3

import string
import random 

#all_chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_'
all_chars = string.digits + string.ascii_letters + '_'

pwd = ''

for i in range(8):
    char = random.choice(all_chars)
    pwd += char

print(pwd)












