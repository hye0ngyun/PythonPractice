import json

# 파일 열기
with open(r"C:\Users\shg72\Downloads\safe_json\result6.json", "r") as f:
    json_data = json.load(f)

# 파일 저장
with open(r"C:\Users\shg72\Downloads\safe_json\safe_transformed\result6.json", "w") as f:
    f.write('[')
    for i in range(len(json_data)):
        f.write(' {\n')
        f.write(f'  "TYPE": "{json_data[i]["TYPE"]}", \n')
        f.write(f'  "METADATA_1": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}{json_data[i]["METADATA"][json_data[i]["METADATA"].find("/"):]}", \n')
        f.write(f'  "METADATA_2": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}", \n')
        f.write(f'  "CENTER_X": {json_data[i]["CENTER_X"]}, \n')
        f.write(f'  "CENTER_Y": {json_data[i]["CENTER_Y"]}, \n')
        f.write(f'  "HEIGHT": {json_data[i]["HEIGHT"]}, \n')
        f.write(f'  "WIDTH": {json_data[i]["WIDTH"]}, \n')
        f.write(f'  "FILE_ORIGINAL": "{json_data[i]["FILE_ORIGINAL"]}", \n')
        f.write(f'  "FILE_RESULT": "{json_data[i]["FILE_RESULT"]}", \n')
        f.write(f'  "DOCID": "F{i:08}", \n')
        f.write(f'  "FROM_TYPE": "{json_data[i]["FROM_TYPE"]}", \n')
        f.write(f'  "FROM_PATH": "{json_data[i]["FROM_PATH"]}" \n')
        if i == (len(json_data)-1): f.write('} ')
        else: f.write('}, ')
        
    f.write(']')
