# QT Designer 연동소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui', self)

        # ui에 있는 위젯의 시그널처리(컨트롤 이벤트 처리)
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)
        self.TblResult.itemSelectionChanged.connect(self.TblResult_Selected)
        self.TxtSearchword.returnPressed.connect(self.btnSearch_Clicked)    # 엔터치면 검색
    
    def TblResult_Selected(self):
        selected = self.TblResult.currentRow()  # 현재 선택된 열의 인덱스
        url = self.TblResult.item(selected, 1).text()
        # QMessageBox.about(self, 'URL', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.TblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.TblResult.setColumnCount(2)
        self.TblResult.setRowCount(len(result))

        self.TblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            title = post['title'].replace('&lt;', '<').replace('&gt', '>').replace('<b>', '').replace('</b>', '').replace('&quot;',"''")
            self.TblResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.TblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.TblResult.setColumnWidth(0, 400)
        self.TblResult.setColumnWidth(1, 300)
        self.TblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # C# readonly


    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.TxtSearchword.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를 입력하세요')
            return

        # naver API Search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items'] # item 리스트 분리
        print(len(jsonResult))
        self.StsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        # print(jsonSearch)
        # model = QtGui.QStandardItemModel()  # 새로운 모델생성
        # self.lsvResult.setModel(model)  # 리스트형태로 필요한 컬럼들을 집어넣음(model에)
        

        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
