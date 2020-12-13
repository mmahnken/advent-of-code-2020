"""
Day 6

"""


def process(filename):
	f = open(filename)

	contents = f.read()

	groups = contents.split('\n\n')
	return groups

# Part 1
def count_questions(groups):
	count = 0

	for g in groups:
		group_questions = set()
		people = g.split()

		for person in people:
			print(f'person {person}')
			
			for question in person:
				print(f'   {question}')
				group_questions.add(question)
		count += len(group_questions)

	return count


def get_questions(people):
	
	counts = {}

	for person in people:
			
			for question in person:
				if counts.get(question):
					counts[question] += 1
				else:
					counts[question] = 1
	num = 0
	for q in counts:
		print(f'{q} {counts[q]}')
		if counts[q] == len(people):
			num += 1
	return num

				

# Part 2
def count_questions_unanimous(groups):
	count = 0

	for g in groups:
		people = g.split()

		num = get_questions(people)

		count += num

	return count



result = process("input.txt")
num = count_questions_unanimous(result)
print(num)
