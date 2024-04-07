from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSvg
from PyQt5.QtSvg import QSvgRenderer,QSvgWidget
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QMainWindow, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from widget2 import mywidget2
from opengl2 import RubikCubeWindow
import os
import sys

class mywidget(QtWidgets.QWidget):
    def __init__(self):
        super(mywidget,self).__init__()
        self.setObjectName("mywidget")
        self.resize(1140,760)
        self.widget2 = mywidget2()
        self.drag_region = self.widget2.rect()
        layout = QtWidgets.QVBoxLayout(self)
        self.widget2.pushButton.clicked.connect(self.showMinimized)
        self.widget2.pushButton_2.clicked.connect(self.changeWindowState)
        self.widget2.pushButton_3.clicked.connect(self.close)
        self.rubikcubeFrom = RubikCubeWindow()
        layout.addWidget(self.widget2,1)
        layout.addWidget(self.rubikcubeFrom,30)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground,False)
        a = os.path.abspath('.')
        b = a.split("\\")
        c = tuple(b)
        d = '/'.join(c)
        style_file = QFile(d + "/style/defaultstyle.qss")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            style_sheet = stream.readAll()
            self.setStyleSheet(style_sheet)

    def close(self):
        reply = QMessageBox.question(self,'Message','是否退出？',QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            os._exit(0)

    def maximizeWindow(self):
        # 将窗口状态设置为最大化
        self.setWindowState(self.windowState() | QtCore.Qt.WindowMaximized)

    def changeWindowState(self):
        if self.isMaximized():
            self.showNormal()   # 如果窗口已经最大化，则切换为普通状态
            self.setAttribute(Qt.WA_TranslucentBackground, False)
        else:
            self.showMaximized()   # 如果窗口未最大化，则将其最大化
            self.setAttribute(Qt.WA_TranslucentBackground, False)

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton and self.drag_region.contains(event.pos()):
            self.dragging = True
            self.is_follow_mouse = True
        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()
        self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self,event):
        if 1:
            try:
                if Qt.LeftButton and self.is_follow_mouse and self.dragging:
                    self.move(event.globalPos() - self.mouse_drag_pos)
                event.accept()
            except AttributeError as A:
                pass

    def mouseReleaseEvent(self,event):
        self.dragging = False
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def enterEvent(self,event):
        self.setCursor(Qt.ArrowCursor)