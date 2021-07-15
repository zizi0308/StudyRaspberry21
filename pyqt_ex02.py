## Qt5 사용자 윈도우클래스 생성예제
import sys
from PyQt5.QtWidgets import *   # Qt5로 윈폼 만들기

# 윈도우 클래스 선언
class MyWindow(QMainWindow):    # Qt의 윈도우 클래스를 상속
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

# button = QPushButton('Click Me!')
# button.show()
# label = QLabel('Hello Qt5!')
# label.show()
win = MyWindow()
win.show()
app.exec_()
