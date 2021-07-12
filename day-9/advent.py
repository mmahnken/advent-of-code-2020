"""

Day 9

"""
PREAMBLE_LENGTH = 25

def process(filename):
	f = open(filename)

	nums = []

	for line in f:
		nums.append(int(line.strip()))

	return nums


def get_all_valid(nums):
	all_sums = set()

	for num in nums:
		for num2 in nums:
			all_sums.add(num+num2)

	return all_sums


def find_invalid_num(nums):
	for i, num in enumerate(nums[PREAMBLE_LENGTH:]):
		i = i + PREAMBLE_LENGTH
		previous_five = nums[i-PREAMBLE_LENGTH:i]


		possible_valid_nums = get_all_valid(previous_five)

		print(f'checking if {num} is valid')
		print(f'   previous five {previous_five}')
		print(f'   possible sums: {possible_valid_nums}')
		if not (num in possible_valid_nums):
			return num


def find_contiguous_addends(goal_num, nums):
	for i, n in enumerate(nums):
		current_sequence = [n]
		
		for n2 in nums[i+1:]:
			if sum(current_sequence) > goal_num:
				break 
			if sum(current_sequence) == goal_num:
				return min(current_sequence) + max(current_sequence)

			current_sequence.append(n2)






n = process("input.txt")
num = find_invalid_num(n)
print(f'answer {num}')


print('part 2 answer')
print(find_contiguous_addends(num, n))
