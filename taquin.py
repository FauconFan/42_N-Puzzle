#!/usr/bin/python3

import math
from enum import Enum

class Movement(Enum):
	UP = 1
	RIGHT = 2
	DOWN = 3
	LEFT = 4


class Taquin(object):
	"""docstring for Taquin"""
	def __init__(self, size, dico):
		# size of the taquin
		self.size = size
		# (x, y) -> value between 1 and size * size - 1
		self.dico = dico

	def __str__(self):
		s = ""
		for i in range(self.size):
			for j in range(self.size):
				s += str(self.dico[(i, j)]) + " "
			s += "\n"
		return s

	def clone(self):
		ret = Taquin(self.size, self.dico.copy())
		return ret

	def find_case(self, value):
		for i in range(0, self.size):
			for j in range(0, self.size):
				id = self.dico[(i, j)]
				if id is value:
					return (i, j)
		return (-1, -1)

	def get_right_positions(self, value):
		if value is 0:
			return (self.size - 1, self.size - 1)
		x = (value - 1) // self.size
		y = (value - 1) % self.size
		return x, y

	def swap_values(self, x1, y1, x2, y2):
		tmp = self.dico[(x1, y1)]
		self.dico[(x1, y1)] = self.dico[(x2, y2)]
		self.dico[(x2, y2)] = tmp

	def get_possible_moves(self):
		x0, y0 = self.find_case(0)
		ret = []
		if x0 > 0:
			cl = self.clone()
			cl.swap_values(x0, y0, x0 - 1, y0)
			ret.append((cl, Movement.UP))
		if y0 > 0:
			cl = self.clone()
			cl.swap_values(x0, y0, x0, y0 - 1)
			ret.append((cl, Movement.LEFT))
		if x0 < self.size - 1:
			cl = self.clone()
			cl.swap_values(x0, y0, x0 + 1, y0)
			ret.append((cl, Movement.DOWN))
		if y0 < self.size - 1:
			cl = self.clone()
			cl.swap_values(x0, y0, x0, y0 + 1)
			ret.append((cl, Movement.RIGHT))
		return ret

	""" Score avec la distance euclidienne """
	def score_euclidian(self):
		score = 0
		for i in range(self.size):
			for j in range(self.size):
				real_x, real_y = self.get_right_positions(self.dico[(i, j)])
				score += (real_x - i) ** 2 + (real_y - j) ** 2
		score = math.sqrt(score)
		return score

	def score(self):
		return self.score_euclidian()
