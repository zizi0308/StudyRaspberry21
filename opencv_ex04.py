import cv2
import numpy as np

org = cv2.imread('./image/samsac.jpeg') # 이미지 로드
dst = cv2.resize(org, dsize=(640, 480)) # 이미지 크기 조정

center = (250, 250) # x, y
color = (0, 0, 255)

cv2.rectangle(dst, (100, 100), (500, 300), (255, 0, 0)) # 사각형은 시작점과 끝점이 같이 있어야 함
cv2.circle(dst, center, 30, color)
cv2.imshow('dest', dst) # 이미지 창 띄우기

cv2.waitKey(0)  # 키 대기
cv2.destroyAllWindows() # OpenCV 인스턴스 종료