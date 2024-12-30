import numpy as np
import cv2

image=np.ones((500,500,3),dtype=np.uint8)*255

for i in range(10):
    for j in range(10):
        if i==j or i+j==10-1:
            color=np.random.randint(0,254,size=3)
            image[i*50:(i+1)*50,j*50:(j+1)*50,:]=color
cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()