import pyperclip

# the string to be encrypted/decrypted
message = input('Please enter the message : ')

# the encryption/decryption key
key = int(input('Please enter the key (integer value) : '))

# tells the program to encrypt or decrypt
#mode = 'encrypt' # set to 'encrypt' or 'decrypt'
mode = int(input('For encrypting the message press 1 & decrypting press 0 : ')) # set to 'encrypt' or 'decrypt'
if mode==1:
    mode = 'encrypt'
if mode == 0:
    mode = 'decrypt'

# every possible symbol that can be encrypted
LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        #print(symbol,num)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)

# copy the encrypted/decrypted string to the clipboard
#pyperclip.copy(translated)

# With the help of following link
# Reference link: http://inventwithpython.com/cracking/chapter5.html
# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
