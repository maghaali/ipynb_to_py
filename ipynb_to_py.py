#!/usr/bin/env python
"""
This script goes through all subdirectories, finds all `.ipynb` files and converts them to `.py`
"""
import os
import time


tup_ = os.walk(".", topdown=True, onerror=None, followlinks=False)
converted_list = []
start_time = time.time()
print("Converting started: ")
print("="*20)
for (dirpath, dirnames, filenames) in tup_:
    for filename in filenames:
        if filename.endswith(".ipynb"):
            file_path = os.path.join(dirpath, filename)
            converted_list.append(file_path)
            os.system(f'jupyter nbconvert --to script {file_path}')

with open("ipynb_to_py_converted_list.txt", "w") as file:
    file.write('\n'.join(converted_list))

end_time = time.time()
print("="*20)
print("List of converted files is available in: 'ipynb_to_py_converted_list.txt'")
print(f"Totally {len(converted_list)} files converted in {end_time - start_time} second")
