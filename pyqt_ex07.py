import cv2
import numpy as np
import sys
import datetime
from PIL import ImageFont, ImageDraw, Image
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# 함수선언
# 영상간의 차이나는 부분 표시 이미지, 차이나는 픽셀갯수 리턴함수
def get_diff_image(frame_a, frame_b, frame_c, threshold):
    # 3개의 모든 프레임을 회색으로 변환(경계선을 따기위해)
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # a, b 사이의 영상차이값, b, c사이의 영상차이값 구함
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray) # 둘다 초기에 찍힌것이기때문에 차이X
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray) # 차이날수도 안날수도 있음

    # 영상 차이값(경계 값이 다른 부분)이 40이상이면 값을 흰색으로 바꿔줌
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)  # 흰부분찾기
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)  # 흰부분찾기

    # 두 영상에서 공통된 부분은 1로만듦
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    # 영상에서 1이 된 부분을 확장(mophology)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt = cv2.countNonZero(diff)

    return diff, diff_cnt


# 카메라 기본 틀
# 움직임 발생시 화면캡쳐

cap = cv2.VideoCapture(0)    # 번호 0부터 +1, 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 넓이와 높이 수동설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 25)
# 영상 코덱 설정
fource = cv2.VideoWriter_fourcc(*'XVID')
is_record = False   # 녹화상태

threshold = 40  # 영상 차이가 나는 threshold 설정
diff_max = 10   # 영상 차이가 나는 최대픽셀수

# 최초의 이미지 필요 거기에 선을따서 흑백처리(Aframe) 후 얘를 반전(Bframe)시킴
# ab의 이미지와 bc의 이미지가 차이나면 그부분이 움직임 감지된 부분 
ret, frame_a = cap.read()   # 그냥 빈공간을 위해 필요하다고 생각하면 됨
ret, frame_b = cap.read()

# 무한루프 (q를 입력할 때까지)
while True: # 반복문을 통해 웹캠을 지속함
    now = datetime.datetime.now()
    currdt = now.strftime('%Y-%m-%d %H:%M:%S')
    filedt = now.strftime('%Y%m%d_%H%M%S')  # 20210720_164725 파일이름에 :사용시 에러
    ret, frame = cap.read() # 카메라 현재 영상 로드 frame에 저장, ret T/F
    h, w, _ = frame.shape   # 값은 보낼건데 그 값이 필요없을 때 _사용
    

    if ret != True: break   # return이 False면 루프탈출

    # 현재영상과 초기영상 비교, 움직임 감지
    diff, diff_cnt = get_diff_image(frame_a=frame_a, frame_b=frame_b, frame_c=frame, threshold=threshold)
    #print(diff_cnt)

    # 차이나는 이미지 갯수 차이가 10개 이상이 나면 움직임이 발생했다고 판단
    if diff_cnt > diff_max:
        cv2.imwrite('./capture/img_{0}.png'.format(currdt), frame)
        print('움직임 발생 이미지 캡쳐완료')

    # 움직임 결과 영상출력
    cv2.imshow('Diff Result', diff)

    # 이전값을 계속 집어넣어야지 계속 영상이 실행, 바뀐영상과 이전영상을 비교하기때문에 계속 업데이트필요
    frame_a = np.array(frame_b) # 이전화면 이전 
    frame_b = np.array(frame)   # 현재화면 이전

    frame = Image.fromarray(frame)  # 영상을 이미지 값으로 바꿈
    # draw = ImageDraw.Draw(frame)    # 위의 것으로 draw작업을 위한 코드
    # draw.text(xy=(10, (h-40)), text='실시간 영상입니다. - {0}'.format(currdt), font=font, fill=(0, 0, 255))
    frame = np.array(frame) # 이미지값에서 영상으로 다시 바꿈
    
    
    key = cv2.waitKey(1)
    if key == ord('q'): break  # q 입력시 루프탈출

    # cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움

cap.release()    # 웹캠 해제
cv2.destroyAllWindows()