import matplotlib.pyplot as plt
import numpy as np
from functions import *

# Joints
L_ELBOW = (5,6,7)
R_ELBOW = (2,3,4)
L_SHOULDER = (1,5,6)
R_SHOULDER = (1,2,3)
L_HIP = (8,12,13)
R_HIP = (8,9,10)
L_KNEE = (12,13,14)
R_KNEE = (9,10,11)

JOINTS = {
		L_ELBOW: "Left Elbow",
		R_ELBOW: "Right Elbow",
		L_SHOULDER: "Left Shoulder",
		R_SHOULDER: "Right Shoulder",
		L_HIP: "Left Hip",
		R_HIP: "Right Hip",
		L_KNEE: "Left Knee",
		R_KNEE: "Right Knee"
}

BODY_FOLDER = "arms_output"
BODY_DATA = load_openpose(BODY_FOLDER)

# Extract the pose keypoints from the data
BODY_DATA = [x["people"][0]["pose_keypoints_2d"] for x in BODY_DATA]
# Split data into points
BODY_DATA = [split_to_points(x) for x in BODY_DATA]

# Graph only points of body
'''
frame = BODY_DATA[40]  # plotting for the specific frame number from 0-180
x = np.array(frame)[:, 0]  # all of the x values of the pixels
y = np.array(frame)[:, 1]  # all of the y values of the pixels
plt.figure(1)  # opens a figure 1 file
# plots the x and y coordinates of the pixels in blue cirlces
plt.plot(x, y, 'bo')
plt.xlabel('x position (pixels)')  # provides x label
plt.ylabel('y position (pixels)')  # provides y label
plt.xlim([0, 854])  # makes the x limits
plt.ylim([0, 480])  # makes the y limits
plt.title('Plotted Data Points of the Video In Pixels')  # gives title
plt.gca().invert_yaxis()  # inverts the axis
plt.show()  # shows the plot
'''

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

def plot_joint_over_time(joint, data):
	angles = [angle_from_frame(joint, frame) for frame in data]
	plt.figure(1)  # opens a figure 1 file
	# plots the x and y coordinates of the pixels in blue cirlces
	plt.plot(range(len(angles)), angles, 'b')
	plt.title("Graph of Angle of " + JOINTS[joint] + " Over Time")
	plt.xlabel("Frame")
	plt.ylabel("Angle of " + JOINTS[joint] + " (degrees)")
	plt.ylim([0,180])
	plt.show()
		
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

# Graph angle of each joint over time
for joint in JOINTS.keys():
		plot_joint_over_time(joint, BODY_DATA)

plot_joint_vs_joint(R_ELBOW, L_ELBOW, BODY_DATA)