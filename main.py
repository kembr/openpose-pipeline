import matplotlib.pyplot as plt
from functions import *
from plotter import *

data = load_openpose("arms_output")

for i, joint in enumerate(JOINTS.values(), 1):
	print(i, joint)

selection = int(input("Enter the number for the joint: "))

joint = list(JOINTS.keys())[selection - 1]

plot_joint_over_time(joint, data)