import os

File_path = "test.txt"
if os.path.exist(File_path):
    if os.path.isfile(File_path):
        print("it exixts{test.txt}")
    elif os.path.isdir(File_path):
        print("That is a directory")
    else:
        print("doest exist")
