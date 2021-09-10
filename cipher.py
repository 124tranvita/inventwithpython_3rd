MAX_KEY_SIZE = 26

# Deciding to Encrypt or Decrypt
def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        mode = input().lower()

        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "Encrypt" or "e" or "Decrypt" or "d" or "Brute" or "b"')

# Getting the message for the Player
def get_message():
    return input('Enter your message:\n')

# Getting the key from Player
def get_key():
    key = 0

    while True:
        key = int(input('Enter the key number (1 - {}):\n'.format(MAX_KEY_SIZE)))
        if key >= 0 and key <= MAX_KEY_SIZE:
            return key

# Encrypt or Decrypt the message with the given key
def get_translated_message(mode, key, message):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            # encrypting or decrypting each letter
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
        
            translated += chr(num)
        else:
            translated += symbol

    return translated

# The start of program
mode = get_mode()
message = get_message()

if mode[0] != 'b':
    key = get_key()

print('Your translated text is: ')

if mode[0] != 'b':
    print(get_translated_message(mode, key, message))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, get_translated_message('decrypt', key, message))