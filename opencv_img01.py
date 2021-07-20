import cv2
import numpy # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

org = cv2.imread('./image/samsac.jpeg')

cv2.imshow('Original', org)  # cv 새창열림
cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제