import numpy as np
import cv2
from datetime import datetime

while True:
    img=np.ones((500,500,3),dtype=np.uint8)*255
    cv2.putText(img,datetime.now().strftime("%H:%M:%S"),(25,25),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(200,190,0),thickness=3)

    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()