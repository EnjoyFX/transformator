import json

# transformation from plain to nested dict

ROOT_KEY = "cfg"
CHILD = "child"


def insert_empty_path(base, path_list):
    if len(path_list) == 1:
        if path_list[0] not in base:
            base[path_list[0]] = {CHILD: {}}
    else:
        if path_list[0] not in base:
            base[path_list[0]] = {CHILD: {}}
        insert_empty_path(base[path_list[0]][CHILD], path_list[1:])


def insert_item(base, path_list, item):
    if len(path_list) == 1:
        base[path_list[0]] = {**base[path_list[0]], **item}
    else:
        insert_item(base[path_list[0]][CHILD], path_list[1:], item)


def transform_to_nested(data):
    nested_dict = {}
    for item in data[ROOT_KEY]:
        key = list(item.keys())[0]
        path = item[key]['path'].split('.')
        insert_empty_path(nested_dict, path)

    for item in data[ROOT_KEY]:
        key = list(item.keys())[0]
        path = item[key]['path'].split('.')
        insert_item(nested_dict, path, item[key])

    return {ROOT_KEY: nested_dict}


# read the in-file
with open('in.json', 'r') as infile:
    data = json.load(infile)

# transformation
transformed_data = transform_to_nested(data)

# write the out-file
with open('out.json', 'w') as outfile:
    json.dump(transformed_data, outfile, indent=4)

print("Transformation done!")
