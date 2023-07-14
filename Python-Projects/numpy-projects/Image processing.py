# Image processing: Implement a basic image filter using NumPy arrays.

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def apply_filter(image, kernel):
    # Get image dimensions
    height, width = image.shape

    # Get kernel dimensions
    k_height, k_width = kernel.shape

    # Calculate padding sizes
    pad_height = k_height // 2
    pad_width = k_width // 2

    # Create padded image
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Create output image
    output_image = np.zeros_like(image)

    # Apply filter
    for i in range(height):
        for j in range(width):
            output_image[i, j] = np.sum(padded_image[i:i+k_height, j:j+k_width] * kernel)

    return output_image

# Load image
image = Image.open("input_image.jpg").convert("L")
image = np.array(image)

# Define the filter kernel (averaging filter)
kernel = np.ones((3, 3)) / 9

# Apply the filter
filtered_image = apply_filter(image, kernel)

# Display the original and filtered images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(image, cmap='gray')
ax1.set_title('Original Image')
ax1.axis('off')
ax2.imshow(filtered_image, cmap='gray')
ax2.set_title('Filtered Image')
ax2.axis('off')
plt.show()
