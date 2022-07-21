# Python v3.7.2

import string

def calculate_decimal_sum(list_of_characters):
	decimal_sum = 0
	for i in range(len(list_of_characters)):
		decimal_sum += int(ord(list_of_characters[i])*pow(2, (len(list_of_characters) - 1 - i)*8))
	return decimal_sum

def create_base_58_alphabet():
	base_58_characters = list(range(1,10)) + list(string.ascii_uppercase + string.ascii_lowercase)
	base_58_characters.remove("I")
	base_58_characters.remove("O")
	base_58_characters.remove("l")
	return base_58_characters

def convert_to_base_58(string_to_be_converted):
	list_of_characters = list(string_to_be_converted)
	decimal_sum = calculate_decimal_sum(list_of_characters)
	
	base_58_alphabet = create_base_58_alphabet()
	
	list_of_remainders = []
	while (decimal_sum/58 != 0):
		list_of_remainders.append(decimal_sum%58)
		decimal_sum //= 58
	list_of_remainders.append(decimal_sum%58)
	
	list_of_base_58 = []
	for item in list_of_remainders:
		list_of_base_58.append(str(base_58_alphabet[item]))
	list_of_base_58.pop()
	return ''.join(list_of_base_58[::-1])

if __name__ == "__main__":
	string_to_be_converted = input("Enter a string to be converted to base 58: ")
	base_58_representation = convert_to_base_58(string_to_be_converted)
	print(f'Base-58 representation: {base_58_representation}')
