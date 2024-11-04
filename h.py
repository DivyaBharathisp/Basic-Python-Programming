import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
image_size = (256, 256)  # Size of the hologram
num_holograms = 20  # Number of holograms to generate
output_dir = 'circular_hologram_images'  # Directory to save holograms

def create_circle(image_size, radius, center):
    """ Create a synthetic circular shape image with a specified radius and center. """
    height, width = image_size
    y, x = np.ogrid[:height, :width]
    distance = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    circle_image = (distance <= radius).astype(float)
    return circle_image

def generate_hologram(circle_image):
    """ Generate a synthetic hologram from a circular shape image. """
    # Fourier Transform of the circle image
    circle_fft = np.fft.fft2(circle_image)
    
    # Hologram is the squared magnitude of the FFT
    hologram = np.abs(circle_fft)**2
    
    return np.fft.fftshift(hologram)

def save_hologram(hologram, filename):
    """ Save the hologram to a file. """
    plt.figure(figsize=(6, 6))
    plt.imshow(np.log1p(hologram), cmap='gray')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate and save multiple holograms
np.random.seed(42)  # For reproducibility

for i in range(num_holograms):
    # Randomly select radius and center position
    radius = np.random.randint(10, 50)  # Random radius between 10 and 50
    center = (np.random.randint(image_size[0]), np.random.randint(image_size[1]))  # Random center position

    # Create circle image and generate hologram
    circle_image = create_circle(image_size, radius, center)
    hologram = generate_hologram(circle_image)
    
    # Define filename based on the index
    filename = os.path.join(output_dir, f'hologram_{i+1}.png')
    save_hologram(hologram, filename)

print(f"Saved {num_holograms} holograms to '{output_dir}'")

