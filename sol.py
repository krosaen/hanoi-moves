"""
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

NOTE: You need to write the full code taking all inputs are from stdin and outputs to stdout

"""

import fileinput



def main():
	n, k, start, goal = parseinput()

	print start
	print goal

	pegstate = transform_to_pegs(start, k)

	print pegstate

	print list(candidate_moves(pegstate))


	moves = solve(pegstate, goal)
	print len(moves)
	for start, end in moves:
		print "%s %s" % (start, end)

def transform_to_pegs(rep, k):
	"""
	rep: [int, int, ...] 
		Each integer is in the range 0 to K-1 where the i-th integer denotes the peg to which disc of radius i is present in the initial configuration.
	returns: [[], ...]
		Each list represents radiuses on pegs. Transforms to zero
		based offsets.
	"""
	result = [[] for i in xrange(k)]
	for r, pos in reversed(list(enumerate(rep))):
		result[pos].append(r)
	return result


observed_moves = set()

def hash_pegstate(pegstate):
	return hash(tuple([tuple(peg) for peg in pegstate]))

def make_move(pegstate, goal, moves, depth = 0):
	print "make_move%s(%s, %s, %s)" % (depth, pegstate, goal, moves)
	if solved(pegstate, goal):
		print "solved!! moves = %s" % moves
		return True

	global observed_moves
	observed_moves.add(hash_pegstate(pegstate))
	for start, end in candidate_moves(pegstate):
		print "candidate: %s, %s for %s" % (start, end, pegstate)
		next_state = apply_move(pegstate, start, end)
		if hash_pegstate(next_state) in observed_moves:
			print "skipping"
			continue
		result = make_move(
			next_state,
			goal,
			moves + [(start, end)],
			depth + 1)
		if result:
			return result
	return False

def solved(pegstate, goal):
	for r, pos in enumerate(goal):
		if r not in pegstate[pos]:
			return False
	return True

def top_of_pegs(pegstate):
	for i, peg in enumerate(pegstate):
		if len(peg):
			yield i, peg[-1]


def candidate_moves(pegstate):
	for i, top_r in top_of_pegs(pegstate):
		for j, peg in enumerate(pegstate):
			if i != j and (len(peg) == 0 or top_r < peg[-1]):
				yield (i, j)

def apply_move(pegstate, start, end):
	result = [peg[:] for peg in pegstate]
	result[end].append(result[start].pop())
	return result


def solve(pegstate, goal):
	moves = []
	make_move(pegstate, goal, moves)
	print "solved moves: %s" % moves
	return moves


def parseinput():
	thein = fileinput.input()
	n, k = map(int, thein.next().split())
	start = map(lambda el: int(el) - 1, thein.next().split())
	goal = map(lambda el: int(el) - 1, thein.next().split())
	return n, k, start, goal



main()