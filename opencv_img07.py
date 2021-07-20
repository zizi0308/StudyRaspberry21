import cv2
import numpy as np # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

# 이미지 로드 기본틀
# 이미지 대비
org = cv2.imread('./image/samsac.jpeg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, 0, (0,255,0), 2)
cv2.imshow('Result', org)

cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제