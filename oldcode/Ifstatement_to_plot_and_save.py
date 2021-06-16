from functions import *
from matplotlib import pyplot as plt
import os
import shutil

def angle_from_frame(joint, frame):
    # creates array of the output of calc_angle function
    return calc_angle(*[frame[x][0:2] for x in joint])

def plot_and_sort_angle():
    plt.figure()
    plt.plot(range(len(angles)), angles, 'b')
    plt.title("Graph of " + A + " Angle")
    plt.xlabel("Frame")
    plt.ylabel("Angle of" + A +' [degrees]')
    plt.savefig(str(A) + '.png')
    plt.show()  # shows the plot

    source = os.path.join('/Users/christinacoulton/Desktop/Python Files/openpose-pipeline')
    sort = os.path.join('/Users/christinacoulton/Desktop/Python Files/openpose-pipeline/Plots')

    for f in os.listdir(source):
        if f.endswith(".png"):
            shutil.move(os.path.join(source, f), sort)



folder = "arms_output"
data = load_openpose(folder)

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]
# Split data into points
data = [split_to_points(x) for x in data]

# Uses input to produce angle over frame graph for any joint, must input exactly from the library in Github
A = input('What joint would you like to analyze? Please refer to the list of options stated.')
if A == 'Right Elbow':
    joint = (2, 3, 4)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Left Elbow':
    joint = (5, 6, 7)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Left Shoulder':
    joint = (1, 5, 6)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Right Shoulder':
    joint = (1, 2, 3)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Left Hip':
    joint = (8, 12, 13)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Right Hip':
    joint = (8, 9, 10)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Left Knee':
    joint = (12, 13, 14)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()
elif A == 'Right Knee':
    joint = (9, 10, 11)
    angles = [angle_from_frame(joint, frame) for frame in data]
    plot_and_sort_angle()

