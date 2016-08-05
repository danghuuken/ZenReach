import unittest
import magic_sauce
import os

class HighestSuitibilityScoreTest(unittest.TestCase):
	
	# Read in test input file
	def setUp(self):
		test_input_file_dir = os.path.join(os.getcwd(), "TestInputFiles")
		self.simple_customer_input = os.path.join(test_input_file_dir, "simple_customer_input.txt")
		self.test_input_1 = os.path.join(test_input_file_dir, "test_input1.txt")

	def tearDown(self):
		pass

	def test_taking_input_file_and_return_highest_SS_score_per_case(self):

		#loop through the amount of test cases there are 
		for test_case in magic_sauce.seperate_test_cases(self.test_input_1):

			print("{0:.2f}".format(magic_sauce.eval_test(test_case)))

		self.fail('Finish functional test')

	# A Test to take in a simple input file of one customer and 3 products, and seeing what 
	# product has the highest score for the customer.
	def test_one_customer_and_three_products(self):
		#read in the file.
		file_data = magic_sauce.read_file(self.simple_customer_input)
		
		# Get list of customers
		customers = magic_sauce.get_customers(file_data)

		# Get list of products
		products = magic_sauce.get_products(file_data)

		highest_score = 0

		#Pass in file string into single SS calculator
		for customer in customers:
			for product in products:
				score = magic_sauce.single_SS_eval(customer, product)

				if score > highest_score: 
					highest_score = score

		# return the highest score
		print(highest_score)



if __name__ == '__main__':
	unittest.main(warnings='ignore')