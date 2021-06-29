import matplotlib.pyplot as plt
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
L_ANKLE = (10,11,23)
R_ANKLE = (13,14,20)

JOINTS = {
		L_ELBOW: "Left Elbow",
		R_ELBOW: "Right Elbow",
		L_SHOULDER: "Left Shoulder",
		R_SHOULDER: "Right Shoulder",
		L_HIP: "Left Hip",
		R_HIP: "Right Hip",
		L_KNEE: "Left Knee",
		R_KNEE: "Right Knee",
		L_ANKLE: "Left Ankle",
		R_ANKLE: "Right Ankle"
}

def plot_joint_over_time(joint, data, show=True, save=False, save_dir="plot.png"):
	angles = [angle_from_frame(joint, frame) for frame in data]
	plt.figure()
	# plots the x and y coordinates of the pixels in blue circles
	plt.plot(range(len(angles)), angles, 'b')
	plt.title("Graph of Angle of " + JOINTS[joint] + " Over Time")
	plt.xlabel("Frame")
	plt.ylabel("Angle of " + JOINTS[joint] + " (degrees)")
	plt.xlim([0, 180])
	plt.ylim([0, 180])
	if save:
		plt.savefig(save_dir)
	if show:
		plt.show()
	plt.close()


def plot_line(p1, p2):
	plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')

# Shows an animation of the data for a body model or a hand model
def animate(data_path, model_type):
	os.system(f"animate.py {data_path} {model_type}")
