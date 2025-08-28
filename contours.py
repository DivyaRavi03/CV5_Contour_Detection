import cv2
import numpy as np

img_path = "../images/test_img.jpg"

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if img is None:
	print(f"Error in {img_path}")
else:
	print("Image loaded")
	ret, binary = cv2.threshold(gray, 125,255,cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	print(f"There are {len(contours)} in the image")
	c_img = img.copy()
	cv2.drawContours(c_img, contours, -1, (0,255,0),2)
	print(f"The thresholding value is {ret}")
	cv2.imshow("The image", img)
	cv2.imshow("Binary", binary)
	cv2.imshow("Contours", c_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
