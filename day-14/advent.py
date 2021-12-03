def apply_bitmask(bitnum, mask):
	bitnum_list = list(bitnum)

	for idx, char in enumerate(mask):
		# print(char)
		# import pdb; pdb.set_trace()

		if char == "0" or char == "1":
			bitnum_list[idx] = char
	
	return "".join(bitnum_list)


def dec2bin(decnum):
	return f"{decnum:036b}"		


def bin2dec(bitnum):
	return int(bitnum, 2)




def process(filename):
	f = open(filename)
	mem = {}
	for line in f:
		line = line.strip()
		tokens = line.split(" = ")

		if tokens[0] == "mask":
			# update bitmask
			bitmask = tokens[1]

		elif tokens[0][:3] == "mem":
			mem_location = int(tokens[0].split('[')[1][:-1])
			num = int(tokens[1])
			# print(f'mem location {mem_location} num {num}')

			bin_number = dec2bin(num)
			bin_number = apply_bitmask(bin_number, bitmask)
			num = bin2dec(bin_number)

			mem[mem_location] = num

	# print(sum_mem_numbers(mem))

	print(sum([mem[k] for k in mem]))




if __name__ == "__main__":
	process("input.txt")