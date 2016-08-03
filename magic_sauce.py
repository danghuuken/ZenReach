
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

if __name__ == '__main__':
	pass