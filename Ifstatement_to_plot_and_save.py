from functions import *


def angle_from_frame(joint, frame):
    # creates array of the output of calc_angle function
    return calc_angle(*[frame[x][0:2] for x in joint])




folder = "arms_output"
data = load_openpose(folder)

