import magic_sauce
import argparse


parser = argparse.ArgumentParser(description="Lets fine the most optimum product for a customer")
parser.add_argument("--file", required=True)

if __name__ == '__main__':
	args = parser.parse_args()
	test_cases = magic_sauce.seperate_test_cases(args.file)

	print("Test cases have loaded, and found " + str(len(test_cases))  + " tests.\n\n")

	test_counter = 1

	for test_case in test_cases:
		print("Test Case #" + str(test_counter))
		evaluation = magic_sauce.eval_test(test_case)
		print("Overall Score is: {0:.2f}".format(evaluation[0]))
		print("\nHere is the list of top scores: ")
		print(evaluation[1])
		print ("\n")
		test_counter += 1