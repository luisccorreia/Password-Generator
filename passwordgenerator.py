import random
import string

print("Password Generator")

length = int(input("Password lenght - min [14]:\n")) # The user sets the length of the password here.

if length >= 14: # The program checks whether the user's input is '14' or more than '14'.
  
	print("[+] Generating a strong password ...\n")
	
	lower = string.ascii_lowercase # Get ASCII in lower case (i.e: a,b,c,d,e,f,...)
	upper = string.ascii_uppercase # Get ASCII in upper case (i.e: A,B,C,D,E,F,...)
	num = string.digits           # Get ASCII digits: 0123456789
	symbols = string.punctuation   # Get ASCII punctuation: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
		
	combine = lower + upper + num + symbols # Include all into one variable.
		
	mix = random.sample(combine, length) # Shuffles 'combine' variable per user input length given.
  
	pwd = "".join(mix) # Join all items in a tuple into a string, using a quotion mark character as separator
	print("↳" + " " + f"{pwd}") #  The curly braces will be replaced with "pwd" actual value.
  
else: # The program checks if the length is less than '14'.
  
		print("Error password length too short...")
    
    
