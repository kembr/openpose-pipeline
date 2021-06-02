import math
import os
import json

# Elan Shetreat-Klein, 5/25/21
# Calculates angle between segments 12 and 23, P2 is the vertex
def calc_angle(p1, p2, p3, degrees=True):

    # calculate lengths
    d12 = math.dist(p1, p2)
    d23 = math.dist(p2, p3)
    d13 = math.dist(p1, p3)

    result = math.acos((d12**2 + d23**2 - d13**2) / (2 * d12 * d23))

    if not degrees:
        return result

    return math.degrees(result)

# Utility function to split data
def split_to_points(lst):
    CHUNK_SIZE = 3 # A point is (x, y, confidence)
    return [tuple(lst[i:(i + CHUNK_SIZE)]) for i in range(0, len(lst), CHUNK_SIZE)]

def load_openpose(folder):
    data = []
    # Load from each file in folder
    for file in sorted(os.listdir(folder)):
        with open(os.path.join(folder, file)) as jsonfile:
            data.append(json.load(jsonfile))
    return data
