import cv2
import numpy as np
image=np.zeros((600,600),dtype='uint8')
def circle(image,r,center_x,center_y):
    h,w=image.shape
    for i in range(h):
        for j in range(w):
            if (center_x-i)**2+(center_y-j)**2<=r**2:
                image[i,j]=255
    return image

for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            image=circle(image,25,2*i*50,2*j*50)



cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
