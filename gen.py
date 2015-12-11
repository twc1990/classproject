#!/bin/python

import random
import os, random, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

passPhrase="This is a very long sentence that serves only to tests if the algorithms are using )*&0912ethe correct password 198026813265 sdalku1268435362 fasd6aoiyonmLKHAslfb.wek8"
passPhrase+=' '* (16 - len(passPhrase) % 16)
def firstLast(): #only generates letters
    tell=random.randint(1,2)
    if tell==1:
        let+=chr(random.randint(65,90))
    elif tell==2:
        let+=chr(random.randint(97,122))
    return let
def ranAlphNum(size): #generates letters and numbers
    let = ''
    for x in range(size):
        tell=random.randint(1,3)
        if tell==1:
            let+=chr(random.randint(48,57))
        elif tell==2:
            let+=chr(random.randint(65,90))
        elif tell==3:
            let+=chr(random.randint(97,122))
    return let
def ranAll(special, size): #generates letters, numbers, special characters
    let = ''
    if special=="Restricted Special": #does not use some special characters
        for x in range(size):
            tell=random.randint(1,3)
            if tell==1:
                let+=chr(random.randint(33,57))
            elif tell==2:
                let+=chr(random.randint(65,90))
            elif tell==3:
                let+=chr(random.randint(97,122))
    else: #uses all special characters for password
        for x in range(size):
            let+=chr(random.randint(33,126))
    print(let)
    return let

def runGen(size, generator, ends):    
    print(size)
    print(generator)
    print(ends)
    password=""
    if ends==1:
        size=size-2
        password=firstLast()
        if generator=="Alphanumeric":
            password=password+""+ranAlphNum(size)+""+firstLast()
        else:
            password=password+""+ranAll(generator, size)+""+firstLast()
    else:
        if generator=="Alphanumeric":
            password=ranAlphNum(size)
        else:
            password=ranAll(generator, size)
    print(password)
    return password
            
            
def cryptTest(password, accounts):
    chunksize=64*1024
    iv = ''.join(chr(random.randint(0, 0xF)) for i in range(16))
    iterations = 5000
    key = ''
    salt = os.urandom(64)
    key = PBKDF2(password, salt, dkLen=32, count=iterations)
    #key=key.digest()
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    testEnc=encryptor
    #filesize = os.path.getsize('pas.txt')
    with open('test.enc', 'wb') as testFile:
        testFile.write(encryptor.encrypt(passPhrase))
    with open('pas.enc', 'wb') as outfile:
        outfile.write(struct.pack('<Q'))
        ivencode = iv.encode('utf-8')
        outfile.write(ivencode)
        outfile.write(salt)
        while True:
            chunk=""
            for key in accounts:
                chunk=key+" "+accounts[key]+"\r\n"
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += ' '.encode('utf-8') * (16 - len(chunk) % 16)
            outfile.write(encryptor.encrypt(chunk))
#encrypt_file(key, "pas.txt")
def decrTest(password):
    testPass=False
    chunksize=24*1024
    iterations = 5000
    key = ''
    #key=key.digest()
    with open('pas.enc', 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        salt=infile.read(64)
        key = PBKDF2(password, salt, dkLen=32, count=iterations)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        pasTest=decryptor
        with open('test.enc', 'rb') as testfile:
            while True:
                test=testfile.read(chunksize)
                if len(test)==0:
                    break
                m=pasTest.decrypt(test).decode()
                if m==passPhrase:
                    testPass=True
        print(testPass)
        if testPass:
            with open('testing.txt', 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    all=decryptor.decrypt(chunk).decode().strip()
                    allsep=all.split("\r\n")
                    leng=int(len(allsep)/2)
                    dic={}
                    for x in allsep:
                        v=x.split()
                        dic[v[0]]=v[1]
                #outfile.truncate(origsize)
                return dic

