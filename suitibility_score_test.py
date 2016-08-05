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

		self.assertEqual(magic_sauce.letter_count("Hello"), 5)
		self.assertEqual(magic_sauce.letter_count("1Hello"), 5)
		self.assertEqual(magic_sauce.letter_count("Hello 2"), 5)
		self.assertEqual(magic_sauce.letter_count("Hello % ^ &"), 5)
		self.assertEqual(magic_sauce.letter_count("   "), 0)
		self.assertEqual(magic_sauce.letter_count(None), None)

	# Determines if a word is Odd or Even 
	def test_is_number_of_letters_odd_or_even(self):
		
		self.assertEqual(magic_sauce.is_even("Hello"), False)
		self.assertEqual(magic_sauce.is_even("1HelloO"), True)
		self.assertEqual(magic_sauce.is_even("Helloa 2"), True)
		self.assertEqual(magic_sauce.is_even("HelloW % ^ &"), True)
		self.assertEqual(magic_sauce.is_even("\n Hello"), False)
		self.assertEqual(magic_sauce.is_even("   "), True)
		self.assertEqual(magic_sauce.is_even(None), None)

		self.assertEqual(magic_sauce.is_odd("Hello"), True)
		self.assertEqual(magic_sauce.is_odd("1HelloO"), False)
		self.assertEqual(magic_sauce.is_odd("Helloa 2"), False)
		self.assertEqual(magic_sauce.is_odd("HelloW % ^ &"), False)
		self.assertEqual(magic_sauce.is_odd("\n Hello"), True)
		self.assertEqual(magic_sauce.is_odd("   "), False)
		self.assertEqual(magic_sauce.is_odd(None), None)
	
	# Test of a count of number of vowels in a customers name
	def test_count_number_of_vowels(self):
		
		self.assertEqual(magic_sauce.count_vowels("COOEEING"), 5)
		self.assertEqual(magic_sauce.count_vowels("HellO"), 2)
		self.assertEqual(magic_sauce.count_vowels("SYMPHYSY"), 0)
		self.assertEqual(magic_sauce.count_vowels(""), 0)
		self.assertEqual(magic_sauce.count_vowels(None), None)
		self.assertEqual(magic_sauce.count_vowels("Wonderful World!@$%$"), 4)

	# Test of the number of consonants in the customer's name
	def test_number_of_consonants(self):

		self.assertEqual(magic_sauce.count_consonants("COOEEING"), 3)
		self.assertEqual(magic_sauce.count_consonants("HellO"), 3)
		self.assertEqual(magic_sauce.count_consonants("SYMPHYSY"), 8)
		self.assertEqual(magic_sauce.count_consonants(""), 0)
		self.assertEqual(magic_sauce.count_consonants(None), None)
		self.assertEqual(magic_sauce.count_consonants("Wonderful World!@$%$"), 10)

	# Test to check if the products # of letters is divisiable with the customers # of leters
	# or viceversa 
	def test_check_if_number_of_letters_are_divisiable(self):
		self.assertEqual(magic_sauce.is_divisible("abcd", 'ab'), True)
		self.assertEqual(magic_sauce.is_divisible("45abcd32","34ab56"), True)
		self.assertEqual(magic_sauce.is_divisible("ab - ed", "a -- b"), True)
		self.assertEqual(magic_sauce.is_divisible("qqwert yuiop asdfg", "asdfg"), True)
		self.assertEqual(magic_sauce.is_divisible("1234543 - a", "asfwladva12323"), True)
		self.assertEqual(magic_sauce.is_divisible("asdf", "as"), False)
		self.assertEqual(magic_sauce.is_divisible("as!@#df", "a!@#s"), False)
		self.assertEqual(magic_sauce.is_divisible("as!@#df", None), None)
		self.assertEqual(magic_sauce.is_divisible(None, "a!@#s"), None)


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

	# Testing to see if a specific character is a letter or not. 
	def test_if_letter(self):

		self.assertEqual(magic_sauce.is_letter('a'), True)
		self.assertEqual(magic_sauce.is_letter('z'), True)
		self.assertEqual(magic_sauce.is_letter('A'), True)
		self.assertEqual(magic_sauce.is_letter('Z'), True)
		self.assertEqual(magic_sauce.is_letter('e'), True)
		self.assertEqual(magic_sauce.is_letter('x'), True)
		self.assertEqual(magic_sauce.is_letter('4d'), False)
		self.assertEqual(magic_sauce.is_letter('4'), False)
		self.assertEqual(magic_sauce.is_letter('SD'), False)
		self.assertEqual(magic_sauce.is_letter('sF'), False)
		self.assertEqual(magic_sauce.is_letter('^'), False)
		self.assertEqual(magic_sauce.is_letter('Q'), True)
		self.assertEqual(magic_sauce.is_letter(')'), False)
		self.assertEqual(magic_sauce.is_letter('!'), False)
		self.assertEqual(magic_sauce.is_letter(None), None)


if __name__ == '__main__':
	unittest.main(warnings='ignore')