import os
path = input('enter root dir path: ')
path.replace('\\', '/')
os.chdir(path)

files_oldname = os.listdir()
files_newname_prefix = input('enter files newname suffix: ')
files_extension_index = files_oldname[0].find('.png')
files_extension = files_oldname[0][files_extension_index:]

for index, item in enumerate(files_oldname):
  os.rename(files_oldname[index], f'{files_newname_prefix}_{index}{files_extension}')
