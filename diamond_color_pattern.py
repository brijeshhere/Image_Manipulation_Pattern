import numpy as np
import cv2

image=np.ones((500,500,3),dtype=np.uint8)*255
center_x,center_y=5,5
for i in range(10):
    for j in range(10):
        if abs(center_x-i)+abs(center_y-j)==4:
            color=np.random.randint(0,255,size=3)
            image[i*50:(i+1)*50,j*50:(j+1)*50,:]=color
            
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()