import cv2
import numpy as np

# 카메라 기본 틀
# 영상 자르기
cap = cv2.VideoCapture(0)    # 번호 0부터 +1, 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 넓이와 높이 수동설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한루프 (q를 입력할 때까지)
while True: # 반복문을 통해 웹캠을 지속함
    ret, frame = cap.read() # 카메라 현재 영상 로드 frame에 저장, ret T/F
    blur = cv2.blur(frame, (50, 50))    # 값이 클수록 흐릿해짐
    h, w, c = frame.shape
    noise = np.uint8(np.random.normal(loc=0, scale=80, size=[h, w, c]))  # 원본보다 색상을 줄이는게 노이즈
    noise_img = cv2.add(frame, noise) # 원본 이미지에 노이즈 추가

    if ret != True: break   # return이 False면 루프탈출

    total = cv2.hconcat([frame, noise_img]) # 화면을 하나로 합침(가로로), 세로는 vconcat활용
    cv2.imshow('Concat', total)
    #cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움
    #cv2.imshow('Blur Result', blur)
    #cv2.imshow('Noise Result', noise_img)

    if cv2.waitKey(1) == ord('q'): break  # q 입력시 루프탈출

cap.release()    # 웹캠 해제
cv2.destroyAllWindows()