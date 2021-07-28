from flask import Flask, request, render_template 	# 플라스크 모듈호출
import RPi.GPIO as GPIO
import time						
 
app = Flask(__name__)					# 플라스크 앱 생성
ledPin = 26
triggerPin = 14
echoPin = 4
pinPiezo = 2
sound = 6

GPIO.setwarnings(False)			        # 오류방지처리
GPIO.setmode(GPIO.BCM)		            # 핀넘버 호출모드 선택
GPIO.setup(ledPin, GPIO.OUT)		    # ledPin의 핀모드 설정(출력)
GPIO.setup(pinPiezo, GPIO.OUT)		    # pinPiezo의 핀모드 설정(출력)
GPIO.setup(sound, GPIO.OUT)		        # sound의 핀모드 설정(출력)
GPIO.setup(triggerPin, GPIO.OUT)	    # triggerPin의 핀모드 설정(출력)
GPIO.setup(echoPin, GPIO.IN)		    # echoPin의 핀모드 설정(입력)
Melody = [262, 294, 330, 349, 392, 440, 494, 523, 523, 494, 440, 392, 349, 330, 294, 262]		# pinPiezo의 소리를 설정하기 위한 배열
p = GPIO.PWM(ledPin, 255)		    # ledPin 초기화
Buzz = GPIO.PWM(pinPiezo, 100)		# pinPiezo 초기화
Alram = GPIO.PWM(sound, 440)		# sound 초기화
p.start(0)				# ledPin 시작
@app.route('/')		    # 웹표현 route()
def home():			    # home 함수 실행
    return render_template("index.html")	    # index.html을 받아서 페이지를 로드
@app.route('/leddata', methods = ['POST'])      # POST방식을 사용해 주소를 직접입력
def leddata():
   leddata = request.form['led']		 # 웹에서 데이터를 받기 위한 request.form[]
   if leddata == 'on':			         # 웹에서 on을 설정할 때
      while True:			            # 무한반복 실행
         for i in range(100):		    # i는 1부터 100까지
            p.ChangeDutyCycle(i)	    # ledPin의 출력값 변경
            time.sleep(0.1)		        # 100 millisecond 딜레이
         for i in reversed(range(100)):	# 이제 반대로 i는 100부터 1까지
            p.ChangeDutyCycle(i)	    # ledPin의 출력값 변경
            time.sleep(0.1)		        # 100 millisecond 딜레이
   else:					            # on이 아닐때
      GPIO.output(ledPin, GPIO.LOW)	    # ledPin 꺼지고
      GPIO.cleanup()			        # 리소스 해제
 
   return home()			            # 주소로 다시 리턴시켜줌(안시키면 오류)
@app.route('/ultrasonic', methods = ['POST'])   # POST 방식을 사용한 주소지정
def ultrasonic():				                # 초음파센서 실행을 위한 함수
   ultrasonic = request.form['sonic']	        # 웹데이터를 받기 위한 request.form[]
   if ultrasonic == 'on':			            # ultrasonic의 on버튼을 눌렀을 때
      while True:			                    # 무한반복문 실행
         GPIO.output(triggerPin, GPIO.HIGH)     # 트리거 펄스 송신
         time.sleep(0.00001)		            # 10us동안 트리거 펄스송신
         GPIO.output(triggerPin, GPIO.LOW)      # 측정할 수 있는 펄스를 만들기 위한 조건
         while GPIO.input(echoPin) == 0:        # 초음파 전송이 끝나는 전송시간 저장
            start = time.time()
         while GPIO.input(echoPin) == 1:        # 초음파 수신이 완료될때까지 수신시간 저장
            stop = time.time()

         rtTotime = stop - start		        # 시간측정
         distance = rtTotime * 34000 / 2	    # 시간을 거리로 변환(왕복이므로 %2)
         print("distance : %.2f cm" % distance)	# 거리 값 출력
         time.sleep(0.3)
         if (distance < 40) and (distance >= 20):		# 후방감지센서 알람조건식1
            Alram.start(50)				        # PWM 시작
            Alram.ChangeFrequency(349)		    # 주파수 설정 및 변경
            time.sleep(0.3)				        # 딜레이 시간 설정
            Alram.stop()
         elif (distance < 20) and (distance >= 10):	    # 후방감지센서 알람조건식2
            Alram.start(50)
            Alram.ChangeFrequency(349)
            time.sleep(0.2)				        # 딜레이 시간 변경
            Alram.stop()
         elif distance <= 9:			                # 후방감지센서 알람조건식3
            Alram.start(50)
            Alram.ChangeFrequency(349)
            time.sleep(0.1)				        # 딜레이 시간 변경
            Alram.stop()
   else:							        # off버튼 클릭 시
      GPIO.cleanup()					    # 할당된 리소스 해제
   return render_template("index.html")		# 다시 홈으로 리턴
@app.route('/sound', methods = ['POST'])    # POST 방식을 사용한 주소지정
def sound():					            # 피아노사운드 실행을 위한 함수
   sound = request.form['piano']            # 웹데이터를 받기 위한 request.form[]
   if sound == 'on':
      while True:
         Buzz.start(50)
         for i in range(0, len(Melody)):	# 배열의 길이를 구하기 위한 for문
            Buzz.ChangeFrequency(Melody[i])	# 위에 설정해둔 배열로 소리출력
            time.sleep(0.3)			  
         Buzz.stop()
         time.sleep(1)
   else:
      GPIO.cleanup()			
   return home()

if __name__ == "__main__":		            # 호스트와 포트를 할당 받아서 웹에 연결해줌
   app.run(host = "0.0.0.0", port = "8080") 