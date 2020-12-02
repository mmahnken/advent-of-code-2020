"""

Day 1

Find the two entries that sum to 2020 
and then multiply those two numbers together.

"""

def process(file):
	f = open(file)
	nums = set()
	for line in f:
		num = int(line.strip())
		nums.add(num)

	return nums


# O(n^2)
def find_sum_to_2020(nums):
	for num in nums:
		for num2 in nums:
			if num + num2 == 2020:
				return (num, num2)


# O(n)
def find_sum_to_2020_better(nums):
	counterparts = set()

	for num in nums:
		if 2020-num in nums:
			return num, 2020-num



# O(n^3))        :(
def find_three_sum_to_2020(nums):
	for num in nums:
		for num2 in nums:
			for num3 in nums:
				if num + num2 + num3 == 2020:
					return (num, num2, num3)


nums = process("input.txt")


# Part 1
num1, num2 = find_sum_to_2020(nums)
print("the answer is", num1, num2)
print("multiplied together", num1*num2)


# Part 1 O(n)
num1, num2 = find_sum_to_2020_better(nums)
print("the better answer is", num1, num2)
print("multiplied together", num1*num2)

# Part 2
print("starting part 2")
num1, num2, num3 = find_three_sum_to_2020(nums)
print(num1, num2, num3)
print("multiplied together", num1*num2*num3)


