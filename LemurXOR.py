from PIL import Image
import numpy as np

# Load images
img1 = Image.open("lemur.png").convert("RGB")
img2 = Image.open("flag.png").convert("RGB")

# Ensure images are the same size
if img1.size != img2.size:
    raise ValueError("Images must be the same size")

# Convert images to NumPy arrays
arr1 = np.array(img1)
arr2 = np.array(img2)

# Perform XOR operation on RGB values
xor_result = np.bitwise_xor(arr1, arr2)

# Convert the result back to an image
xor_image = Image.fromarray(xor_result)

# Save or show the image
xor_image.save("xor_result.png")
xor_image.show()
print('done')