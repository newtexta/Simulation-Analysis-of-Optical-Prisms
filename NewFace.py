from openglui import Ui_Dialog_10
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sqlite3
import os
from openglui import Ui_Dialog_11
from openglui import Ui_Dialog_12
from openglui import Ui_Dialog_13
from openglui import Ui_Dialog_14
from openglui import Ui_Dialog_15
class LargeDialog3(QtWidgets.QDialog,Ui_Dialog_11):
    def __init__(self):
        super(LargeDialog3,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)

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
        self.line_action = QAction("显示线数据",self.tableView)
        self.lines_action = QAction("显示多线数据",self.tableView)
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.line_action.triggered.connect(self.linedata)
        self.lines_action.triggered.connect(self.linesdata)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.line_action)
        menu.addAction(self.lines_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def linedata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("line1")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linesdata(self):
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

class LargeDialog4(QtWidgets.QDialog,Ui_Dialog_12):
    def __init__(self):
        super(LargeDialog4,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        print(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)
        self.model.setTable("NewFace2D")
        self.tableView.setModel(self.model)
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()

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
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
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

class LargeDialog5(QtWidgets.QDialog,Ui_Dialog_13):
    def __init__(self):
        super(LargeDialog5,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)

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
        self.line_action = QAction("显示线数据",self.tableView)
        self.lines_action = QAction("显示多线数据",self.tableView)
        self.triangle_action = QAction("显示三角形",self.tableView)
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.line_action.triggered.connect(self.linedata)
        self.lines_action.triggered.connect(self.linesdata)
        self.triangle_action.triggered.connect(self.triangledata)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.line_action)
        menu.addAction(self.lines_action)
        menu.addAction(self.triangle_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def linedata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("line1")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linesdata(self):
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

    def triangledata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("triangles",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("triangles")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

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

class LargeDialog6(QtWidgets.QDialog,Ui_Dialog_14):
    def __init__(self):
        super(LargeDialog6,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)
        self.model.setTable("tempFace3D")
        self.tableView.setModel(self.model)
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()

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
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
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

class LargeDialog7(QtWidgets.QDialog,Ui_Dialog_15):
    def __init__(self):
        super(LargeDialog7,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.tableView.clicked.connect(self.on_cell_clicked)
        self.model.setTable("NewFace3D")
        self.tableView.setModel(self.model)
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()

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
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
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

class NewFace(QtWidgets.QDialog,Ui_Dialog_10):
    def __init__(self):
        super(NewFace,self).__init__()
        self.setupUi(self)
        self.databasepath()
        self.timer = QTimer()
        self.timer.timeout.connect(self.comboBoxtext)
        self.timer.start(1000)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.comboBoxtext2)
        self.timer2.start(1000)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.clicked.connect(self.on_cell_clicked3)
        self.tableView_5.clicked.connect(self.on_cell_clicked5)
        self.tableView_5.horizontalHeader().setStretchLastSection(True)
        self.tableView_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_4.clicked.connect(self.on_cell_clicked4)
        self.tableView_4.horizontalHeader().setStretchLastSection(True)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model2 = QSqlTableModel(db=db)
        self.model = QSqlTableModel(db=db)
        self.model3 = QSqlTableModel(db=db)
        self.model4 = QSqlTableModel(db=db)
        self.model5 = QSqlTableModel(db=db)
        self.setup_context_menu()
        self.setup_context_menu0()
        self.setup_context_menu3()
        self.setup_context_menu5()
        self.setup_context_menu4()
        self.tableView_2.clicked.connect(self.on_cell_clicked)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.clicked.connect(self.on_cell_clicked0)
        self.tableView.setModel(self.model)
        self.model.setTable("NewFace2D")
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()
        self.tableView_5.setModel(self.model4)
        self.model4.setTable("tempFace3D")
        self.model4.setSort(0, Qt.AscendingOrder)
        self.model4.select()
        self.tableView_4.setModel(self.model5)
        self.model5.setTable("NewFace3D")
        self.model5.setSort(0, Qt.AscendingOrder)
        self.model5.select()
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged.connect(self.on_current_index_changed)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_2.currentIndexChanged.connect(self.on_current_index_changed2)
        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.submit3)
        self.pushButton_5.clicked.connect(self.delete_table_view5)
        self.pushButton_7.clicked.connect(self.submit4)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.cancel)

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

    def submit4(self):
        facename = self.lineEdit_3.text()
        Refractivity1 = self.lineEdit_4.text()
        Refractivity2 = self.lineEdit_6.text()
        conn = sqlite3.connect(pathfinal1)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tempFace3D")
        results = cursor.fetchall()
        conn.close()
        result = []
        for r in results:
            r = list(r)
            ritem = eval(r[1])
            result.extend(ritem)
        Lines = result
        if facename and Refractivity2 and Refractivity1 and (result != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewFace3D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewFace3D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace3D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewFace3D
                    (id INTEGER PRIMARY KEY, facename TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace3D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,1)
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
        if ("NewFace3D",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("NewFace3D")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_6.setText("")

    def confirm4(self):
        facename = self.lineEdit_3.text()
        Refractivity1 = self.lineEdit_4.text()
        Refractivity2 = self.lineEdit_6.text()
        conn = sqlite3.connect(pathfinal1)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tempFace3D")
        results = cursor.fetchall()
        conn.close()
        result = []
        for r in results:
            r = list(r)
            ritem = eval(r[1])
            result.extend(ritem)
        Lines = result
        if facename and Refractivity2 and Refractivity1 and (result != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewFace3D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewFace3D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace3D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewFace3D
                    (id INTEGER PRIMARY KEY, facename TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace3D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,1)
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
        if ("NewFace3D",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("NewFace3D")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_6.setText("")
        self.close()

    def on_cell_clicked4(self,index):
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def setup_context_menu4(self):
        self.tableView_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_4.customContextMenuRequested.connect(self.show_context_menu4)
        self.large_action4 = QAction("放大",self.tableView_4)
        self.refresh_action4 = QAction("刷新", self.tableView_4)
        self.delete_action4 = QAction("删除行",self.tableView_4)
        self.delete_action4.setEnabled(False)
        self.large_action4.triggered.connect(self.large4)
        self.refresh_action4.triggered.connect(self.refresh_table_view4)
        self.delete_action4.triggered.connect(self.delete_table_view4)

    def large4(self):
        self.LargeDialog7 = LargeDialog7()
        self.LargeDialog7.show()

    def show_context_menu4(self, position):
        menu = QMenu(self.tableView_4)
        menu.addAction(self.large_action4)
        menu.addAction(self.refresh_action4)
        menu.addAction(self.delete_action4)
        menu.exec_(self.tableView_4.viewport().mapToGlobal(position))

    def refresh_table_view4(self):
        self.model5.select()

    def delete_table_view4(self):
        try:
            del_row = self.tableView_4.currentIndex().row()
            self.model5.removeRow(del_row)
            self.model5.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

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
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
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

    def closeEvent(self,event):
       self.timer.stop()
       self.timer2.stop()

    def on_cell_clicked(self,index):
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def on_cell_clicked0(self,index):
        # 在这里处理点击单元格的行和列索引
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def submit3(self):
        Lines = str(checked_items2)
        if checked_items2 != []:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'tempFace3D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tempFace3D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO tempFace3D (Lines,id) VALUES(?,?)"
                data = (Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass
            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE tempFace3D
                    (id INTEGER PRIMARY KEY, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO tempFace3D (Lines,id) VALUES(?,?)"
                data = (Lines,1)
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
        if ("tempFace3D",) in tables:
            self.tableView_5.setModel(self.model4)
            self.model4.setTable("tempFace3D")
            self.model4.setSort(0, Qt.AscendingOrder)
            self.model4.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def on_cell_clicked5(self,index):
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def setup_context_menu5(self):
        self.tableView_5.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_5.customContextMenuRequested.connect(self.show_context_menu5)
        self.large_action5 = QAction("放大",self.tableView_5)
        self.refresh_action5 = QAction("刷新", self.tableView_5)
        self.delete_action5 = QAction("删除行",self.tableView_5)
        self.delete_action5.setEnabled(False)
        self.large_action5.triggered.connect(self.large5)
        self.refresh_action5.triggered.connect(self.refresh_table_view5)
        self.delete_action5.triggered.connect(self.delete_table_view5)

    def large5(self):
        self.LargeDialog6 = LargeDialog6()
        self.LargeDialog6.show()

    def show_context_menu5(self, position):
        menu = QMenu(self.tableView_5)
        menu.addAction(self.large_action5)
        menu.addAction(self.refresh_action5)
        menu.addAction(self.delete_action5)
        menu.exec_(self.tableView_5.viewport().mapToGlobal(position))

    def refresh_table_view5(self):
        self.model4.select()

    def delete_table_view5(self):
        try:
            del_row = self.tableView_5.currentIndex().row()
            self.model4.removeRow(del_row)
            self.model4.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def on_cell_clicked3(self,index):
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action.setEnabled(False)

    def setup_context_menu3(self):
        self.tableView_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_3.customContextMenuRequested.connect(self.show_context_menu3)
        self.large_action3 = QAction("放大",self.tableView_3)
        self.refresh_action3 = QAction("刷新", self.tableView_3)
        self.delete_action3 = QAction("删除行",self.tableView_3)
        self.delete_action3.setEnabled(False)
        self.line_action3 = QAction("显示线数据",self.tableView_3)
        self.lines_action3 = QAction("显示多线数据",self.tableView_3)
        self.triangle_action3 = QAction("显示三角形",self.tableView_3)
        self.large_action3.triggered.connect(self.large3)
        self.refresh_action3.triggered.connect(self.refresh_table_view3)
        self.delete_action3.triggered.connect(self.delete_table_view3)
        self.line_action3.triggered.connect(self.linedata3)
        self.lines_action3.triggered.connect(self.linesdata3)
        self.triangle_action3.triggered.connect(self.triangledata3)

    def large3(self):
        self.LargeDialog5 = LargeDialog5()
        self.LargeDialog5.show()

    def show_context_menu3(self, position):
        menu = QMenu(self.tableView_3)
        menu.addAction(self.large_action3)
        menu.addAction(self.refresh_action3)
        menu.addAction(self.delete_action3)
        menu.addSeparator()
        menu.addAction(self.line_action3)
        menu.addAction(self.lines_action3)
        menu.addAction(self.triangle_action3)
        menu.exec_(self.tableView_3.viewport().mapToGlobal(position))

    def triangledata3(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("triangles",) in tables:
            self.tableView_3.setModel(self.model3)
            self.model3.setTable("triangles")
            self.model3.setSort(0, Qt.AscendingOrder)
            self.model3.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linedata3(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            self.tableView_3.setModel(self.model3)
            self.model3.setTable("line1")
            self.model3.setSort(0, Qt.AscendingOrder)
            self.model3.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linesdata3(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("lines",) in tables:
            self.tableView_3.setModel(self.model3)
            self.model3.setTable("lines")
            self.model3.setSort(0, Qt.AscendingOrder)
            self.model3.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def refresh_table_view3(self):
        self.model3.select()

    def delete_table_view3(self):
        try:
            del_row = self.tableView_3.currentIndex().row()
            self.model3.removeRow(del_row)
            self.model3.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def setup_context_menu0(self):
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.show_context_menu0)
        self.large_action0 = QAction("放大",self.tableView)
        self.refresh_action0 = QAction("刷新", self.tableView)
        self.delete_action0 = QAction("删除行",self.tableView)
        self.delete_action0.setEnabled(False)
        self.large_action0.triggered.connect(self.large0)
        self.refresh_action0.triggered.connect(self.refresh_table_view0)
        self.delete_action0.triggered.connect(self.delete_table_view0)

    def large0(self):
        print(11111)
        self.LargeDialog4 = LargeDialog4()
        self.LargeDialog4.show()

    def refresh_table_view0(self):
        self.model.select()

    def delete_table_view0(self):
        try:
            del_row = self.tableView.currentIndex().row()
            self.model.removeRow(del_row)
            self.model.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def show_context_menu0(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.large_action0)
        menu.addAction(self.refresh_action0)
        menu.addAction(self.delete_action0)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def setup_context_menu(self):
        self.tableView_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_2.customContextMenuRequested.connect(self.show_context_menu)
        self.large_action = QAction("放大",self.tableView_2)
        self.refresh_action = QAction("刷新", self.tableView_2)
        self.delete_action = QAction("删除行",self.tableView_2)
        self.delete_action.setEnabled(False)
        self.line_action = QAction("显示线数据",self.tableView_2)
        self.lines_action = QAction("显示多线数据",self.tableView_2)
        self.large_action.triggered.connect(self.large)
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.line_action.triggered.connect(self.linedata)
        self.lines_action.triggered.connect(self.linesdata)

    def large(self):
        self.LargeDialog3 = LargeDialog3()
        self.LargeDialog3.show()

    def show_context_menu(self, position):
        menu = QMenu(self.tableView_2)
        menu.addAction(self.large_action)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.line_action)
        menu.addAction(self.lines_action)
        menu.exec_(self.tableView_2.viewport().mapToGlobal(position))

    def linedata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("line1",) in tables:
            self.tableView_2.setModel(self.model2)
            self.model2.setTable("line1")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linesdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("lines",) in tables:
            self.tableView_2.setModel(self.model2)
            self.model2.setTable("lines")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def refresh_table_view(self):
        self.model2.select()

    def delete_table_view(self):
        try:
            del_row = self.tableView_2.currentIndex().row()
            self.model2.removeRow(del_row)
            self.model2.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def on_current_index_changed(self,index):
        global checked_items
        checked_items = []
        for i in range(self.comboBox.count()):
            if self.comboBox.itemChecked(i):
                checked_items.append(self.comboBox.itemText(i))

    def on_current_index_changed2(self,index):
        global checked_items2
        checked_items2 = []
        for i in range(self.comboBox_2.count()):
            if self.comboBox_2.itemChecked(i):
                checked_items2.append(self.comboBox_2.itemText(i))

    def submit(self):
        facename = self.lineEdit_2.text()
        Refractivity1 = self.lineEdit.text()
        Refractivity2 = self.lineEdit_5.text()
        Lines = str(checked_items)
        if facename and Refractivity2 and Refractivity1 and (checked_items != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewFace2D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewFace2D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace2D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewFace2D
                    (id INTEGER PRIMARY KEY, facename TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace2D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,1)
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
        if ("NewFace2D",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("NewFace2D")
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
        facename = self.lineEdit_2.text()
        Refractivity1 = self.lineEdit.text()
        Refractivity2 = self.lineEdit_5.text()
        Lines = str(checked_items)
        if facename and Refractivity2 and Refractivity1 and (checked_items != []):
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            #获取表名，保存在tab_name列表
            cu.execute("select name from sqlite_master where type='table'")
            tab_name=cu.fetchall()
            tab_name=[line[0] for line in tab_name]
            conn.close()
            if 'NewFace2D' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NewFace2D")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace2D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE NewFace2D
                    (id INTEGER PRIMARY KEY, facename TEXT, Refractivity1 TEXT, Refractivity2 TEXT, Lines TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO NewFace2D (facename,Refractivity1,Refractivity2,Lines,id) VALUES(?,?,?,?,?)"
                data = (facename,Refractivity1,Refractivity2,Lines,1)
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
        if ("NewFace2D",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("NewFace2D")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass
        self.close()

    def cancel(self):
        self.close()