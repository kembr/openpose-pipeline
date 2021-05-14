import json

with open("output.json") as jsonfile:
    data = json.load(jsonfile)

hand_left_x = data["people"][0]["hand_left_keypoints_2d"][0]
hand_left_y = data["people"][0]["hand_left_keypoints_2d"][1]

added = hand_left_x + hand_left_y

print(added)
print(hand_left_x)
print(hand_left_y)
