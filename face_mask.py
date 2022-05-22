import cv2
import numpy as np

face_img = cv2.imread("cropped2.jpg")
face_img_ycrcb = cv2.cvtColor(face_img, cv2.COLOR_BGR2YCrCb)

#YCbCr Color Space내에서 사람의 피부는 (0,133,77) ~ (255,173,127) 영역 내에 존재
lower = np.array([0,133,77], dtype = np.uint8)
upper = np.array([255,173,127], dtype = np.uint8)
#inRange함수는 특정 이미지 데이터의 상/하한선을 정해놓고 
# 그 안에 들어오는 pixel들은 1 나머지는 0으로 만드는 함수
skin_msk = cv2.inRange(face_img_ycrcb, lower, upper)

skin = cv2.bitwise_and(face_img, face_img, mask = skin_msk)
cv2.imwrite("skin2.jpg",skin)