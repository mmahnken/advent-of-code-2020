"""Day 5

"""


def find_row(directions):
	lower = 0
	upper = 127

	for d in directions:
		diff = round((upper-lower) / 2, ndigits=0)
		if d == "F":
			upper = int(upper - diff)

		if d == "B":
			lower = int(lower + diff)

		# print(f'{lower}-{upper}')

	if directions[-1] == "F":
		return lower
	else:
		return upper


def find_coloumn(directions):
	lower = 0
	upper = 7

	for d in directions:
		diff = round((upper-lower) / 2, ndigits=0)
		if d == "L":
			upper = int(upper - diff)

		if d == "R":
			lower = int(lower + diff)

		# print(f'{lower}-{upper}')

	if directions[-1] == "L":
		return lower
	else:
		return upper
		

def find_seat_id(seat_spec):
	col = find_coloumn(seat_spec[-3:])
	row = find_row(seat_spec[:-3])
	return row * 8 + col

def process(filename):
	f = open(filename)
	
	all_seat_ids = set()

	
	for line in f:
		current_id = find_seat_id(line.strip())
		all_seat_ids.add(current_id)
	return all_seat_ids	

	return all_seat_ids

def find_max_id(all_seat_ids):
	max_id = 0
	for id_ in all_seat_ids:
		
		if id_ > max_id:
			max_id = id_
	return max_id

def find_my_seat(all_ids):
	for i, id_ in enumerate(all_ids):
		if i == 0:
			continue
		if id_ + 1 not in all_ids:
			return id_ + 1
		if id_ - 1 not in all_ids:
			return id_ - 1



# print(find_row('FBFBBF'))
# print()
# print(find_row('BFFFBBF'))

# print(find_coloumn('RLR'))
# print()


result = process("input.txt")
print(find_my_seat(result))