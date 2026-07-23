import json

student = {"name": "trish", "roll_no": 1, "marks": [99, 98, 97]}
with open("data.json","w") as f:
    json.dump(student, f)
with open("data.json","r") as f:
    data=json.load(f)
    print(data)    
    print(type(data["roll_no"]))
    print(type(data["name"]))
    print(type(data["marks"]))