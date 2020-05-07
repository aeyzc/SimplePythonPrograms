#Simple Encryption Code Example
#Basit Şifreleme 

import random

def encryption(strx):
    n = []
    j=0

    for i in range(len(strx)*3):
        if i%3==0:
            
            n.append(chr(ord(strx[j])+2))
            j+=1
        
        else:
            n.append(chr(random.randint(97,122)))

    return n

def decoding(strx):
    n=[]

    for i in range(len(strx)):
        if i%3==0:
            n.append(chr(ord(strx[i])-2))

    return n


print('What you wanna do?\n1-Encryption\n2-Decoding')

selected=int(input(''))
print('\n')
if selected==1:
    str1=input('Text: ')
    str2=encryption(str1)

elif selected==2:
    str1=input('Text: ')
    str2=decoding(str1)

else:
    str2='Wrong Choice!'


print('\n')
print(''.join(str2))