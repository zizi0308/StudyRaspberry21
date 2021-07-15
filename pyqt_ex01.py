## Qt5 베이스 프레임 소스
import sys
from PyQt5.QtWidgets import *   # Qt5로 윈폼 만들기

app = QApplication(sys.argv)
win = QWidget() # Qt에서는 위젯을 만들어서 직접코딩을 하고 그 다음에 디자인으로 넘어감
win.show()

app.exec_()