#!/usr/bin/env python
import os

directories = [directory for directory in os.listdir() if os.path.isdir(directory) if not directory.startswith(".")] 
files = [file_name for file_name in os.listdir() if (os.path.isfile(file_name) and file_name.endswith(".ipynb")) if not file_name.startswith(".")]
for file_name in files:
    os.system(f'jupyter nbconvert --to script {file_name}')
