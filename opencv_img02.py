import cv2
import numpy # 행렬이나 배열 수식처리를 하기위한 라이브러리 (C#은 리스트나 행렬이 포함되있음)

org = cv2.imread('./image/samsac.jpeg', cv2.IMREAD_REDUCED_COLOR_2)   # 크기 반으로
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape # 이미지 객체의 속성을 다 가져옴 변환객체(Gray)는 같은 타입이 아님
print('Width:{0}, Height:{1}, Channel:{2}'.format(w, h, c))
size_small = cv2.resize(gray, dsize=(int(w/2),int(h/2)))    # 사이즈 변경

cv2.imshow('Original', org)  # cv 새창열림
cv2.imshow('Gray', gray)
cv2.imshow('Resize', size_small)

cv2.waitKey(0)  # 창에서 키입력 대기 (이게 없으면 창이 열리고 바로 꺼짐)
cv2.destroyAllWindows() # 메모리 해제