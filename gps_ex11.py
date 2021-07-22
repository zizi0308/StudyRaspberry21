import serial # 시리얼통신 모듈

# GPS 함수
def get_GPS_INFO(buffer):
    nmea_latitude = buffer[1] # 위도
    nmea_longitude = buffer[3] # 경도
    # 3507.061040 / 12905.427695
    # print('{0} / {1}'.format(nmea_latitude, nmea_longitude))
    
    latitude = convert_to_degree(nmea_latitude)
    longitude = convert_to_degree(nmea_longitude)
    # 35.1177N / 129.0905E
    print('{0} / {1}'.format(latitude, longitude))

# 정확한 위도, 경도 값을 구하기 위한 함수(100만 곱한다고 되는게 아님)
def convert_to_degree(raw_value):
    decimal_value = float(raw_value) / 100.00   # float 값
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - degrees)/0.6
    position = '%.4f' %(degrees + mm_mmmm)
    return position


# 초기화
tag_info = 'GNGGA,' # 위치 NMEA 내가 쓰는 GPS모듈값 확인필요(GPGGA도 있음)
ser = serial.Serial('/dev/ttyS0', baudrate=9600) #시리얼 객체 생성

# 무한루프
try:
    while True:
        if ser.readable():
            res = ser.readline()    # 데이터 한 줄씩 읽기
            try:
                rec_data = res.decode(encoding='utf-8')[:len(res)-1]
                #print(res_data)
                tag_available = rec_data.find(tag_info)
                if (tag_available > 0):
                    buffer = rec_data.split(tag_info, 1)[1]
                    #print(buffer)
                    nmea_buf = buffer.split(',')    # ,값으로 잘라서 배열로 만듬
                    get_GPS_INFO(nmea_buf)  # 처리할 일이 있으면 함수로 만들어서 사용(위로)
            except:
                pass
except KeyboardInterrupt:
    print('GPS 종료')