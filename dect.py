txt_data = "i like pizza🍕"
file_path = "test.txt"
try:
    with open(file_path, "w"):
        file_path.write(txt_data)
        print(f"text written to {file_path}")
except FileExistsError:
    print(f"file {file_path} already exists.")
    import os
