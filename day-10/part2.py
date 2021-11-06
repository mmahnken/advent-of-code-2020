class Node:
	def __init__(self, jolts):
		self.jolts = jolts
		self.adjacent = []

	def add_adapter(self, node):
		self.adjacent.append(node)

	def __repr__(self):
		return f"<Node {self.jolts} ajd={[n.jolts for n in self.adjacent]}>"


class AdapterGraph:
	def __init__(self):
		self.nodes = {}

	def add_node(self, jolts):
		if jolts not in self.nodes:
			new_node = Node(jolts)
			self.nodes[jolts] = new_node
			return new_node

	# def __contains__(self):

	def count_paths(self):
		start = min(self.nodes)
		stop = max(self.nodes)
		current_node = self.nodes[start]

		term = [0 for i in range(stop+1)]

		def count_recursive(current, stop, seen):
			current_sum = 0
			if current.jolts == stop:
				print("END!")
				return 1

			


			seen.add(current)
			for node in current.adjacent:
				if term[node.jolts]:
					to_add = term[node.jolts]
				else:
					to_add = count_recursive(node, stop, seen)
					term[node.jolts] = to_add

				current_sum += to_add

			return current_sum

		print(count_recursive(self.nodes[0], stop, set()))








def make_graph(adapters):
	"""Make all possible combos"""

	adapters.append(max(adapters)+3)
	adapters.sort()

	adapters_set = set(adapters)

	graph = AdapterGraph()
	print(adapters)

	for adapter in adapters:

		# if not in graph
		if adapter not in graph.nodes:
			current_node = graph.add_node(adapter)
			# print(f"adding {adapter} to graph")
		else:
			current_node = graph.nodes[adapter]

		adjacent = [adapter+num for num in [1,2,3] if adapter+num in adapters_set]
		# print(f"Adjacency for {adapter}: {adjacent}")

		for next_adapter in adjacent:

			# check to see if we have computed this before, if so, look up
			# and use previously computed value
			if next_adapter not in graph.nodes:
				node = graph.add_node(next_adapter)
			else:
				node = graph.nodes[next_adapter]

			current_node.add_adapter(node)

	return graph




if __name__ == "__main__":
	
	from advent import process

	nums = process("input.txt")
	g = make_graph(nums)
	g.count_paths()