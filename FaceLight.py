from openglui import Ui_Dialog_7
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
class FaceLight(QtWidgets.QDialog,Ui_Dialog_7):
    def __init__(self):
        super(FaceLight,self).__init__()
        self.setupUi(self)
        self.lineEdit.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_2.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_3.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_4.setFocusPolicy(Qt.TabFocus)
        self.pushButton_3.setFocusPolicy(Qt.TabFocus)
        self.pushButton_6.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_5.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_6.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setFocus()
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3,self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4,self.pushButton_3)
        self.setTabOrder(self.pushButton_3,self.pushButton_6)
        self.setTabOrder(self.pushButton_6,self.pushButton)
        self.setTabOrder(self.pushButton,self.pushButton_2)
        self.pushButton_3.clicked.connect(self.colordialog)
        self.pushButton_4.clicked.connect(self.clear)
        self.pushButton_5.clicked.connect(self.delete_table_view2)
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
        self.dot_action.triggered.connect(self.facelightdb)

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

    def facelightdb(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("facelight",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("facelight")
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

    def colordialog(self):
        color = QColorDialog.getColor()
        HTMLcolor = color.name()
        self.lineEdit_5.setText(HTMLcolor)

    def confirm(self):
        facelightname = self.lineEdit.text()
        facelightx = self.lineEdit_2.text()
        facelighty = self.lineEdit_3.text()
        facelightz = self.lineEdit_4.text()
        facelightcolor = self.lineEdit_5.text()
        facelightsequence = self.lineEdit_6.text()
        direction = self.lineEdit_7.text()
        if facelightname and facelightx and facelighty and facelightz and facelightcolor and facelightsequence and direction:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'facelight' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM facelight")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO facelight (facelightname,facelightx,facelighty,facelightz,facelightcolor,facelightsequence,direction,id) VALUES(?,?,?,?,?,?,?,?)"
                data = (facelightname,facelightx,facelighty,facelightz,facelightcolor,facelightsequence,direction,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE facelight
                    (id INTEGER PRIMARY KEY, facelightname TEXT, facelightx TEXT, facelighty TEXT, facelightz TEXT, facelightcolor TEXT, facelightsequence TEXT, direction TEXT)""")
                conn.close()
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO facelight (facelightname,facelightx,facelighty,facelightz,facelightcolor,facelightsequence,direction,id) VALUES(?,?,?,?,?,?,?,?)"
                data = (facelightname,facelightx,facelighty,facelightz,facelightcolor,facelightsequence,direction,1)
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
        if ("facelight",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("facelight")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def cancel(self):
        self.close()