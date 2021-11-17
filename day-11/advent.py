from copy import copy
import sys
from termcolor import colored, cprint

def process(filename):
	f = open(filename)

	graph = SeatGraph()

	for line in f:
		line = line.strip()
		row = []

		for seat in line:
			if seat == ".":
				new_node = Node("floor")
			elif seat == "L":
				new_node = Node("empty")
			elif seat == "#":
				new_node = Node("occupied")

			row.append(new_node)

		graph.nodes.append(row)

	return graph





class Node:
	def __init__(self, state):
		self.state = state

		self.left = None 
		self.right = None 
		self.above = None 
		self.below = None 

		self.ne = None 
		self.se = None 
		self.nw = None 
		self.sw = None 

		self.neighbors = []
		self.extended_neighbors = []


	def __repr__(self):
		if self.state == "empty":
			return "L"
		elif self.state == "floor":
			return "_"
		elif self.state == "occupied":
			return "#"

	def get_next_state(self, extended):
		num_occupied = 0


		if extended:
			neighbors = self.extended_neighbors
		else:
			neighbors = self.neighbors



		for neighbor in neighbors:

			if neighbor.state == "occupied":
				num_occupied += 1

		if num_occupied == 0 and self.state == "empty":
			return "occupied"
		elif extended == False and num_occupied >= 4 and self.state == "occupied":
			return "empty"
		elif extended == True and num_occupied >= 5 and self.state == "occupied":
			return "empty"
		else:
			return self.state


	def neighbor_dictionary(self):
		return {"north": self.above,
				"south": self.below,
				"east": self.right,
				"west": self.left,
				"nw": self.nw,
				"ne": self.ne,
				"sw": self.sw,
				"se": self.se,
		}

	def add_extended_neighbor(self, direction):
		

		# print(f'going {direction}')

		# if self.x == 3 and self.y == 4:
		# 	import pdb; pdb.set_trace()

		if self.state == "floor":
			return

		current = self.neighbor_dictionary()[direction]

		while True:
			if not current:
				return

			if current.state != "floor":
				self.extended_neighbors.append(current)
				return
			else:
				next_node = current.neighbor_dictionary()[direction]
				if not next_node:
					return
				else:
					current = next_node




class SeatGraph:
	def __init__(self):
		self.nodes = []


	def set_positions(self):
		for y, row in enumerate(self.nodes):
			for x, node in enumerate(row):
				node.y = y 
				node.x = x		

	def set_neighbors(self):
		for row in self.nodes:
			for node in row:
				y = node.y 
				x = node.x
				last_index = len(row) - 1
				last_row = len(self.nodes) -1
				# print(f"y {y}, x{x}")
				if y != 0:
					# there is a row above
					node.above = self.nodes[y-1][x] # y-1, same x
					node.neighbors.append(node.above)

				if x != 0:
					# there is a space to the left
					node.left = self.nodes[y][x-1]    # same y, x - 1
					node.neighbors.append(node.left)


				if x != last_index:
					# there is a space to the right
					node.right = self.nodes[y][x+1]   # same y, x + 1
					node.neighbors.append(node.right)

				if y != last_row:
				    # there is a space below
					node.below = self.nodes[y+1][x] # y+1, same x
					node.neighbors.append(node.below)


				if y != 0 and x != 0:
				    # there is a space to the left and above
					node.nw = self.nodes[y-1][x-1]    # y-1, x-1
					node.neighbors.append(node.nw)

				if y != last_row and x != last_index :
					# there is a space below and to the right
					node.se = self.nodes[y+1][x+1]    # y+1, x+1
					node.neighbors.append(node.se)

				if y != 0 and x != last_index:
					# there is a space to the right and above
					node.ne = self.nodes[y-1][x+1]    # y-1, x+1 
					node.neighbors.append(node.ne)

				if y != last_row and x != 0:
					# there is a space below and to the left
					node.sw = self.nodes[y+1][x-1]    # y+1, x-1
					node.neighbors.append(node.sw)
	

	def set_extended_neighbors(self):
		for row in self.nodes:
			for node in row:
				# print(f"y {node.y}, x{node.x}, state {node.state}")
				node.add_extended_neighbor(direction="north")
				node.add_extended_neighbor(direction="south")
				node.add_extended_neighbor(direction="east")
				node.add_extended_neighbor(direction="west")
				node.add_extended_neighbor(direction="nw")
				node.add_extended_neighbor(direction="ne")
				node.add_extended_neighbor(direction="sw")
				node.add_extended_neighbor(direction="se")



	def distribute(self, new_graph, extended=False):
		# import pdb; pdb.set_trace()
		made_switch = False
		for row in self.nodes:
			new_row = []
			new_graph.nodes.append(new_row)
			for node in row:
				current_state = node.state
				next_state = node.get_next_state(extended)
				if current_state != next_state:
					made_switch = True

				new_node = Node(next_state)
				# new_node.state = next_state
				new_row.append(new_node)

		new_graph.set_positions()
		new_graph.set_neighbors()
		
		if extended:
			new_graph.set_extended_neighbors()
		
			



		return made_switch, new_graph

	def pprint(self):
		print()
		for row in self.nodes:
			for n in row:
				if n.state == "floor":
					cprint(n, "cyan", end="")
				if n.state == "empty":
					cprint(n, "yellow", end="")
				if n.state == "occupied":
					cprint(n, "magenta", end="")
			print()
		print()

	def num_occupied(self):
		count = 0
		for row in self.nodes:
			for node in row:
				if node.state == "occupied":
					count += 1
		return count


def begin_simulation(graph, extended=False):
	count = 0

	while True:
		count += 1
		print(f"Simulation {count} in progress")

		made_switch, graph = graph.distribute(SeatGraph(), extended)
		print('-------------------------------')
		graph.pprint()
		# import pdb; pdb.set_trace()
		if made_switch  == False:
			print(graph.num_occupied())
			return 
		






if __name__ == "__main__":
	graph = process("input.txt")
	graph.set_positions()
	graph.set_neighbors()
	graph.set_extended_neighbors()
	count = begin_simulation(graph, extended=True)
	print(count)
