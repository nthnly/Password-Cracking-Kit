#importing the MD5 hashing library to hash the randomly generated pasword. 
import hashlib

#Importing random and string libraries to randomly generate strings of desired length.
import random
import string

#importing time library to keep track of how long my program was running for.
import time

#This variable is the length password you want to crack. Change the variable as necessary.
strlength=5

start_time = time.time()
#Function that creates a randomly generated password that is a mixture of letters, numbers, and symbols. The pwbyte variable is the randomly generated string converted into bytes.
def randomstring(strlength):
    pw = string.ascii_letters + string.digits + string.punctuation
    pwfin = '' .join(random.choice(pw) for i in range (strlength))
    pwbyte = bytes(pwfin, 'utf-8')
    return pwbyte

#opens and reads the text file with the hashes of passwords I'm trying to crack
hashtext = open("hashes.txt", "r+")
linereader = hashtext.read().splitlines()
print(linereader)

#Hashed version of the randomly generated string. The while loop exists because we don't know how many times we need to iterate this to crack the password.
i = 0
while i < 50000000000000000000:
    #hashedpw is the MD5 hashed version of the generated password
    hashedpw = hashlib.md5(randomstring(strlength))


    #reads the bytes as a string
    strpws = (str(hashedpw.hexdigest()))

    #checks to see if the generated password matches any string in the list
    if strpws in linereader:
        #prints out what the hashed value of the new password is, and the time it took (in seconds) to crack it.
        print('This is the MD5 hashed value of the generated password: ' + strpws)
        print(" The code took %s seconds to run." % (time.time() - start_time))
        break
    else:
        i = i+1
        






