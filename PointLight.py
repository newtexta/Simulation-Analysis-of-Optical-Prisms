from openglui import Ui_Dialog_5
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class PointLight(QtWidgets.QDialog,Ui_Dialog_5):
    def __init__(self):
        super(PointLight,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.confirm)
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3,self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4,self.pushButton)
        self.setTabOrder(self.pushButton,self.pushButton_2)
        self.setTabOrder(self.pushButton_2,self.pushButton_3)
        self.pushButton.clicked.connect(self.colordialog)
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

    def colordialog(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_5.setText(HTMLcolor)

    def confirm(self):
        PointLightname = self.lineEdit.text()
        PointLightx = self.lineEdit_2.text()
        PointLighty = self.lineEdit_3.text()
        PointLightz = self.lineEdit_4.text()
        PointLightcolor = self.lineEdit_5.text()
        direction = self.lineEdit_6.text()
        if PointLightname and PointLightx and PointLighty and PointLightz and PointLightcolor and direction:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'pointlight' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM PointLight")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO pointlight (PointLightname,PointLightx,PointLighty,PointLightz,PointLightcolor,direction,id) VALUES(?,?,?,?,?,?,?)"
                data = (PointLightname,PointLightx,PointLighty,PointLightz,PointLightcolor,direction,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE PointLight
                    (id INTEGER PRIMARY KEY, PointLightname TEXT, PointLightx TEXT, PointLighty TEXT, PointLightz TEXT, PointLightcolor TEXT, direction TEXT)""")
                conn.close()
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO pointlight (PointLightname,PointLightx,PointLighty,PointLightz,PointLightcolor,direction,id) VALUES(?,?,?,?,?,?,?)"
                data = (PointLightname,PointLightx,PointLighty,PointLightz,PointLightcolor,direction,1)
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