# Hanoi Moves Solution

[Interview Street](https://www.interviewstreet.com) has a sample problem called 'Hanoi Moves'. 
While I couldn't solve it in the allotted hour (let alone even starting the other 2 questions that were part
of the sample test), it was a fun problem to play with.

See the top of `sol.py` for a full description of the problem and the txt files for
some sample inputs and outputs.

The first attempt was a depth first traversal of the search space, and it didn't work (blew the stack
even for the simple input00.txt).

Next, I tried breadth first search combined with a hashlookup to avoid duplicate visits,
and that worked for both sample inputs, but was slow (800 visits for input01.txt).

Finally, I remembered the best first search from school (EECS 543!) and put that into practice, estimating
the number of moves to the goal for the cost function. This results in a solution visiting only
6 possible configurations before settling on the goal.

Here's a trace of the solution to input01.txt:

	$ python2.7 sol.py < input01.txt 
	INFO:root:6, 4
	INFO:root:[3, 1, 3, 2, 0, 0]
	INFO:root:[0, 0, 0, 0, 0, 0]
	INFO:root:[[5, 4], [1], [3], [2, 0]] via None->None (0 moves so far, 0 candidates under consideration)
	INFO:root:[[5, 4, 3], [1], [], [2, 0]] via 2->0 (1 moves so far, 5 candidates under consideration)
	INFO:root:[[5, 4, 3], [1], [0], [2]] via 3->2 (2 moves so far, 10 candidates under consideration)
	INFO:root:[[5, 4, 3, 2], [1], [0], []] via 3->0 (3 moves so far, 15 candidates under consideration)
	INFO:root:[[5, 4, 3, 2, 1], [], [0], []] via 1->0 (4 moves so far, 20 candidates under consideration)
	INFO:root:[[5, 4, 3, 2, 1, 0], [], [], []] via 2->0 (5 moves so far, 24 candidates under consideration)
	5
	3 1
	4 3
	4 1
	2 1
	3 1
