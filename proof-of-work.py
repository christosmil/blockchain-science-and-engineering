# Python v3.7.2

import hashlib
from itertools import product
import string
import time

LETTERS_LIST = list(string.ascii_lowercase + string.ascii_uppercase)

def proof_of_work(pswd, min_len, max_len):
	for letters_of_pswd in (min_len, max_len):
		for c in product(LETTERS_LIST, repeat = letters_of_pswd): 
			my_var = hashlib.sha256((pswd+''.join(c)).encode('utf-8')).hexdigest()[:5]
			if (int(my_var, 16) == int(0x0000)):
				return True, ''.join(c), (hashlib.sha256((pswd+''.join(c)).encode('utf-8')).hexdigest())
	return False, '', ''

if __name__ == "__main__":
	PASSWORD = "blockchain-course.org:78"
	MIN_PSWD_LEN = 1
	MAX_PSWD_LEN = 5
	
	start = time.time()
	proof_ow, c, full_hash = proof_of_work(PASSWORD, MIN_PSWD_LEN, MAX_PSWD_LEN)
	end = time.time()
	if proof_ow:
		print(f"Proof-of-Work succeed!\n{c}, {PASSWORD}{c}, {full_hash}")
	else:
		print("Proof-of-Work failed!")
	print(f"PoW time: {end-start} seconds")
