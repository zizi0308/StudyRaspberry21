import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image


# 카메라 기본 틀
# 영상 캡쳐, 녹화
cap = cv2.VideoCapture(0)    # 번호 0부터 +1, 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 넓이와 높이 수동설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 25)
# 영상 코덱 설정
fource = cv2.VideoWriter_fourcc(*'XVID')
is_record = False   # 녹화상태


# 무한루프 (q를 입력할 때까지)
while True: # 반복문을 통해 웹캠을 지속함
    ret, frame = cap.read() # 카메라 현재 영상 로드 frame에 저장, ret T/F
    h, w, _ = frame.shape   # 값은 보낼건데 그 값이 필요없을 때 _사용
    now = datetime.datetime.now()
    currdt = now.strftime('%Y-%m-%d %H:%M:%S')
    filedt = now.strftime('%Y%m%d_%H%M%S')  # 20210720_164725 파일이름에 :사용시 에러

    if ret != True: break   # return이 False면 루프탈출

    frame = Image.fromarray(frame)  # 영상을 이미지 값으로 바꿈
    draw = ImageDraw.Draw(frame)    # 위의 것으로 draw작업을 위한 코드
    draw.text(xy=(10, (h-40)), text='실시간 영상입니다. - {0}'.format(currdt), font=font, fill=(0, 0, 255))
    frame = np.array(frame) # 이미지값에서 영상으로 다시 바꿈

    
    key = cv2.waitKey(1)
    if key == ord('q'): break  # q 입력시 루프탈출
    elif key == ord('c'):   # 화면캡쳐부분
        cv2.imwrite('./capture/img_{0}.png'.format(filedt), frame)
        print('이미지 저장 완료')
    elif key == ord('r') and is_record == False: # 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./capture/record_{0}.avi'.format(filedt), fource, 20, (w, h))
        print('녹화 시작')
    elif key == ord('r') and is_record == True: #레코드 종료
        is_record = False
        video.release() # 객체 해제
        print('녹화 완료')
    
    if is_record:
        video.write(frame)
        # 녹화중일때만 빨간 동그라미가 나옴
        cv2.circle(img=frame, center=(620, 15), radius=10, color=(0, 0, 255), thickness=1)

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움

cap.release()    # 웹캠 해제
cv2.destroyAllWindows()