import pygal

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	steps_total = 1000
	rw = RandomWalk(steps_total)
	rw.fill_walk()
	
	#rw_chart = pygal.XY(stroke=False)
	rw_chart = pygal.XY()
	rw_chart.title = 'Random Walk'

	rw_chart.add('rw', [(rw.x_values[z],rw.y_values[z]) 
		for z in range(steps_total)])

	rw_chart.render_to_file('random_walk_visual.svg')

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
