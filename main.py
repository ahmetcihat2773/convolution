import numpy as np 
import cv2
from matplotlib import pyplot as plt 
from skimage.util import random_noise

def show_img(img,title):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




img = cv2.imread('images/harold_original.jpg',0)
cv2.imwrite('images/harold_gray.jpg', img)
show_img(img,"Original Image")
# original image
img_noise = random_noise(img, mode='gaussian')
show_img(img_noise,"Image with Noise")
cv2.imwrite('images/harold_gray_noise.jpg', img_noise)
# Averaging Filter
kernel = np.ones((5,5),np.float32)/25
img_filtered_avg = cv2.filter2D(img,-1,kernel)
show_img(img_filtered_avg,"Averaged Filter Applied")
cv2.imwrite('images/harold_gray_filtered.jpg', img_filtered_avg)
# Gaussian Filtering
img_filtered_noise = cv2.GaussianBlur(img_noise,(5,5),1)
show_img(img_filtered_noise,"Gaussian Filter")
