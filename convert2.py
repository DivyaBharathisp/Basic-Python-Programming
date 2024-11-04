from PIL import Image
import os

# Function to convert .ppm images in a folder to .jpg and save them in the output folder
def convert_ppm_to_jpg(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".ppm"):
            # Open the .ppm image
            img = Image.open(os.path.join(input_folder, filename))
            
            # Replace .ppm with .jpg in the filename
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            
            # Save the image in .jpg format
            img.save(os.path.join(output_folder, jpg_filename), "JPEG")

            print(f"Converted {filename} to {jpg_filename}")

# Specify your input and output folders for both directories
input_folder1 = '/home/divya/Desktop/retinal images/HR'
output_folder1 = '/home/divya/Desktop/retinal images/HR1'

input_folder2 = '/home/divya/Desktop/retinal images/LR'
output_folder2 = '/home/divya/Desktop/retinal images/LR1'

# Convert all .ppm images in the first and second input folders to .jpg
convert_ppm_to_jpg(input_folder1, output_folder1)
convert_ppm_to_jpg(input_folder2, output_folder2)
