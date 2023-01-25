import numpy as np
from PIL import Image


def rms(array1, array2):
    return np.sqrt(((array1 - array2) ** 2).mean())

def edges(pix_list):       #get the edge and return array
    return np.array(pix_list)

img1 = Image.open("eifel02.jpg")
img2 = Image.open("eifel.jpg")


size1 = img1.size
size2 = img2.size


#___________ list of pixel image 1____________
right_img1 = []
left_img1 = []
up_img1 = []
down_img1 = []

#___________ list of pixel image 2____________
right_img2 = []
left_img2 = []
up_img2 = []
down_img2 = []

#loop on image 1
for i in range(size1[0]):
    in_pixel = img1.getpixel((i, 0))
    up_img1.append(in_pixel)

for i in range(size1[0]):
    in_pixel = img1.getpixel((i, size1[1] - 1))
    down_img1.append(in_pixel)

for j in range(size1[1]):
    in_pixel = img1.getpixel((size1[0] - 1, j))
    right_img1.append(in_pixel)


for j in range(size1[1]):
    in_pixel = img1.getpixel((0, j))
    left_img1.append(in_pixel)



for i in range(size2[0]):
    in_pixel = img2.getpixel((i, 0))
    up_img2.append(in_pixel)

for j in range(size2[1]):
    in_pixel = img2.getpixel((size2[0] - 1, j))
    right_img2.append(in_pixel)

for i in range(size2[0]):
    in_pixel = img2.getpixel((i, size2[1] - 1))
    down_img2.append(in_pixel)

for j in range(size2[1]):
    in_pixel = img2.getpixel((0, j))
    left_img2.append(in_pixel)


if size1[0] == size2[0] == size1[1] == size2[1]:
    rms_min = min(rms(edges(up_img1), edges(down_img2)),
                  rms(edges(down_img1), edges(up_img2)),
                  rms(edges(right_img1), edges(left_img2)),
                  rms(edges(left_img1), edges(right_img2)))

elif size1[0] == size2[0]:
    rms_min = min(rms(edges(up_img1), edges(down_img2)),
                  rms(edges(down_img1), edges(up_img2)))

elif size1[1] == size2[1]:
    rms_min = min(rms(edges(left_img1), edges(right_img2)),
                  rms(edges(right_img1), edges(left_img2)))

# rms value

if rms_min == rms(edges(up_img1), edges(down_img2)):
    new_image = Image.new('RGB', (size1[0], (2 * size1[1])))
    new_image.paste(img2, (0, 0))
    new_image.paste(img1, (0, size2[1]))
    new_image.show()


elif rms_min == rms(edges(down_img1), edges(up_img2)):
    new_image = Image.new('RGB', (size1[0], (2 * size1[1])))
    new_image.paste(img1, (0, 0))
    new_image.paste(img2, (0, size1[1]))
    new_image.show()


elif rms_min == rms(edges(right_img1), edges(left_img2)):
    new_image = Image.new('RGB', (2 * size1[0], size1[1]))
    new_image.paste(img1, (0, 0))
    new_image.paste(img2, (size1[0], 0))
    new_image.show()


elif rms_min == rms(edges(left_img1), edges(right_img2)):
    new_image = Image.new('RGB', (2 * size1[0], size1[1]))
    new_image.paste(img2, (0, 0))
    new_image.paste(img1, (size1[0], 0))
    new_image.show()