# 하위 디렉터리 검색하기
import os
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]   # os.path.splitext함수는 파일명을 확장자 기준으로 두 부분으로 나눈다. 따라서 [-1]은 확장자명이 된다.    
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
search('C:/')
''' 하위 디렉터리 검색을 쉽게 해주는 os.walk
for(path, dir, files) in os.walk('C:/'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print(('%s%s) %(payh, filename))
'''