import json

# 파일 열기
with open(r"C:\Users\shg72\Downloads\ResultJson\result6.json", "r") as f:
    json_data = json.load(f)
# # list
# print(type(json_data), len(json_data))
# # list
print(json_data[231]["METADATA"].lower())
print(f'  "METADATA_1": "{json_data[0]["METADATA"][:json_data[0]["METADATA"].find("/")].lower()}{json_data[0]["METADATA"][json_data[0]["METADATA"].find("/"):]}", \n')
# print(type(json_data[0]["METADATA"]))
# print(json_data[0]["METADATA"][:json_data[0]["METADATA"].find('/')])
# i = 1
# print(f'{i:08}')
# 파일 저장
with open(r"C:\Users\shg72\Downloads\ResultJson\transformed_lower\result6_1.json", "w") as f:
    f.write('[')
    for i in range(len(json_data)):
        f.write(' {\n')
        f.write(f'  "TYPE": "{json_data[i]["TYPE"]}", \n')
        f.write(f'  "METADATA_1": "{json_data[0]["METADATA"][:json_data[0]["METADATA"].find("/")].lower()}{json_data[0]["METADATA"][json_data[0]["METADATA"].find("/"):]}", \n')
        f.write(f'  "METADATA_2": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}", \n')
        f.write(f'  "CENTER_X": "{json_data[i]["CENTER_X"]}", \n')
        f.write(f'  "CENTER_Y": "{json_data[i]["CENTER_Y"]}", \n')
        f.write(f'  "HEIGHT": "{json_data[i]["HEIGHT"]}", \n')
        f.write(f'  "WIDTH": "{json_data[i]["WIDTH"]}", \n')
        f.write(f'  "FILE_ORIGINAL": "{json_data[i]["FILE_ORIGINAL"]}", \n')
        f.write(f'  "FILE_RESULT": "{json_data[i]["FILE_RESULT"]}", \n')
        f.write(f'  "DOCID": "G{i:08}", \n')
        f.write(f'  "FROM_TYPE": "{json_data[i]["FROM_TYPE"]}", \n')
        f.write(f'  "FROM_PATH": "{json_data[i]["FROM_PATH"]}" \n')
        if i == (len(json_data)-1): f.write('} ')
        else: f.write('}, ')
        
    f.write(']')
