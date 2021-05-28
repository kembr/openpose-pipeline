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

