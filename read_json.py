import json

with open("ark.json",'r') as file:
    temp=json.loads(file.read())
    for i in range(len(temp)):
        print(temp[i]['name_zh'][0])