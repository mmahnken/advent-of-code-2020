"""

Day 3


You start on the open square (.) in the top-left corner and need to 
reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a 
cheaper model that prefers rational numbers); start by counting all the 
trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 
3 and down 1. Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map.


Starting at the top-left corner of your map and following a slope of 
right 3 and down 1, how many trees would you encounter?

Part 2

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

"""



def process(filename, x_slope, y_slope):
	f = open(filename)

	x_pos = 0
	y_pos = y_slope   # always count the first row
	num_trees = 0

	for i, line in enumerate(f):
		# import pdb; pdb.set_trace()

		if y_pos != y_slope:   # if this row should not count
			y_pos += 1
			continue
		else:				   # this row should count
			y_pos = 0

		line = line.strip()
		
		if (x_pos) >= len(line):
			last_x = x_pos - x_slope
			left_in_line = len(line) - (x_pos - x_slope)

			# print('    end of line,', left_in_line, "left in line")
			x_pos = x_slope - left_in_line

		# print('checking character', x_pos, "in line", i+1 )
		if line[x_pos] == "#":
			# print('tree found')
			num_trees += 1


		x_pos += x_slope
		y_pos += 1

	return num_trees




result1 = process("input.txt", 1, 1)
print("result1", result1)

result2 = process("input.txt", 3, 1)  # part 1
print("result2", result2)

result3 = process("input.txt", 5, 1)
print("result3", result3)

result4 = process("input.txt", 7, 1)
print("result4", result4)

result5 = process("input.txt", 1, 2)
print("result5", result5)

print("part 2: ", result1 * result2 * result3 * result4 * result5)

			
		


		