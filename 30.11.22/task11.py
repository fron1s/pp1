import json

with open("filename.json") as file:
    data = json.load(file)

    for dict in data:
        for k,v in data.items():
            print(f"{k}: {v}")
        print()