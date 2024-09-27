'''
In case you're wondering, this is just RC4 with single b64 rotation.
'''

import base64
from typing import List

def initialize(key: str):
    start = list(range(256)) 

    j = 0
    for i in range(256):
        j = (j + start[i] + key[i % len(key)]) % 256
        start[i], start[j] = start[j], start[i]
    
    return start

def stream(start: List[int]):
    i = j = 0
    
    while True:
        i = (i + 1) % 256
        j = (j + start[i]) % 256
        start[i], start[j] = start[j], start[i]
        k = start[(start[i] + start[j]) % 256]
        yield k

def encrypt(key: str, message: str):
    key = [ord(c) for c in key]
    start = initialize(key)
    
    generator = stream(start)
    cipher = bytes([ord(c) ^ next(generator) for c in message])
    encoded = base64.b64encode(cipher).decode('utf-8')
    
    return encoded

def decrypt(key: str, message: str):
    cipher = base64.b64decode(message)
    key = [ord(c) for c in key]
    
    start = initialize(key)
    generator = stream(start)
    plaintext = ''.join(chr(c ^ next(generator)) for c in cipher)
    
    return plaintext
