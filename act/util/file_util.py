import json

def read_json_as_dict(file_name: str) -> dict:
    with open(file_name) as f:
        contents = "".join(f.readlines())
    return json.loads(contents)

def write_dict_as_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
