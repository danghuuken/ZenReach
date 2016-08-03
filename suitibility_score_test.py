import unittest
import magic_sauce
import os

# Set of test to test the functionality of the sutibility score
class SuitibilityScoreTest(unittest.TestCase):
	def setUp(self):
		test_input_file_dir = os.path.join(os.getcwd(), "TestInputFiles")
		self.simple_input = os.path.join(test_input_file_dir, "simple_input.txt")
		self.test_case = magic_sauce.seperate_test_cases(self.simple_input)[0]
		self.customers = magic_sauce.get_customers(self.test_case)
		self.products = magic_sauce.get_products(self.test_case)		

	def tearDown(self):
		# Close any connections to our test file.
		pass

	# Test to count the number of letters in a word
	def test_count_number_of_letters(self):

		self.assertEqual(magic_sauce.character_count("Hello"), 5)
		self.assertEqual(magic_sauce.character_count("1Hello"), 6)
		self.assertEqual(magic_sauce.character_count("Hello 2"), 6)
		self.assertEqual(magic_sauce.character_count("Hello % ^ &"), 8)
		self.assertEqual(magic_sauce.character_count("   "), 0)
		self.assertEqual(magic_sauce.character_count(None), None)

	# Determines if a word is Odd or Even 
	def test_is_number_of_letters_odd_or_even(self):
		
		self.assertEqual(magic_sauce.is_even("Hello"), False)
		self.assertEqual(magic_sauce.is_even("1Hello"), True)
		self.assertEqual(magic_sauce.is_even("Hello 2"), True)
		self.assertEqual(magic_sauce.is_even("Hello % ^ &"), True)
		self.assertEqual(magic_sauce.is_even("\n Hello"), False)
		self.assertEqual(magic_sauce.is_even("   "), True)
		self.assertEqual(magic_sauce.is_even(None), None)

		self.assertEqual(magic_sauce.is_odd("Hello"), True)
		self.assertEqual(magic_sauce.is_odd("1Hello"), False)
		self.assertEqual(magic_sauce.is_odd("Hello 2"), False)
		self.assertEqual(magic_sauce.is_odd("Hello % ^ &"), False)
		self.assertEqual(magic_sauce.is_odd("\n Hello"), True)
		self.assertEqual(magic_sauce.is_odd("   "), False)
		self.assertEqual(magic_sauce.is_odd(None), None)
	
	# Test of a count of number of vowels in a customers name
	def test_count_number_of_vowels(self):
		self.fail('Finish the test')

	# Test of the number of consonants in the customer's name
	def test_number_of_consonants(self):
		self.fail('Finish the test')

	# Test to check if the product # of letters is divisiable with the customers # of leters
	def test_check_if_number_of_letters_are_divisiable(self):
		self.fail('Finish the test')

	# Test to see if the length of customers name is the same as the products name
	def test_two_strings_have_the_same_length(self):
		self.fail('Finish the test')

	# Test to see if both product and customers have are even # of letters
	def test_both_words_have_even_letters(self):
		self.fail('Finish the test')

	# Test to see if both product and customers have odd # of letters
	def test_both_words_have_odd_number_of_letters(self):
		self.fail('Finish the test')

	# Test to see if the # of letters add up to a multiple of 10 
	def test_number_of_letters_in_word_is_multiple_of_10(self):
		self.fail('Finish the test')

	# Test to see if the # of letters add up to a multiple of 5
	def test_number_of_letters_in_word_is_multiple_of_5(self):
		self.fail('Finish the test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')