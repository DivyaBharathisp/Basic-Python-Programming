import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
image_size = (256, 256)  # Size of the hologram
shape_radius_list = [10, 20, 30, 40]  # Different radii for circular shapes
output_dir = 'circular_hologram_images'  # Directory to save holograms

def create_circle(image_size, radius):
    """ Create a synthetic circular shape image. """
    height, width = image_size
    y, x = np.ogrid[:height, :width]
    center = (height // 2, width // 2)
    distance = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    circle_image = (distance <= radius).astype(float)
    return circle_image

def generate_hologram(circle_image):
    """ Generate a synthetic hologram from a circular shape image. """
    height, width = circle_image.shape
    
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

# Generate and save circular holograms
for radius in shape_radius_list:
    circle_image = create_circle(image_size, radius)
    hologram = generate_hologram(circle_image)
    
    # Define filename based on radius
    filename = os.path.join(output_dir, f'circular_radius_{radius}.png')
    save_hologram(hologram, filename)

print(f"Saved circular holograms to '{output_dir}'")

