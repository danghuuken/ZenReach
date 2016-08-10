This repository is used to track and store my coding challenge for Zen Reach. 

This coding challenge is about getting highest SS score to the top Customers.

For this project, I did not use any third party programs. I did not find a reason to use any.

To run the assignment, you'll need to run the main.py. 
Example: python3 main.py --file={File Path}
Example 2: python main.py --file ./TestInputFiles/test_input1.txt

You can also run the tests by running "run_test.sh". At the time of submittion, all the functional test are not complete, due to my lack of prioritizing time. I got to the point where I needed to submit my solution, rather than trying to perfect the code. 

As for my approach, I broke up each of the 3 way we are suppose to evaluate the scores into smaller functions. Each doing a simple task that I can test then using those functions to eventually getting a score together. As you will see, there are a lot of smaller functions that does all the dirty work, and then one evaluation function that will actually calculate the SS score. I did this so that its a lot easier to Unit test, and for me to have a peace of mind that my base functions are functionally correctly. 

As to calculating the max SS, I interpreted the problem as trying to get the Highest SS score you can possible get between the customers and products. So as I was evaluating the score between the customers and products, I wanted to store them into a single list, which I would later sort them by the Score. This would then give me a list of highest score to lowest, and I can then cherry picked the highest score for each product that did not have a common customer that was already picked earlier. This then gave me a list of the highest scores of each product for a customer. Since we are more concerned about the product score rather than the customers individual score. (this is because there might be more customers than products) I was able to limit the size of our final list to the size of the products in the test cases. 
