
# Open the input file and return the file as one string
def read_file(input):
	with open(input, 'r') as f:
		read_data = f.read()

	return read_data

# Returns a list of test cases read in from an input file
def seperate_test_cases(input):
	return read_file(input).splitlines()

# Returns a list of customers from the input data, which is seperated by a semicolon from 
# the product names. We also strip the customer name of leading and trailing spaces
def get_customers(input_data):
	return [ x.strip() for x in input_data[:input_data.find(";")].split(',')]

# Returns a list of products from the input data which is sperated by a simicolon from 
# the customer names (which is in the begining of the string). 
def get_products(input_data):
	return [x.strip() for x in input_data[input_data.find(";") + 1 :].split(',')]

def character_count(string):
	return len(string.strip().replace(" ", "")) if not string == None else None

def is_even(string):
	# we want to not the output since when modding by 2, 0 is even and 1 is odd but 
	# when converting to a boolean, 0 is false and 1 is true.
	return not bool(character_count(string) % 2) if not string == None else None

# Might not be used but could be useful when specifically looking for odd
def is_odd(string):

	return bool(character_count(string) % 2) if not string == None else None


if __name__ == '__main__':
	pass