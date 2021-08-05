import cv2
import numpy as np

threshold = 30  # 영상 차이가 나는 threshold 설정
diff_max = 5    # 영상 차이가 나는 최대 픽셀 수

frame_a, frame_b, frame_c = None, None, None  # 프레임 초기화

# 카메라 기본 틀
# 움직임 발생시 사각형이 생성되어 움직임을 따라감
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

if cap.isOpened():
    ret, frame_a = cap.read()   # 첫번째 프레임 읽음
    ret, frame_b = cap.read()   # 두번째 프레임 읽음
    while ret:  # 움직임이 있을 때 동안
        ret, frame_c = cap.read()
        draw = frame_c.copy()   # 세번째 프레임을 복사한다
        if not ret: # 움직임이 없으면 >> ret : 움직임으로 인해 변한부분을 표시 T/F
            break
        # 모든 픽셀에 노이즈가 끼여있기에 프레임 2개로는 정확한 값 측정 어려움, 때문에 프레임 3개 씀
        frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
        frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
        frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

        # a, b 사이의 영상차이값, b, c사이의 영상차이값 구함
        diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray) # 둘다 초기에 찍힌것이기때문에 차이X
        diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray) # 차이날수도 안날수도 있음

        # 영상 차이값(경계 값이 다른 부분)이 40이상이면 값을 흰색으로 바꿔줌 
        ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)  # 흰부분찾기
        ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)  # 흰부분찾기
        
        # 두 영상 모두 움직임이 나타났을 때 >> 둘 다 1일 때
        diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

        # 영상에서 1이 된 부분을 확장(mophology) 
        # mophology 변환 : 영상이나 이미지를 Segmentation 하여 단순화, 제거, 보정을 통해 형태를 파악하는 목적으로 사용
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # 십자가형태의 구조요소생성, 중심점은 3,3
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)    # 이미지에 침식 적용 후 팽창적용 >> 가장자리 영역을 둥글게 만듬

        diff_cnt = cv2.countNonZero(diff)
        if diff_cnt > diff_max:
            nzero = np.nonzero(diff)    # diff는 영상과 사이즈가 같으며, a, b프레임의 차이 어레이를 의미(0이 아닌 값(차이)을 반환)
            cv2.rectangle(draw, (min(nzero[1]), 
                                min(nzero[0])), # diff가 0이 아닌 값 중 행,열이 가장 작은 포인트
                                (max(nzero[1]), # diff가 0이 아닌 값 중 행,열이 가장 큰 포인트
                                max(nzero[0])), 
                                (0, 255, 0), 2) # 사각형 색상 값, thickness = 2 # 이전값을 계속 집어넣어야지 계속 영상이 실행, 바뀐영상과 이전영상을 비교하기때문에 계속 업데이트필요
                                
            cv2.putText(draw, 'Motion detected!', (10, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
            
        stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_BAYER_GB2BGR))) # 두 배열(draw와 diff)을 왼쪽에서 오른쪽으로 붙임
        cv2.imshow('motion', stacked)
        
        # cv2.imshow('real', draw)
        # cv2.imshow('diff', diff)

        frame_a = frame_b
        frame_b = frame_c

        key = cv2.waitKey(1)
        if key == ord('q'): break  # q 입력시 루프탈출
