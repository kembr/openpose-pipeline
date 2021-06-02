import matplotlib.pyplot as plt
import numpy as np
from functions import *

folder = "arms_output"
data = load_openpose(folder)

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]
# Split data into points
data = [split_to_points(x) for x in data]

frame = data[40]  # plotting for the specific frame number from 0-180
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

# Plots a hand given an array of points
def plot_hand(data):
    connections = [(0,17,20), (0,13,16), (0,9,12), (0,5,8), (0,1,4)]
    for i in range(len(connections)):
        subline = connections[i]
        plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
        for j in range(subline[1], subline[2]):
            plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
    plt.gca().invert_yaxis()

