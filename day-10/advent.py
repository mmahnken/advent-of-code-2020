""" 

Day 10

"""


def process(filename):
	adapters = [0]
	f = open(filename)
	for line in f:
		adapters.append(int(line.strip()))
	return adapters


def count_diffs(adapters):
	nums_1s = 0
	nums_3s = 0
	adapters = sorted(adapters)

	adapters.append(adapters[-1]+3)


	for i, a in enumerate(adapters[:-1]):
		diff = adapters[i+1] - adapters[i] 
		if diff == 1:
			nums_1s += 1
		if diff == 3:
			nums_3s += 1

	return nums_1s, nums_3s

def get_new_neighbors(adapters):
	adapters = sorted(adapters)
	adapters.append(adapters[-1]+3)

	new_neighbors = []

	for i, a in enumerate(adapters):
		print(f"checking i {i}")
		for j in range(2,4):
			
			if i+j <= len(adapters)-1:
				next_next_adapter = adapters[i+j]
				print(f"   {i+j}")

				if (next_next_adapter - a) < 4:
					new_neighbors.append((i, i+j))

	return new_neighbors

def organize_new_neighbors(nn):
	valid_mutuals = {}

	for pair in nn:
		valid_mutuals[tuple(pair)] = set()
		for pair2 in nn:
			if pair == pair2:
				continue

			if pair2[0] == pair[0]:
				continue

			
			if pair2[0] > pair[0] and pair2[0] < pair[1]:
				continue

			valid_mutuals[tuple(pair)].add(pair2)

	return valid_mutuals


		
	return overlaps

def count_new_arrangements(new_neighbors, valid_mutuals):
	
	arrangements = set()
	for x in range(len(new_neighbors)):
		for i, pair in enumerate(new_neighbors):
			current_arrangement = [pair]

			arrangements.add(s(current_arrangement[:]))
			for j in range(x):
				# if i >= j:
				# 	continue
				print(i, j)

				pair2 = new_neighbors[j]

				if pair2 in valid_mutuals[pair]:
				

				

					current_arrangement.append(pair2) 
					current_arrangement.sort()
					arrangements.add(s(current_arrangement[:]))

	return (arrangements)

def s(pairs):
	stringified_pairs = ""
	for pair in pairs:
		string_version = str(pair[0]) + str(pair[1])
		stringified_pairs = stringified_pairs + string_version 

	return stringified_pairs





a = process("input3.txt")
# a, b = count_diffs(a)
# print(f'answer is {a*b}')
nn = get_new_neighbors(a)
a = organize_new_neighbors(nn)
arr = count_new_arrangements(nn, a)
print(len(arr))

