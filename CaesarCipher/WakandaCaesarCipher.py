# A Wakandian python program to show the basics of a caesar cipher
import random


def encrypt(string, key=4):
    '''Encrypts a string'''
    # traverse or looks over the "text" from line one
    result = ""
    for character in string:
        if character.isalpha():
            # Encrypt uppercase characters
            if character.isupper():
                result += chr((ord(character) + key - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(character) + key - 97) % 26 + 97)
        else:
            result +=character

    print ("Text  : ", string)
    print ("Key : ", str(key))
    print ("Cipher: ", result)
    return result


def decrypt(string, key=-4):
    '''decrypt a string'''

    result = ""
    for character in string:
        if character.isalpha():
            # Decrpypt uppercase characters
            if character.isupper():
                result += chr((ord(character) + key - 65) % 26 + 65)

            # Decrypt lowercase characters
            else:
                result += chr((ord(character) + key - 97) % 26 + 97)
        else:
            result +=character

    print ("Cipher  : ", string)
    print ("Shift : ", str(key))
    print ("Text: ", result)

    return result


def main():
    choice = input("Enter 1 to encryption.  Enter 2 for decryption: ")
    if choice == "1":
        string_to_encrypt = input("What string do you want to encrypt?")
        #s = random.randint(1, 13)
        #print("s:", s)
        encrypt(string_to_encrypt)
    elif choice == "2":
        string_to_decrypt = input("What string do you want to decrypt?")
        #s = random.randint(1,13)
        # print("s:",s)
        decrypt(string_to_decrypt)
    else:
        print("You choose an invalid option.")


if __name__ == "__main__":
    main()
