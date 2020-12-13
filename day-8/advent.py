"""
Day 8
"""

from copy import copy

def process(filename):
	f = open(filename)

	directions = []

	for line in f:
		line = line.strip().split()
		
		keyword = line[0]
		num = int(line[1])
		directions.append((keyword, num))

	return directions


def run_code(directions):
	import pdb; pdb.set_trace()
	lines_ran = set()

	accumulator = 0
	i = 0

	while i != len(directions):
		# if i in lines_ran:
		# 	break

		print(f'running {i}')
		lines_ran.add(i)

		keyword, num = directions[i]
		
		if keyword == "nop":
			i += 1
			continue
		elif keyword == "acc":
			accumulator += num
			i += 1
		elif keyword == "jmp":
			i += num

	return accumulator


def is_natural_end(directions):
	lines_ran = set()

	accumulator = 0
	i = 0
	print('simulating code run')
	while i != len(directions)-1:
		if i in lines_ran:
			return False

		print(f'running {i}, {directions[i]}')
		lines_ran.add(i)

		keyword, num = directions[i]
		
		if keyword == "nop":
			i += 1
			continue
		elif keyword == "acc":
			accumulator += num
			i += 1
		elif keyword == "jmp":
			i += num

	return True


def fix_corrupted_code(directions):
	i = 0

	for d in directions:
		print(f'checking {i} --- {d}')
		keyword, num = d
		
		if keyword == "nop":
			print('change to jmp', i)
			directions_copy = copy(directions)
			directions_copy[i] = ("jmp", num)
			if is_natural_end(directions_copy):
				print('   found natural end!')
				return run_code(directions_copy)
			else:
				print('   no natural end')

		elif keyword == "jmp":
			print('change to nop', i)
			directions_copy = copy(directions)
			directions_copy[i] = ("nop", num)
			# import pdb; pdb.set_trace()
			if is_natural_end(directions_copy):
				print('   found natural end!')

				return run_code(directions_copy)
			else:
				print('   no natural end')				

		i += 1




d = process("input.txt")
a = fix_corrupted_code(d)
print(f"answer {a}")

