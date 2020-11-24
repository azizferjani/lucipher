# ----------------------------------------------------------------------------------------------
#        LUcipher.
#
#        Author : Aziz 'AF' Ferjani
#        Email  : contact@azizferjani.com
#        Github : https://github.com/azizferjani
#
# ----------------------------------------------------------------------------------------------

from random import randint
import argparse
import base64

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#VCRYPT ENCRYPTION ALGORITHM
def vcrypt(k, m, x):
    t = []
    d = 0
    k = k.upper()

    for s in m: 
        n = l.find(s.upper())
        if n != -1: # 
            if x == 'encrypt':
                n += l.find(k[d])
            elif x == 'decrypt':
                n -= l.find(k[d])
            n %= len(l)

            if s.isupper():
                t.append(l[n])
            elif s.islower():
                t.append(l[n].lower())
            d += 1
            if d == len(k):
                d = 0
        else:
            t.append(s)

    return ''.join(t)

#LCRYPT ENCRYPTION ALGORITHM
def lcrypt(st, sf):
    cp = ''
    for ch in st: 
        if ch == ' ':
            cp = cp + ch
        elif  ch.isupper():
            cp = cp + chr((ord(ch) + sf - 65) % 26 + 65)
        else:
            cp = cp + chr((ord(ch) + sf - 97) % 26 + 97)
    return cp

#LUCIPHER CHARSET
ch = ['A', 'B', 'C', 'D', 'E','F','G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q','R','S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', 'a', 'b', 'c','d','e', 'f', 'g', 'h', 'i','j','k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u','v','w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','+','/','=',".",'_',' ']

#LUCIPHER ENCRYPT
def encrypt(text,key):
    if len(key) >= 4:
        c = len(l) * len(key)
        e = [x for x in range(c,c+69)]
        z = [e[ch.index(l)] for l in text]

        q = ''.join(str(e) for e in z)

        f = []
        for x in q:
            a = randint(0, int(x))
            b = int(x) - a
            f.append(str(a)+str(b))

        t = ''.join(str(i) for i in f)
        o = [lcrypt(l,len(key))[['0','1','2','3','4','5','6','7','8','9'].index(x)] for x in t]

        return vcrypt(key, o, 'encrypt')
    else:
        return 6999

#LUCIPHER DECRYPT
def decrypt(ciphertext,key):
    if len(key) >= 4:
        decrypted = vcrypt(key, ciphertext, 'decrypt')

        t = ''.join(str(i) for i in decrypted)

        c = [i for i in lcrypt(l, len(key))[:10]]

        g = [['0','1','2','3','4','5','6','7','8','9'][c.index(x)] for x in t]
        y = list(map(int, g))
        h = [sum(y[i:i+2]) for i in range(0, len(y), 2)]

        c = len(l) * len(key)
        p = [x for x in range(c,c+69)]

        s = ''.join(str(i) for i in h)
        v = list(map(int,[s[i:i+3] for i in range(0, len(s), 3)]))

        z = [ch[p.index(u)] for u in v]
        return ''.join(str(i) for i in z)
    else:
        return 9666

#ART
def usage():
    print("""
 /$$       /$$   /$$           /$$           /$$                          
| $$      | $$  | $$          |__/          | $$                          
| $$      | $$  | $$  /$$$$$$$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$      | $$  | $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$      | $$  | $$| $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$  | $$| $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$      
|________/ \______/  \_______/|__/| $$____/ |__/  |__/ \_______/|__/      
                                  | $$                                    
                                  | $$                                    
                                  |__/""")
    print("LUcipher created by AF")
    print("lucipher.py -h for help")


#EXECUTE
parser = argparse.ArgumentParser(description='LUcipher Encryption Algorithm')
parser.add_argument('-m','--mode', help='Encryption or Decryption mode')
parser.add_argument('-t','--text', help='Enter the text you want to encrypt')
parser.add_argument('-k','--key', help='Enter your encryption key')


args = parser.parse_args()
if args.mode == 'e':
    if len(args.key) >= 4:
        print(encrypt(args.text,args.key))
    else:
        print("Key is too short (4)")
elif args.mode == 'd':
    if len(args.key) >= 4:
        print(decrypt(args.text,args.key))
else:
    usage()
