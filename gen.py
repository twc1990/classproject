#!/bin/python

import random
import os, random, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from crypt import encrypt_file, decrypt_file

def firstLast(): #only generates letters
    tell=random.randint(1,2)
    if tell==1:
        let=chr(random.randint(65,90))
    elif tell==2:
        let=chr(random.randint(97,122))
    return let
def ranAlphNum(size): #generates letters and numbers
    for x in range(size):
		tell=random.randint(1,3)
		if tell==1:
			let=chr(random.randint(48,57))
		elif tell==2:
			let=chr(random.randint(65,90))
		elif tell==3:
			let=chr(random.randint(97,122))
    return let
def ranAll(special, size): #generates letters, numbers, special characters
    if special==2: #does not use some special characters
        for x in range(size)
            tell=random.randint(1,3)
            if tell==1:
                let=chr(random.randint(33,57))
            elif tell==2:
                let=chr(random.randint(65,90))
            elif tell==3:
                let=chr(random.randint(97,122))
    elif special==3: #uses all special characters for password
        for x in range(size)
        let=chr(random.randint(33,126))
    return let

def runGen(size, generator, ends):    
    password=""
    if ends==1:
        size=size-2
        password=firstLast()
        if generator==1:
            password=password+""+ranAlphNum(size)+""+firstLast()
        else:
            password=password+""+ranAll(generator, size)+""+firstLast()
    elif ends==0:
        if generator==1:
            password=ranAlphNum(size)
        else:
            password=ranAll(generator, size)
	return password.
			
			
def cryptTest():
    key = SHA256.new()
    key.update(b'password')
    key=key.digest()
    chunksize=64*1024
    print(key)
    iv = ''.join(chr(random.randint(0, 0xF)) for i in range(16))
    print(iv)
    #encryptor = AES.new(keyb, AES.MODE_CBC, iv)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize('pas.txt')
    with open('pas.txt', 'rb') as infile:
        with open('pas.enc', 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            ivencode = iv.encode('utf-8')
            outfile.write(ivencode)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode('utf-8') * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))
#encrypt_file(key, "pas.txt")
def decrTest():
    chunksize=24*1024
    key = SHA256.new()
    key.update(b'password')
    key=key.digest()
    with open('pas.enc', 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open('testing.txt', 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)