from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

filename = raw_input("Insert image filename: ")
try:
    image = Image.open(filename)
except IOError:
    print("Can't find image '" + str(filename) + "' please give correct image filename")
    exit()

print("> Reading image's pixel ...")
pixel = np.array(image)
pixel.shape

# Array of pixels to be calculated in histogram
pixel_r = np.zeros(pixel.shape[0:2], pixel.dtype)
pixel_g = np.zeros(pixel.shape[0:2], pixel.dtype)
pixel_b = np.zeros(pixel.shape[0:2], pixel.dtype)
pixel_gray = np.zeros(pixel.shape[0:2], pixel.dtype)

for i, row in enumerate(pixel):
    for j, pix in enumerate(row):
        pixel_r[i][j] = pix[0]
        pixel_g[i][j] = pix[1]
        pixel_b[i][j] = pix[2]
        pixel_gray[i][j] = np.uint8(pix.mean())

pixel_r = np.ndarray.flatten(pixel_r)
pixel_g = np.ndarray.flatten(pixel_g)
pixel_b = np.ndarray.flatten(pixel_b)
pixel_gray = np.ndarray.flatten(pixel_gray)

print("> Displaying histogram for R channel ...")
plt.hist(pixel_r, range= (0, 255), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram Cannel R")
plt.savefig("output/histogram_r.png", bbox_inches='tight')
plt.show()

print("> Displaying histogram for G channel ...")
plt.hist(pixel_g, range= (0, 255), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram Cannel G")
plt.savefig("output/histogram_g.png", bbox_inches='tight')
plt.show()

print("> Displaying histogram for B channel ...")
plt.hist(pixel_b, range= (0, 255), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram Cannel B")
plt.savefig("output/histogram_b.png", bbox_inches='tight')
plt.show()

print("> Displaying histogram for Grayscale channel ...")
plt.hist(pixel_gray, range= (0, 255), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram Gray Image")
plt.savefig("output/histogram_gray.png", bbox_inches='tight')
plt.show()


print("> End of program.")