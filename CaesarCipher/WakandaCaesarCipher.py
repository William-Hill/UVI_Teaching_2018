 #A Wakandian python program to show the basics of a caesar cipher
import random
#def encrypt(str, rotate_cipher)
def blackpanther(tachalla, s = 7):
    '''Encrypts a string'''

    #traverse or looks over the "text" from line one
    result = ""
    for i in range(len(tachalla)):
        char = tachalla[i]

        #Encryt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)


        #Encrypt lowercase characters
        else:  
            result += chr((ord(char) + s - 97) % 26 + 97)

            #return result

    #check the wakandian function
    print ("Text  : ", tachalla)
    print ("Shift : ", str (s))
    print ("Cipher: ", result)

def killmonger(njadaka, s = -7):
    '''decrypt a string'''

    result= ""
    for i in range(len(njadaka)):
        char = njadaka[i]

   #Decrpypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)


        #Decrypt lowercase characters
        else:  
            result += chr((ord(char) + s - 97) % 26 + 97)

            #return result



    
    print ("Cipher  : ", njadaka)
    print ("Shift : ", str (s))
    print ("Text: ", result)

    

def main():
    string_to_encrypt = input("What string do you want to encrypt?")
    #s = random.randint(1, 13)
    #print("s:", s)
    blackpanther(string_to_encrypt)


    string_to_decrypt = input ("What string do you want to decrypt?")
    #s = random.randint(1,13)
    #print("s:",s)
    killmonger(string_to_decrypt) 

    


if __name__ == "__main__":
    main()





    

    
