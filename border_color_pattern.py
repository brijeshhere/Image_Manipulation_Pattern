import numpy as np
import cv2

image=np.ones((500,500,3),dtype=np.uint8)*255

color=np.random.randint(0,255,size=3)
image[0:10,:]=color
image[:,0:10]=color
image[-10:,:]=color
image[:,-10:]=color
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()