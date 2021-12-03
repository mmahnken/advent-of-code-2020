"""Notes on this solution

I had circled around versions of using the consistent 
addition between working multiples and using lcm calculate
how to jump ahead, but I couldn't get the math to work on
my own.

Was looking on reddit and found this comment, which helped
unlock how to join the various ideas I had been trying to 
put together. 

https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/

"""

from helpers import *
import advent


def loop_quickly(buses):
	lines = [line for line in buses]
	first = lines[0]
	rest = lines[1:]

	jump_ahead_num = first
	t = first

	for line in rest:
		print(f"t {t}, jump ahead num {jump_ahead_num}")
		# input('press enter to continue')
		t = find_next_alignment(line, buses[line], jump_ahead_num, t)
		# jump_ahead_num = lcm(jump_ahead_num, line)
		jump_ahead_num *= line  # this works bc all numbers are prime
	return t



def find_next_alignment(current_num, offset, jump_ahead_num, t):
	print('finding next alignment')
	while True:
		

		# loop by lcm 
		if (t + offset) % current_num == 0:
			return t
		else:
			t += jump_ahead_num


if __name__ == "__main__":
	buses, _ = advent.process("input.txt", part2=True)
	buses = advent.setup(buses)
	print(f"the answer {loop_quickly(buses)}")
