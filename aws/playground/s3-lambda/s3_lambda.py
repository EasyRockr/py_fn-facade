import json

def Handler(event, context):
    print("S3 Event!")
    print(json.dumps(event, indent=2))

    return "ok!"