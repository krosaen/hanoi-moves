# Hanoi Moves Solution

[Interview Street](https://www.interviewstreet.com) has a sample problem called 'Hanoi Moves'. 
While I couldn't solve it in the allotted hour (let alone even starting the other 2 questions that were part
of the sample test), it was a fun problem to play with.

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

## Full Problem Description

There are K pegs. Each peg can hold discs in decreasing order of radius when looked from bottom to top of the peg. There are N discs which have radius 1 to N; Given the initial configuration of the pegs and the final configuration of the pegs, output the moves required to transform from the initial to final configuration. You are required to do the transformations in minimal number of moves.

A move consists of picking the topmost disc of any one of the pegs and placing it on top of anyother peg.
At anypoint of time, the decreasing radius property of all the pegs must be maintained.

Constraints:
	1<= N<=8
	3<= K<=5


Input Format:

N K

2nd line contains N integers.
Each integer in the second line is in the range 1 to K where the i-th integer denotes the peg to which disc of radius i is present in the initial configuration.
3rd line denotes the final configuration in a format similar to the initial configuration.


Output Format:
The first line contains M - The minimal number of moves required to complete the transformation.
The following M lines describe a move, by a peg number to pick from and a peg number to place on.
If there are more than one solutions, it's sufficient to output any one of them. You can assume, there is always a solution with less than 7 moves and the initial confirguration will not be same as the final one.

Sample Input #00:

 
	2 3
	1 1
	2 2

Sample Output #00:
 
	3
	1 3
	1 2
	3 2

Sample Input #01:

	6 4
	4 2 4 3 1 1
	1 1 1 1 1 1

Sample Output #01:

	5
	3 1
	4 3
	4 1
	2 1
	3 1
