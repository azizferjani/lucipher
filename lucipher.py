from random import randint
import base64


#Vigenre cipher
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)

#LUKEY table generator
def luci(string, shift):
    cipher = ''
    for char in string: 
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher



#lucipher charset
ch = ['A', 'B', 'C', 'D', 'E','F',
      'G', 'H', 'I', 'J', 'K','L',
      'M', 'N', 'O', 'P', 'Q','R',
      'S', 'T', 'U', 'V', 'W','X', 
      'Y', 'Z','a',  'b', 'c', 'd',
      'e', 'f', 'g', 'h', 'i','j',
      'k', 'l', 'm', 'n', 'o', 'p',
      'q', 'r', 's', 't', 'u', 'v',
      'w', 'x', 'y', 'z','0','1','2',
      '3','4','5','6','7','8','9','+','/',
      '=',"'",'_']
#Lucipher encrypt function
def encrypt(text,key):
    e = []
    z = []

    if len(key) >= 4:
        c = len(LETTERS) * len(key)
        for x in range(c, c+68):
            e.append(x)
    
        for l in text:
        	z.append(e[ch.index(l)])

    else:
        print('key is too short')

    #transform to 1 digit numbers
    q = ''.join(str(e) for e in z)
    j = [q[i:i+1] for i in range(0, len(q), 1)]
    #make a empty list
    n = list(map(int, j))
    #fill the empty list with new data
    f = []
    for x in n:
        a = randint(0, int(x))
        b = int(x) - a
        f.append(str(a)+str(b))



    e = ['0','1','2','3','4','5','6','7','8','9']
    t = ''.join(str(i) for i in f)
    k = len(key)
    g = []
    c = []
    j = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = luci(j, k)
    for i in f[:10]:
        c.append(i)
    for x in t:
            g.append(c[e.index(x)])
            y = ''.join(str(i) for i in g)
    #Encrypt in vigerne cipher
    return encryptMessage(key,g)


#Lucipher decrypt function
#Same as encrypt function but reversed
def decrypt(ciphertext,key):
    #Decrypt from vigenre cipher
    decrypted = decryptMessage(key,ciphertext)
    e = ['0','1','2','3','4','5','6','7','8','9']
    t = ''.join(str(i) for i in decrypted)
    k = len(key)
    g = []
    p = []
    z = []

    c = []
    j = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = luci(j, k)
    for i in f[:10]:
        c.append(i)
    for x in t:
            g.append(e[c.index(x)])
            y = ''.join(str(i) for i in g)
    y = list(map(int, g))
    h = [sum(y[i:i+2]) for i in range(0, len(y), 2)]

    

    c = len(LETTERS) * len(key)
    for x in range(c, c+68):
        p.append(x)
    s = ''.join(str(i) for i in h)
    v = list(map(int,[s[i:i+3] for i in range(0, len(s), 3)]))

    for l in v:
        z.append(ch[p.index(l)])
    return ''.join(str(i) for i in z)

#Image encryption function
#still on progress ~check sumcrypt.py for image encryption script
def imageEncrypt(n):
	with open(n, "rb") as img:
		i = base64.b64encode(img.read())
		r = encrypt(i.decode(),'lucipher').lower()
		p = scramble(r)
		file = open('r.txt','wb')
		file.write(''.join(str(i) for i in p).encode())
		print('File encrypted succesfully')

def imageDecrypt(n):
	with open(n,'rb') as img:
		r = decrypt(img.read().decode().upper(),'lucipher')
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