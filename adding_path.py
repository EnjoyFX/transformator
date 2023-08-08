import json


ROOT_KEY_FULL = "cfg"
ROOT_KEY_PARTIAL = "cfg"
KEY_TO_MAP = "path"

# get full file
with open('full.json', 'r') as full_file:
    full_data = json.load(full_file)

# get partial file
with open('partial.json', 'r') as partial_file:
    partial_data = json.load(partial_file)

# Data mapping
mapping = {}
for item in full_data[ROOT_KEY_FULL]:
    key = list(item.keys())[0]
    path = item[key][KEY_TO_MAP]
    mapping[key] = path

# adding needed key to partial.json
for item in partial_data[ROOT_KEY_PARTIAL]:
    key = list(item.keys())[0]
    if key in mapping:
        item[key][KEY_TO_MAP] = mapping[key]

# Save the result
with open('out2.json', 'w') as out_file:
    json.dump(partial_data, out_file, indent=4)

print("Needed key have been added")
