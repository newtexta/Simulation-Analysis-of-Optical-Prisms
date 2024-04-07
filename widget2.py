from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSvg
from PyQt5.QtSvg import QSvgRenderer,QSvgWidget
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QMainWindow, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer

class mywidget2(QtWidgets.QWidget):
    def __init__(self):
        super(mywidget2,self).__init__()
        self.setObjectName("mywidget2")
        layout2 = QtWidgets.QHBoxLayout(self)
        self.labelicon = QtWidgets.QLabel()
        self.labelicon.setObjectName("ICON")
        self.label = QtWidgets.QLabel("Simulation Analysis of Optical Prisms")
        self.label.setObjectName("Title")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("wpushButton")
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("wpushButton2")
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setObjectName("wpushButton3")

        layout2.addWidget(self.labelicon,1)
        layout2.addWidget(self.label,50)
        layout2.addWidget(self.pushButton,1)
        layout2.addWidget(self.pushButton_2,1)
        layout2.addWidget(self.pushButton_3,1)