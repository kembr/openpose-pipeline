# C Coulton 06092021

import matplotlib.pyplot as plt
from functions import *


def angle_from_frame(joint, frame):
    # creates array of the output of calc_angle function
    return calc_angle(*[frame[x][0:2] for x in joint])

def plot_angle():
    plt.plot(range(len(angles)), angles, 'b')
    plt.title("Graph of " + A + " Angle")  # will change body part based on input
    plt.xlabel("Frame")
    plt.ylabel("Angle of" + A + ' [degrees]')
    plt.show()  # shows the plot


folder = "arms_output"
data = load_openpose(folder)

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]
# Split data into points
data = [split_to_points(x) for x in data]

joints = {'Left Elbow': (5, 6, 7),  # dictionary of joints
          'Right Elbow': (2, 3, 4),
          'Left Shoulder': (1, 5, 6),
          'Right Shoulder': (1, 2, 3),
          'Left Hip': (8, 12, 13),
          'Right Hip': (8, 9, 10),
          'Left Knee': (12, 13, 14),
          'Right Knee': (9, 10, 11)

          }

A = input('What joint would you like to analyze? Please refer to the list of options stated.')
joint = joints[A] # will call from dictionary
angles = [angle_from_frame(joint, frame) for frame in data]
plot_angle() # will plot angle over time
