# Python v3.7.2

import hashlib
from itertools import product
import string
import time

LETTERS_LIST = list(string.ascii_lowercase + string.ascii_uppercase)

def brute_force_pswd(pswd, min_len, max_len):
	for letters_of_pswd in (min_len, max_len):
		for c in product(LETTERS_LIST, repeat = letters_of_pswd):
			myVar = hashlib.sha256((PASSWORD + ''.join(c)).encode('utf-8')).hexdigest()
			if (int(myVar, 16) == int(0x7d9eb5ee94f9ca95d640eb79cc8766fe44d5b9744602469fc6bdc748cb3c41f5)):
				return True, ''.join(c)
	return False, ''

if __name__ == "__main__":
	PASSWORD = "blockchain-course.org:"
	MIN_PSWD_LEN = 1
	MAX_PSWD_LEN = 5
	
	start = time.time()
	broken, c = brute_force_pswd(PASSWORD, MIN_PSWD_LEN, MAX_PSWD_LEN)
	end = time.time()
	if broken:
		print(f"Success!\n{c}, {PASSWORD}{c}")
	else:
		print("Password not found!")
	print(f"Brute force time: {end-start} seconds")
