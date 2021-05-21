import json

with open("output.json") as jsonfile:
    data = json.load(jsonfile)

hand_left_x0 = data["people"][0]["hand_left_keypoints_2d"][0]
hand_left_y0 = data["people"][0]["hand_left_keypoints_2d"][1]

added = hand_left_x0 + hand_left_y0

# next we want to calculate the angles from (x0,y0) to (x1,y1)

print(added)
print(hand_left_x)
print(hand_left_y)
