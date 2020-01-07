from myascii import *

#Directions
def generalRules():
  print ('Welcome to the CoE Security CTF')
  printEscapeRoom()
  print ('Rules:')
  print ('* Do NOT close this window!')
  print ("* Do NOT search this machines file system!")
  print ('* Do NOT write down or share any passwords.')
  print ('* Do NOT leave your seat until your time is up!')
  print ('* Do search the \'Ikes Document\' folder only!')
  print ('* After each level, please notify a CoE Presenter.')
  print ('* After each level, please return each prop to its original position and location.')
  print ('* Each prop will only be used once.')
  print ('* Using Google is allowed and encouraged.')
  print ('* You will be allowed to ask for only \'3\' hints. \n')

def lvl1Directions(numOfTries):
  print ('Welcome to level 1')
  print ('You have', numOfTries, 'attempts to guess Tom\'s password. \n')
  print ('Hints:') 
  print ('* Tom\'s password is 6 numeric characters long.')
  print ('* Tom\'s password can be guessed by looking at the surrounding area for clues.')
  print ('* Tom can hardly use a computer.')
  print ('* Tom\'s password is most likely a top ten commonly used password.')
  print ('* Feel free to use google if you cannot find the clue')

def lvl2Directions(numOfTries):
  print ('Welcome to level 2')
  print ('You have', numOfTries, 'attempts to guess Camila\'s password. \n')
  print ('Hints:') 
  print ('* Camila\'s password is 5 to 8 alpha-numeric characters long.')
  print ('* Camila\'s password can be guessed by looking at the surrounding area for clues.')
  print ('* Camila only uses a computer to check email and view videos on youtube.')
  print ('* Camila LOVES her pets.')
  print ('* Camila usually creates her passwords in the following format: Name + 2 digit year')

def lvl3Directions(numOfTries):
  print ('Welcome to level 3')
  print ('You have', numOfTries, 'attempts to guess Ike\'s password. \n')
  print ('Hints:') 
  print ('* Ike\'s password is 16 alpha-numeric characters long.')
  print ('* Ike\'s password can be guessed by searching the \'Ikes Documents\' folder on the desktop.')
  print ('* Ike is a first year cyber security student right out of high school.')
  print ('* Ike has recently learned about steganography.')
  print ('* Steganography is the practice of concealing messages or information within other nonsecret text or data, LIKE A PICTURE.')
  print ('* Ike loves action movies, cars, and science fiction.')
  print ('* Use default settings and NO passwords when decoding.')
  print ('* Chrome may have a bookmark that may be handy.')

def lvl4Directions(numOfTries):
  print ('Welcome to level 4')
  print ('You have', numOfTries, 'attempts to guess the password.')
  print ("Hashes play a role in security systems where they're used to ensure that transmitted messages have not been tampered with. The sender generates a hash of the message, encrypts it, and sends it with the message itself.") 
  print ('Hints:') 
  print ('* The password can be guessed by looking at the surrounding area for clues.')
  print ('Locate box 1. In the box will contain the password for this challenge.\n')
  print ("The combination to open the lock on the box can be found by getting the last 4 digits of a certain 'SHA256 hash'.")
  print ("* The hash is a number generated from a string of text.")
  print ('* Please keep in mind the spelling of the string of text, as it can change the hash drastically.')
  print ('* Chrome may have a bookmark that may be handy.')
  print ('* Dont look so \'puzzled\', my favorite color is red.')

def lvl5Directions(numOfTries):
  print ('Welcome to level 5')
  print ('You have', numOfTries, 'attempts to guess the password. \n')
  print ('You have 1 minutes to pick the lock and retrieve the password from a CoE Presenter. \n')
  print ('Hints:') 
  print ("* Quick tutorial: https://youtu.be/H8UF6lY-jo4?t=110")
  print ('* If you cant pick the lock there is a hint for the password, somewhere.')

