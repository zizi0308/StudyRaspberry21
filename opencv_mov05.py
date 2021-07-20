import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image


# 카메라 기본 틀
# 영상에 글자 출력
cap = cv2.VideoCapture(0)    # 번호 0부터 +1, 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 넓이와 높이 수동설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 25)


# 무한루프 (q를 입력할 때까지)
while True: # 반복문을 통해 웹캠을 지속함
    ret, frame = cap.read() # 카메라 현재 영상 로드 frame에 저장, ret T/F
    h, _, _ = frame.shape   # 값은 보낼건데 그 값이 필요없을 때 _사용
    now = datetime.datetime.now()
    currdt = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True: break   # return이 False면 루프탈출

    frame = Image.fromarray(frame)  # 영상을 이미지 값으로 바꿈
    draw = ImageDraw.Draw(frame)    # 위의 것으로 draw작업을 위한 코드
    draw.text(xy=(10, (h-40)), text='실시간 영상입니다. - {0}'.format(currdt), font=font, fill=(0, 0, 255))
    frame = np.array(frame) # 이미지값에서 영상으로 다시 바꿈

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움
    if cv2.waitKey(1) == ord('q'): break  # q 입력시 루프탈출

cap.release()    # 웹캠 해제
cv2.destroyAllWindows()