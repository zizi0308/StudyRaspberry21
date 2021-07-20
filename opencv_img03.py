import cv2
import numpy # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

# 이미지 로드 기본틀
org = cv2.imread('./image/samsac.jpeg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)


h, w, c = org.shape

cropped = org[:, :int(w/2)] # 원본(이미지 객체)을 배열로 자름(이미지 넓이 반으로 자르기)
# cropped = org[:int(h/2), :] # 원본(이미지 객체)을 배열로 자름(이미지 높이 반으로 자르기)

cv2.imshow('Original', org)  # cv 새창열림
cv2.imshow('Cropped', cropped)  # 반으로 자른 이미지

cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제