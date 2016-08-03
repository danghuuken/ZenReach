import unittest
import os
import magic_sauce

# Test to make sure we are able to read the input file and parse the product and customer data correctly
class FileReaderTest(unittest.TestCase):


	# Setts up input file to read
	def setUp(self):
		test_input_file_dir = os.path.join(os.getcwd(), "TestInputFiles")
		self.text_input1 = os.path.join(os.getcwd(), "test_input1.txt")
		self.simple_read_file = os.path.join(test_input_file_dir, "simple_read_file.txt")
		self.simple_line_segment = os.path.join(test_input_file_dir, "simple_line_segment.txt")
		self.simple_input = os.path.join(test_input_file_dir, "simple_input.txt")


	# Closes and file connections that are open
	def tearDown(self):
		pass


	# Test to see if we are able to open up a file.
	def test_open_file(self):
		# Read in the file and return out the string content of file
		file_content = magic_sauce.read_file(self.simple_read_file)

		# Verify that the file isnt null
		self.assertNotEqual(file_content, None)


	# Test to make sure we can read contents of the file.
	def test_read_file(self):
		file_content = magic_sauce.read_file(self.simple_read_file)

		self.assertEqual(file_content,"test")

	# Test to seperate file into new line segments.
	def test_seperate_new_line_segments(self):
		
		file_segments = magic_sauce.seperate_test_cases(self.simple_line_segment)

		self.assertEqual(len(file_segments), 6)
		self.assertEqual(file_segments[0], "One")
		self.assertEqual(file_segments[1], "Two")
		self.assertEqual(file_segments[2], "Three")
		# Testing to make sure spaces are kept
		self.assertEqual(file_segments[3], "Four 4")
		# making sure ending spaces are kept
		self.assertEqual(file_segments[4], "Five V  ")
		self.assertEqual(file_segments[5], "Six ^")

	# Test to see if we can get a list of customers.
	def test_extract_list_of_customers(self):
		test_case = magic_sauce.seperate_test_cases(self.simple_input)[0]
		customers = magic_sauce.get_customers(test_case)

		self.assertEqual(len(customers), 4)

	# Test to see if we can seperate individual customers.
	#Jack Abraham,John Evans,Ted Dziuba
	def test_extract_individual_customers(self):
		test_case = magic_sauce.seperate_test_cases(self.simple_input)[0]
		customers = magic_sauce.get_customers(test_case)

		self.assertNotEqual(customers[0], "Jack Abraham,")
		self.assertEqual(customers[1], "John Evans")
		# Testing to make sure we remove all white spaces
		self.assertEqual(customers[2],"Ted Dziuba")
		# making sure leading white spaces are removed
		self.assertEqual(customers[3],"Kent Daniels")

	# Test to verify that we can get a list of products.
	def test_extract_list_of_products(self):
		test_case = magic_sauce.seperate_test_cases(self.simple_input)[0]
		products = magic_sauce.get_products(test_case)

		self.assertEqual(len(products), 3)

	# Test to see if we can seperate products individually.
	#iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow 
	def test_extract_individual_products(self):
		test_case = magic_sauce.seperate_test_cases(self.simple_input)[0]
		products = magic_sauce.get_products(test_case)

		self.assertEqual(products[0], "iPad 2 - 4-pack")
		self.assertEqual(products[1], "Girl Scouts Thin Mints")
		self.assertEqual(products[2], "Nerf Crossbow")

if __name__ == '__main__':
	unittest.main(warnings='ignore')