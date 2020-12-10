"""

Day 4

Required Passport Fields:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) -- optional!

Count the number of valid passports - those that have all required fields.

"""

import string

class Passport():
	# def __init__(id=None, expiration_year=None, birth_year=None, issue_year=None, 
	# 	         height=None, hair_color=None, eye_color=None, 
	# 	         country_id=None):

	# 	self.pid = id
	# 	self.expiration_year = expiration_year
	# 	self.birth_year = birth_year
	# 	self.issue_year = issue_year

	# 	self.height = height
	# 	self.hair_color = hair_color
	# 	self.eye_color = eye_color

	# 	self.country_id = country_id
	def __init__(self, passport_string):
		
		tokens = passport_string.split()
		passport_fields = {}

		for token in tokens:
			key, val = token.split(':')
			passport_fields[key] = val

		self.fields = passport_fields

	def year_valid(self, year):
		if not year:
			return False

		if not year.isdigit():
			return False

		if not len(year) == 4:
			return False

		return True

	def is_birth_year_valid(self):

		byr = self.fields.get('byr')
		
		if not self.year_valid(byr):
			return False

		byr = int(byr)

		if byr < 1920 or byr > 2002:
			return False

		return True

	def is_issue_year_valid(self):
		iyr = self.fields.get('iyr')

		if not self.year_valid(iyr):
			return False

		iyr = int(iyr)

		if iyr < 2010 or iyr > 2020:
			return False

		return True

	def is_exp_year_valid(self):
		eyr = self.fields.get('eyr')

		if not self.year_valid(eyr):
			return False

		eyr = int(eyr)

		if eyr < 2020 or eyr > 2030:
			return False

		return True

	def is_height_valid(self):
		height = self.fields.get("hgt")
		if not height:
			return False

		unit = height[-2:]

		if not (unit == "cm" or unit == "in"):
			return False

		if not height[:-2].isdigit():
			return False

		num = int(height[:-2])

		if unit == "cm":
			if num < 150 or num > 193:
				return False

		if unit == "in":
			if num < 59 or num > 76:
				return False

		return True

	def is_hair_color_valid(self):
		color = self.fields.get('hcl')
		if not color:
			return False

		if not color[0] == "#":
			return False

		color = color[1:]
		
		for char in color:
			if not char in string.hexdigits[:-6]:
				return False

		return True

	def is_eye_color_valid(self):
		color = self.fields.get('ecl')
		if not color:
			return False

		valid_eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
		return color in valid_eye_colors

	def is_id_valid(self):
		pid = self.fields.get('pid')
		
		if not pid:
			return False

		if len(pid) != 9:
			return False

		if not pid.isdigit():
			return False

		return True
			


	def is_valid(self):
		id = self.is_id_valid()
		eye = self.is_eye_color_valid()
		height = self.is_height_valid()
		hair = self.is_hair_color_valid()
		exp = self.is_exp_year_valid()
		birth = self.is_birth_year_valid()
		issue = self.is_issue_year_valid()

		print(f"""    id {id}
	eye {eye}
	height {height}
	hair {hair}
	exp {exp}
	birth {birth}
	issue {issue}""")

		if (id and eye and height and hair and exp and birth and issue):
			return True
		else:
			return False




def process(filename):
	f = open(filename)

	passport_obj = []
	contents = f.read()

	passports = contents.split('\n\n')
	
	for passport_string in passports:
		passport_obj.append(Passport(passport_string))


	return passport_obj

def count_valid_passwords(passports, debug=False):
	# import pdb; pdb.set_trace()
	count = 0
	for p in passports:
		if p.is_valid():
			if debug:
				print("found valid!")
			count += 1
		else:
			if debug:
				print("NOT valid")
	return count


print("TESTING INVALID PASSPORTS")
result = process("input2.txt")
num = count_valid_passwords(result, debug=True)
print('looking for 0 valid passports')
print('found', num, 'valid passports')


print("TESTING VALID PASSPORTS")
result = process("input3.txt")
num = count_valid_passwords(result, debug=True)
print('looking for 4 valid passports')
print('found', num, 'valid passports')

print("REAL INPUT")
result = process("input.txt")
num = count_valid_passwords(result)
print('result is', num)

