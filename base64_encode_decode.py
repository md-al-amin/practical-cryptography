# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:33:27 2022

@author: AL-AMIN
Base 64 encoder & decoder
"""


import base64
  
#encoding

sample_string = input('Enter Simple String: ')
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
  
print("Encoded string: ", base64_string)


#decoding

base64_cipher_string = input('Enter cipher String: ')
base64_bytes = base64_cipher_string.encode("ascii")
  
sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")
  
print(f"Decoded string: {sample_string}")

