# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Print the covariance matrix
# Load the image into an array: image
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

print(type(new_pixels))
# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)
print(new_pixels.shape)
print(new_image.shape)

# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.imshow(new_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')


# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(np.array(new_pixels), bins=64, range=(0,256), normed=False, alpha=0.4,  color='red')
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()
