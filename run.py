import os
import shutil
from os.path import isfile, join, isdir

# # Define paths
# data_path = os.getenv('DATA_PATH', r"C:\Users\nob40\OneDrive - Newcastle University\040 - Move_Inputs_To_Outputs\data")
# inputs_path = os.path.join(data_path, 'inputs')
# outputs_path = os.path.join(data_path, 'outputs')
# if not os.path.exists(outputs_path):
#     os.mkdir(outputs_path)

# # fetch all files
# for file_name in os.listdir(inputs_path):
#     # construct full file path
#     source = inputs_path +"\\" +file_name
#     print(source)
#     destination = outputs_path +"\\"+ file_name
#     print(destination)
#     # move only files
#     if os.path.isfile(source):
#         shutil.move(source, destination)

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
    