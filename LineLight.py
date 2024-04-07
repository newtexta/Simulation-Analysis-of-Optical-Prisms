from openglui import Ui_Dialog_6
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class LineLight(QtWidgets.QDialog,Ui_Dialog_6):
    def __init__(self):
        super(LineLight,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_2.clicked.connect(self.confirm)
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3,self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4,self.pushButton_3)
        self.setTabOrder(self.pushButton_3,self.lineEdit_6)
        self.setTabOrder(self.lineEdit_6,self.lineEdit_9)
        self.setTabOrder(self.lineEdit_9,self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7,self.pushButton_4)
        self.setTabOrder(self.pushButton_4,self.pushButton)
        self.setTabOrder(self.pushButton,self.pushButton_2)
        self.pushButton_3.clicked.connect(self.colordialog1)
        self.pushButton_4.clicked.connect(self.colordialog2)
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

    def colordialog1(self):
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_5.setText(HTMLcolor)

    def colordialog2(self):
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_8.setText(HTMLcolor)

    def confirm(self):
        linelightname = self.lineEdit.text()
        linelightx1 = self.lineEdit_2.text()
        linelighty1 = self.lineEdit_3.text()
        linelightz1 = self.lineEdit_4.text()
        linelightcolor1 = self.lineEdit_5.text()
        linelightx2 = self.lineEdit_6.text()
        linelighty2 = self.lineEdit_7.text()
        linelightz2 = self.lineEdit_8.text()
        linelightcolor2 = self.lineEdit_9.text()
        direction = self.lineEdit_10.text()
        if linelightname and linelightx1 and linelighty1 and linelightz1 and linelightcolor1 and linelightx2 and linelighty2 and linelightz2 and linelightcolor2 and direction:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'linelight' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM linelight")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO linelight (linelightname,linelightx1,linelighty1,linelightz1,linelightcolor1,linelightx2,linelighty2,linelightz2,linelightcolor2,direction,id) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
                data = (linelightname,linelightx1,linelighty1,linelightz1,linelightcolor1,linelightx2,linelighty2,linelightz2,linelightcolor2,direction,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE linelight
                    (id INTEGER PRIMARY KEY, linelightname TEXT, linelightx1 TEXT, linelighty1 TEXT, linelightz1 TEXT, linelightcolor1 TEXT, linelightx2 TEXT, linelighty2 TEXT, linelightz2 TEXT, linelightcolor2 TEXT, direction TEXT)""")
                conn.close()
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO linelight (linelightname,linelightx1,linelighty1,linelightz1,linelightcolor1,linelightx2,linelighty2,linelightz2,linelightcolor2,direction,id) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
                data = (linelightname,linelightx1,linelighty1,linelightz1,linelightcolor1,linelightx2,linelighty2,linelightz2,linelightcolor2,direction,1)
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