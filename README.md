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
