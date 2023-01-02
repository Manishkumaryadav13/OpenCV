import cv2
import time
camera = cv2.VideoCapture(0)
i = 0
while i < 10:
    return_value, image = camera.read()
    cv2.imwrite('D:\cv Images\Image'+str(i)+'.png',image) # image Loaction+file extension
    img = cv2.imread('D:\cv Images\Image' + str(i) + '.png', 1) # 1 for color image
    cv2.imshow('Image' + str(i), img) # to display image
    print('Number of Images:', i)
    cv2.waitKey(2) #to wait in seconds
    time.sleep(3)
    # print("\n")
    cv2.destroyAllWindows() # to close the image window
    i += 1
    time.sleep(2)
del camera

