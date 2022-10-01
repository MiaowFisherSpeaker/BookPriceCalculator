import sys
import pic_rc
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI import Ui_MainWindow
from Table import Ui_TableCheckWindow


def newData(bookid: int, bookName: str, Pre: float, rate: float, Now: float, Pra: float):
    return {bookid: {"名称": bookName, "原价": Pre, "折扣": rate, "折后": Now, "应交": Pra}}


class TableWindow(QMainWindow):
    def __init__(self):
        super(TableWindow, self).__init__()
        self.ui = Ui_TableCheckWindow()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = {}  # book: bookInfo
        self.cb_selected = set()

        self.initData()  # 存放数据
        self.initCb()  # 复选框绑定动作槽

        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.pushButton_2.clicked.connect(self.search)
        self.ui.pushButton_3.clicked.connect(self.priceCheck)
        # self.logger(1)

    def logger(self, flag=0):
        print(type(self.data))
        print(self.cb_selected)

    def changecb(self, update_num):
        if update_num == 1:
            if self.ui.checkBox_01.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 2:
            if self.ui.checkBox_02.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 3:
            if self.ui.checkBox_03.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 4:
            if self.ui.checkBox_04.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 5:
            if self.ui.checkBox_05.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 6:
            if self.ui.checkBox_06.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 7:
            if self.ui.checkBox_07.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 8:
            if self.ui.checkBox_08.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 9:
            if self.ui.checkBox_09.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 10:
            if self.ui.checkBox_10.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        elif update_num == 11:
            if self.ui.checkBox_11.isChecked():
                self.cb_selected.add(update_num)
            else:
                self.cb_selected.discard(update_num)
        # print(self.cb_selected)

    def search(self):
        if len(self.cb_selected) >= 2:
            QMessageBox.critical(None, "错误提示", "只能选择一个", QMessageBox.Ok)
        elif len(self.cb_selected) < 1:
            QMessageBox.critical(None, "错误提示", "至少选择一个", QMessageBox.Ok)
        else:
            processed_data = self.data[list(self.cb_selected)[0]]
            bookName = processed_data["名称"]
            Pre = str(processed_data["原价"])
            rate = str(processed_data["折扣"])
            Now = str(processed_data["折后"])
            Pra = str(processed_data["应交"])
            self.ui.lineEdit_02.setText(bookName)
            self.ui.lineEdit_03.setText(Pre)
            self.ui.lineEdit_04.setText(rate)
            self.ui.lineEdit_05.setText(Now)
            self.ui.lineEdit_06.setText(Pra)
            # print(bookName)

    def calculate(self):
        bookIdLst = list(self.cb_selected)
        if len(bookIdLst) == 0:
            QMessageBox.critical(None, "错误提示", "请至少选择一个再计算", QMessageBox.Ok)
            self.ui.lineEdit_01.setText("0")
        else:
            price_list = []
            # print(bookIdLst)
            for i in bookIdLst:
                bookInfo = self.data[i]
                price_list.append(bookInfo["应交"])
            total_price = "%.2f" % sum(price_list)
            self.ui.lineEdit_01.setText(total_price)

    def priceCheck(self):
        self.table = TableWindow()
        self.table.show()

    def initCb(self):
        self.ui.checkBox_01.stateChanged.connect(lambda: self.changecb(1))
        self.ui.checkBox_02.stateChanged.connect(lambda: self.changecb(2))
        self.ui.checkBox_03.stateChanged.connect(lambda: self.changecb(3))
        self.ui.checkBox_04.stateChanged.connect(lambda: self.changecb(4))
        self.ui.checkBox_05.stateChanged.connect(lambda: self.changecb(5))
        self.ui.checkBox_06.stateChanged.connect(lambda: self.changecb(6))
        self.ui.checkBox_07.stateChanged.connect(lambda: self.changecb(7))
        self.ui.checkBox_08.stateChanged.connect(lambda: self.changecb(8))
        self.ui.checkBox_09.stateChanged.connect(lambda: self.changecb(9))
        self.ui.checkBox_10.stateChanged.connect(lambda: self.changecb(10))
        self.ui.checkBox_11.stateChanged.connect(lambda: self.changecb(11))

    def initData(self):
        self.data.update(newData(1, "概率论与数理统计学习指导练习", 38, 0.87, 33.06, 33.06))
        self.data.update(newData(2, "基础化学实验", 89, 0.87, 77.43, 77.43))
        self.data.update(newData(3, "基础有机化学上册", 89, 0.87, 77.43, 77.43))
        self.data.update(newData(4, "大学数学4", 40.7, 0.87, 35.409, 35.41))
        self.data.update(newData(5, "基因克隆与DNA分析", 47, 0.87, 40.89, 40.89))
        self.data.update(newData(6, "毛概", 25, 1, 25, 25.00))
        self.data.update(newData(7, "生物化学原理", 128, 0.87, 111.36, 111.36))
        self.data.update(newData(8, "人体解剖生理学", 58, 0.87, 50.46, 50.46))
        self.data.update(newData(9, "大学物理实验", 67, 0.87, 58.29, 58.29))
        self.data.update(newData(10, "数学分析", 46.8, 0.87, 40.716, 40.72))
        self.data.update(newData(11, "常微分方程", 39.8, 0.87, 34.626, 34.63))


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
