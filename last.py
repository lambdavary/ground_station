# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'big_daddy.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
import serial
import syslog
import time
from threading import Thread
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import src_rc

#port = '/dev/tty'
#port = '/dev/ttyUSB0'
port = '/dev/ttyUSB1'
ard = serial.Serial(port,9600,timeout=5)

altitudes = []
longtitudes = []
latitudes = []
temperatures = []
indeces = []

#640 / 400
#800 / 450

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(78, 6, 3);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(3, 10, 80);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.graphWidget = PlotWidget(self.frame_2)
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_8.addWidget(self.graphWidget, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setLineWidth(1)
        self.frame_10.setMidLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(1, 71, 21);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_10, 2, 3, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(45, 3, 76);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.graphWidget_4 = PlotWidget(self.frame_4)
        self.graphWidget_4.setObjectName("graphWidget_4")
        self.gridLayout_11.addWidget(self.graphWidget_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 0, 3, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphWidget_3 = PlotWidget(self.frame_9)
        self.graphWidget_3.setObjectName("graphWidget_3")
        self.gridLayout_10.addWidget(self.graphWidget_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_9, 0, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphWidget_2 = PlotWidget(self.frame_3)
        self.graphWidget_2.setObjectName("graphWidget_2")
        self.gridLayout_9.addWidget(self.graphWidget_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        canvas = QtGui.QPixmap(640, 360)
        self.label_9.setPixmap(canvas)
        #self.label_9.setPixmap(QtGui.QPixmap(":/home/faraklit/fold/image.png"))
        #self.label_9.setScaledContents(True)
        #self.label_9.setWordWrap(False)
        #self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 1, 1, 2, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        timer = QTimer(MainWindow)
        timer.timeout.connect(self.draw_something)
        timer.start(1000)


        self.draw_something()

        self.retranslateUi(MainWindow)
        
        t1 = Thread(target=self.read_ard)
        t1.start()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_big_daddy(self):
        t1 = Thread(target=self.read_ard)
        t1.start()

    def plot(self):
        pen = pg.mkPen(color=(78, 6, 3))
        pen2 = pg.mkPen(color=(3, 10, 80))
        pen3 = pg.mkPen(color=(1, 71, 21))
        pen4 = pg.mkPen(color=(45, 3, 76))
        self.graphWidget.plot(indeces,altitudes, pen=pen)
        self.graphWidget_2.plot(indeces, longtitudes, pen=pen4)
        self.graphWidget_3.plot(indeces, latitudes, pen=pen3)
        self.graphWidget_4.plot(indeces, temperatures, pen=pen2)

    def draw_something(self):
        import math 
        import random
        canvas = QtGui.QPixmap(640, 360)
        self.label_9.setPixmap(canvas)
        angle = random.randint(0, 360)
        print(angle)
        rand_x = 320+100*math.cos(angle)
        rand_y = 180+100*math.sin(angle)
        print(rand_x)
        print(rand_y)
        painter = QtGui.QPainter(self.label_9.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('white'))
        painter.setPen(pen)

        painter.drawText(50, 50, "Angle:"+str(angle))
        painter.drawText(50, 70, "Estimated range:"+str(angle)+"m")

        painter.drawText(320, 30, "N")
        painter.drawText(470, 180, "E")
        painter.drawText(320, 330, "S")
        painter.drawText(170, 180, "W")
        painter.drawPoint(320, 180)
        painter.drawPoint(rand_x, rand_y)
        painter.drawLine(320, 180, rand_x, rand_y)
        painter.end()

    def read_ard(self):
        index = 0
        while True:
            self.label_9.update()
            msg = ard.read(ard.inWaiting())
            ard.flushOutput()
            msg = msg.decode("utf-8")
            time.sleep(0.8)
            if ',' in msg:            
                altitude, longtitude, latitude, temperature = msg.split(',')
                altitudes.append(int(altitude))
                longtitudes.append(int(longtitude))
                latitudes.append(int(latitude))
                temperatures.append(int(temperature))
                indeces.append(index)
                self.label_5.setText(altitude)
                self.label_6.setText(latitude)
                self.label_4.setText(longtitude)
                self.label_2.setText(temperature)
                index += 1
                self.plot()
                self.label_9.update()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Altitude(m)"))
        self.label_5.setText(_translate("MainWindow", "1000"))
        self.label.setText(_translate("MainWindow", "Distance(m)"))
        self.label_2.setText(_translate("MainWindow", "952"))
        self.label_8.setText(_translate("MainWindow", "Latitude"))
        self.label_6.setText(_translate("MainWindow", "38\' 54\'\'"))
        self.label_3.setText(_translate("MainWindow", "Longtitude"))
        self.label_4.setText(_translate("MainWindow", "36\' 42\'\'"))

from pyqtgraph import PlotWidget
import the_resource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

