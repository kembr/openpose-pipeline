def plot_joint_vs_joint(joint1, joint2, data):
	angles1 = [angle_from_frame(joint1, frame) for frame in data]
	angles2 = [angle_from_frame(joint2, frame) for frame in data]
	fig = plt.figure()  # opens a figure 1 file
	# plots the x and y coordinates of the pixels in blue cirlces
	plt.plot(angles1, angles2, 'b')
	plt.title("Graph of " + JOINTS[joint1] + " Angle vs " + JOINTS[joint2] + " Angle")
	plt.xlabel("Angle of " + JOINTS[joint1] + " (degrees)")
	plt.ylabel("Angle of " + JOINTS[joint2] + " (degrees)")
	plt.xlim([0, 180])
	plt.ylim([0, 180])
	plt.show()
	fig.savefig('plot.png')

# Optional sorting code
import os
import shutil
def plot_and_sort_angle():
		plt.savefig(str(A) + '.png')

		source = os.path.join('/Users/christinacoulton/Desktop/Python Files/openpose-pipeline')
		sort = os.path.join('/Users/christinacoulton/Desktop/Python Files/openpose-pipeline/Plots')

		for f in os.listdir(source):
				if f.endswith(".png"):
						shutil.move(os.path.join(source, f), sort)

						# Plots a line segment between two points
def plot_line(p1, p2):
	plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')

# Plots a body_25 given an array of points
def plot_body(data):
	connections = [(8,9,11), (11,22,23), (11,24,24), (8,12,14), (14,19,20), (14,21,21), (0,1,4), (1,5,7), (1,8,8), (0,15,15), (15,17,17), (0,16,16), (16,18,18)]
	for i in range(len(connections)):
			subline = connections[i]
			plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
			for j in range(subline[1], subline[2]):
					plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
	plt.gca().invert_yaxis()
	plt.title('Plotted Data Points of the Body In Pixels')  # gives title
	plt.xlabel('x position (pixels)')  # provides x label
	plt.ylabel('y position (pixels)')  # provides y label
	plt.xlim([0, 854])  # makes the x limits
	plt.ylim([0, 480])  # makes the y limits
	plt.show()

# Plots a hand given an array of points
def plot_hand(data):
	connections = [(0,17,20), (0,13,16), (0,9,12), (0,5,8), (0,1,4)]
	for i in range(len(connections)):
			subline = connections[i]
			plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
			for j in range(subline[1], subline[2]):
					plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
	plt.gca().invert_yaxis()
	plt.title('Plotted Data Points of the Hand In Pixels')  # gives title
	plt.xlabel('x position (pixels)')  # provides x label
	plt.ylabel('y position (pixels)')  # provides y label
	plt.show()