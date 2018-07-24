
# coding: utf-8
# Hvy_D


import os, random

def randPassGen():
    key_L = 128
    key_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%*'
    print(''.join(random.choice(key_chars)for password in range(key_L)))
    
    
randPassGen()


