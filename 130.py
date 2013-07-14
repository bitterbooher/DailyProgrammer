#Daily Programmer 130
#Roll The Die
#NdM -> Listof Numbers
#
from random import randrange
# rolldie(2d20) -> 19 7
# rolldie(4d6) -> 5 3 4 6
# first component is the number of die
# second component is the range of possible random numbers

def rolldie(ndm):
	rolls, sides = ndm.split('d')

	for rolls in range(int(rolls)):
		print randrange(1, int(sides))

rolldie("2d30")


def roll(d_str):
    import random

    num, size = map(int, d_str.split('d'))[:2] # cast them as int, iterable is a sequence of split objects
    face_values = range(1, size+1) # why size + 1, unless its counting from 0
    rolls = [str(random.choice(face_values)) for i in xrange(num)]
    print(' '.join(rolls))

roll("2d30")