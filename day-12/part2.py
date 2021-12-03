"""
Notes

R90:   x, y  --> y, -x
L90:   x, y  --> -y, x



R180/L180:  x, y ---> -x, -y

R270 == L90
L270 == R90

"""



class LLNode:

	def __init__(self, data, next=None, previous=None):
		self.data = data

		self.next = next
		self.previous = previous



def rotate_waypoint(waypoint_coords, action, units):
	"""Given current waypoint and a token like R180, return new waypoint rotated around ship


	>>> rotate_waypoint([10, 1], 'R', 180)

	

	>>> rotate_waypoint([10, 1], 'L', 270)
	

	"""

	orig_waypoint_coords = waypoint_coords

	if action == "L":
		if units == 90:
			waypoint_coords = rotate_l90(waypoint_coords)
		elif units == 270:
			waypoint_coords = rotate_r90(waypoint_coords)

	elif action == "R":
		if units == 90:
			waypoint_coords = rotate_r90(waypoint_coords)
		elif units == 270:
			waypoint_coords = rotate_l90(waypoint_coords)


	if units == 180:
		waypoint_coords = rotate_180(waypoint_coords)

	# print(f"rotating {action}{units} {orig_waypoint_coords} --> {waypoint_coords}")	

	return waypoint_coords


def rotate_r90(coords):
	return [coords[1], -coords[0]]

def rotate_l90(coords):
	return [-coords[1], coords[0]] 

def rotate_180(coords):
	return [-coords[0], -coords[1]] 


def move_waypoint(current_coords, direction, units):
	orig_waypoint = current_coords[:]
	if direction == "N":
		
		current_coords[1] += units

	elif direction == "S":
		current_coords[1] -= units


	elif direction == "E":
		current_coords[0] += units

	elif direction == "W":
		current_coords[0] -= units

	return current_coords

def move(current_coords, waypoint_coords, units):
	# import pdb; pdb.set_trace()
	new_x = current_coords[0] + waypoint_coords[0]*units
	new_y = current_coords[1] + waypoint_coords[1]*units
	return [new_x, new_y]


def process(filename):
	f = open(filename)

	current_coords = [0, 0]
	waypoint_coords = [10, 1]

	for i, line in enumerate(f):

		orig_ship = current_coords[:]
		orig_waypoint = waypoint_coords[:]

		line = line.strip()
		# print(line)
		
		action = line[0] 
		units = int(line[1:])

		if action in ["L", "R"]:
			# change direction!
			waypoint_coords = rotate_waypoint(waypoint_coords, action, units) #TODO
			# print(f"updated waypoint {waypoint_coords} ...... ship still at {current_coords}")

		elif action in ["N", "W", "E", "S"]:
			waypoint_coords = move_waypoint(waypoint_coords, action, units)
			# print(f"updated waypoint {waypoint_coords} ...... ship still at {current_coords}")


		elif action == "F":
			current_coords = move(current_coords, waypoint_coords, units)
			# print(f"updated ship {current_coords} ...... waypoint still at {waypoint_coords}")


		if orig_ship != current_coords:
			print(f"{action}{units}  🛳 {orig_ship} --> 🛳 {current_coords} ")
		elif orig_waypoint != waypoint_coords:
			print(f"{action}{units}  ❇️ {orig_waypoint} --> ❇️ {waypoint_coords}")
		else:
			print(f"{action}{units} NO CHANGE")

	print (current_coords)
	return abs(current_coords[0]) + abs(current_coords[1])


if __name__ == "__main__":
	print(process("input.txt"))






