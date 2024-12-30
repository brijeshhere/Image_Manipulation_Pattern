import numpy as np
import cv2

image=np.zeros((500,500),dtype='uint8')
def random_box(image,i,j):
    img=np.zeros((50,50),dtype='uint8')
    for k in range(200):
          row=np.random.randint(0,50)
          col=np.random.randint(0,50)
          img[row,col]=255
    # center_x,center_y=2*i*50,2*j*50
    image[i:i+50,j:j+50]=img
    return image
for i in range(0,5):
    for j in range(0,5):
        if (i+j)%2==0:
            image[i*100:(i+1)*100,j*100:(j+1)*100]=255
            image=random_box(image,i*100+25,j*100+25)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
            