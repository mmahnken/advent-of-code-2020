"""

Day 2


How many passwords are valid according to their policies?

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy 
indicates the lowest and highest number of times a given letter must appear 
for the password to be valid. For example, 1-3 a means that the password must 
contain a at least 1 time and at most 3 times.


"""

class Password():
	def __init__(self, pw, letter, min_, max_):

		self.pw = pw 
		self.letter = letter
		self.max_ = max_
		self.min_ = min_


	def is_valid_sled_rental(self):
		"""The Part 1 is_valid function."""
		
		letter_count = 0
		
		for letter in self.pw:
			if letter == self.letter:
				letter_count += 1

		return letter_count >= self.min_ and letter_count <= self.max_

	def is_valid(self):
		"""The is_valid for Part 2"""

		possible_match1 = self.pw[self.min_-1]
		possible_match2= self.pw[self.max_-1]

		if possible_match1==self.letter and possible_match2 != self.letter:
			return True

		elif possible_match2==self.letter and possible_match1 != self.letter:
			return True
		else:
			return False





	def __repr__(self):
		return "<Password pw={} letter={} min={} max={}>".format(
			self.pw,
			self.letter,
			self.min_,
			self.max_
		)




def process(filename):
	data = []
	f = open(filename)
	for line in f:
		tokens = line.split()
		min_letter, max_letter = [int(t) for t in tokens[0].split('-')]
		letter = tokens[1][0]
		pw = tokens[2]


		new_password = Password(pw, letter, min_letter, max_letter)
		data.append(new_password)

	return data


def get_num_valid_passwords(data):
	return len([pw for pw in data if pw.is_valid() ])



d = process("input.txt")
print('answer:', get_num_valid_passwords(d))



