import os
import mrcfile
import numpy as np
from PIL import Image

def convert_mrc_to_png(input_folder, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.mrc'):
            # Construct full file path
            mrc_filepath = os.path.join(input_folder, filename)
            # Open the .mrc file
            with mrcfile.open(mrc_filepath) as mrc:
                data = mrc.data
                # Normalize data to 0-255 range and convert to uint8
                data = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)
                img = Image.fromarray(data)
                # Save as .png with the same base name
                png_filename = os.path.splitext(filename)[0] + '.png'
                output_filepath = os.path.join(output_folder, png_filename)
                img.save(output_filepath)
                print(f'Converted {mrc_filepath} to {output_filepath}')

# Define the input and output paths
input_folder = '/home/divya/Desktop/Programs/DATSETDFCAN/input'
output_folder = '/home/divya/Desktop/Programs/DATSETDFCAN/output'

# Run the conversion
convert_mrc_to_png(input_folder, output_folder)

