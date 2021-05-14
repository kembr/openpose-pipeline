import json

with open("output.json") as jsonfile:
    data = jsonfile.read()

# people = data["people"]
print(data)
