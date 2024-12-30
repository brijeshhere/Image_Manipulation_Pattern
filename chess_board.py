import cv2
import numpy as np
import time



num_block=5
toggle=1

while True:
    img=np.zeros((500,500),dtype='uint8')
    for i in range(num_block):
        for j in range(num_block):
            if (i+j+toggle)%2==0:
                img[i*100:(i+1)*100,j*100:(j+1)*100]=255


    cv2.imshow('image',img)
    toggle=1-toggle
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
    

# cv2.waitKey(0)
cv2.destroyAllWindows()