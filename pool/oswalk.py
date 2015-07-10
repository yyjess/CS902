import os
filelist = []
rootdir = "C:\Users\yyjess\Downloads"
for root, subFolders, files in os.walk(rootdir):
    print (root, subFolders, files)
    print
    print

print

for file in files:
    if file.find(".pdf") != -1:
        file_dir_path = os.path.join(root, file)
        filelist.append(file_dir_path)
for i in filelist:
    print i
