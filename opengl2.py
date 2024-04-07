#pyuic5 Rubik_Cube1.ui -o Rubik_Cube1.py
#pyrcc5 -o min_white.py min_white.qrc
###################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSvg
from PyQt5.QtSvg import QSvgRenderer,QSvgWidget
from PyQt5.QtWidgets import QMessageBox,QHeaderView,QApplication, QMenu, QAction, QTableView, QMainWindow, QColorDialog,QComboBox, QCheckBox, QListView
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.Qt import Qt,QTimer,QTableView,QStyledItemDelegate
from PyQt5.QtGui import QCursor,QPen,QPixmap,QPainter,QOpenGLContext,QIcon,QStandardItemModel, QStandardItem
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal,QDate,QSize,QPoint,QRect,QCoreApplication,QMetaObject,QBasicTimer,Qt,QUrl,QFile, QTextStream,QTimer
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import freetype
from PIL import Image
from Gate import GateDialog
from Dot import DotDialog
from Line import LineDialog
from Lines import LinesDialog
from Triangles import Triangles
from PointLight import PointLight
from LineLight import LineLight
from FaceLight import FaceLight
from openglui import Ui_Dialog_8
from openglui import Ui_Dialog_9
from NewFace import NewFace
from openglui import Ui_Dialog_Settings
from openglui import Ui_Dialog_16
from openglui import Ui_Dialog_17
from openglui import Ui_Dialog_18
from openglui import Ui_Dialog_19
from NewLen import NewLen
from raytrace import hex2rgb
from raytrace import *
import sys
import os
import ctypes
import sqlite3
import logging
from logging.handlers import TimedRotatingFileHandler

a = os.path.abspath('.')
b = a.split("\\")
c = tuple(b)
d = '/'.join(c)
log_dir = d + './logs'  # 日志目录
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 配置日志
log_formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s]: %(message)s')
log_handler = TimedRotatingFileHandler(
    os.path.join(log_dir, 'app.log'), when='D', interval=1, backupCount=7, encoding='utf-8'
)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
###############################################################################################
class SettingsDialog(QtWidgets.QDialog,Ui_Dialog_Settings):
    def __init__(self):
        super(SettingsDialog,self).__init__()
        self.setupUi(self)



class LargeDialog(QtWidgets.QDialog,Ui_Dialog_8):
    def __init__(self):
        super(LargeDialog,self).__init__()
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
        self.dot_action = QAction("显示点数据",self.tableView)
        self.line_action = QAction("显示线数据",self.tableView)
        self.lines_action = QAction("显示多线数据",self.tableView)
        self.triangle_action = QAction("显示三角形数据",self.tableView)
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.dot_action.triggered.connect(self.dotdata)
        self.line_action.triggered.connect(self.linedata)
        self.lines_action.triggered.connect(self.linesdata)
        self.triangle_action.triggered.connect(self.triangledata)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.dot_action)
        menu.addAction(self.line_action)
        menu.addAction(self.lines_action)
        menu.addAction(self.triangle_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def dotdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("dot",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("dot")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

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

class LargeDialog2(QtWidgets.QDialog,Ui_Dialog_9):
    def __init__(self):
        super(LargeDialog2,self).__init__()
        self.setupUi(self)
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model2 = QSqlTableModel(db=db)
        self.setup_context_menu2()
        self.tableView.clicked.connect(self.on_cell_clicked2)

    def on_cell_clicked2(self,index):
        # 在这里处理点击单元格的行和列索引
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action2.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action2.setEnabled(False)

    def setup_context_menu2(self):
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.show_context_menu2)
        self.refresh_action2 = QAction("刷新", self.tableView)
        self.delete_action2 = QAction("删除行",self.tableView)
        self.delete_action2.setEnabled(False)
        self.pointlight_action = QAction("显示点光源数据",self.tableView)
        self.linelight_action = QAction("显示线光源数据",self.tableView)
        self.facelight_action = QAction("显示面光源数据",self.tableView)
        self.refresh_action2.triggered.connect(self.refresh_table_view2)
        self.delete_action2.triggered.connect(self.delete_table_view2)
        self.pointlight_action.triggered.connect(self.pointlightdata)
        self.linelight_action.triggered.connect(self.linelightdata)
        self.facelight_action.triggered.connect(self.facelightdata)

    def show_context_menu2(self, position):
        menu2 = QMenu(self.tableView)
        menu2.addAction(self.refresh_action2)
        menu2.addAction(self.delete_action2)
        menu2.addSeparator()
        menu2.addAction(self.pointlight_action)
        menu2.addAction(self.linelight_action)
        menu2.addAction(self.facelight_action)
        menu2.exec_(self.tableView.viewport().mapToGlobal(position))

    def pointlightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("PointLight",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("PointLight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linelightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("linelight",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("linelight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def facelightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("facelight",) in tables:
            self.tableView.setModel(self.model2)
            self.model2.setTable("facelight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def refresh_table_view2(self):
        self.model2.select()

    def delete_table_view2(self):
        try:
            del_row = self.tableView.currentIndex().row()
            self.model2.removeRow(del_row)
            self.model2.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

class RubikCube_Widget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        global IS_PERSPECTIVE
        global VIEW
        global SCALE_K
        global EYE
        global EYE_UP
        global LOOK_AT
        global WIN_W
        global WIN_H
        global LEFT_IS_DOWNED
        global MOUSE_X
        global MOUSE_Y
        global DIST
        global PHI
        global THETA
        global Axis
        self.initial_pos = None
        self.model_scale = 1.0
        Axis = False
        Mode = False
        IS_PERSPECTIVE = True                               # 透视投影
        VIEW = np.array([-0.8, 0.8, -0.8, 0.8, 1.0, 20.0])  # 视景体的left/right/bottom/top/near/far六个面
        SCALE_K = np.array([1.0, 1.0, 1.0])                 # 模型缩放比例
        EYE = np.array([1.0, 1.0, 1.0])                     # 眼睛的位置（默认z轴的正方向）
        LOOK_AT = np.array([0.0, 0.0, 0.0])                 # 瞄准方向的参考点（默认在坐标原点）
        EYE_UP = np.array([0.0, 1.0, 0.0])                  # 定义对观察者而言的上方（默认y轴的正方向）
        WIN_W, WIN_H = 850, 750                             # 保存窗口宽度和高度的变量
        LEFT_IS_DOWNED = False                              # 鼠标左键被按下
        MOUSE_X, MOUSE_Y = 0, 0                             # 考察鼠标位移量时保存的起始位置
        DIST, PHI, THETA = self.getposture() 

    def getposture(self):
        global EYE, LOOK_AT        
        dist = np.sqrt(np.power((EYE-LOOK_AT), 2).sum())
        if dist > 0:
            phi = np.arcsin((EYE[1]-LOOK_AT[1])/dist)
            theta = np.arcsin((EYE[0]-LOOK_AT[0])/(dist*np.cos(phi)))
        else:
            phi = 0.0
            theta = 0.0
        return dist, phi, theta

    def initializeGL(self):
        global IS_PERSPECTIVE, VIEW
        global EYE, LOOK_AT, EYE_UP
        global SCALE_K
        global WIN_W, WIN_H
        glClearColor(0.0, 0.0, 0.0, 1.0) # 设置画布背景色。注意：这里必须是4个参数
        glEnable(GL_DEPTH_TEST)          # 开启深度测试，实现遮挡关系
        glDepthFunc(GL_LEQUAL)           # 设置深度测试函数（GL_LEQUAL只是选项之一）

    def load_font(self,font_file, font_size):
        face = freetype.Face(font_file)
        face.set_pixel_sizes(0, font_size)
        return face

    def create_texture(self,face, char):
        face.load_char(char)
        bitmap = face.glyph.bitmap
        width = bitmap.width
        height = bitmap.rows
        data = bitmap.buffer

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RED, width, height, 0, GL_RED, GL_UNSIGNED_BYTE, data)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return texture_id, width, height

    def draw_text(face, text, x, y):
        glColor(1, 1, 1)
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(x, y, 0)

        for char in text:
            texture_id, width, height = self.create_texture(face, char)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glBegin(GL_QUADS)
            glTexCoord2f(0, 0)
            glVertex2f(0, 0)
            glTexCoord2f(1, 0)
            glVertex2f(width, 0)
            glTexCoord2f(1, 1)
            glVertex2f(width, height)
            glTexCoord2f(0, 1)
            glVertex2f(0, height)
            glEnd()
            glTranslatef(face.glyph.advance.x // 64, 0, 0)

        glPopMatrix()

    def drawAxis(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_LINES)               # 开始绘制
        # x轴
        glColor4f(1.0, 0.0, 0.0, 1.0)   # 红色不透明
        glVertex3f(-0.5, 0.0, 0.0)      # 设置x轴起始点 +
        glVertex3f(0.5, 0.0, 0.0)       # 设置x轴结束点  -
 
        # y轴
        glColor4f(0.0, 1.0, 0.0, 1.0)   # 绿色不透明
        glVertex3f(0.0, -0.5, 0.0)      # 设置x轴起始点 +
        glVertex3f(0.0, 0.5, 0.0)       # 设置x轴结束点  -
 
        # z轴
        glColor4f(0.0, 0.0, 1.0, 1.0)   # 蓝色不透明
        glVertex3f(0.0, 0.0, -0.5)      # 设置x轴起始点 +
        glVertex3f(0.0, 0.0, 0.5)       # 设置x轴结束点  -
        # font_file = "arial.ttf"
        # font_size = 36
        # face = self.load_font(font_file, font_size)
        # self.draw_text(face, "Hello, OpenGL!", 100, 100)
 
        glEnd()                         # 结束绘制

    def drawAxis2(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_LINES)               # 开始绘制
        # x轴
        glColor4f(1.0, 0.0, 0.0, 1.0)   # 红色不透明
        glVertex2f(-0.5, 0.0)      # 设置x轴起始点 +
        glVertex2f(0.5, 0.0)       # 设置x轴结束点  -
 
        # y轴
        glColor4f(0.0, 1.0, 0.0, 1.0)   # 绿色不透明
        glVertex2f(0.0, -0.5)      # 设置x轴起始点 +
        glVertex2f(0.0, 0.5)       # 设置x轴结束点  -
 
        glEnd()                         # 结束绘制

    def drawDot(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'dot' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM dot")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_POINTS)
                color = r[-1]
                color = hex2rgb.h2r(color)
                glColor4f(color[0],color[1],color[2],color[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glEnd()
        else:
            pass

    def drawLine(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        #获取表名，保存在tab_name列表
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'line1' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM line1")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_LINES)
                color2 = r[-1]
                color2 = hex2rgb.h2r(color2)
                color1 = r[-5]
                color1 = hex2rgb.h2r(color1)
                glColor4f(color1[0],color1[1],color1[2],color1[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glColor4f(color2[0],color2[1],color2[2],color2[3])
                glVertex3f(eval(r[6]),eval(r[7]),eval(r[8]))
                glEnd()
        else:
            pass

    def drawLines(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'lines' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM lines")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_LINES)
                color2 = r[-1]
                color2 = hex2rgb.h2r(color2)
                color1 = r[5]
                color1 = hex2rgb.h2r(color1)
                glColor4f(color1[0],color1[1],color1[2],color1[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glColor4f(color2[0],color2[1],color2[2],color2[3])
                glVertex3f(eval(r[6]),eval(r[7]),eval(r[8]))
                glEnd()
        else:
            pass

    def drawTriangles(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'triangles' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM triangles")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_TRIANGLES)
                color3 = r[-1]
                color3 = hex2rgb.h2r(color3)
                color2 = r[9]
                color2 = hex2rgb.h2r(color2)
                color1 = r[5]
                color1 = hex2rgb.h2r(color1)
                glColor4f(color1[0],color1[1],color1[2],color1[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glColor4f(color2[0],color2[1],color2[2],color2[3])
                glVertex3f(eval(r[6]),eval(r[7]),eval(r[8]))
                glColor4f(color3[0],color3[1],color3[2],color3[3])
                glVertex3f(eval(r[10]),eval(r[11]),eval(r[12]))
                glEnd()
        else:
            pass

    def drawPointLight(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'PointLight' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM PointLight")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_POINTS)
                color = r[-2]
                color = hex2rgb.h2r(color)
                glColor4f(color[0],color[1],color[2],color[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glEnd()
        else:
            pass

    def drawLineLight(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'linelight' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM linelight")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_LINES)
                color2 = r[-2]
                color2 = hex2rgb.h2r(color2)
                color1 = r[5]
                color1 = hex2rgb.h2r(color1)
                glColor4f(color1[0],color1[1],color1[2],color1[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glColor4f(color2[0],color2[1],color2[2],color2[3])
                glVertex3f(eval(r[6]),eval(r[7]),eval(r[8]))
                glEnd()
        else:
            pass

    def drawFaceLight(self):
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
        conn.close()
        path = list(row)[1]
        conn = sqlite3.connect(path)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        if 'facelight' in tab_name:
            conn  = sqlite3.connect(path)
            cu = conn.cursor()
            cu.execute("SELECT * FROM facelight")
            result = cu.fetchall()
            cu.close()
            conn.close()
            num = 0
            for r in result:
                r = list(r)
                glBegin(GL_POLYGON)
                color2 = r[-2]
                color2 = hex2rgb.h2r(color2)
                color1 = r[5]
                color1 = hex2rgb.h2r(color1)
                glColor4f(color1[0],color1[1],color1[2],color1[3])
                glVertex3f(eval(r[2]),eval(r[3]),eval(r[4]))
                glColor4f(color2[0],color2[1],color2[2],color2[3])
                glVertex3f(eval(r[6]),eval(r[7]),eval(r[8]))
                glEnd()
        else:
            pass

    def drawRay(self):
        glBegin(GL_LINES)
        glColor4f(255,255,255,255)
        glVertex3f(3,0.5,0)
        glColor4f(255,255,255,255)
        glVertex3f(1.5,0.5,0)
        glColor4f(255,255,255,255)
        glVertex3f(1.5,0.5,0)
        # glColor4f(255,255,255,255)
        # glVertex3f(-5.7,2.5,-2)#[-58.04937382  24.48795968 -54.04937382]
        # glColor4f(255,255,255,255)
        # glVertex3f(-5.7,2.5,-2)
        glColor4f(255,255,255,255)
        glVertex3f(1,0.6,-0.1)
        glColor4f(255,255,255,255)
        glVertex3f(1,0.6,-0.1)
        glColor4f(255,255,255,255)
        glVertex3f(-58.7,26.9,-56)
        glEnd()

    def paintGL(self):
        global IS_PERSPECTIVE, VIEW
        global EYE, LOOK_AT, EYE_UP
        global SCALE_K
        global WIN_W, WIN_H
        a = os.path.abspath('.')
        b = a.split("\\")
        c = tuple(b)
        d = '/'.join(c)
        path = d + "/resource/initial.sqlite"
        # 清除屏幕及深度缓存
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # 设置投影（透视投影）
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if WIN_W > WIN_H:
            if IS_PERSPECTIVE:
                glFrustum(VIEW[0]*WIN_W/WIN_H, VIEW[1]*WIN_W/WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])
            else:
                glOrtho(VIEW[0]*WIN_W/WIN_H, VIEW[1]*WIN_W/WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])
        else:
            if IS_PERSPECTIVE:
                glFrustum(VIEW[0], VIEW[1], VIEW[2]*WIN_H/WIN_W, VIEW[3]*WIN_H/WIN_W, VIEW[4], VIEW[5])
            else:
                glOrtho(VIEW[0], VIEW[1], VIEW[2]*WIN_H/WIN_W, VIEW[3]*WIN_H/WIN_W, VIEW[4], VIEW[5])
        # 设置模型视图
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # 几何变换
        glScale(SCALE_K[0], SCALE_K[1], SCALE_K[2])
        #设置视点
        gluLookAt(
            EYE[0], EYE[1], EYE[2], 
            LOOK_AT[0], LOOK_AT[1], LOOK_AT[2],
            EYE_UP[0], EYE_UP[1], EYE_UP[2]
        )
        #设置视口
        glViewport(0, 0, WIN_W, WIN_H)
        if mode == "2D Mode":
            if Axis:
                self.drawAxis2()
            EYE = np.array([0.0, 0.0, 2.0])
        else:
            if Axis:
                self.drawAxis()
        self.drawDot()
        self.drawLine()
        self.drawLines()
        self.drawTriangles()
        self.drawPointLight()
        self.drawLineLight()
        self.drawFaceLight()
        self.drawRay()
        # 发送绘制命令到 GPU
        glFlush()

    def resizeGL(self, width, height):
        global WIN_W, WIN_H
        WIN_W, WIN_H = width, height

    def wheelEvent(self, event):
        global EYE
        delta = event.angleDelta().y() # 获取鼠标滚轮的滚动值
        if delta > 0:
            EYE *= 0.95 # 放大视角
            self.update()
        else:
            EYE *= 1.05 # 缩小视角
            self.update()

    def mousePressEvent(self, event):
        global SCALE_K
        global LEFT_IS_DOWNED
        global MOUSE_X, MOUSE_Y
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.initial_pos = event.pos()
            x = self.initial_pos.x()
            y = self.initial_pos.y()
            MOUSE_X, MOUSE_Y = x, y
            LEFT_IS_DOWNED = True

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            LEFT_IS_DOWNED = False

    def mouseMoveEvent(self, event):
        global LEFT_IS_DOWNED
        global EYE, EYE_UP
        global MOUSE_X, MOUSE_Y
        global DIST, PHI, THETA
        global WIN_W, WIN_H
        super().mouseMoveEvent(event)
        if LEFT_IS_DOWNED:
            self.middle_pos = event.pos()
            x = self.middle_pos.x()
            y = self.middle_pos.y()
            dx = MOUSE_X - x
            dy = y - MOUSE_Y
            MOUSE_X, MOUSE_Y = x, y
            
            PHI += 2*np.pi*dy/WIN_H
            PHI %= 2*np.pi
            THETA += 2*np.pi*dx/WIN_W
            THETA %= 2*np.pi
            r = DIST*np.cos(PHI)
            
            EYE[1] = DIST*np.sin(PHI)
            EYE[0] = r*np.sin(THETA)
            EYE[2] = r*np.cos(THETA)
                
            if 0.5*np.pi < PHI < 1.5*np.pi:
                EYE_UP[1] = -1.0
            else:
                EYE_UP[1] = 1.0
        self.update()

    def keyPressEvent(self, event):
        global DIST, PHI, THETA
        global EYE, LOOK_AT, EYE_UP
        global IS_PERSPECTIVE, VIEW

        if event.text() == "X":
            LOOK_AT[0] += 0.1
            self.update()
        elif event.text() == "x":
            LOOK_AT[0] -= 0.1
            self.update()
        elif event.text() == "Y":
            LOOK_AT[1] += 0.1
            self.update()
        elif event.text() == "y":
            LOOK_AT[1] -= 0.1
            self.update()
        elif event.text() == "Z":
            LOOK_AT[2] += 0.1
            self.update()
        elif event.text() == "z":
            LOOK_AT[1] -= 0.1
            self.update()
        elif event.text() == "w":
            if mode == "3D Mode":
                arr = LOOK_AT - EYE
                arrlist = list(arr)
                # 使用argmin函数找出最小值的索引
                min_index = arr.argmin()
                minvalue = arrlist[min_index]
                minvalue1 = abs(minvalue)
                arrlist.pop(min_index)
                arrlist1 = []
                for i in arrlist:
                    i /= minvalue1
                    i *= 0.05
                    i = round(i,3)
                    arrlist1.append(i)
                minvalue *= 0.05
                minvalue = round(minvalue,3)
                arrlist1.insert(min_index,minvalue)
                arr1 = np.array(arrlist1)
                LOOK_AT += arr1
                EYE += arr1
                self.update()
            else:
                delta = np.array([0,0.05,0])
                LOOK_AT += delta
                EYE += delta
                self.update()
        elif event.text() == "W":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            arrlist.pop(min_index)
            arrlist1 = []
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT += arr1
            EYE += arr1
            self.update()
        elif event.key() == Qt.Key_Up:
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            arrlist.pop(min_index)
            arrlist1 = []
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT += arr1
            EYE += arr1
            self.update()
        elif event.text() == "s":
            if mode == "3D Mode":
                arr = LOOK_AT - EYE
                arrlist = list(arr)
                # 使用argmin函数找出最小值的索引
                min_index = arr.argmin()
                minvalue = arrlist[min_index]
                minvalue1 = abs(minvalue)
                arrlist.pop(min_index)
                arrlist1 = []
                for i in arrlist:
                    i /= minvalue1
                    i *= 0.05
                    i = round(i,3)
                    arrlist1.append(i)
                minvalue *= 0.05
                minvalue = round(minvalue,3)
                arrlist1.insert(min_index,minvalue)
                arr1 = np.array(arrlist1)
                LOOK_AT -= arr1
                EYE -= arr1
                self.update()
            else:
                delta = np.array([0,0.05,0])
                LOOK_AT -= delta
                EYE -= delta
                self.update()
        elif event.text() == "S":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            arrlist.pop(min_index)
            arrlist1 = []
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT -= arr1
            EYE -= arr1
            self.update()
        elif event.key() == Qt.Key_Down:
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            arrlist.pop(min_index)
            arrlist1 = []
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT -= arr1
            EYE -= arr1
            self.update()
        elif event.text() == "a":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT += arr1
            EYE += arr1
            self.update()
        elif event.text() == "A":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT += arr1
            EYE += arr1
            self.update()
        elif event.text() == "d":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT -= arr1
            EYE -= arr1
            self.update()
        elif event.text() == "D":
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT -= arr1
            EYE -= arr1
            self.update()
        elif event.key() == Qt.Key_Left:
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT += arr1
            EYE += arr1
            self.update()
        elif event.key() == Qt.Key_Right:
            arr = LOOK_AT - EYE
            arrlist = list(arr)
            det = arrlist.pop(1)
            arrlist.insert(1,0)
            arr2 = np.array(arrlist)
            if det < 0:
                nv = - np.cross(arr,arr2)
            else:
                nv = np.cross(arr,arr2)
            # print(nv)
            arrlist = list(nv)
            # 使用argmin函数找出最小值的索引
            min_index = arr.argmin()
            minvalue = arrlist[min_index]
            minvalue1 = abs(minvalue)
            if minvalue1 == 0:
                arrlist.pop(min_index)
                minvalue1 = min(arrlist)
                minvalue1 = abs(minvalue1)
                arrlist.insert(min_index,0)
            arrlist.pop(min_index)
            arrlist1 = []
            arrlist0 = []
            for i in arrlist:
                i = round(i,1)
                arrlist0.append(i)
            arrlist = arrlist0
            for i in arrlist:
                i /= minvalue1
                i *= 0.05
                i = round(i,3)
                arrlist1.append(i)
            minvalue *= 0.05
            minvalue = round(minvalue,3)
            arrlist1.insert(min_index,minvalue)
            arr1 = np.array(arrlist1)
            LOOK_AT -= arr1
            EYE -= arr1
            self.update()
        elif event.text() == "r":
            if mode == "3D Mode":
                EYE = np.array([1.0, 1.0, 1.0])
                LOOK_AT = np.array([0.0, 0.0, 0.0])
                self.update()
            else:
                EYE = np.array([0.0,0.0,2.0])
                LOOK_AT = np.array([0.0,0.0,0.0])
                self.update()
        elif event.text() == "R":
            if mode == "3D Mode":
                EYE = np.array([1.0, 1.0, 1.0])
                LOOK_AT = np.array([0.0, 0.0, 0.0])
                self.update()
            else:
                EYE = np.array([0.0,0.0,2.0])
                LOOK_AT = np.array([0.0,0.0,0.0])
                self.update()
        else:
            pass

class RubikCubeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 4, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 5, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 1, 1, 1, 1)
        self.tableView_2 = QtWidgets.QTableView(self.groupBox)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_2.addWidget(self.tableView_2, 2, 1, 1, 1)
        self.tableView_3 = QtWidgets.QTableView(self.groupBox)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout_2.addWidget(self.tableView_3, 4, 1, 2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.RubikCube_Widget = RubikCube_Widget(self.centralwidget)
        self.RubikCube_Widget.setObjectName("RubikCube_Widget")
        self.RubikCube_Widget.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.RubikCube_Widget, 0, 1, 3, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Simulation_Analysis_of_Optical_Prisms = QtWidgets.QAction(MainWindow)
        self.actionAbout_Simulation_Analysis_of_Optical_Prisms.setObjectName("actionAbout_Simulation_Analysis_of_Optical_Prisms")
        self.actionAbout_Author = QtWidgets.QAction(MainWindow)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMinimize)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_Simulation_Analysis_of_Optical_Prisms)
        self.menuHelp.addAction(self.actionAbout_Author)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle("Simulation Analysis of Optical Prisms")
        self.groupBox_2.setTitle("Basic Settings")
        self.pushButton_6.setText("Reset")
        self.checkBox.setText("Display Axis")
        self.pushButton_5.setText("Apply")
        self.pushButton_4.setText("More Settings")
        self.groupBox.setTitle("Drawing")
        self.groupBox_3.setTitle("Basic Shape")
        self.pushButton.setText("Dot")
        self.pushButton_2.setText("Line")
        self.pushButton_3.setText("Lines")
        self.pushButton_7.setText("Triangles")
        self.pushButton_8.setText("New Lens")
        self.groupBox_4.setTitle("Light Source")
        self.pushButton_10.setText("Point-Light ")
        self.pushButton_11.setText("Line-Light")
        self.pushButton_12.setText("Face-Light")
        self.pushButton_9.setText("New Face")
        self.groupBox_5.setTitle("Execute")
        self.pushButton_13.setText("Display Light Path")
        self.pushButton_14.setText("Repaint")
        self.menuFile.setTitle("File")
        self.menuHelp.setTitle("Help")
        self.actionSave.setText("Save")
        self.actionMinimize.setText("Minimize")
        self.actionQuit.setText("Quit")
        self.actionAbout_Simulation_Analysis_of_Optical_Prisms.setText("About Simulation Analysis of Optical Prisms")
        self.actionAbout_Author.setText("About Author")

        self.pushButton_4.clicked.connect(self.settings)
        self.pushButton_14.clicked.connect(self.repaint)

        self.pushButton.clicked.connect(self.Dot)
        self.pushButton_2.clicked.connect(self.Line)
        self.pushButton_3.clicked.connect(self.Lines)
        self.pushButton_7.clicked.connect(self.Triangles)
        self.pushButton_10.clicked.connect(self.PointLight)
        self.pushButton_11.clicked.connect(self.LineLight)
        self.pushButton_12.clicked.connect(self.FaceLight)
        self.pushButton_9.clicked.connect(self.NewFace)
        self.checkBox.stateChanged.connect(self.drawAxis)
        self.pushButton_8.clicked.connect(self.NewLen)
        self.pushButton_14.clicked.connect(self.repaint)
        self.pushButton_13.clicked.connect(self.ray_display)

        self.databasepath()
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(pathfinal1)
        db.open()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QSqlTableModel(db=db)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model2 = QSqlTableModel(db=db)
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model3 = QSqlTableModel(db=db)

        self.setup_context_menu()
        self.setup_context_menu2()
        self.setup_context_menu3()
        self.tableView.clicked.connect(self.on_cell_clicked)
        self.tableView_2.clicked.connect(self.on_cell_clicked2)
        self.tableView_3.clicked.connect(self.on_cell_clicked3)

    def NewLen(self):
        self.NewLen = NewLen()
        self.NewLen.show()

    def settings(self):
        self.SettingsDialog = SettingsDialog()
        self.SettingsDialog.show()


############################    tableview3区域     ################################

    def on_cell_clicked3(self,index):
        # 在这里处理点击单元格的行和列索引
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action3.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action3.setEnabled(False)

    def setup_context_menu3(self):
        self.tableView_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_3.customContextMenuRequested.connect(self.show_context_menu3)
        self.refresh_action3 = QAction("刷新", self.tableView_3)
        self.delete_action3 = QAction("删除行",self.tableView_3)
        self.delete_action3.setEnabled(False)
        self.len_action = QAction("显示棱镜数据",self.tableView_3)
        self.face_action = QAction("显示棱面数据",self.tableView_3)
        self.refresh_action3.triggered.connect(self.refresh_table_view3)
        self.delete_action3.triggered.connect(self.delete_table_view3)
        self.len_action.triggered.connect(self.lendata)
        self.face_action.triggered.connect(self.facedata)

    def show_context_menu3(self, position):
        menu3 = QMenu(self.tableView_3)
        menu3.addAction(self.refresh_action3)
        menu3.addAction(self.delete_action3)
        menu3.addSeparator()
        menu3.addAction(self.len_action)
        menu3.addAction(self.face_action)
        menu3.exec_(self.tableView_3.viewport().mapToGlobal(position))

    def lendata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("len",) in tables:
            self.tableView_3.setModel(self.model3)
            self.model3.setTable("len")
            self.model3.setSort(0, Qt.AscendingOrder)
            self.model3.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def facedata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("face",) in tables:
            self.tableView_3.setModel(self.model3)
            self.model3.setTable("face")
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

#######################################################################################################

############################    tableview2区域     ################################

    def on_cell_clicked2(self,index):
        # 在这里处理点击单元格的行和列索引
        row = index.row()
        column = index.column()
        if (row and column) or (row == 0) or (column == 0):
            self.delete_action2.setEnabled(True)
            print("Clicked cell: row {}, column {}".format(row, column))
        else:
            self.delete_action2.setEnabled(False)

    def setup_context_menu2(self):
        self.tableView_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_2.customContextMenuRequested.connect(self.show_context_menu2)
        self.large_action2 = QAction("放大",self.tableView_2)
        self.refresh_action2 = QAction("刷新", self.tableView_2)
        self.delete_action2 = QAction("删除行",self.tableView_2)
        self.delete_action2.setEnabled(False)
        self.pointlight_action = QAction("显示点光源数据",self.tableView_2)
        self.linelight_action = QAction("显示线光源数据",self.tableView_2)
        self.facelight_action = QAction("显示面光源数据",self.tableView_2)
        self.refresh_action2.triggered.connect(self.refresh_table_view2)
        self.delete_action2.triggered.connect(self.delete_table_view2)
        self.pointlight_action.triggered.connect(self.pointlightdata)
        self.linelight_action.triggered.connect(self.linelightdata)
        self.facelight_action.triggered.connect(self.facelightdata)
        self.large_action2.triggered.connect(self.large2)

    def large2(self):
        self.LargeDialog2 = LargeDialog2()
        self.LargeDialog2.show()

    def show_context_menu2(self, position):
        menu2 = QMenu(self.tableView_2)
        menu2.addAction(self.large_action2)
        menu2.addAction(self.refresh_action2)
        menu2.addAction(self.delete_action2)
        menu2.addSeparator()
        menu2.addAction(self.pointlight_action)
        menu2.addAction(self.linelight_action)
        menu2.addAction(self.facelight_action)
        menu2.exec_(self.tableView_2.viewport().mapToGlobal(position))

    def pointlightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("PointLight",) in tables:
            self.tableView_2.setModel(self.model2)
            self.model2.setTable("PointLight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def linelightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("linelight",) in tables:
            self.tableView_2.setModel(self.model2)
            self.model2.setTable("linelight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

    def facelightdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("facelight",) in tables:
            self.tableView_2.setModel(self.model2)
            self.model2.setTable("facelight")
            self.model2.setSort(0, Qt.AscendingOrder)
            self.model2.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass


    def refresh_table_view2(self):
        self.model2.select()

    def delete_table_view2(self):
        try:
            del_row = self.tableView_2.currentIndex().row()
            self.model2.removeRow(del_row)
            self.model2.select()
        except AttributeError as A:
            reply = QMessageBox.warning(self,u'提示',u'未打开任何数据库，此操作无效！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

##########################################################################################################

############################    tableview区域     ################################
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
        self.large_action = QAction("放大",self.tableView)
        self.refresh_action = QAction("刷新", self.tableView)
        self.delete_action = QAction("删除行",self.tableView)
        self.delete_action.setEnabled(False)
        self.dot_action = QAction("显示点数据",self.tableView)
        self.line_action = QAction("显示线数据",self.tableView)
        self.lines_action = QAction("显示多线数据",self.tableView)
        self.triangle_action = QAction("显示三角形数据",self.tableView)
        self.refresh_action.triggered.connect(self.refresh_table_view)
        self.delete_action.triggered.connect(self.delete_table_view)
        self.dot_action.triggered.connect(self.dotdata)
        self.line_action.triggered.connect(self.linedata)
        self.lines_action.triggered.connect(self.linesdata)
        self.triangle_action.triggered.connect(self.triangledata)
        self.large_action.triggered.connect(self.large)

    def show_context_menu(self, position):
        menu = QMenu(self.tableView)
        menu.addAction(self.large_action)
        menu.addAction(self.refresh_action)
        menu.addAction(self.delete_action)
        menu.addSeparator()
        menu.addAction(self.dot_action)
        menu.addAction(self.line_action)
        menu.addAction(self.lines_action)
        menu.addAction(self.triangle_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))

    def large(self):
        self.LargeDialog = LargeDialog()
        self.LargeDialog.show()

    def dotdata(self):
        conn = sqlite3.connect(pathfinal1)
        cu = conn.cursor()
        cu.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cu.fetchall()
        cu.close()
        conn.close()
        if ("dot",) in tables:
            self.tableView.setModel(self.model)
            self.model.setTable("dot")
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
        else:
            reply = QMessageBox.warning(self,u'提示',u'数据库未创建或已损坏，无法显示！',QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                pass

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
###########################################################################################################
        
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
        print(pathfinal1)
        try:
            conn = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            sql = "SELECT * FROM users WHERE id = ?"
            cu.execute(sql,(1,))
            row = cu.fetchone()
            conn.close()
            mode = list(row)[2]
        except:
            pass

    def Dot(self):
        self.Dot = DotDialog()
        self.Dot.show()

    def Line(self):
        self.Line = LineDialog()
        self.Line.show()

    def Lines(self):
        self.Lines = LinesDialog()
        self.Lines.show()

    def Triangles(self):
        self.Triangles = Triangles()
        self.Triangles.show()

    def PointLight(self):
        self.PointLight = PointLight()
        self.PointLight.show()

    def LineLight(self):
        self.LineLight = LineLight()
        self.LineLight.show()

    def FaceLight(self):
        self.FaceLight = FaceLight()
        self.FaceLight.show()

    def NewFace(self):
        self.NewFace = NewFace()
        self.NewFace.show()

    def chooseMode(self):
        global Mode
        global EYE
        if self.radioButton.isChecked():
            Mode = False
        else:
            Mode = True
        self.RubikCube_Widget.update()

    def drawAxis(self,state):
        global Axis
        if state == 0:
            Axis = False
        else:
            Axis = True
        self.RubikCube_Widget.update()

    def repaint(self):
        self.RubikCube_Widget.update()

    def ray_display(self):
        a = os.path.abspath('.')
        b = a.split("\\")
        c = tuple(b)
        d = '/'.join(c)
        conn = sqlite3.connect(pathfinal1)
        cu=conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name=cu.fetchall()
        tab_name=[line[0] for line in tab_name]
        conn.close()
        print(tab_name)
        if 'PointLight' in tab_name:
            conn  = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM PointLight")
            result = cu.fetchall()
            cu.close()
            conn.close()
            pointlight_dict = {}
            for r in result:
                r = list(r)
                direction = r[-1]
                x = r[2]
                y = r[3]
                z = r[4]
                name = r[1]
                value_list = [x,y,z,direction]
                pointlight_dict[name] = value_list
        else:
            pass

        if "LineLight" in tab_name:
            pass
        else:
            pass
        if "FaceLight" in tab_name:
            pass
        else:
            pass
        if "NewLen3D" in tab_name:
            conn  = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM NewLen3D")
            result = cu.fetchall()
            cu.close()
            conn.close()
            Len_dict = {}
            for r in result:
                r = list(r)
                R1 = r[2]
                R2 = r[3]
                Lines = eval(r[4])
                name = r[1]
                Len_list = [R1,R2,Lines]
                Len_dict[name] = Len_list
        else:
            pass
        if "NewFace2D" in tab_name:
            pass
        else:
            pass

        # print(pointlight_dict)
        # print(Len_dict)
        for key,value in Len_dict.items():
            resource_table_str = value[2][1]
            resource_table_ = resource_table_str.split("_")
            resource_table = resource_table_[-1]
            # if resource_table in tab_name:
            #     conn  = sqlite3.connect(pathfinal1)
            #     cu = conn.cursor()
            #     cu.execute(f"SELECT * FROM {resource_table}")
            #     result = cu.fetchall()
            #     cu.close()
            #     conn.close()
            #     for r in result:
            #         r = list(r)
            #         direction = r[-1]
            #         x = r[2]
            #         y = r[3]
            #         z = r[4]
            #         name = r[1]
            #         value_list = [x,y,z,direction]
            #         pointlight_dict[name] = value_list

        der = [-1,0,0]
        start = [3,1,0]
        face3D = [[[-2,-2,0],[4,0,0],[-2,2,0]]]
        faceside2={"line1":[[0,0,0],[-2,-2,0]],"line2":[[-2,-2,0],[2,-2,0]],"line3":[[2,-2,0],[0,0,0]]}
        n_all = [[0.5,0.6]]
        if "lines" in tab_name:
            conn  = sqlite3.connect(pathfinal1)
            cu = conn.cursor()
            cu.execute("SELECT * FROM lines")
            result = cu.fetchall()
            cu.close()
            conn.close()
            faceside3D = {}
            for r in result:
                r = list(r)
                line_name = r[1]
                line_x = [eval(r[2]),eval(r[3]),eval(r[4])]
                line_y = [eval(r[6]),eval(r[7]),eval(r[8])]
                line_list = [line_x,line_y]
                faceside3D[line_name] = line_list
            face1 = {"L1":faceside3D["L1"],"L2":faceside3D["L2"],"L3":faceside3D["L3"]}
            face2 = {"L4":faceside3D["L4"],"L5":faceside3D["L5"],"L6":faceside3D["L6"]}
            face3 = {"L1":faceside3D["L1"],"L5":faceside3D["L5"],"L7":faceside3D["L7"]}
            face4 = {"L2":faceside3D["L2"],"L4":faceside3D["L4"],"L8":faceside3D["L8"]}
            face5 = {"L3":faceside3D["L3"],"L7":faceside3D["L7"],"L6":faceside3D["L6"],"L8":faceside3D["L8"]}
            print(face1)
            print(face2)
            print(face3)
            print(face4)
            conclusion1 = {'dot1': [[2, 0, 0], ['L2', 'L1'], True], 'dot2': [[2, 2, 2], ['L1', 'L3'], True], 'dot3': [[2, 2, -2], ['L3', 'L1'], True]}
            der = [-1,0,0]
            start = [3,1,0]
            face3D = [[[2,0,0],[1,1,1],[1,1,-1]]]
            # direction = pointlight.determine3D(der,start,conclusion1,face3D)
            # print(direction)
            start = [3,0.5,0]
            end = [1.5,0.5,0]
            if 'ray' in tab_name:
                conn = sqlite3.connect(pathfinal1)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM ray")
                results = cursor.fetchall()
                conn.close()
                idnumber = len(results) + 1

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO ray (rayname,start,end_p,id) VALUES(?,?,?,?)"
                data = (rayname,start,end_p,idnumber)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
                
                reply = QtWidgets.QMessageBox.warning(self,u'Information',u'Added Successfully！',QMessageBox.Yes)
                if reply == QtWidgets.QMessageBox.Yes:
                    pass

            else:
                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                cu.execute("""CREATE TABLE ray
                    (id INTEGER PRIMARY KEY, rayname TEXT, start TEXT, end_p TEXT)""")
                conn.close()

                conn = sqlite3.connect(pathfinal1)
                cu = conn.cursor()
                sql = "INSERT INTO ray (rayname,start,end_p,id) VALUES(?,?,?,?)"
                data = (rayname,start,end_p,1)
                cu.execute(sql,data)
                conn.commit()
                conn.close()
