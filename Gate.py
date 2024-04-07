from openglui import Ui_Dialog_0
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class GateDialog(QtWidgets.QDialog,Ui_Dialog_0):
    signal = pyqtSignal(str)
    signal2 = pyqtSignal(str)
    def __init__(self):
        super(GateDialog,self).__init__()
        self.setupUi(self)
        self.setFixedSize(550,400)
        self.pushButton_5.clicked.connect(self.reject)
        self.pushButton_4.clicked.connect(self.accept)
        self.pushButton_3.clicked.connect(self.create)
        self.pushButton.clicked.connect(self.openfile)

    def create(self):
        if self.lineEdit.text():
            name = self.lineEdit.text()
            name += ".sqlite"
        else:
            name = ""
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", name, "Sqlite Files (*.sqlite);;All Files (*)")
        if file_path:
            try:
                conn = sqlite3.connect(file_path)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE users
                    (id INTEGER PRIMARY KEY, name TEXT, mode TEXT, filepath TEXT)""")
                conn.close()
            except sqlite3.OperationalError as SQ:
                reply = QtWidgets.QMessageBox.warning(self,u'Warning',u'Database already exists！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

        if self.radioButton.isChecked() and file_path:
            a = os.path.abspath('.')
            b = a.split("\\")
            c = tuple(b)
            d = '/'.join(c)
            p = d + "/resource/initial.sqlite"
            mode = self.radioButton.text()
            name = self.lineEdit.text()
            conn = sqlite3.connect(p)
            cu = conn.cursor()
            sql = "UPDATE databasepath SET Dpath = ? WHERE id = ?"
            data = (file_path, 1)
            cu.execute(sql, data)
            conn.commit()
            conn.close()
            conn = sqlite3.connect(file_path)
            cu = conn.cursor()
            sql = "INSERT INTO users (name,mode,filepath,id) VALUES(?,?,?,?)"
            data = (name,mode,file_path,1)
            cu.execute(sql,data)
            conn.commit()
            conn.close()

        if self.radioButton_2.isChecked() and file_path:
            mode = self.radioButton_2.text()
            name = self.lineEdit.text()
            a = os.path.abspath('.')
            b = a.split("\\")
            c = tuple(b)
            d = '/'.join(c)
            p = d + "/resource/initial.sqlite"
            conn = sqlite3.connect(p)
            cu = conn.cursor()
            sql = "UPDATE databasepath SET Dpath = ? WHERE id = ?"
            data = (file_path, 1)
            cu.execute(sql, data)
            conn.commit()
            conn.close()
            conn = sqlite3.connect(file_path)
            cu = conn.cursor()
            sql = "INSERT INTO users (name,mode,filepath,id) VALUES(?,?,?,?)"
            data = (name,mode,file_path,1)
            cu.execute(sql,data)
            conn.commit()
            conn.close()

    def openfile(self):
        # 打开文件对话框
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setWindowTitle("Open File")  # 设置对话框标题
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)  # 设置对话框模式为打开现有文件
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)  # 设置对话框接受打开操作

        # 设置过滤器，只显示特定类型的文件
        file_dialog.setNameFilter("DataBase Files (*.sqlite);;All Files (*)")

        # 如果用户选择了文件，则获取选中文件的路径
        if file_dialog.exec_() == QtWidgets.QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            self.lineEdit_2.setText(selected_file)