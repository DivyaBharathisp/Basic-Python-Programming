import os
import glob

# Path to the main folder
main_folder_path = '/home/divya/Desktop/OP1'

# Iterate over each subfolder in the main folder
for subfolder in glob.glob(os.path.join(main_folder_path, 'Cell_*')):
    # Construct the path to the specific file
    file_to_delete = os.path.join(subfolder, 'SIM_gt.jpg')
    
    # Check if the file exists and delete it
    if os.path.isfile(file_to_delete):
        os.remove(file_to_delete)
        print(f"Deleted: {file_to_delete}")
    else:
        print(f"File not found: {file_to_delete}")

