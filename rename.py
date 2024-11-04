import os
import shutil

# Path to the main folder
main_folder_path = '/home/divya/Desktop/OP1'

# Create directories for ground truth and input images if they don't exist
gt_directory = os.path.join(main_folder_path, 'Ground_Truth_Images')
input_directory = os.path.join(main_folder_path, 'Input_Images')

os.makedirs(gt_directory, exist_ok=True)
os.makedirs(input_directory, exist_ok=True)

# Function to rename and move files
def rename_and_move_files(subfolder, cell_number):
    for file_name in os.listdir(subfolder):
        if file_name.startswith('RawSIMData_gt.jpg'):
            new_name = f'cell{cell_number}_gt.jpg'
            new_path = os.path.join(gt_directory, new_name)
            shutil.move(os.path.join(subfolder, file_name), new_path)
            print(f'Moved {file_name} to {new_path}')
        elif file_name.startswith('RawSIMData_level_'):
            level_number = file_name.split('_')[-1].replace('.jpg', '')
            new_name = f'cell{cell_number}_level_{level_number}.jpg'
            new_path = os.path.join(input_directory, new_name)
            shutil.move(os.path.join(subfolder, file_name), new_path)
            print(f'Moved {file_name} to {new_path}')

# Iterate over each subfolder in the main folder
for subfolder in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, subfolder)
    if os.path.isdir(subfolder_path) and subfolder.startswith('Cell_'):
        cell_number = subfolder.split('_')[1]
        rename_and_move_files(subfolder_path, cell_number)

