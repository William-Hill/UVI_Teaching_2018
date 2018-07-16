''' A python program to show the basics of a caesar cipher'''
import random

#The chr() function (pronounced “char”, short for “character”) takes an integer ordinal and returns a single-character string
#The ord() function (short for “ordinal”) takes a single-character string, and returns the integer ordinal value

def encrypt(string, key=4):
    '''Encrypts a string'''
    # traverse or looks over the "text" from line one
    result = ""
    for character in string:
        if character.isalpha():
            #Convert character to ASCII index
            num = ord(character)
            #add key to ASCII index
            num += key
            # Encrypt uppercase characters
            if character.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                result += chr(num)
            # Encrypt lowercase characters
            else:
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                result += chr(num)
        else:
            result +=character

    print ("Text  : ", string)
    print ("Key : ", str(key))
    print ("Cipher: ", result)
    return result


def decrypt(string, key=-4):
    '''decrypt a string'''
    if key > 0:
        key = -key
    result = ""
    for character in string:
        if character.isalpha():
            #Convert character to ASCII index
            num = ord(character)
            #add key to ASCII index
            num += key
            # Decrpypt uppercase characters
            if character.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                result += chr(num)
            # Decrypt lowercase characters
            else:
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                result += chr(num)
        else:
            result +=character

    print ("Cipher  : ", string)
    print ("Key : ", str(key))
    print ("Text: ", result)

    return result


def main():
    choice = input("Enter 1 to encryption.  Enter 2 for decryption: ")
    if choice == "1":
        string_to_encrypt = input("What string do you want to encrypt? ")
        #s = random.randint(1, 13)
        #print("s:", s)
        encrypt(string_to_encrypt)
    elif choice == "2":
        string_to_decrypt = input("What string do you want to decrypt? ")
        #s = random.randint(1,13)
        # print("s:",s)
        decrypt(string_to_decrypt)
    else:
        print("You choose an invalid option.")


if __name__ == "__main__":
    main()
