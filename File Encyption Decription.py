
# coding: utf-8
# Hvy_D


import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import getpass


class CryptoKey:
'Encryption and decryption of files'

    def __init__(self):
        pass

    def loadfile(self, masterfile):
        with open(masterfile) as f:
            token = f.readlines()
        f.close()
        token = [x.strip() for x in token]
        token = token[0]
        return(token)

    def keygen(self, password):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password.encode(encoding = 'utf-8'))
        key = base64.urlsafe_b64encode(digest.finalize())
        return(key)

    def encrypter(self, key, token):
        f = Fernet(key)
        encrypted = f.encrypt(token.encode(encoding = 'utf-8'))
        print(encrypted)

    def decrypter(self, key, token):
        f = Fernet(key)
        decrypted = f.decrypt(token.encode(encoding = 'utf-8'))
        print(decrypted)



# decrypt file
Crypto = CryptoKey()
token = Crypto.loadfile('~/file.txt')  # provide file path
password = getpass.getpass('key: ')    # provide password
key = Crypto.keygen(password)          # generate key
Crypto.decrypter(key,token)            # decrypt file

