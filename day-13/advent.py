

def get_earliest_start(num, limit):
	
	current = 0
	while current < limit:
		# print(current)
		current = num + current

	return current



def find_best_bus(buses, limit):
	min_diff = float("inf")
	bus = None

	for line in buses:
		closest = get_earliest_start(line, limit)

		diff = closest-limit
		if diff < min_diff:
			min_diff = diff
			bus = line

	return bus * min_diff



def process(filename, part2=False):

	f = open(filename)

	buses = []
	for i, line in enumerate(f):
		if i == 0:
			earliest_time = int(line.strip())
		if i == 1:
			line = line.strip()
			line = line.split(",")
			for busline in line:
				if busline == "x":
					if part2:
						buses.append('x')
					else:
						continue
				else:
					buses.append(int(busline))
	return buses, earliest_time

def setup(buses):

	# {id: offset}
	reqs = {}
	for i, bus in enumerate(buses):
		if bus != 'x':
			reqs[bus] = i
	return reqs


def closest_multiple(num, starting):
	i = starting
	while True:
		if i%num == 0:
			return i 
		else:
			i += 1


def find_timestamp_t(buses):
	lines = [id for id in buses]
	first = lines[0]
	i = first
	# i = closest_multiple(first, 100000000000000)
	lines = lines[1:]

	while True:
		# print(f"trying i={i}")
		works = True
		num_tried = 0
		for id in lines:
			
			multiple = i + buses[id]
			num_tried += 1
			# print(f"   id {id}  offset {buses[id]}  multiple {multiple}")
			if multiple % id != 0:
				works = False
				print(f"num tried {num_tried} / {len(lines)}")
				break

		if works:
			return i
		else:
			i += first

		# if i % 100000 == 0:
		# 	print(i)


def find_offset_multiple(core_num, base_num, offset):
	
	i = core_num

	while True:
		if (i - offset) % base_num == 0:
			return i - offset

		i += core_num


def try_timestamp(t, buses):
	# print("TRYING OTHERS")

	works = True
	for id in buses:
		multiple = t + buses[id]
		
		if multiple % id != 0:
			works = False
			break

	return works



def find_timestamp_t_2(buses):

	
	lines = [id for id in buses]
	multiples = {line: set() for line in buses}

	first = lines[0]
	lines = lines[1:]
	multiplier = 1
	while True:
		for id in lines:
			offset = buses[id]
			possible_first_multiple= (id*multiplier) - offset
			print(possible_first_multiple)

			if (possible_first_multiple) % first == 0:
				multiples[id].add(possible_first_multiple)

		result = set()
		for k in multiples:
			result = multiples[k] & result
		if len(result):
			return result

		multiplier += 1

def loop_biggest_multiple(buses):

	lines = [id for id in buses]
	first_id = lines[0]

	largest_id = max(buses)
	offset = buses[largest_id]
	possible_answers = set()

	i = largest_id
	# i = closest_multiple(largest_id, 100000000000000)
	while True:
		# print(i)
		if (i - offset) % first_id == 0:
			# try with other numbers
			if try_timestamp(i - offset, buses):
				possible_answers.add(i-offset)
				# return i-offset
		i += largest_id

		if len(possible_answers) == 2:
			s = sorted(possible_answers)
			return (s[0], s[1]-s[0])

def find_all_multiples(buses):

	lines = [id for id in buses]
	first_id = lines[0]
	rest = lines[0]

	for line in lines:
		line_info = find_one_multiple(line, buses[line], first_id)
		offset = buses[line]
		buses[line] = {'offset': offset, 
					   'first': line_info[0], 
					   'diff between multiples': line_info[1]}
	return buses


def find_one_multiple(line, offset, first_id):
	i = line
	possible_answers = set()

	while True:
		if (i - offset) % first_id == 0:
			possible_answers.add(i-offset)
			
		i += line

		if len(possible_answers) == 2:
			s = sorted(possible_answers)
			return (s[0], s[1]-s[0])
			
		
def find_intersection(answer1, answer2):
	print("finding intersection")
	start1, offset1 = answer1
	print(f"start {start1} offset {offset1}")
	start2, offset2 = answer2
	print(f"start {start2} offset {offset2}")

	possibilities1 = set([start1])
	possibilities2 = set([start2])

	
	i = start1
	j = start2

	while True:
		if possibilities1 & possibilities2:
			return possibilities1 & possibilities2
		else:
			i += offset1
			j += offset2
			# print(j)
			possibilities1.add(i)
			possibilities2.add(j)

def divide(buses):
	# import pdb; pdb.set_trace()
	lines = [id for id in buses]
	
	first = lines[0]
	rest = lines[1:]

	half = len(rest)//2
	keys1 = [first] + rest[:half]
	keys2 = [first] + rest[half:]

	buses1 = {k: buses[k] for k in keys1}
	buses2 = {k: buses[k] for k in keys2}

	buses1[first] = buses[first]
	buses2[first] = buses[first]

	return buses1, buses2


# def gradually_add_buses(buses):
# 	# import pdb; pdb.set_trace()
# 	lines = [bus for bus in buses]
# 	first = lines[0]

# 	i = 1
# 	t = 0
# 	to_add = lines[i]
	

# 	while True:
		
# 		t += to_add
# 		print(t)
# 		mult_of_first = t-buses[lines[i]]

# 		if (mult_of_first) % first == 0: 
# 			print(mult_of_first)
# 			to_add = ???


# 		# current_bus = rest[current_bus_i]
# 		# offset = buses[current_bus]
	
# 		# if t % (current_bus - offset) == 0:
# 		# 	if current_bus_i == len(rest) -1:
# 		# 		return t
# 		# 	incr = current_bus
# 		# 	current_bus_i += 1
# 		# else:
# 		# 	t += incr
	





if __name__ == "__main__":
	# Part 1
	# print(find_best_bus(buses, limit))


	# Part 2
	buses, limit = process("test.txt", part2=True)
	buses = setup(buses)


	# Divide and conquer
	# buses1, buses2 = divide(buses)
	# start1 = loop_biggest_multiple(buses1)
	# start2 = loop_biggest_multiple(buses2)
	

	# print(find_intersection(start1, start2))

	# Gradual approach
	# print(gradually_add_buses(buses))


	buses = find_all_multiples(buses)

   																														    # 100000000000000
# {11696956928, 10100820451, 8504683974, 6908547497, 5312411020, 3716274543, 2120138066, 524001589, 16485366359, 14889229882, 13293093405}

