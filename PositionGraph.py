
import matplotlib.pyplot as plt
import numpy as np
from functions import *

folder = "arms_output"
data = []
# Load from files
for file in sorted(os.listdir(folder)):
    with open(os.path.join(folder, file)) as jsonfile:
        data.append(json.load(jsonfile))

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]


def plot_body():
    x = np.array(frame)[:, 0] # x position of body 25
    y = np.array(frame)[:, 1] # y position of body 25
    plt.plot(x, y, 'bo')
    plt.xlabel('x position (pixels)')
    plt.ylabel('y position (pixels)')
    plt.xlim([0, 854])
    plt.ylim([0, 480])
    plt.title('Plotted Data Points of the Video')
    plt.gca().invert_yaxis()
    plt.show()

# Split data into points
data = [split_to_points(x) for x in data]

A = input('Which Frame would you like to analyze?') # can check body position graph in any frame
frame = data[int(A)]
plot_body()
