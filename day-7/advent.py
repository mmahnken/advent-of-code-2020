"""Day 7



"""


class BagNode:
	def __init__(self, color, parents=None):
		self.color = color

		if not parents:
			self.parents = []
		else:
			self.parents = parents

	def __repr__(self):
		return f'<BagNode color={self.color}>'

class BagGroupNode:
	def __init__(self, color, num):
		self.color = color
		self.num = num


	def __repr__(self):
		return f'<BagNode color={self.color}>'

def get_container(line):
	tokens = line.strip().split(' bags contain')
	return tokens[0]

def get_inside(line):
	tokens = line.strip().split(' contain ')

	color_tuples = []
	insides = tokens[1].split(',')
	for inside in insides:
		core = inside.split(' bag')[0].strip()
		if core == "no other":
			continue
		# print(f'core is {core}')
		num = int(core[0])
		color = core[2:]
		color_tuples.append((color, num))
	return color_tuples


def process(filename):
	node_refs = {}
	
	f = open(filename)

	for line in f:
		container = get_container(line)
		inside_list = get_inside(line)

		
		if container in node_refs:
			container_node = node_refs[container]
		else:
			container_node = BagNode(container)
			node_refs[container] = container_node



		inside_nodes = []
		# print(f'processing {container} bags')
		for color, num in inside_list:
			# print(f'    {color}')
			
			if color in node_refs:
				node = node_refs[color]
				node.parents.append(container_node)
			else:
				node = BagNode(color, [container_node])
				node_refs[color] = node
		

	return node_refs

def process2(filename):
	parents = {}
	
	f = open(filename)

	for line in f:
		container = get_container(line)
		inside_list = get_inside(line)

		inside_nodes = []
		# print(f'processing {container} bags')
		for color, num in inside_list:
			# print(f'    {color}')
			node = BagGroupNode(color, num)	
			inside_nodes.append(node)


		if container in parents:
			parents[container].extend(inside_nodes)
			
		else:
			parents[container] = inside_nodes
		

	return parents


def count_possible_outer_bags(node):
	nodes_to_count = node.parents
	unique_outer_bags = set()

	while nodes_to_count:
		current = nodes_to_count.pop()
		print(f'counting {current.color}')
		nodes_to_count.extend(current.parents)
		unique_outer_bags.add(current.color)

	return len(unique_outer_bags)

def count_inside_bags(data, bag_color):
	num = 0

	to_count = data[bag_color]

	while to_count:
		current = to_count.pop()
		num += current.num
		for i in range(current.num):
			to_count.extend(data[current.color])

	return num


d = process2('input.txt')
# num = count_possible_outer_bags(d['shiny gold'])

num = count_inside_bags(d, 'shiny gold')
print(f'answer {num}')


