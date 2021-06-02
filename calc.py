from functions import *

folder = "arms_output"
data = load_openpose(folder)

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]
# Split data into points
data = [split_to_points(x) for x in data]
