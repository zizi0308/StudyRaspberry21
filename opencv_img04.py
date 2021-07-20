import cv2
import numpy as np # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

# 이미지 로드 기본틀
# 이미지 흐리게 하기(Blur)
# 이미지 선명하게 하기
org = cv2.imread('./image/samsac.jpeg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) # 회색이미지
blur = cv2.blur(org, (10, 10)) # 값이 클수록 흐릿해짐
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])    # 커널값은 이미 정해짐
sharp = cv2.filter2D(org, -1, kernel)

cv2.imshow('Original', org)  # 이미지 새창열림
cv2.imshow('Blur', blur)    # 흐리게 변경한 이미지
cv2.imshow('Sharp', sharp)

cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제