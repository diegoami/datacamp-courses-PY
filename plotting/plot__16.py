# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity)

# Display the intensity with a colormap of 'gray'
plt.imshow(X=intensity,cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()

