import math

# Open the input file and return the file as one string
def read_file(input):
	with open(input, 'r') as f:
		read_data = f.read()

	return read_data

# Returns a list of test cases read in from an input file
def seperate_test_cases(input):
	test_cases = []

	for line in read_file(input).splitlines():
		if not line.strip() == "":
			test_cases.append(line)
	return test_cases

# Returns a list of customers from the input data, which is seperated by a semicolon from 
# the product names. We also strip the customer name of leading and trailing spaces
def get_customers(input_data):
	return [ x.strip() for x in input_data[:input_data.find(";")].split(',')]

# Returns a list of products from the input data which is sperated by a simicolon from 
# the customer names (which is in the begining of the string). 
def get_products(input_data):
	return [x.strip() for x in input_data[input_data.find(";") + 1 :].split(',')]

def character_count(String):
	return len(string.strip().replace(" ", "")) if not string == None else None

def letter_count(string):
	if string == None:
		return None

	count = 0 

	for c in string:
		if is_letter(c):
			count += 1
	
	return count

def is_even(string):
	# we want to not the output since when modding by 2, 0 is even and 1 is odd but 
	# when converting to a boolean, 0 is false and 1 is true.
	return not bool(letter_count(string) % 2) if not string == None else None

# Might not be used but could be useful when specifically looking for odd
def is_odd(string):

	return bool(letter_count(string) % 2) if not string == None else None

# Loops through a string and does a character comparison to see if the caracter is one
# of the vowels
def count_vowels(string):
	if string == None:
		return None

	count = 0

	for c in string:
		if c in "AEIOUaeiou":
			count += 1

	return count

def count_consonants(string):
	if string == None:
		return None

	count = 0
	for c in string:
		if not c in "AEIOUaeiou":
			if is_letter(c):
				count += 1

	return count

# fucntion to determine if a character is a letter or not. The function only takes one letter
# so if another letter is given, then itll return false
def is_letter(c):

	if c == None:
		return None

	if len(c) > 1:
		return False
	decimal_value = ord(c.lower())
	if 97 <= decimal_value <= 122:
		return True

	return False

# Takes two words, and counts the letters in each string. then from that number count, we check
# if the numers are divisible of each other. 
def is_divisible(customer, product):
	if customer == None or product == None:
		return None

	num_customer = letter_count(customer)
	num_product = letter_count(product)

	# We cant divide by zero, so if any of the number counts is zero, we want to return false
	if num_product == 0 or num_customer == 0:
		return False

	if num_customer % num_product == 0 or num_product % num_customer == 0:
		return True

	# When doing mods, and tryign to find a number that is common divided number, we want 
	# the larger number to be first
	if num_customer > num_product:
		mod_result = num_customer%num_product
		if not mod_result == 1 and not mod_result == num_customer:
			if num_customer%mod_result == 0 and num_product%mod_result ==0:
				return True
	elif num_product > num_customer:
		mod_result = num_product%num_customer
		if not mod_result == 1 and not mod_result == num_product:
			if num_customer%mod_result == 0 and num_product%mod_result == 0:
				return True

	return False
# Takes two strings, counts the number of letters within the string and then checks to see
# if they have the same amount of letters
def is_same_length(customer, product):
	if customer == None or product == None:
		return None

	if letter_count(customer) == letter_count(product):
		return True

	return False

def is_both_even(customer, product):
	if customer == None or product == None:
		return None

	if is_even(customer) and is_even(product):
		return True

	return False

def is_both_odd(customer, product):
	if customer == None or product == None:
		return None

	if is_odd(customer) and is_odd(product):
		return True

	return False

def same_vowel_count(customer, product):
	if customer == None or product == None:
		return None

	if count_vowels(customer) == count_vowels(product):
		return True

	return False

def same_consonant_count(customer, product):
	if customer == None or product == None:
		return None

	if count_consonants(customer) == count_consonants(product):
		return True

	return False

def num_of_common_factors(customer, product):
	if customer == None or product == None:
		return None

	count = 0 

	if is_same_length(customer,product):
		count += 1

	if is_both_odd(customer, product):
		count += 1

	if is_divisible(customer, product):
		count += 1

	if  same_vowel_count(customer,product):
		count += 1

	if  same_consonant_count(customer,product):
		count += 1

	return count


def single_SS_eval(customer, product):
	if customer == None or product == None:
		return None

	SS = 0

	# Takes care the first part of the algorithm
	if is_even(product):
		SS = count_vowels(customer) * 1.5
	# Takes care of the second part of the algorithm
	elif is_odd(product):
		SS = count_consonants(customer)

	number_common = num_of_common_factors(customer,product)

	SS = SS * math.pow(1.5, float(number_common))

	return SS

def eval_test(test_case):
	# Get list of customers
	customers = get_customers(test_case)

	# Get list of products
	products = get_products(test_case)

	highest_score = 0

	#Pass in file string into single SS calculator
	for customer in customers:
		for product in products:
			score = single_SS_eval(customer, product)

			if score > highest_score: 
				highest_score = score

	return highest_score

if __name__ == '__main__':
	pass