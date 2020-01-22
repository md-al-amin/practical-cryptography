# Generate MD5 and ssa1 hash value
# Following wrinnte my MD AL AMIN; Email: info3.alamin@gmail.com

import hashlib  

string1 =  "Practical Cryptography" # String1
myName = "MD AL AMIN" #String2 
enstring1 = string1.encode()  # convert the string into byte  format
en_myName = myName.encode() # convert string into byte format
#print (hashlib.md5(enstring1)) # Generate MD5 cryptograpic hash value

print ("MD5 hash value of  Practical Cryptography : " +(hashlib.md5(enstring1).hexdigest())) # To display MD5 hash through hexadecimal character
print ("sha1 hash value of  Practical Cryptography : " +(hashlib.sha1(enstring1).hexdigest())) #To display sha1 hash through hexadecimal character
print ("MD5 hash value of  MD AL AMIN : " +(hashlib.md5(en_myName).hexdigest())) # To display MD5 hash through hexadecimal character
print ("sha15 hash value of  MD AL AMIN : " +(hashlib.sha1(en_myName).hexdigest())) #To display sha1 hash through hexadecimal character



