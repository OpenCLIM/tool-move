import os
import shutil
from os.path import isfile, join, isdir

# move files to output dir
result_data_dir = '/data/inputs'
output_data_dir = '/data/outputs'

# make output dir if not exists
os.makedirs(output_data_dir, exist_ok=True)

if not os.path.exists(output_data_dir):
    os.mkdir(output_data_dir)
    print("couldn't find")

# fetch all files
for file_name in os.listdir(result_data_dir):
    # construct full file path
    print(file_name)
    source = os.path.join(result_data_dir,file_name)
    destination = os.path.join(output_data_dir, file_name)
    #move only files
    print(source)
    print(destination)
    if os.path.isfile(source):
        dest = shutil.move(result_data_dir + '/' + file_name, output_data_dir + '/' + file_name)
        print("File is moved successfuly to: ",dest)
    
