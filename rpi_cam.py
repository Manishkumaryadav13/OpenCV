import cv2
import time
camera = cv2.VideoCapture(0)
i = 0
while i < 10:
    # input('Press Enter to capture')
    return_value, image = camera.read()
    cv2.imwrite('D:\cv Images\Image'+str(i)+'.png',image)
    i += 1
    print('Number of Images:', i)
    time.sleep(5)
del camera

