import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn  # Bessel function of the first kind

# Parameters
image_size = (256, 256)  # Size of the hologram
shape_type = 'circle'    # Type of shape ('circle' or 'square')
shape_radius = 30        # Radius for circles or size for squares

def create_shape(shape_type, image_size, shape_radius):
    """ Create a synthetic shape image. """
    height, width = image_size
    y, x = np.ogrid[:height, :width]
    
    if shape_type == 'circle':
        center = (height // 2, width // 2)
        distance = np.sqrt((x - center[1])**2 + (y - center[0])**2)
        shape_image = (distance <= shape_radius).astype(float)
    
    elif shape_type == 'square':
        center = (height // 2, width // 2)
        shape_image = (
            (np.abs(x - center[1]) <= shape_radius) &
            (np.abs(y - center[0]) <= shape_radius)
        ).astype(float)
    
    else:
        raise ValueError("Unsupported shape_type. Use 'circle' or 'square'.")
    
    return shape_image

def generate_hologram(shape_image):
    """ Generate a synthetic hologram from a shape image. """
    height, width = shape_image.shape
    y, x = np.ogrid[:height, :width]
    kx, ky = np.meshgrid(np.fft.fftfreq(width), np.fft.fftfreq(height))
    
    # Fourier Transform of the shape image
    shape_fft = np.fft.fft2(shape_image)
    
    # Hologram is the squared magnitude of the FFT
    hologram = np.abs(shape_fft)**2
    
    return np.fft.fftshift(hologram)

# Create shape and hologram
shape_image = create_shape(shape_type, image_size, shape_radius)
hologram = generate_hologram(shape_image)

# Display the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title(f'Shape: {shape_type}')
plt.imshow(shape_image, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Synthetic Hologram')
plt.imshow(np.log1p(hologram), cmap='gray')  # Use log1p to better visualize the hologram
plt.colorbar()

plt.show()
