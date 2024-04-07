from openglui import Ui_Dialog_3
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class LinesDialog(QtWidgets.QDialog,Ui_Dialog_3):
    def __init__(self):
        super(LinesDialog,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton.clicked.connect(self.cancel)
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3,self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4,self.pushButton_6)
        self.setTabOrder(self.pushButton_6,self.lineEdit_6)
        self.setTabOrder(self.lineEdit_6,self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7,self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8,self.pushButton_7)
        self.setTabOrder(self.pushButton_7,self.pushButton_3)
        self.setTabOrder(self.pushButton_3,self.pushButton)
        self.setTabOrder(self.pushButton,self.pushButton_2)
        self.pushButton_6.clicked.connect(self.colordialog6)
        self.pushButton_7.clicked.connect(self.colordialog7)
        self.pushButton_5.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.delete_table_view2)
        self.pushButton_3.clicked.connect(self.submit)
        self.databasepath()

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)
        
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

    def on_cell_clicked(self,index):
        # 在这里处理点击单元格的行和列索引
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def setup_context_menu(self):
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.show_context_menu)
        self.refresh_action = QAction("刷新", self.tableView)
        self.delete_action = QAction("删除行",self.tableView)
        self.delete_action.setEnabled(False)
        self.dot_action = QAction("显示数据",self.tableView)

        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.dot_action.triggered.connect(self.linesdb)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.dot_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def refresh_table_view(self):
        self.model.select()

    def delete_table_view(self):
        try:
            del_row = self.tableView.currentIndex().row()
            self.model.removeRow(del_row)
            self.model.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def delete_table_view2(self):
        try:
            del_row = self.tableView.currentIndex().row()
            self.model.removeRow(del_row)
            self.model.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linesdb(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("lines",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("lines")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")

    def colordialog6(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_5.setText(HTMLcolor)

    def colordialog7(self):
        # 创建颜色对话框
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_9.setText(HTMLcolor)

    def submit(self):
        linename = self.lineEdit.text()
        linex1 = self.lineEdit_2.text()
        liney1 = self.lineEdit_3.text()
        linez1 = self.lineEdit_4.text()
        linecolor1 = self.lineEdit_5.text()
        linex2 = self.lineEdit_6.text()
        liney2 = self.lineEdit_7.text()
        linez2 = self.lineEdit_8.text()
        linecolor2 = self.lineEdit_9.text()
        if linename and linex1 and liney1 and linez1 and linecolor1 and linex2 and liney2 and linez2 and linecolor2:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'lines' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM lines")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO lines (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE lines
                    (id INTEGER PRIMARY KEY, linename TEXT, linex1 TEXT, liney1 TEXT, linez1 TEXT, linecolor1 TEXT, linex2 TEXT, liney2 TEXT, linez2 TEXT, linecolor2 TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO lines (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,1)
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
        if ("lines",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("lines")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def confirm(self):
        linename = self.lineEdit.text()
        linex1 = self.lineEdit_2.text()
        liney1 = self.lineEdit_3.text()
        linez1 = self.lineEdit_4.text()
        linecolor1 = self.lineEdit_5.text()
        linex2 = self.lineEdit_6.text()
        liney2 = self.lineEdit_7.text()
        linez2 = self.lineEdit_8.text()
        linecolor2 = self.lineEdit_9.text()
        if linename and linex1 and liney1 and linez1 and linecolor1 and linex2 and liney2 and linez2 and linecolor2:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'lines' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM lines")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO lines (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE lines
                    (id INTEGER PRIMARY KEY, linename TEXT, linex1 TEXT, liney1 TEXT, linez1 TEXT, linecolor1 TEXT, linex2 TEXT, liney2 TEXT, linez2 TEXT, linecolor2 TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO lines (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,id) VALUES(?,?,?,?,?,?,?,?,?,?)"
                data = (linename,linex1,liney1,linez1,linecolor1,linex2,liney2,linez2,linecolor2,1)
                cu.execute(sql,data)
                conn.commit()
                conn.close()

                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
        else:
            pass
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("lines",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("lines")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
            self.close()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def cancel(self):
        self.close()