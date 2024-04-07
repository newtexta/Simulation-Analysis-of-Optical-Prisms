from color import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os

class colordialog1(QDialog,Ui_Dialog):
    def __init__(self):
        super(colordialog1,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.colordialog)

    def colordialog(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit.setText(HTMLcolor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = colordialog1()
    win.show()
    sys.exit(app.exec())

os.system("python colorrun.py")
