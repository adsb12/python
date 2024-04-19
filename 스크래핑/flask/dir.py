import os

file_name = "java"
f_dir = os.path.dirname(os.path.realpath(__file__)) + f"\\{file_name}.csv"
print(f_dir)