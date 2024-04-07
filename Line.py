from openglui import Ui_Dialog_2
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class LineDialog(QtWidgets.QDialog,Ui_Dialog_2):
    def __init__(self):
        super(LineDialog,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton.clicked.connect(self.cancel)
        self.setTabOrder(self.lineEdit,self.pushButton_3)
        self.setTabOrder(self.pushButton_3,self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3,self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4,self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5,self.pushButton_4)
        self.setTabOrder(self.pushButton_4,self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7,self.lineEdit_9)
        self.setTabOrder(self.lineEdit_9,self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8,self.pushButton_5)
        self.setTabOrder(self.pushButton_5,self.pushButton)
        self.setTabOrder(self.pushButton,self.pushButton_2)
        self.pushButton_4.clicked.connect(self.colordialog4)
        self.pushButton_5.clicked.connect(self.colordialog5)
        self.databasepath()
        
    def databasepath(self):
        global pathfinal1
        global mode
        a = os.path.abspath('.')
        b = a.split("\\")
        c = tuple(b)
        d = '/'.join(c)
        p = d + "/resource/initial.sqlite"
        conn = sqlite3.connect(p)
        cu = conn.cursor()
        sql = "SELECT * FROM databasepath WHERE id = ?"
        cu.execute(sql,(1,))
        row = cu.fetchone()
        cu.close()
        conn.close()
        pathfinal1 = list(row)[1]
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        sql = "SELECT * FROM users WHERE id = ?"
        cu.execute(sql,(1,))
        row = cu.fetchone()
        conn.close()
        mode = list(row)[2]

    def colordialog4(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_6.setText(HTMLcolor)

    def colordialog5(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_10.setText(HTMLcolor)

    def confirm(self):
        linename = self.lineEdit.text()
        linecolor = self.lineEdit_2.text()
        linex1 = self.lineEdit_3.text()
        liney1 = self.lineEdit_4.text()
        linez1 = self.lineEdit_5.text()
        linecolor1 = self.lineEdit_6.text()
        linex2 = self.lineEdit_7.text()
        liney2 = self.lineEdit_9.text()
        linez2 = self.lineEdit_8.text()
        linecolor2 = self.lineEdit_10.text()

        if linename and linecolor and linex1 and liney1 and linez1 and linecolor1 and linex2 and liney2 and linez2 and linecolor2:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'line1' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM line1")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO line1 (linename,linecolor,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linecolor,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE line1
                    (id INTEGER PRIMARY KEY, linename TEXT, linecolor TEXT, linex1 TEXT, liney1 TEXT, linez1 TEXT, linecolor1 TEXT, linex2 TEXT, liney2 TEXT, linez2 TEXT, linecolor2 TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO line1 (linename,linecolor,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linecolor,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,1)
                cu.execute(sql,data)
                conn.commit()
                conn.close()

                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
        else:
            reply = QtWidgets.QMessageBox.warning(self,u'Warning',u'Please complete all information！',QMessageBox.Yes)
            if reply == QtWidgets.QMessageBox.Yes:
                pass

    def cancel(self):
        self.close()