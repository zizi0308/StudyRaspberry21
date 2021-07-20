import cv2
import numpy as np # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

# 이미지 로드 기본틀
# 이미지 대비
org = cv2.imread('./image/samsac.jpeg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('Original', org)  # 이미지 새창열림
cv2.imshow('Gray', gray)
cv2.imshow('Enhance', enhanced)

cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제