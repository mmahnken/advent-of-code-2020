

class LLNode:

	def __init__(self, data, next=None, previous=None):
		self.data = data

		self.next = next
		self.previous = previous



def get_direction(current_direction, action, units):
	"""Given current direction and a token like R180, return next direction.


	>>> get_direction('N', 'R180')
	'S'

	>>> get_direction('W', 'L270')
	'N'

	"""

	steps = int(units/90)

	# set up circular array
	north = LLNode('N')
	south = LLNode('S')
	west = LLNode('W', previous=south, next=north)
	east = LLNode('E', next=south, previous=north)
	north.next = east
	north.previous = west
	south.next = west
	south.previous = east


	nodes = {'N': north, 'S': south, 'E': east, 'W': west}

	current = nodes[current_direction]
	for i in range(steps):
		if action == "L":
			current = current.previous
		else:
			current = current.next

	return current.data


def move(current_coords, direction, units):

	if direction == "N":
		current_coords[0] += units

	elif direction == "S":
		current_coords[0] -= units


	elif direction == "E":
		current_coords[1] += units

	elif direction == "W":
		current_coords[1] -= units

	return current_coords


def process(filename):
	f = open(filename)


	current_direction = "E"

	current_coords = [0, 0]

	for line in f:
		line = line.strip()
		
		action = line[0] 
		units = int(line[1:])

		if action in ["L", "R"]:
			# change direction!
			current_direction = get_direction(current_direction, action, units)

		elif action in ["N", "W", "E", "S"]:
			current_coords = move(current_coords, action, units)


		elif action == "F":
			current_coords = move(current_coords, current_direction, units)

	
	return abs(current_coords[0]) + abs(current_coords[1])


if __name__ == "__main__":
	print(process("input.txt"))






