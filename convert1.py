import os
from PIL import Image

# Function to downscale an image
def convert_to_lr(image_path, scale_factor):
    # Open the image
    img = Image.open(image_path)

    # Get original dimensions
    original_width, original_height = img.size

    # Calculate new dimensions
    new_width = original_width // scale_factor
    new_height = original_height // scale_factor

    # Resize image
    img_lr = img.resize((new_width, new_height), Image.BICUBIC)

    return img_lr

# Paths to HR and LR folders
hr_folder = '/home/divya/Desktop/retinal images/HR'
lr_folder = '/home/divya/Desktop/retinal images/LR'
scale_factor = 4  # Downscaling by a factor of 4

# Create LR folder if it doesn't exist
os.makedirs(lr_folder, exist_ok=True)

# Loop through all .ppm files in the HR folder
for filename in os.listdir(hr_folder):
    if filename.endswith('.ppm'):  # Filter for .ppm images
        hr_image_path = os.path.join(hr_folder, filename)
        lr_image = convert_to_lr(hr_image_path, scale_factor)

        # Save LR image to the destination folder
        lr_image_path = os.path.join(lr_folder, filename)
        lr_image.save(lr_image_path)

print("Conversion completed!")
