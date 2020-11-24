<p align=center>
  <img src="https://user-images.githubusercontent.com/45538475/100033033-97b10700-2df9-11eb-8e46-3dfa08aa0ade.jpg"/>
  <br>
  <span>Because the devil has secrets.</span>
  <br>
</p>

## Introduction
LUcipher is a secure encryption algorithm that also uses other secure cryptography techniques to encrypt a message using a key / password
## Usage

```console
$ python lucipher.py --help
optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Encryption or Decryption mode
  -t TEXT, --text TEXT  Enter the text you want to encrypt
  -k KEY, --key KEY     Enter your encryption key

LUcipher: Encrypt your secrets with a key (Version 0.0.1)

positional arguments:
  USERNAMES             One or more usernames to check with social networks.

optional arguments:
  -h, --help            show this help message and exit
                        Display extra debugging information and metrics.
  -m , --mode           Specificy Encryption or Decryption mode (e / d)
  -t , --text           Enter the text that will be encrypted/decrypted.
  -k , --key            Encryption key or password.
  
```

Example:
```
python sherlock.py -m e -t "Hello World" -k passkey12
```

Created by AF.
