#!/bin/python

import random



def generator():
	password=""
	identifier="none"
	identifier = input("Please enter the website associated with the password. Default is none")
	var = input("Please enter a positive integer for password length: ")
	y = int(var)
	for x in range(y):
		tell=random.randint(1,3)
		let =ranAlphNum()
		password=password+""+let
	with open("pass.txt", "a") as textfile:
		textfile.write(identifier +" " +password+"\n")	
def firstLast(): #only generates letters
	tell=random.randint(1,2)
	if tell==1:
		let=chr(random.randint(65,90))
	elif tell==2:
		let=chr(random.randint(97,122))
def ranAlphNum(): #generates letters and numbers
	tell=random.randint(1,3)
	if tell==1:
		let=chr(random.randint(48,57))
	elif tell==2:
		let=chr(random.randint(65,90))
	elif tell==3:
		let=chr(random.randint(97,122))
	return let
def ranAll(special): #generates letters, numbers, special characters
	if special==1: #does not use some special characters
		tell=random.randint(1,3)
		if tell==1:
			let=chr(random.randint(33,57))
		elif tell==2:
			let=chr(random.randint(65,90))
		elif tell==3:
			let=chr(random.randint(97,122))
	elif special==2: #uses all special characters for password
		let=chr(random.randint(33,126))
	tell=random.randint(1,3)
	return let
def reader():
	print ("Your Passwords are:")
	with open("pass.txt", "r") as textfile:
		print (textfile.read())

class runProj():	
	print ("Please enter the letter 'r' if you want to read your passwords")
	print ("enter the letter 'g' if you want to generate them")
	var = input()
	if var=="g":
		generator()
	elif var=="r":
		reader()
