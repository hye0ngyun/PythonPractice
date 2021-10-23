import json

      
# with open('ex1.py', 'r', encoding="utf-8") as f:
#   print(f.readlines())

# docid
doc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# for j in range(1, 6):
#     # 파일 열기
#     with open(rf"C:\Users\shg72\Downloads\safe_json\Blackbox{j}_result.json", "r") as f1:
#         json_data = json.load(f1)
#     # 파일 저장
#     with open(rf"C:\Users\shg72\Downloads\safe_json\safe_transformed\Blackbox{j}_result.json", "w") as f:
#         f.write('[')
#         for i in range(len(json_data)):
#             f.write(' {\n')
#             f.write(f'  "TYPE": "{json_data[i]["TYPE"]}", \n')
#             f.write(f'  "METADATA_1": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}{json_data[i]["METADATA"][json_data[i]["METADATA"].find("/"):]}", \n')
#             f.write(f'  "METADATA_2": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}", \n')
#             f.write(f'  "CENTER_X": {json_data[i]["CENTER_X"]}, \n')
#             f.write(f'  "CENTER_Y": {json_data[i]["CENTER_Y"]}, \n')
#             f.write(f'  "WIDTH": {json_data[i]["WIDTH"]}, \n')
#             f.write(f'  "HEIGHT": {json_data[i]["HEIGHT"]}, \n')
#             f.write(f'  "FILE_ORIGINAL": "./blackbox{j}/original_frames{json_data[i]["FILE"][json_data[i]["FILE"].rfind("/"):]}", \n')
#             f.write(f'  "FILE_RESULT": "./blackbox{j}/result_frames{json_data[i]["FILE"][json_data[i]["FILE"].rfind("/"):]}", \n')
#             f.write(f'  "DOCID": "{doc[j-1]}{i:08}", \n')
#             f.write(f'  "FROM_TYPE": "{json_data[i]["FROM"]["TYPE"]}", \n')
#             f.write(f'  "FROM_PATH": "./blackbox{j}/{json_data[i]["FROM"]["TYPE"]}/{json_data[i]["FROM"]["FILE"]}" \n')
#             if i == (len(json_data)-1): f.write('} ')
#             else: f.write('}, ')
#         f.write(']')


# 파일 열기
with open(rf"C:\Users\shg72\Downloads\mask_walking_view\mask_training_dataset.json", "r") as f1:
    json_data = json.load(f1)
# 파일 저장
with open(rf"C:\Users\shg72\Downloads\mask_walking_view\transformed\t_mask_training_dataset.json", "w") as f:
    f.write('[')
    for i in range(len(json_data)):
        f.write(' {\n')
        f.write(f'  "TYPE": "{json_data[i]["TYPE"]}", \n')
        f.write(f'  "METADATA_1": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}{json_data[i]["METADATA"][json_data[i]["METADATA"].find("/"):]}", \n')
        f.write(f'  "METADATA_2": "{json_data[i]["METADATA"][:json_data[i]["METADATA"].find("/")].lower()}", \n')
        f.write(f'  "CENTER_X": {json_data[i]["CENTER_X"]}, \n')
        f.write(f'  "CENTER_Y": {json_data[i]["CENTER_Y"]}, \n')
        f.write(f'  "WIDTH": {json_data[i]["WIDTH"]}, \n')
        f.write(f'  "HEIGHT": {json_data[i]["HEIGHT"]}, \n')
        f.write(f'  "FILE_ORIGINAL": "./image_data/original_images/{json_data[i]["FILE"]}", \n')
        f.write(f'  "FILE_RESULT": "./image_data/result_images/{json_data[i]["FILE"]}", \n')
        f.write(f'  "DOCID": "I{i:08}", \n')
        f.write(f'  "FROM_TYPE": "url", \n')
        f.write(f'  "FROM_PATH": "www.kaggle.com" \n')
        if i == (len(json_data)-1): f.write('} ')
        else: f.write('}, ')
    f.write(']')