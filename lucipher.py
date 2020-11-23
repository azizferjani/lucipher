# ----------------------------------------------------------------------------------------------
#        LucipherPY.
#
#        Author : Aziz 'AF' Ferjani
#        Email  : contact@azizferjani.com
#        Github : https://github.com/azizferjani
#
# ----------------------------------------------------------------------------------------------

from random import randint
import base64

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#VCRYPT ENCRYPTION ALGORITHM
def vcrypt(key, message, mode):
    translated = []

    keyIndex = 0

    key = key.upper()

    for symbol in message: 
        num = l.find(symbol.upper())
        if num != -1: # 
            if mode == 'encrypt':
                num += l.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= l.find(key[keyIndex])
            num %= len(l)

            if symbol.isupper():
                translated.append(l[num])
            elif symbol.islower():
                translated.append(l[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

#LCRYPT ENCRYPTION ALGORITHM
def lcrypt(string, shift):
    cipher = ''
    for char in string: 
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

#LUCIPHER CHARSET
ch = ['A', 'B', 'C', 'D', 'E','F','G', 'H', 'I', 'J', 'K','L',
      'M', 'N', 'O', 'P', 'Q','R','S', 'T', 'U', 'V', 'W','X', 
      'Y', 'Z', 'a', 'b', 'c','d','e', 'f', 'g', 'h', 'i','j',
      'k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u','v',
      'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9',
      '+','/','=',"'",'_',' ']

#LUCIPHER ENCRYPT
def encrypt(text,key):
    if len(key) >= 4:
        c = len(l) * len(key)
        e = [x for x in range(c,c+69)]
        z = [e[ch.index(l)] for l in text]

    else:
        print('key is too short')

    q = ''.join(str(e) for e in z)

    f = []
    for x in q:
        a = randint(0, int(x))
        b = int(x) - a
        f.append(str(a)+str(b))
        
    t = ''.join(str(i) for i in f)
    o = [lcrypt(l,len(key))[['0','1','2','3','4','5','6','7','8','9'].index(x)] for x in t]

    return vcrypt(key, o, 'encrypt')


#lcryptpher decrypt function
#Same as encrypt function but reversed
def decrypt(ciphertext,key):
    #Decrypt from vigenre cipher
    decrypted = vcrypt(key, ciphertext, 'decrypt')
    e = ['0','1','2','3','4','5','6','7','8','9']
    t = ''.join(str(i) for i in decrypted)
    g = []
    p = []
    z = []

    c = []
    f = lcrypt(l, len(key))
    for i in f[:10]:
        c.append(i)
    for x in t:
            g.append(e[c.index(x)])
            y = ''.join(str(i) for i in g)
    y = list(map(int, g))
    h = [sum(y[i:i+2]) for i in range(0, len(y), 2)]

    

    c = len(l) * len(key)
    for x in range(c, c+68):
        p.append(x)
    s = ''.join(str(i) for i in h)
    v = list(map(int,[s[i:i+3] for i in range(0, len(s), 3)]))

    for u in v:
        z.append(ch[p.index(u)])
    return ''.join(str(i) for i in z)

#Image encryption function
#still on progress ~check sumcrypt.py for image encryption script
def imageEncrypt(n):
    with open(n, "rb") as img:
        i = base64.b64encode(img.read())
        r = encrypt(i.decode(),'lcryptpher').lower()
        p = scramble(r)
        file = open('r.txt','wb')
        file.write(''.join(str(i) for i in p).encode())
        print('File encrypted succesfully')

def imageDecrypt(n):
    with open(n,'rb') as img:
        r = decrypt(img.read().decode().upper(),'lcryptpher')
        z = base64.b64decode(r)
        with open("result.png", "wb") as fh:
            fh.write(z) 
def scramble(n):
    p = []
    for x in n:
        t = randint(0,2)
        if t == 0:
            p.append(x.upper())
        else:
            p.append(x)
    return ''.join(str(i) for i in p)


def main():
    eMode = input('Enter encryption mode : i (img) / t (txt) :')
    if eMode == 'i':
        mode = input('Enter e ( encrypted ) / d ( decrypt ) :')
        if mode == 'e':
            img = input('Image name : ')
            imageEncrypt(img)
        elif mode == 'd':
            img = input('Image name : ')
            imageDecrypt(img)
        else:
            print('Please use e (encrypt) / d (decrypt)')
    elif eMode == 't' :
        mode = input('Enter e ( encrypted ) / d ( decrypt ) :')
        txt = input('Text: ')
        key = input('Key :')
        if mode == 'e':
            print(scramble(encrypt(txt,key).lower()))
        elif mode == 'd':
            print(decrypt(txt.upper(),key))
        else:
            print('Please use e (encrypt) / d (decrypt)')
    else:
        print('Please use : i (img) / t (txt)')

if __name__ == '__main__':
    main()