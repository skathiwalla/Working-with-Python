'''
Baruch Python course final project.
By: Shameem Kathiwalla
Date: Feb 27, 2020

Description: I created a simple Caesar's cypher that can be used to encrypt a message or
decrypt a code. Encryption or decryption can be achieved with the help of a key.
In the case below the encryption key is randomly generated between negative 5 to positive 10.
This makes it pretty easy to break the message but its still cool to see how it works.
Once you encrypt a message you can decrypt it by providing the coded message and the key. 


Some points:
1.I use random.randint(-5,10) to generate the key. One of the issues is that it does pick zero sometimes
then the code has to be rerun. 
2.users can encrypt/decrypt a message with spl characters, a blank space,upper or
lower case alpahbetes and numbers.On the Ascii table thats from 32 to 126.
3. I usedthe functions ord() to convert to ascii and chr() to convert from ascii code to charater
 
'''
import random

a=input('Would you like to encrypyt a phrase (Y/N): ')
while a.lower() not in ['y', 'n', 'yes', 'no']:
    a=input('Please type Y/N, thanks.\nWould you like to encrypt a phrase (Y/N): ')

if a in ('Y','y','Yes','yes'):
    message=input('Enter a phrase to encrypt: ')
    key=random.randint(-5,10)
    
    e_message=""

    for x in range(0,len(message)):
        ascii=ord(message[x])
        ascii=ascii+int(key)
        if ascii>126:
            ascii=ascii-94
        e_message=e_message+chr(ascii)
    print('The encrypted message is: ',e_message)
    print('The encryption key is:',key)

elif a in ('N','n','no','No'):
    decypyted_message=input('Enter a phrase to decrypt: ')
    key=input('Please enter decryption key: ')
    
    d_message=""

    for x in range(0,len(decypyted_message)):
    
        ascii=ord(decypyted_message[x])
        ascii=ascii-int(key)
        if ascii>126:
            ascii=ascii-94
        d_message=d_message+chr(ascii)
    print('The decrypted message is: ',d_message)
    print('The decryption key is: ',key)
         

