
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Consider the natural numbers laid out in a square spiral, with 1 occupying the center of the spiral.

This spiral has several interesting features. The southeast diagonal has several prime numbers (3, 13, 31, 57, and 91) along it. The southwest diagonal has a weaker concentration of prime numbers (5, 17, 37) along it. 

To construct the spiral we start with 1 at the center, with 2 to the right, and 3 below it, 4 to the left, and so on. A part of the problem for this assignment is to figure out the rule to fill the spiral for an arbitrary size. Once you have that rule you can complete the rest of the assignment. 

In this assignment your task is to implement a python program with the name Spiral.py.

You program should have the following input and output

Input:

You will read your input data from a file called spiral.in. The format of the file will be as follows:

11
1
42
110
91

The first line will be the dimension of the spiral. It will always be odd and greater than 1 and less than 100. This will be followed by an arbitrary number of lines. There will be a single number on each line. These numbers will be numbers inside the spiral. Some of these numbers will be interior numbers, others will be numbers on the edge, and yet others will be numbers at the corners of the spirals. Assume that the input file that we will be testing your program will be valid.

Output:

For each of the numbers inside the spiral, your output will be the sum of all the numbers adjacent to this number, but not including this number.

For the above input file you will output on the console:

44
382
477
239

We get 44 by adding the numbers adjacent to 1 (2 + 3 + 4 + 5 + 6 + 7 + 8 + 9). Similarly we get 239 by
adding the numbers adjacent to 91 (57 + 90 + 92).

You will read your input from stdin like so:

	Mac:
	python3 Spiral.py < spiral.in

	Windows:
	python Spiral.py < spiral.in


We will use our own input file to test your program. You must read the input in the format described
above.

Once you read the first line from the input file you will create a 2-D list with the spiral of numbers. Then from the 2-D list you will obtain the sum of adjacent numbers for a given number in the spiral and print it. The number of lines of input will be arbitrary and greater than 1.
