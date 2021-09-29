import json


def transform(x):
    if "XMIN" in x:
        t = {}

        t["TYPE"] = x["TYPE"]
        t["FILE_ORIGINAL"] = x["FILE"]["original"]
        t["FILE_RESULT"] = x["FILE"]["result"]
        t["METADATA"] = x["METADATA"]
        t["CENTER_X"] = x["CENTER_X"]
        t["CENTER_Y"] = x["CENTER_Y"]
        t["WIDTH"] = x["WIDTH"]
        t["HEIGHT"] = x["HEIGHT"]
        t["FROM_TYPE"] = x["FROM"]["TYPE"]
        # FROM안에 FILE이 있다면
        if "FILE" in x["FROM"]:
            t["FROM_FILE"] = x["FROM"]["FILE"]
            t["FROM_URL"] = ""
        elif "URL" in x["FROM"]:
            t["FROM_FILE"] = ""
            t["FROM_URL"] = x["FROM"]["URL"]
        return t
    return None


with open(r"PythonPractice\Playground\transformJson\index_files\safe\safe_blackbox1.json", "r") as f:
    json_data = json.load(f)
# list
print(type(json_data), len(json_data))
# list
print(json_data[0]["METADATA"])
# print(type(json_data["METADATA"]))

# 파일 저장
with open(r"PythonPractice\Playground\transformJson\transformed_index_files\transformed_safe_blackbox1.json", "a") as f:
    f.write(json_data["TYPE"])
    f.write(json_data["FILE_ORIGINAL"])["original"]
    f.write(json_data["FILE_RESULT"])["result"]
    f.write(json_data["METADATA"])
    f.write(json_data["CENTER_X"])
    f.write(json_data["CENTER_Y"])
    f.write(json_data["WIDTH"])
    f.write(json_data["HEIGHT"])


# tmp = json_data["METADATA"]
# a = map(transform, tmp[3000:3005])
# # print(list(a)[0])
# print("FILE" in tmp[3000:3001][0]["fields"]["FROM"])
# print(tmp[3000:3001][0])
# b = map(transform, tmp[0:5])
# print(list(b))

# c = map(transform, tmp)
# print(list(c)[-5:][0])

# for i in range(len(tmp)):
#     if "XMIN" in tmp[i]["fields"]:
#         # 539: XMIN이 나오기 시작한 인덱스
#         print(i)
#         break
# # 전역적으로 i를 사용 가능
# print(i)

# d = map(transform, tmp[i:])
# # print(list(d))

# with open("./transformed_index_files/transformed_safe_blackbox1.json", "w") as f:
#     f.writelines(str(list(d)))
