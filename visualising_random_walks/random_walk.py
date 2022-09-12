from random import choice

class RandomWalk():
	"""A class to generate random walks."""

	def __init__(self, num_points=5000):
		"""Initialise attributes of a walk."""
		self.num_points = num_points

		# All walks start at (0,0).
		self.x_values = [0]
		self.y_values = [0]
		self.step = 0

	def fill_walk(self):
		"""Calculate all the points in the walk."""

		def get_step():
			direction = choice ([1,-1])
			distance = choice (list(range(0,9,1)))
			step = direction * distance
			return step

		# Keep taking steps until the walk reaches the desired length. 
		while len(self.x_values) < self.num_points:

			x_step = get_step()
			y_step = get_step()

			# Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the next x and y values.
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)
