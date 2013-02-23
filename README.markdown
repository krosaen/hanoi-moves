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