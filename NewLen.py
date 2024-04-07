from openglui import Ui_Dialog_20
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class NewLen(QtWidgets.QDialog,Ui_Dialog_20):
    def __init__(self):
        super(NewLen,self).__init__()
        self.setupUi(self)
        self.databasepath()
        self.timer = QTimer()
        self.timer.timeout.connect(self.comboBoxtext)
        self.timer.start(1000)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.comboBoxtext2)
        self.timer2.start(1000)
        self.comboBox_2.currentIndexChanged.connect(self.on_current_index_changed2)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.model2 = QSqlTableModel(db=db)
        self.pushButton_8.clicked.connect(self.cancel)
        self.pushButton_9.clicked.connect(self.submit)
        self.pushButton_10.clicked.connect(self.confirm)

    def on_current_index_changed2(self,index):
        global checked_items2
        checked_items2 = []
        for i in range(self.comboBox_2.count()):
            if self.comboBox_2.itemChecked(i):
                checked_items2.append(self.comboBox_2.itemText(i))

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

    def comboBoxtext(self):
        checked_items_2 = []
        for i in range(self.comboBox.count()):
            if self.comboBox.itemChecked(i):
                checked_items_2.append(self.comboBox.itemText(i))
        if checked_items_2 == []:
            self.comboBox.setCurrentIndex(-1)
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM line1")
            result = cu.fetchall()
            cu.close()
            conn.close()
            for i in range(self.comboBox.count()):
                items.append(self.comboBox.itemText(i))
            for r in result:
                r = list(r)
                r = r[1] + "_line1"
                if r in items:
                    pass
                else:
                    self.comboBox.addItem(r)
                    self.comboBox.setCurrentIndex(-1)
        if ("lines",) in tables:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM lines")
            result = cu.fetchall()
            cu.close()
            conn.close()
            items = []
            for i in range(self.comboBox.count()):
                items.append(self.comboBox.itemText(i))
            for r in result:
                r = list(r)
                r = r[1] + "_lines"
                if r in items:
                    pass
                else:
                    self.comboBox.addItem(r)
                    self.comboBox.setCurrentIndex(-1)
        # if ("NewLen3D",) in tables:
        #     conn = sqlite3.connect(pathfinal1)
        #     cu = conn.cursor()
        #     cu.execute("SELECT * FROM NewLen3D")
        #     result = cu.fetchall()
        #     cu.close()
        #     conn.close()
        #     items = []
        #     for i in range(self.comboBox.count()):
        #         items.append(self.comboBox.itemText(i))
        #     for r in result:
        #         r = list(r)
        #         r = r[1] + "_lines"
        #         if r in items:
        #             pass
        #         else:
        #             self.comboBox.addItem(r)
        #             self.comboBox.setCurrentIndex(-1)

    def comboBoxtext2(self):
        checked_items_2 = []
        for i in range(self.comboBox_2.count()):
            if self.comboBox_2.itemChecked(i):
                checked_items_2.append(self.comboBox_2.itemText(i))
        if checked_items_2 == []:
            self.comboBox_2.setCurrentIndex(-1)
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM line1")
            result = cu.fetchall()
            cu.close()
            conn.close()
            for i in range(self.comboBox_2.count()):
                items.append(self.comboBox_2.itemText(i))
            for r in result:
                r = list(r)
                r = r[1] + "_line1"
                if r in items:
                    pass
                else:
                    self.comboBox_2.addItem(r)
                    self.comboBox_2.setCurrentIndex(-1)
        if ("lines",) in tables:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM lines")
            result = cu.fetchall()
            cu.close()
            conn.close()
            items = []
            for i in range(self.comboBox_2.count()):
                items.append(self.comboBox_2.itemText(i))
            for r in result:
                r = list(r)
                r = r[1] + "_lines"
                if r in items:
                    pass
                else:
                    self.comboBox_2.addItem(r)
                    self.comboBox_2.setCurrentIndex(-1)
        if ("triangles",) in tables:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM triangles")
            result = cu.fetchall()
            cu.close()
            conn.close()
            items = []
            for i in range(self.comboBox_2.count()):
                items.append(self.comboBox_2.itemText(i))
            for r in result:
                r = list(r)
                r = r[1] + "_triangles"
                if r in items:
                    pass
                else:
                    self.comboBox_2.addItem(r)
                    self.comboBox_2.setCurrentIndex(-1)
        # if ("NewFace3D",) in tables:
        #     conn = sqlite3.connect(pathfinal1)
        #     cu = conn.cursor()
        #     cu.execute("SELECT * FROM NewFace3D")
        #     result = cu.fetchall()
        #     cu.close()
        #     conn.close()
        #     items = []
        #     for i in range(self.comboBox_2.count()):
        #         items.append(self.comboBox_2.itemText(i))
        #     for r in result:
        #         r = list(r)
        #         r = r[1] + "_triangles"
        #         if r in items:
        #             pass
        #         else:
        #             self.comboBox_2.addItem(r)
        #             self.comboBox_2.setCurrentIndex(-1)

    def closeEvent(self,event):
       self.timer.stop()
       self.timer2.stop()

    def submit(self):
        lenname = self.lineEdit_5.text()
        Refractivity1 = self.lineEdit_3.text()
        Refractivity2 = self.lineEdit_4.text()
        Lines = str(checked_items2)
        if lenname and Refractivity2 and Refractivity1 and (checked_items2 != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewLen3D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewLen3D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewLen3D (lenname,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (lenname,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewLen3D
                    (id INTEGER PRIMARY KEY, lenname TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewLen3D (lenname,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (lenname,Refractivity1,Refractivity2,Lines,1)
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
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("NewLen3D",) in tables:
            self.tableView_4.setModel(self.model2)
            self.model2.setTable("NewLen3D")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
        self.lineEdit.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_2.setText("")

    def confirm(self):
        lenname = self.lineEdit_2.text()
        Refractivity1 = self.lineEdit.text()
        Refractivity2 = self.lineEdit_5.text()
        Lines = str(checked_items2)
        if lenname and Refractivity2 and Refractivity1 and (checked_items2 != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewLen3D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewLen3D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewLen3D (lenname,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (lenname,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewLen3D
                    (id INTEGER PRIMARY KEY, lenname TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewLen3D (lenname,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (lenname,Refractivity1,Refractivity2,Lines,1)
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
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("NewLen3D",) in tables:
            self.tableView_5.setModel(self.model2)
            self.model2.setTable("NewLen3D")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
        self.close()

    def cancel(self):
        self.close()