import json
import os

folder = "arms_output"
data = []
# Load from files
for file in sorted(os.listdir(folder)):
    with open(os.path.join(folder, file)) as jsonfile:
        data.append(json.load(jsonfile))

# Extract the pose keypoints from the data
data = [x["people"][0]["pose_keypoints_2d"] for x in data]

# Utility function to split data
def split_to_points(lst):
    CHUNK_SIZE = 3 # A point is (x, y, confidence)
    return [tuple(lst[i:(i + CHUNK_SIZE)]) for i in range(0, len(lst), CHUNK_SIZE)]

# Split data into points
data = [split_to_points(x) for x in data]
