'''
 Assignment 5_1
 Discrription - Write a program that asks the user to 
 imput a string and convers it to Morse code
 Department, Job Title pass it to a list
 Programming in Python 
 Submitted by - William Songer
 Course - COSC 2348 Introduction to Scripting
 Instructor - Adarsh Kesireddy

Work Cited:
Author: Tony Gaddis
Title: Starting Out with Python (5th Edition)

'''
n = input("type in text to be coverted to morse code: ")
value = (n)
string = value.upper()

Morse_code = {' ': '|', "'": '.----.','(': '-.--.-',')': '-.--.-',',': '--..--','-': '-....-','.': '.-.-.-',
              '/': '-..-.','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....', 
              '6': '-....','7': '--...','8': '---..','9': '----.',':': '---...',';': '-.-.-.','?': '..--..',
              'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....', 
    	      'I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.',
    	      'Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-', 
	          'Y': '-.--','Z': '--..','_': '..--.-'} 
	          
for element in range(0, len(string)):
    print(Morse_code.get(string[element]), end='')
