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
