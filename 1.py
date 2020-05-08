import cv2
import numpy as np

from PIL import ImageGrab
from matplotlib import pyplot as plt

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def ShowImage(pilImage):
	# convert to opencv readable
	img = np.array(pilImage)

	img = image_resize(img, height = 500)

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	# grey scale 
	img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


	#cv2.imshow('image',img)
	cv2.imshow('image_gray', img_gray)

	# show histogram
	plt.rcParams['toolbar'] = 'None'
	plt.hist(img_gray.ravel(), 256, [0, 256])
	plt.axis('off')
	plt.show() 

	cv2.waitKey(0)
	cv2.destroyAllWindows()


# only work for copying actual image data
imgToRead = ImageGrab.grabclipboard()
print(imgToRead)

# pass to opencv
if imgToRead != "None":
	ShowImage(imgToRead)
else:
	print("no image is found")